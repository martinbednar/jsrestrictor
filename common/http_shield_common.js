//
//  JavaScript Restrictor is a browser extension which increases level
//  of security, anonymity and privacy of the user while browsing the
//  internet.
//
//  Copyright (C) 2020  Pavel Pohner
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.
//

// Implementation of HTTP webRequest shield, file: http_shield_common.js
// Contains common functions for both versions - Chrome and Firefox.
// Mainly for reading CSV files, and checking IP ranges.

//Chrome compatibility
if ((typeof browser) === "undefined") {
	var browser = chrome;
}

/// Locally served IPV4 DNS zones loaded from IANA
var localIPV4DNSZones;
/// Locally served IPV6 DNS zones loaded from IANA
var localIPV6DNSZones;


/***** STATISTICAL PROCESSING - BEGIN ******/
/// Associative array of hosts, that are currently blocked based on their previous actions
var blockedHosts = new Object();
/// Information about hosts, for which cant be used DNS query
var hostStatistics = new Object();

/// Percentage of hosts, that can register an HTTP error response
var uniqueErrorHostsRatio = 10.0;
/// If there are more hosts than uniqueErrorHostsLimit which are targeted from the same origin, the origin host becomes blocked
var uniqueErrorHostsLimit = 20;
/// Number of Request Timed Out errors allowed for one origin
var errorsAllowed = 10;
/// Number of HTTP client errors (eg. 404 not found, 403 forbidden etc.) per requestTimeInterval
var httpClientErrorsAllowed = 5;

/// Errors that are considered as possible attacker threat
var httpErrorList = {
	400:true,
	404:true,
	405:true,
	406:true,
	408:true,
	410:true,
	413:true,
	414:true,
	415:true,
	501:true,
	503:true,
	505:true
};

/// String that defines Request Timed Out error in Chrome
/// according to: https://developer.chrome.com/extensions/webRequest#event-onErrorOccurred
/// It's not backwards compatible, but it's the best we have
var chromeErrorString = "net::ERR_CONNECTION_TIMED_OUT";
/***** STATISTICAL PROCESSING - END ******/


/// Associtive array of hosts, that are currently among trusted "do not blocked" hosts
var doNotBlockHosts = new Object();
browser.storage.sync.get(["whitelistedHosts"], function(result){
		if (result.whitelistedHosts != undefined)
			doNotBlockHosts = result.whitelistedHosts;
	});

/// Hook up the listener for receiving messages
browser.runtime.onMessage.addListener(commonMessageListener);
browser.runtime.onMessage.addListener(messageListener);

/// Check the storage for requestShieldOn object
browser.storage.sync.get(["requestShieldOn"], function(result){
	//If found object is true or undefined, turn the requestShieldOn
	if (result.requestShieldOn == undefined || result.requestShieldOn)
	{
		//Hook up the listeners
		browser.webRequest.onBeforeSendHeaders.addListener(
			beforeSendHeadersListener,
			{urls: ["<all_urls>"]},
			["blocking", "requestHeaders"]
		);
		
		browser.webRequest.onHeadersReceived.addListener(
			onHeadersReceivedRequestListener,
			{urls: ["<all_urls>"]},
			["blocking"]
		);

		browser.webRequest.onErrorOccurred.addListener(
			onErrorOccuredListener,
			{urls: ["<all_urls>"]}
		);

		if (typeof onResponseStartedListener === "function")
		{
			browser.webRequest.onResponseStarted.addListener(
			onResponseStartedListener,
			{urls: ["<all_urls>"]},
			["responseHeaders"]
			);
		}
	}
});


/// Function for reading locally stored csv file
let readFile = (_path) => {
	return new Promise((resolve, reject) => {
		//Fetching locally stored CSV file in same-origin mode
		fetch(_path, {mode:'same-origin'})
			.then(function(_res) {
				//Return data as a blob
				return _res.blob();
			})
			.then(function(_blob) {
				var reader = new FileReader();
				//Wait until the whole file is read
				reader.addEventListener("loadend", function() {
					resolve(this.result);
				});
				//Read blob data as text
				reader.readAsText(_blob);
			})
			.catch(error => {
				reject(error);
			});
	});
};

