/// <reference path="../../common/url.js">

describe("URL", function() {
	describe("Extract root domain function", function() {		
		it("should be defined",function() {
			expect(extractRootDomain).toBeDefined();
		});
		it("should return string",function() {
			expect(extractRootDomain("")).toEqual(jasmine.any(String));
		});
		it("should return undefined when parametr is undefined",function() {
			expect(function() {extractRootDomain(undefined);}).toThrowError();
		});
		it("should return empty string when parametr is empty string",function() {
			expect(extractRootDomain("")).toBe("");
		});
		it("should return parametr when parametr is nonsense",function() {
			expect(extractRootDomain("gsf14f56sdvds1,.-dfsv,§ú")).toBe("gsf14f56sdvds1,.-dfsv,§ú");
		});
		it("should return root domain",function() {
			expect(extractRootDomain("vutbr.cz")).toBe("vutbr.cz");
			expect(extractRootDomain("fit.vutbr.cz")).toBe("vutbr.cz");
			expect(extractRootDomain("wis.fit.vutbr.cz")).toBe("vutbr.cz");
			expect(extractRootDomain("eva.fit.vutbr.cz")).toBe("vutbr.cz");
			expect(extractRootDomain("netfox-hyperv.fit.vutbr.cz")).toBe("vutbr.cz");
			expect(extractRootDomain("project.bigred.cornell.edu")).toBe("cornell.edu");
			expect(extractRootDomain("test.eva.fit.vutbr.cz")).toBe("vutbr.cz");
		});
		xit("should return root domain with subdomain for mutually independent sites on a single root domain",function() {
			expect(extractRootDomain("sites.google.com")).toBe("sites.google.com");
			expect(extractRootDomain("code.google.com")).toBe("code.google.com");
			expect(extractRootDomain("docs.google.com")).toBe("docs.google.com");
			expect(extractRootDomain("support.google.com")).toBe("support.google.com");
			expect(extractRootDomain("polcak.github.io")).toBe("polcak.github.io");
			expect(extractRootDomain("martinbednar.github.io")).toBe("polcak.github.io");
		});
		xit("should return IP address for IP address (no domainname) - example URL: http://89.45.196.133/paneln/Login.aspx)",function() {
			//example web page: http://89.45.196.133/paneln/Login.aspx
			expect(extractRootDomain("89.45.196.133")).toBe("89.45.196.133");
			expect(extractRootDomain("2001:67c:1220:809::93e5:917")).toBe("2001:67c:1220:809::93e5:917");
		});
	});
});