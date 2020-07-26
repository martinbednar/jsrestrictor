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
			for (let key in levels) {
				levels[key].wrappers = wrapping_groups.get_wrappers(levels[key]);
			}
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
		it("should return wrapped code when wrappers are given",function() {
			var rnd_num_regex = /\/\/ \d?\d?\d?\d?\d?\d?\d?\d?\d?\d?/g;
			
			for (level of [0,1,2,3]) {
			for (wrapper of levels[level].wrappers) {
			expect(wrap_code([wrapper]).replace(rnd_num_regex,"123456789")).toEqual(
			(`(function() {
		var original_functions = {};
		`
			+
			build_code(build_wrapping_code[wrapper[0]], wrapper.slice(1))
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
			}
			}
		});
	});
});