/// Obtain file path in user's file system and read CSV file with IPv4 local zones
readFile(browser.runtime.getURL("ipv4.dat"))
	.then(_res => {
		//Parse loaded CSV and store it in prepared variable
		localIPV4DNSZones = parseCSV(_res, true);
	})
	.catch(_error => {
		console.log(_error );
	});

/// Obtain file path in user's file system and read CSV file with IPv6 local zones
readFile(browser.runtime.getURL("ipv6.dat"))
	.then(_res => {
		//Parse loaded CSV and store it in prepared variable
		localIPV6DNSZones = parseCSV(_res, false);
	})
	.catch(_error => {
		console.log(_error );
	});

/// Checks validity of IPv4 addresses,
/// returns TRUE if the url matches IPv4 regex
/// FALSE otherwise
function isIPV4(url)
{
	var reg = new RegExp("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$");
	return reg.test(url);
}

/// Checks validity IPV6 address
/// Returns TRUE, if URL is valid IPV6 address
/// FALSE otherwise
function isIPV6(url)
{
	url = url.substring(1, url.length - 1);
	var reg = new RegExp("^(?:(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){6})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:::(?:(?:(?:[0-9a-fA-F]{1,4})):){5})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){4})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,1}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){3})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,2}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){2})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,3}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:[0-9a-fA-F]{1,4})):)(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,4}(?:(?:[0-9a-fA-F]{1,4})))?::)(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,5}(?:(?:[0-9a-fA-F]{1,4})))?::)(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,6}(?:(?:[0-9a-fA-F]{1,4})))?::))))$", 'm');
	return reg.test(url);
}

/// Checks whether the ipAddr is found in IPv4 localZones
/// Returns TRUE if ipAddr exists in localZones fetched from IANA
/// FALSE otherwise
/// This function should only be called on valid IPv4 address
function isIPV4Private(ipAddr)
{
	//Split IP address on dots, obtain 4 numbers	
	var substrIP = ipAddr.split('.');
	//Convert IP address into array of 4 integers
	var ipArray = substrIP.map(function(val){
	return parseInt(val, 10);
	});
	//For each IPv4 locally served zone
	for (var i = 0; i < localIPV4DNSZones.length; i++)
	{
		//Split the zone into array of J numbers
		var zone = localIPV4DNSZones[i].split('.');
		var k = 0;
		//For each number of local zone IP
		//(Decrementing, because local zones IPs are reverted
		for (var j = zone.length - 1; j >= 0; j--)
		{
			//Check if the corresponding numbers match
			//If not, then break and move onto next local zone
			if (ipArray[k] != zone[j])
			{
			break;
			}
			else if(j == 0) //Checked all numbers of local zone
			{
			return true;
			}
			k++;
		}
	}
	return false;
}

/// Checks whether the ipAddr is found in IPv6 localZones
/// Returns TRUE if ipAddr exists in localZones fetched from IANA
/// FALSE otherwise
/// This function should only be called on valid IPv6 address
function isIPV6Private(ipAddr)
{
	//Expand shorten IPv6 addresses to full length
	ipAddr = expandIPV6(ipAddr);
	//Split into array of fields
	var substrIP = ipAddr.split(":");
	//Join the fields into one string
	ipAddr = substrIP.join("").toUpperCase();
	//For each IPv6 locally served zone
	for (var i = 0; i < localIPV6DNSZones.length; i++)
	{
		var zone = localIPV6DNSZones[i];
		//For each char of zone
		for (var j = 0; j < zone.length; j++)
		{
			//Compare the chars, if they do not match, break and move onto next zone		
			if (ipAddr.charAt(j) != zone.charAt(j))
			{
			break;
			}
			//Checked all chars of current zone -> private IP range
			else if(j == zone.length - 1)
			{
			return true;
			}
		}
	}
	return false;
}

