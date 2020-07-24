/// <reference path="../../common/wrapping.js">

describe("Wrapping", function() {
	describe("Object build_wrapping_code", function() {		
		it("should be defined",function() {
			expect(build_wrapping_code).toBeDefined();
		});
	});
	describe("Function add_wrappers", function() {
		beforeAll(function() {
			build_wrapping_code = {};
		});
		it("should be defined",function() {
			expect(add_wrappers).toBeDefined();
		});
		it("should return nothing",function() {
			var ECMA_DATE_wrappers = [
				{
					parent_object: "window",
					parent_object_property: "Date",
					wrapped_objects: [
						{
							original_name: "Date",
							wrapped_name: "originalDateConstructor",
						},
					],
					helping_code: rounding_function + noise_function +
						`
						var precision = args[0];
						var doNoise = args[1];
						var func = rounding_function;
						if (doNoise) {
							func = noise_function;
						}
						`,
					wrapping_function_args: "",
					wrapping_function_body: `
						var wrapped = new originalDateConstructor(...arguments);
						let cachedValue;
						if (arguments[0] !== undefined) {
							// Don't change lastValue if custom arguments are passed
							 cachedValue = lastValue;
						}
						var changedValue = func(wrapped.getTime(), precision);
						if (cachedValue) {
							// Don't change lastValue if custom arguments are passed
							 lastValue = cachedValue;
						}
						wrapped.setTime(changedValue);
						return wrapped;
						`,
					wrapper_prototype: "originalDateConstructor",
					post_wrapping_code: [
						{
							code_type: "function_define",
							original_function: "originalDateConstructor.now",
							parent_object: "window.Date",
							parent_object_property: "now",
							wrapping_function_args: "",
							wrapping_function_body: "return func(originalDateConstructor.now.call(Date), precision);",
						},
					]
				},
			]
			add_wrappers(ECMA_DATE_wrappers);
			//console.log(build_wrapping_code);
			expect(undefined).toBe(undefined);
		});
		afterAll(function() {
			build_wrapping_code = {};
		});
	});
	describe("Function rounding_function", function() {
		it("should be defined",function() {
			expect(rounding_function).toBeDefined();
		});
		it("should return number",function() {
			eval(rounding_function);
			expect(rounding_function(123123,0)).toEqual(jasmine.any(Number));
		});
		it("should return NaN when number is undefined",function() {
			eval(rounding_function);
			expect(rounding_function(undefined,0)).toEqual(NaN);
		});
		it("should return NaN when precision is undefined",function() {
			eval(rounding_function);
			expect(rounding_function(123456789,undefined)).toEqual(NaN);
		});
		it("should return rounded number for whole number when precision is from {0,1,2}",function() {
			eval(rounding_function);
			expect(rounding_function(123456789,2)).toBe(123456780);
			expect(rounding_function(12,2)).toBe(10);
			expect(rounding_function(123456789,1)).toBe(123456700);
			expect(rounding_function(123,1)).toBe(100);
			expect(rounding_function(123456789,0)).toBe(123456000);
			expect(rounding_function(1234,0)).toBe(1000);
		});
		it("should not round number for whole number when precision is 3",function() {
			eval(rounding_function);
			expect(rounding_function(123456789,3)).toBe(123456789);
		});
		it("should return rounded number for whole number when precision is from {-1,-2,-3}",function() {
			eval(rounding_function);
			expect(rounding_function(123456789,-1)).toBe(123450000);
			expect(rounding_function(123456789,-2)).toBe(123400000);
			expect(rounding_function(123456789,-3)).toBe(123000000);
		});
		it("should return rounded number for float number when precision is from {0,1,2}",function() {
			eval(rounding_function);
			expect(rounding_function(123456789.123,2)).toBe(123456780);
			expect(rounding_function(123456789.123,1)).toBe(123456700);
			expect(rounding_function(123456789.123,0)).toBe(123456000);
		});
		it("should return whole part of number for float number when precision is 3",function() {
			eval(rounding_function);
			expect(rounding_function(123456789.123,3)).toBe(123456789);
		});
		it("should return rounded number for float number when precision is from {-1,-2,-3}",function() {
			eval(rounding_function);
			expect(rounding_function(123456789.123,-1)).toBe(123450000);
			expect(rounding_function(123456789.123,-2)).toBe(123400000);
			expect(rounding_function(123456789.123,-3)).toBe(123000000);
		});
		it("should return zero for number less than 10^(3-precision)",function() {
			eval(rounding_function);
			expect(rounding_function(1,2)).toBe(0);
			expect(rounding_function(12,1)).toBe(0);
			expect(rounding_function(123,0)).toBe(0);
		});
	});
	describe("Function noise_function", function() {		
		it("should be defined",function() {
			expect(noise_function).toBeDefined();
		});
		it("should return number",function() {
			eval(noise_function);
			expect(noise_function(123456.123,3)).toEqual(jasmine.any(Number));
		});
		it("should return 0 when number is undefined",function() {
			eval(noise_function);
			expect(noise_function(undefined,0)).toBe(0);
		});
		it("should return 0 when precision is undefined",function() {
			eval(noise_function);
			expect(noise_function(123456789,undefined)).toBe(0);
		});
		it("should return 0 when precision is 3 and greather",function() {
			eval(noise_function);
			expect(noise_function(123456789,3)).toBe(0);
			expect(noise_function(123456789,4)).toBe(0);
			expect(noise_function(123456789,5)).toBe(0);
			expect(noise_function(123456789,6)).toBe(0);
		});
		it("should not return unchanged float number from argument when precision is 0",function() {
			eval(noise_function);
			var number_changed = false;
			const input_nums = [1009.1013, 1019.1021, 1031.1033, 1039.1049, 1051.1061];
			for (const num of input_nums) {
				if (Math.abs(noise_function(num,0) - num) > 0.0001) {
					number_changed = true;
					break;
				}
			}
			expect(number_changed).toBeTrue();
		});
		it("should not return unchanged float number from argument when precision is 1",function() {
			eval(noise_function);
			var number_changed = false;
			const input_nums = [1009.1013, 1019.1021, 1031.1033, 1039.1049, 1051.1061];
			for (const num of input_nums) {
				if (Math.abs(noise_function(num,1) - num) > 0.0001) {
					number_changed = true;
					break;
				}
			}
			expect(number_changed).toBeTrue();
		});
		it("should not return unchanged whole number from argument when precision is 0",function() {
			eval(noise_function);
			var number_changed = false;
			const input_nums = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061];
			for (const num of input_nums) {
				if (Math.abs(noise_function(num,0) - num) > 0.0001) {
					number_changed = true;
					break;
				}
			}
			expect(number_changed).toBeTrue();
		});
		it("should not return unchanged whole number from argument when precision is 1",function() {
			eval(noise_function);
			var number_changed = false;
			const input_nums = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061];
			for (const num of input_nums) {
				if (Math.abs(noise_function(num,1) - num) > 0.0001) {
					number_changed = true;
					break;
				}
			}
			expect(number_changed).toBeTrue();
		});
	});
});
