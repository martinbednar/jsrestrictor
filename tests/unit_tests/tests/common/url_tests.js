/// <reference path="../../common/url.js">

describe("URL", function() {
	describe("Extract root domain function", function() {		
		it("should be defined",function() {
			expect(extractRootDomain).toBeDefined();
		});
		it("should return string",function() {
			expect(extractRootDomain("")).toEqual(jasmine.any(String));
		});
		xit("should return undefined when parametr is undefined",function() {
			expect(extractRootDomain(undefined)).toBe(undefined);
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
		xit("should return root domain for FQDN",function() {
			expect(extractRootDomain("vutbr.cz.")).toBe("vutbr.cz.");
			expect(extractRootDomain("fit.vutbr.cz.")).toBe("vutbr.cz.");
			expect(extractRootDomain("wis.fit.vutbr.cz.")).toBe("vutbr.cz.");
			expect(extractRootDomain("eva.fit.vutbr.cz.")).toBe("vutbr.cz.");
			expect(extractRootDomain("netfox-hyperv.fit.vutbr.cz.")).toBe("vutbr.cz.");
			expect(extractRootDomain("project.bigred.cornell.edu.")).toBe("cornell.edu.");
			expect(extractRootDomain("test.eva.fit.vutbr.cz.")).toBe("vutbr.cz.");
		});
		it("should return root domain for hostname with ccTLD",function() {
			expect(extractRootDomain("test.co.uk")).toBe("test.co.uk");
			expect(extractRootDomain("sub.test.co.ck")).toBe("test.co.ck");
			expect(extractRootDomain("test.sub.test.co.ck")).toBe("test.co.ck");
		});
		xit("should return IP address for IP address (no domainname) - example URL: http://89.45.196.133/paneln/Login.aspx)",function() {
			//example web page: http://89.45.196.133/paneln/Login.aspx
			expect(extractRootDomain("89.45.196.133")).toBe("89.45.196.133");
		});
	});
});