/// Function for parsing CSV files obtained from IANA
/// Strips .IN-ADDR and .IP6 from zones and comma delimiter,
/// merges them into array by CSV rows
/// Arguments: csv - CSV obtained from IANA
/// 			 ipv4 - bool, saying whether the csv is IPv4 CSV or IPv6
/// Returns: Array of parsed CSV values
function parseCSV(csv, ipv4)
{
	//converting into array
	var csvArray = CSVToArray(csv);
	var DNSzones = [];

	if (ipv4) //ipv4.csv
	{
	//cycle through first column of the CSV -> obtaining IP zones
	//Starting with i = 1, skipping the CSV header
	for (var i = 1; i < csvArray.length; i++)
	{
		//i-1, means start from 0
		//Obtains IP zone, strips .IN-ADDR from the end of it, stroes into array	
		DNSzones[i-1] = csvArray[i][0].substring(0, csvArray[i][0].indexOf(".IN-ADDR"));
	}
	return DNSzones;
	}
	else //ipv6.csv
	{
		//Same as ipv4
		for (var i = 1; i < csvArray.length-1; i++)
		{
			DNSzones[i-1] = csvArray[i][0].substring(0, csvArray[i][0].indexOf(".IP6"));
		}

		for (var i = 0; i < DNSzones.length; i++)
		{
			//Additionally splits the IP zone on dots	
			var splitted = DNSzones[i].split(".");
			DNSzones[i] = "";
			//Joins splitted IP zone into one string
			for (var j = splitted.length - 1; j >= 0 ; j--)
			{
			DNSzones[i] += splitted[j];

			}
		}
		return DNSzones;
	}
}

/// Auxillary function for parsing CSV files
/// Converts CSV to array
/// strData - loaded CSV file
/// Returns array containing CSV rows
function CSVToArray(strData){
	// Create a regular expression to parse the CSV values.
	var objPattern = new RegExp(
		(
		// Delimiters.
		"(\\,|\\r?\\n|\\r|^)" +
		// Quoted fields.
		"(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +
		// Standard fields.
		"([^\"\\,\\r\\n]*))"
		),
		"gi"
		);
	//Array to hold data
	var csvData = [[]];
	//Array to hold regex matches
	var regexMatches = null;
	//While not match
	while (regexMatches = objPattern.exec(strData)){
		// Get the delimiter that was found
		var strMatchedDelimiter = regexMatches[1];
		if (strMatchedDelimiter.length && (strMatchedDelimiter != ",")){
		//New row
		csvData.push([]);
		}
		// captured data (quoted or unquoted)
		if (regexMatches[2]){
		//quoted
		var strMatchedValue = regexMatches[2].replace(
			new RegExp( "\"\"", "g" ),
			"\""
			);
		} else {
			//non-quoted value.
			var strMatchedValue = regexMatches[3];

		}
		//Add to data array
		csvData[csvData.length - 1].push( strMatchedValue );
	}
	// Return the parsed data
	return( csvData );
}

/// Function for expanding shorten ipv6 addresses
/// Takes valid ipv6 address in ip6addr argument
/// Returns expanded ipv6 address in string
/// This function should be only called on valid IPv6 address
function expandIPV6(ip6addr)
{
	ip6addr = ip6addr.substring(1, ip6addr.length - 1);
	var expandedIP6 = "";
	//Check for omitted groups of zeros (::)
	if (ip6addr.indexOf("::") == -1)
	{
		//There are none omitted groups of zeros
		expandedIP6 = ip6addr;
	}
	else
	{
		//Split IP on one compressed group
		var splittedIP = ip6addr.split("::");
		var amountOfGroups = 0;
		//For each group
		for (var i = 0; i < splittedIP.length; ++i)
		{
			//Split on :	
			amountOfGroups += splittedIP[i].split(":").length;
		}
		expandedIP6 += splittedIP[0] + ":";
		//For each splitted group
		for (var i = 0; i < 8 - amountOfGroups; ++i)
		{
			//insert zeroes	
			expandedIP6 += "0000:";
		}
		//Insert the rest of the splitted IP
		expandedIP6 += splittedIP[1];
	}
	//Split expanded IPv6 into parts
	var addrParts = expandedIP6.split(":");
	var addrToReturn = "";
	//For each part
	for (var i = 0; i < 8; ++i)
	{
		//check the length of the part
		while(addrParts[i].length < 4)
		{
			//if it's less than 4, insert zero
			addrParts[i] = "0" + addrParts[i];
		}
		addrToReturn += i != 7 ? addrParts[i] + ":" : addrParts[i];
	}
	return addrToReturn;
}

