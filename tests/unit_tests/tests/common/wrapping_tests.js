/// <reference path="../../common/wrapping.js">

describe("Wrapping", function() {
	describe("Object build_wrapping_code", function() {		
		it("should be defined",function() {
			expect(build_wrapping_code).toBeDefined();
		});
	});
	describe("Function add_wrappers", function() {		
		it("should be defined",function() {
			expect(add_wrappers).toBeDefined();
		});
	});
	describe("Function rounding_function", function() {
		it("should be defined",function() {
			expect(rounding_function).toBeDefined();
		});
		it("should return number",function() {
			eval(rounding_function)
			expect(rounding_function(123123,0)).toEqual(jasmine.any(Number));
		});
		it("should return rounded number for whole number when precision is from {0,1,2}",function() {
			eval(rounding_function)
			expect(rounding_function(123456789,2)).toEqual(123456780);
			expect(rounding_function(12,2)).toEqual(10);
			expect(rounding_function(123456789,1)).toEqual(123456700);
			expect(rounding_function(123,1)).toEqual(100);
			expect(rounding_function(123456789,0)).toEqual(123456000);
			expect(rounding_function(1234,0)).toEqual(1000);
		});
		it("should not round number for whole number when precision is 3",function() {
			eval(rounding_function)
			expect(rounding_function(123456789,3)).toEqual(123456789);
		});
		it("should return rounded number for whole number when precision is from {-1,-2,-3}",function() {
			eval(rounding_function)
			expect(rounding_function(123456789,-1)).toEqual(123450000);
			expect(rounding_function(123456789,-2)).toEqual(123400000);
			expect(rounding_function(123456789,-3)).toEqual(123000000);
		});
		it("should return rounded number for float number when precision is from {0,1,2}",function() {
			eval(rounding_function)
			expect(rounding_function(123456789.123,2)).toEqual(123456780);
			expect(rounding_function(123456789.123,1)).toEqual(123456700);
			expect(rounding_function(123456789.123,0)).toEqual(123456000);
		});
		it("should not round number for float number when precision is 3",function() {
			eval(rounding_function)
			expect(rounding_function(123456789.123,3)).toEqual(123456789);
		});
		it("should return rounded number for float number when precision is from {-1,-2,-3}",function() {
			eval(rounding_function)
			expect(rounding_function(123456789.123,-1)).toEqual(123450000);
			expect(rounding_function(123456789.123,-2)).toEqual(123400000);
			expect(rounding_function(123456789.123,-3)).toEqual(123000000);
		});
		it("should return zero for number less than 10^(3-precision)",function() {
			eval(rounding_function)
			expect(rounding_function(1,2)).toEqual(0);
			expect(rounding_function(12,1)).toEqual(0);
			expect(rounding_function(123,0)).toEqual(0);
		});
	});
	describe("Function noise_function", function() {		
		it("should be defined",function() {
			expect(noise_function).toBeDefined();
		});
	});
});
