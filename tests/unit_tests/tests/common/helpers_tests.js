/// <reference path="../../common/helpers.js">

describe("Helpers", function() {
	describe("Escape function", function() {
		it("should be defined",function() {
			expect(escape).toBeDefined();
		});
		it("should return string",function() {
			expect(escape("")).toEqual(jasmine.any(String));
		});
		it("should replace single character in the middle of the word",function() {
			expect(escape('te"st')).toBe("te&quot;st");
			expect(escape("te'st")).toBe("te&#039;st");
			expect(escape("te&st")).toBe("te&amp;st");
			expect(escape("te<st")).toBe("te&lt;st");
			expect(escape("te>st")).toBe("te&gt;st");
		});
		it("should replace single character in the beginning of the word",function() {
			expect(escape('"test')).toBe("&quot;test");
			expect(escape("'test")).toBe("&#039;test");
			expect(escape("&test")).toBe("&amp;test");
			expect(escape("<test")).toBe("&lt;test");
			expect(escape(">test")).toBe("&gt;test");
		});
		it("should replace single character at the end of the word",function() {
			expect(escape('test"')).toBe("test&quot;");
			expect(escape("test'")).toBe("test&#039;");
			expect(escape("test&")).toBe("test&amp;");
			expect(escape("test<")).toBe("test&lt;");
			expect(escape("test>")).toBe("test&gt;");
		});
		it("should replace multiple single character",function() {
			expect(escape('"test""')).toBe("&quot;test&quot;&quot;");
			expect(escape("'test''")).toBe("&#039;test&#039;&#039;");
			expect(escape("&test&&")).toBe("&amp;test&amp;&amp;");
			expect(escape("<test<<")).toBe("&lt;test&lt;&lt;");
			expect(escape(">test>>")).toBe("&gt;test&gt;&gt;");
		});
		it("should replace multiple character",function() {
			expect(escape("&Te\"stova' 'v<eta>.")).toBe("&amp;Te&quot;stova&#039; &#039;v&lt;eta&gt;.");
		});
	});
});