//Check if the hostname or any of it's domains is whitelisted
function checkWhitelist(hostname)
{
	//Calling a function from url.js
	var domains = extractSubDomains(hostname);
	for (var domain of domains)
	{
		if (doNotBlockHosts[domain] != undefined)
		{
			return true;
		}
	}
	return false;
}
//
/// Creates and presents notification to the user
/// works with webExtensions notification API
/// Creates notification about blocked request
/// Arguments:
/// 	origin - origin of the request
/// 	target - target of the request
/// 	resource - type of the resource
function notifyBlockedRequest(origin, target, resource) {
	browser.notifications.create({
		"type": "basic",
		"iconUrl": browser.extension.getURL("img/icon-48.png"),
		"title": "Network boundary shield blocked suspicious request!",
		"message": `Request from ${origin} to ${target} blocked.\n\nMake sure that you are on a benign page. If you want to allow web requests from ${origin}, please, go to the JS Restrictor settings and add an exception.`
	});
}

/// Event listener hooked up to webExtensions onMessage event
/// Receives full message in message,
/// sender of the message in sender,
/// function for sending response in sendResponse
/// Does appropriate action based on message
function commonMessageListener(message, sender, sendResponse)
{
	//Message came from options.js, updated whitelist
	if (message.message === "whitelist updated")
	{
		//actualize current doNotBlockHosts from storage
		browser.storage.sync.get(["whitelistedHosts"], function(result){
			doNotBlockHosts = result.whitelistedHosts;
		});
	}
	//Mesage came from popup.js, whitelist this site
	else if (message.message === "add site to whitelist")
	{
			//Obtain current hostname and whitelist it
			var currentHost = message.site;
			doNotBlockHosts[currentHost] = true;
			browser.storage.sync.set({"whitelistedHosts":doNotBlockHosts});
	}
	//Message came from popup.js, remove whitelisted site
	else if (message.message === "remove site from whitelist")
	{
			//Obtain current hostname and remove it
			currentHost = message.site;
			delete doNotBlockHosts[currentHost];
			browser.storage.sync.set({"whitelistedHosts":doNotBlockHosts});
	}
	//HTTP request shield was turned on
	else if (message.message === "turn request shield on")
	{
		//Hook up the listeners
		browser.webRequest.onBeforeSendHeaders.addListener(
			beforeSendHeadersListener,
			{urls: ["<all_urls>"]},
			["blocking", "requestHeaders"]
		);
		
		browser.webRequest.onHeadersReceived.addListener(
			onHeadersReceivedRequestListener,
			{urls: ["<all_urls>"]},
			["blocking"]
		);

		browser.webRequest.onErrorOccurred.addListener(
			onErrorOccuredListener,
			{urls: ["<all_urls>"]}
		);

		if (typeof onResponseStartedListener === "function")
		{
			browser.webRequest.onResponseStarted.addListener(
			onResponseStartedListener,
			{urls: ["<all_urls>"]},
			["responseHeaders"]
			);
		}
	}
	//HTTP request shield was turned off
	else if (message.message === "turn request shield off")
	{
		//Disconnect the listeners
		browser.webRequest.onBeforeSendHeaders.removeListener(beforeSendHeadersListener);
		
		browser.webRequest.onHeadersReceived.removeListener(onHeadersReceivedRequestListener);
		browser.webRequest.onErrorOccurred.removeListener(onErrorOccuredListener);
		
		if (typeof onResponseStartedListener === "function")
		{
			browser.webRequest.onResponseStarted.removeListener(onResponseStartedListener);
		}
	}
}

/***** STATISTICAL PROCESSING - BEGIN ******/
/// If the browser regained connectivity - came online
window.addEventListener("online", function()
{
	//Hook up the listener to the onErrorOccured webRequest event
	browser.webRequest.onErrorOccurred.addListener(
		onErrorOccuredListener,
		{urls: ["<all_urls>"]}
	);
});

/// If the browser lost connectivity - gone offline
window.addEventListener("offline", function()
{
	//Disconnect the listener from the onErrorOccured webRequest event
	browser.webRequest.onErrorOccurred.removeListener(onErrorOccuredListener);
});

