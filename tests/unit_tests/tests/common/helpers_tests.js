/// <reference path="../../common/helpers.js">

describe("Helpers", function() {
	describe("Escape function", function() {
		it("function defined",function() {
			expect(escape).toBeDefined();
		});
		it("replace single character in the middle of the word",function() {
			expect(escape('te"st')).toEqual("te&quot;st");
			expect(escape("te'st")).toEqual("te&#039;st");
			expect(escape("te&st")).toEqual("te&amp;st");
			expect(escape("te<st")).toEqual("te&lt;st");
			expect(escape("te>st")).toEqual("te&gt;st");
		});
		it("replace single character in the beginning of the word",function() {
			expect(escape('"test')).toEqual("&quot;test");
			expect(escape("'test")).toEqual("&#039;test");
			expect(escape("&test")).toEqual("&amp;test");
			expect(escape("<test")).toEqual("&lt;test");
			expect(escape(">test")).toEqual("&gt;test");
		});
		it("replace single character at the end of the word",function() {
			expect(escape('test"')).toEqual("test&quot;");
			expect(escape("test'")).toEqual("test&#039;");
			expect(escape("test&")).toEqual("test&amp;");
			expect(escape("test<")).toEqual("test&lt;");
			expect(escape("test>")).toEqual("test&gt;");
		});
		it("replace multiple single character",function() {
			expect(escape('"test""')).toEqual("&quot;test&quot;&quot;");
			expect(escape("'test''")).toEqual("&#039;test&#039;&#039;");
			expect(escape("&test&&")).toEqual("&amp;test&amp;&amp;");
			expect(escape("<test<<")).toEqual("&lt;test&lt;&lt;");
			expect(escape(">test>>")).toEqual("&gt;test&gt;&gt;");
		});
		it("replace multiple character",function() {
			expect(escape("&Te\"stova' 'v<eta>.")).toEqual("&amp;Te&quot;stova&#039; &#039;v&lt;eta&gt;.");
		});
	});
});