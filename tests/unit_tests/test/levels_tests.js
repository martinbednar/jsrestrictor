const chai = require("chai");
const asserttype = require('chai-asserttype');
const rewire = require('rewire');
const { default: browserFake } = require('webextensions-api-fake');

chai.use(asserttype);
const expect = chai.expect;
global.browser = browserFake();

const levels = rewire('../../../common/levels.js');
const getCurrentLevelJSON = levels.__get__('getCurrentLevelJSON');
var default_level = levels.__get__('default_level');

describe("Levels", function() {
	before(async () => {
	
	var ret = await browser.storage.sync.get(null);
	console.log(ret);
	
	browser.storage.sync.set("test", "test value")
	
	var ret = await browser.storage.sync.get(null);
	console.log(ret);
	
	browser.storage.sync.clear();
	var ret = await browser.storage.sync.get(null);
	console.log(ret);
  });
  
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
			//console.log(default_level);
			//default_level = browser.storage.sync.get()["__default__"];
			//console.log(default_level);
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).to.be.equal(default_level);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).to.be.equal(default_level);
		});
		xit("should return default level when root domain from given URL is not saved in domains in browser storage",function() {
			domains['seznam.cz'] = levels[L3];
			browser.storage.sync.set({domains: domains});
			//console.log(getCurrentLevelJSON("https://www.seznam.cz/"));
			//function(done){ setTimeout(function(){ console.log(getCurrentLevelJSON("https://www.seznam.cz/")); done(); }, 3000);};
			expect(getCurrentLevelJSON("https://www.seznam.cz/")).to.be.equal(levels[L3]);
			expect(getCurrentLevelJSON("https://www.fit.vut.cz/research/groups/.cs")).to.be.equal(default_level);
			
			browser.storage.sync.clear();
		});
	});
});