/// webRequest event listener, hooked to onErrorOccured event
/// Catches all errors, checks them for Request Timed out errors
/// Iterates error counter, blocks the host if limit was exceeded
/// Takes object representing error in responseDetails variable
function onErrorOccuredListener(responseDetails) {

	//It's neccessary to have both of these defined, otherwise the error can't be analyzed
	if (responseDetails.initiator === undefined || responseDetails.url === undefined)
	{
		return {cancel:false};
	}
	var sourceUrl = new URL(responseDetails.initiator);
	//Removing www. from hostname, so the hostnames are uniform
	sourceUrl.hostname = sourceUrl.hostname.replace(/^www\./,'');
	var targetUrl = new URL(responseDetails.url);
	targetUrl.hostname = targetUrl.hostname.replace(/^www\./,'');

	//Host found among user's trusted hosts, allow it right away
	if (checkWhitelist(sourceUrl.hostname))
	{
		return {cancel:false};
	}
	//Host found among user's untrusted, thus blocked, hosts, blocking it without further actions
	if (blockedHosts[sourceUrl.hostname] != undefined)
	{
		return {cancel:true};
	}

	//If the error is TIMED_OUT -> access to non-existing IP
	if (responseDetails.error == chromeErrorString)
	{
		//Count erros for given host
		if (hostStatistics[sourceUrl.hostname] != undefined)
		{
			hostStatistics[sourceUrl.hostname]["errors"] += 1;
		}
		else
		{
			hostStatistics[sourceUrl.hostname] = insertHostInStats(targetUrl.hostname);
			hostStatistics[sourceUrl.hostname]["errors"] = 1;
		}
		//Block the host if the error limit was exceeded
		if(hostStatistics[sourceUrl.hostname]["errors"] > errorsAllowed)
		{
			notifyBlockedHost(sourceUrl.hostname);
			blockedHosts[sourceUrl.hostname] = true;
		}

	}
	return {cancel:false};
}

/// webRequest event listener, hooked to onErrorOccured event
/// Catches all responses, analyzes those with record in hostStatistics
/// Modifies counters, blocks if one of the limits was exceeded
function onHeadersReceivedRequestListener(headers)
{
	//It's neccessary to have both of these defined, otherwise the response can't be analyzed
	if (headers.initiator === undefined || headers.url === undefined)
	{
		return {cancel:false};
	}

	var sourceUrl = new URL(headers.initiator);
	//Removing www. from hostname, so the hostnames are uniform
	sourceUrl.hostname = sourceUrl.hostname.replace(/^www\./,'');
	var targetUrl = new URL(headers.url);
	targetUrl.hostname = targetUrl.hostname.replace(/^www\./,'');

	//Host found among user's trusted hosts, allow it right away
	if (checkWhitelist(sourceUrl.hostname))
	{
		return {cancel:false};
	}

	//Host found among user's untrusted, thus blocked, hosts, blocking it without further actions
	if (blockedHosts[sourceUrl.hostname] != undefined)
	{
		return {cancel:true};
	}

	//If it's the error code that exists in httpErrorList
	if (httpErrorList[headers.statusCode] != undefined)
	{
		//Obtain record for given origin from statistics array
		//Record has to be there already, because it was inserted there while
		//encountering the request from this origin
		var currentHost = hostStatistics[sourceUrl.hostname];

		//Check if the target domain was already encountered for this source origin
		if (currentHost[targetUrl.hostname] != undefined)
		{
			//If so, iterate http errors variable for this origin and target domain
			currentHost[targetUrl.hostname]["httpErrors"] += 1;
			//If it's firt error from this target
			if(!currentHost[targetUrl.hostname]["hadError"])
			{
				//Iterate global counter for this source origin
				currentHost["httpErrors"] += 1;
				//Set that we've seen the error from this target already
				currentHost[targetUrl.hostname]["hadError"] = true;

				//Allow atleast one error hosts, if 10% ratio is less than one error host
				//Set hosts to 10, if there are less than 10 hosts
				var hosts = currentHost["hosts"] < uniqueErrorHostsRatio ? uniqueErrorHostsRatio : currentHost["hosts"];
				var errors = currentHost["httpErrors"];
				var errorRatio =	errors*1.0 / hosts * 100;
				//If the ratio, or the fixed limit for source origin was exceeded
				if (errorRatio > uniqueErrorHostsRatio || errors > uniqueErrorHostsLimit)
				{
					//Block the origin
					notifyBlockedHost(sourceUrl.hostname);
					blockedHosts[sourceUrl.hostname] = true;
					return {cancel:true};
				}
			}
			//If the limit for http error response from target host was exceeded
			if(currentHost[targetUrl.hostname]["httpErrors"] > httpClientErrorsAllowed)
			{
				//Block the origin
				notifyBlockedHost(sourceUrl.hostname);
				blockedHosts[sourceUrl.hostname] = true;
				return {cancel:true};
			}
		}
	}
	//Successful response
	else if ((headers.statusCode >= 100) && (headers.statusCode < 400))
	{
		//Obtain record for given origin from statistics array
		var currentHost = hostStatistics[sourceUrl.hostname];
		//Check if we've seen this target for given source origin
		if (currentHost[targetUrl.hostname] != undefined)
		{
			//if so, check if it's the first successful response from this target URL
			if (currentHost[targetUrl.hostname]["successfulResponses"][targetUrl] === undefined)
			{
				//If so, note that we've seen this URL already
				currentHost[targetUrl.hostname]["successfulResponses"][targetUrl] = 1;
				//Decrement the counter
				currentHost[targetUrl.hostname]["httpErrors"] -= 0.5;
			}
			else
			{
				currentHost[targetUrl.hostname]["successfulResponses"][targetUrl] += 1;
			}

			//Normalize the number, if it's less than zero
			if (currentHost[targetUrl.hostname]["httpErrors"] < 0)
				currentHost[targetUrl.hostname]["httpErrors"] = 0;
		}
	}
	return {cancel:false};
}

