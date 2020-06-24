/// <reference path="../../common/levels.js">

describe("Levels", function() {
	describe("getCurrentLevelJSON function", function() {
		beforeAll(function() {
			domains = {};
			domains['stackoverflow.com'] = level_3;
			domains['polcak.github.io'] = level_2;
			domains['swatblog.rtgp.xyz'] = level_1;
			domains['mail.google.com'] = level_0;
			domains['example.net'] = level_3;
			domains['vas-hosting.cz'] = level_2;
			domains['thenetworg.crm4.dynamics.com'] = level_1;
			domains['csob.cz'] = level_0;
		});
		afterAll(function() {
			domains = {};
		});
		it("should be defined",function() {
			expect(getCurrentLevelJSON).toBeDefined();
		});
		it("should return object",function() {
			expect(getCurrentLevelJSON("http://www.seznam.cz/")).toEqual(jasmine.any(Object));
		});
		it("should throw error when parametr is not given",function() {
			expect(function() {getCurrentLevelJSON()}).toThrowError();
		});
		it("should throw error when parametr is undefined",function() {
			expect(function() {getCurrentLevelJSON(undefined)}).toThrowError();
		});
		it("should throw error when parametr is empty string",function() {
			expect(function() {getCurrentLevelJSON("")}).toThrowError();
		});
		it("should throw error when parametr is invalid URL",function() {
			expect(function() {getCurrentLevelJSON("http")}).toThrowError();
			expect(function() {getCurrentLevelJSON("nvjidfnbgfi")}).toThrowError();
			expect(function() {getCurrentLevelJSON("seznam.cz")}).toThrowError();
			expect(function() {getCurrentLevelJSON("seznam")}).toThrowError();
			expect(function() {getCurrentLevelJSON("www")}).toThrowError();
			expect(function() {getCurrentLevelJSON("www.seznam.cz")}).toThrowError();
		});
		it("should return default level when root domain from given URL is not saved in domains in browser storage",function() {
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).toBe(default_level);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).toBe(default_level);
		});
		it("should return set level (from browser storage) for saved domains",function() {
			expect(getCurrentLevelJSON("https://stackoverflow.com/questions/1925976/declaring-functions-in-javascript")).toBe(level_3);
			expect(getCurrentLevelJSON("http://www.example.net/?amount=brass&bird=basketball")).toBe(level_3);
			expect(getCurrentLevelJSON("https://www.vas-hosting.cz/blog-vyhody-dedikovaneho-serveru-vds-oproti-vps")).toBe(level_2);
			expect(getCurrentLevelJSON("https://www.csob.cz/portal/lide")).toBe(level_0);
		});
		// Now this test is not passing because of bug in url - look at url_tests for more information.
		xit("should return set level (from browser storage) for saved domains with subdomains",function() {
			expect(getCurrentLevelJSON("https://polcak.github.io/jsrestrictor/test/test.html")).toBe(level_2);
			expect(getCurrentLevelJSON("https://swatblog.rtgp.xyz/")).toBe(level_1);
			expect(getCurrentLevelJSON("https://mail.google.com/mail/u/0/#inbox")).toBe(level_0);
			expect(getCurrentLevelJSON("https://thenetworg.crm4.dynamics.com/main.aspx#759240725")).toBe(level_1);
		});
	});
});