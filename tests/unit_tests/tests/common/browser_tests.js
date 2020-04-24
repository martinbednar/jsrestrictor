/// <reference path="../../common/browser.js">

describe("Browser", function() {
	describe("Running in Firefox function", function() {
		beforeAll(function() {
			this.isFirefox = typeof InstallTrigger !== 'undefined';
		});
		
		it("should be defined",function() {
			expect(running_in_firefox).toBeDefined();
		});
		it("should return boolean",function() {
			expect(running_in_firefox()).toEqual(jasmine.any(Boolean));
		});
		it("should return true in Firefox and false in other web browsers",function() {
			expect(running_in_firefox()).toBe(this.isFirefox);
		});
	});
});