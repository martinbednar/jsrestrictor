/// <reference path="../../common/levels.js">

describe("Levels", function() {
	describe("getCurrentLevelJSON function", function() {
		/*beforeEach(function(done) {
			console.log(chrome.storage.sync.get);
			console.log(chrome.storage.sync.get(null, function testGet(result) {
			  console.log('Value currently is ');
			  console.log(result);
			  done();
			}));
		});*/
		
		/*afterEach(function(done) {
			setTimeout(function() {
				console.log("yde");
				console.log(getCurrentLevelJSON("https://www.seznam.cz/"));
			  done();
			}, 3000);
		});*/

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
		//var clearStorage = browser.storage.sync.clear();
		it("should return default level when root domain from given URL is not saved in domains in browser storage",function() {
			//init_levels();
			//browser.storage.sync.get(null, updateLevels);
			/*console.log(default_level.is_default);
			function getDefaultLevel(res) {
				default_level = res["__default__"]
			}
			browser.storage.sync.get(null, getDefaultLevel);
			console.log(default_level.level_id);
			console.log(getCurrentLevelJSON("https://www.seznam.cz/"));*/
			console.log(default_level);
			default_level = browser.storage.sync.get()["__default__"];
			console.log(default_level);
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).toEqual(default_level);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).toEqual(default_level);
		});
		xit("should return default level when root domain from given URL is not saved in domains in browser storage",function() {
			domains['seznam.cz'] = levels[L3];
			browser.storage.sync.set({domains: domains});
			//console.log(getCurrentLevelJSON("https://www.seznam.cz/"));
			//function(done){ setTimeout(function(){ console.log(getCurrentLevelJSON("https://www.seznam.cz/")); done(); }, 3000);};
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).toEqual(levels[L3]);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).toEqual(default_level);
			
			browser.storage.sync.clear();
		});
	});
});