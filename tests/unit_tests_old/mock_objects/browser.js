//const browser = chrome;

var browser = {}

browser.storage = {}

browser.storage.onChanged= function () {console.log("bla");};

browser.storage.sync = {
	     __default__: 2, // Default protection level
	     version: 2,     // The version of this storage
	     custom_levels: {}, // associative array of custom level (key, its id => object)
	       /*{level_id: short string used for example on the badge
	        level_text: Short level description
	        level_description: Full level description
	        wrappers": list of wrappers and their parameters
	       }*/
	     domains: {}, // associative array of levels associated with specific domains (key, the domain => object)
	       //{level_id: short string of the level in use
	       //}
		   
		   get: function () {
			   return this;
		   },
		   
		   set: function () {
			   return this.__default__;
		   },
		   
		   clear: function () {
			   return this.__default__;
		   }
		};