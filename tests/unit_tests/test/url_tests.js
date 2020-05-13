const chai = require("chai");
const asserttype = require('chai-asserttype');
const rewire = require('rewire');

chai.use(asserttype);
const expect = chai.expect;

const url = rewire('../../../common/url.js');
global.extractRootDomain = url.__get__('extractRootDomain');


describe("URL", function() {
	describe("Extract root domain function", function() {		
		it("should be defined",function() {
			expect(extractRootDomain).to.be.not.undefined;
		});
		it("should return string",function() {
			expect(extractRootDomain("")).to.be.string();
		});
		it("should throw error when parametr is undefined",function() {
			expect(function() {extractRootDomain(undefined)}).to.throw();
		});
		it("should return empty string when parametr is empty string",function() {
			expect(extractRootDomain("")).to.deep.equal("");
		});
		it("should return parametr when parametr is nonsense without dots",function() {
			expect(extractRootDomain("gsf14f56sdvds1,-dfsv,§ú")).to.deep.equal("gsf14f56sdvds1,-dfsv,§ú");
		});
		it("should return root domain",function() {
			expect(extractRootDomain("vutbr.cz")).to.deep.equal("vutbr.cz");
			expect(extractRootDomain("fit.vutbr.cz")).to.deep.equal("vutbr.cz");
			expect(extractRootDomain("wis.fit.vutbr.cz")).to.deep.equal("vutbr.cz");
			expect(extractRootDomain("eva.fit.vutbr.cz")).to.deep.equal("vutbr.cz");
			expect(extractRootDomain("netfox-hyperv.fit.vutbr.cz")).to.deep.equal("vutbr.cz");
			expect(extractRootDomain("project.bigred.cornell.edu")).to.deep.equal("cornell.edu");
			expect(extractRootDomain("test.eva.fit.vutbr.cz")).to.deep.equal("vutbr.cz");
		});
		xit("should return root domain with subdomain for mutually independent sites on a single root domain",function() {
			expect(extractRootDomain("sites.google.com")).to.deep.equal("sites.google.com");
			expect(extractRootDomain("code.google.com")).to.deep.equal("code.google.com");
			expect(extractRootDomain("docs.google.com")).to.deep.equal("docs.google.com");
			expect(extractRootDomain("support.google.com")).to.deep.equal("support.google.com");
			expect(extractRootDomain("polcak.github.io")).to.deep.equal("polcak.github.io");
			expect(extractRootDomain("martinbednar.github.io")).to.deep.equal("polcak.github.io");
		});
		xit("should return IP address for IP address (no domainname) - example URL: http://89.45.196.133/paneln/Login.aspx)",function() {
			//example web page: http://89.45.196.133/paneln/Login.aspx
			expect(extractRootDomain("89.45.196.133")).to.deep.equal("89.45.196.133");
			expect(extractRootDomain("2001:67c:1220:809::93e5:917")).to.deep.equal("2001:67c:1220:809::93e5:917");
		});
	});
});