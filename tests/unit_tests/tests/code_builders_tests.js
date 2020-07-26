/// <reference path="../../common/code_builders.js">

describe("Code builders", function() {
	describe("Function enclose_wrapping", function() {
		it("should be defined",function() {
			expect(enclose_wrapping).toBeDefined();
		});
	});
	describe("Function enclose_wrapping2", function() {
		it("should be defined",function() {
			expect(enclose_wrapping2).toBeDefined();
		});
	});
	describe("Function define_page_context_function", function() {
		it("should be defined",function() {
			expect(define_page_context_function).toBeDefined();
		});
	});
	describe("Function generate_assign_function_code", function() {
		it("should be defined",function() {
			expect(generate_assign_function_code).toBeDefined();
		});
	});
	describe("Function generate_object_properties", function() {
		it("should be defined",function() {
			expect(generate_object_properties).toBeDefined();
		});
	});
	describe("Function build_code", function() {
		it("should be defined",function() {
			expect(build_code).toBeDefined();
		});
	});
	describe("Function wrap_code", function() {
		beforeAll(function() {
			domains = {};
		});
		it("should be defined",function() {
			expect(wrap_code).toBeDefined();
		});
		it("should return undefined when no wrappers are given as an argument",function() {
			expect(wrap_code([])).toBe(undefined);
		});
		it("should throw error when parametr is not iterable",function() {
			expect(function() {wrap_code(5)}).toThrowError();
		});
		it("should return undefined when no wrappers are given as an argument 2",function() {
			for (let key in levels) {
				levels[key].wrappers = wrapping_groups.get_wrappers(levels[key]);
			}
			var rnd_num_regex = /\d{9}\d?/;
		
			
			expect(wrap_code([levels[1].wrappers[0]]).replace(rnd_num_regex,"123456789")).toEqual(
			(`(function() {
		var original_functions = {};
		`
			+
			build_code(build_wrapping_code[levels[1].wrappers[0][0]], levels[1].wrappers[0].slice(1))
			+
			`
			var originalToStringF = Function.prototype.toString;
			var originalToStringStr = Function.prototype.toString();
			Function.prototype.toString = function() {
				var currentString = originalToStringF.call(this);
				var originalStr = original_functions[currentString];
				if (originalStr !== undefined) {
					return originalStr;
				}
				else {
					return currentString;
				}
			};
			original_functions[Function.prototype.toString.toString()] = originalToStringStr;
		})();`).replace(rnd_num_regex,"123456789")
			);
		});
	});
});