/// Function that creates object representing source host
/// Recieves target hostname in targetDomain argument
function insertHostInStats(targetDomain)
{
	var currentHost = new Object();
	currentHost[targetDomain] = new Object();
	currentHost[targetDomain]["requests"] = 1;
	currentHost[targetDomain]["httpErrors"] = 0;
	currentHost[targetDomain]["hadError"] = false;
	currentHost[targetDomain]["successfulResponses"] = new Object();
	currentHost["hosts"] = 1;
	currentHost["requests"] = 1;
	currentHost["httpErrors"] = 0;
	currentHost["errors"] = 0;

	return currentHost;
}

function beforeSendHeadersStatistical(sourceUrlHostname, targetUrlHostname) {
	//Target is either host name or public IP
	var currentHost = hostStatistics[sourceUrlHostname];

	//If its the first time we're seeing this source host
	if (currentHost == undefined)
	{
		currentHost = insertHostInStats(targetUrlHostname);
		hostStatistics[sourceUrlHostname] = currentHost;
		return;
	}
	//Check if we've seen this target for this source host
	if (currentHost[targetUrlHostname] != undefined)
	{
		currentHost[targetUrlHostname].requests += 1;
	}
	else //If not, just insert the stats
	{
		currentHost[targetUrlHostname] = new Object();
		currentHost[targetUrlHostname]["requests"] = 1;
		currentHost[targetUrlHostname]["httpErrors"] = 0;
		currentHost[targetUrlHostname]["hadError"] = false;
		currentHost[targetUrlHostname]["successfulResponses"] = new Object();
		currentHost["hosts"] += 1;
	}
}

/// Creates and presents notification to the user
/// works with webExtensions notification API
function notifyBlockedHost(host) {
	browser.notifications.create({
		"type": "basic",
		"iconUrl": browser.extension.getURL("img/icon-48.png"),
		"title": "Host was blocked!",
		"message": "Host: " + host + " issued to many unsuccessful requests. This may be just an error in your network connectivity or innocent error of the web site. But it can also be a sign of malicious activities such as using your browser as a proxy to scan your local network. It is up to you to decide if you trust the web site and give it an exception from the Network Boundary Scanner using pop up or the option page."
	});
}
/***** STATISTICAL PROCESSING - END ******/
