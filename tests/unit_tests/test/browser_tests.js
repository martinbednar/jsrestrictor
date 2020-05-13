const browser = rewire('../../../common/browser.js');
const running_in_firefox = browser.__get__('running_in_firefox');


describe("Browser:", function() {
	describe("running_in_firefox function", function() {
		before(function() {
			this.isFirefox = typeof InstallTrigger !== 'undefined';
		});
		
		it("should be defined",function() {
			expect(running_in_firefox).to.be.not.undefined;
		});
		it("should return boolean",function() {
			expect(running_in_firefox()).to.be.boolean();
		});
		xit("should return true in Firefox and false in other web browsers",function() {
			expect(running_in_firefox()).to.deep.equal(this.isFirefox);
		});
	});
});
