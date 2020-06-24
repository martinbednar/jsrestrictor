const levels_file = rewire('../../../common/levels.js');
const getCurrentLevelJSON = levels_file.__get__('getCurrentLevelJSON');
const init_levels = levels_file.__get__('init_levels');


describe("Levels:", function() {
	before(function() {
		browser.storage.sync.clear();
		init_levels();
		this.levels = levels_file.__get__('levels');
		/*var ret = await browser.storage.sync.get(null);
		console.log(ret);
		
		browser.storage.sync.set("test", "test value")
		
		var ret = await browser.storage.sync.get(null);
		console.log(ret);
		
		browser.storage.sync.clear();
		var ret = await browser.storage.sync.get(null);
		console.log(ret);*/
	});
	
	afterEach(function() {
		browser.storage.sync.clear();
	});
  
	describe("getCurrentLevelJSON function", function() {
		it("should be defined",function() {
			expect(getCurrentLevelJSON).to.be.not.undefined;
		});
		it("should return object",function() {
			expect(getCurrentLevelJSON("http://www.seznam.cz/")).to.be.object();
		});
		it("should throw error when parametr is not given",function() {
			expect(function() {getCurrentLevelJSON()}).to.throw();
		});
		it("should throw error when parametr is undefined",function() {
			expect(function() {getCurrentLevelJSON(undefined)}).to.throw();
		});
		it("should throw error when parametr is empty string",function() {
			expect(function() {getCurrentLevelJSON("")}).to.throw();
		});
		it("should throw error when parametr is invalid URL",function() {
			expect(function() {getCurrentLevelJSON("http")}).to.throw();
			expect(function() {getCurrentLevelJSON("nvjidfnbgfi")}).to.throw();
			expect(function() {getCurrentLevelJSON("seznam.cz")}).to.throw();
			expect(function() {getCurrentLevelJSON("seznam")}).to.throw();
			expect(function() {getCurrentLevelJSON("www")}).to.throw();
			expect(function() {getCurrentLevelJSON("www.seznam.cz")}).to.throw();
		});
		it("should return default level when root domain from given URL is not saved in domains in browser storage",function() {
			var default_level = levels_file.__get__('default_level');
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).to.be.deep.equal(default_level);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).to.be.deep.equal(default_level);
		});
		it("should return set level when root domain from given URL is saved in domains in browser storage",function() {
			global.domains = {};
			domains['seznam.cz'] = this.levels['3'];
			browser.storage.sync.set({domains: domains});
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).to.be.equal(this.levels['3']);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).to.be.equal(default_level);
		});
	});
});
