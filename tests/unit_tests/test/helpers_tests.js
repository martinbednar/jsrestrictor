const helpers = rewire('../../../common/helpers.js');
const escape = helpers.__get__('escape');


describe("Helpers:", function() {
	describe("escape function", function() {
		it("should be defined",function() {
			expect(escape).to.be.not.undefined;
		});
		it("should return string",function() {
			expect(escape("")).to.be.string();
			expect(escape("")).to.deep.equal("");
		});
		it("should replace single character in the middle of the word",function() {
			expect(escape('te"st')).to.deep.equal("te&quot;st");
			expect(escape("te'st")).to.deep.equal("te&#039;st");
			expect(escape("te&st")).to.deep.equal("te&amp;st");
			expect(escape("te<st")).to.deep.equal("te&lt;st");
			expect(escape("te>st")).to.deep.equal("te&gt;st");
		});
		it("should replace single character in the beginning of the word",function() {
			expect(escape('"test')).to.deep.equal("&quot;test");
			expect(escape("'test")).to.deep.equal("&#039;test");
			expect(escape("&test")).to.deep.equal("&amp;test");
			expect(escape("<test")).to.deep.equal("&lt;test");
			expect(escape(">test")).to.deep.equal("&gt;test");
		});
		it("should replace single character at the end of the word",function() {
			expect(escape('test"')).to.deep.equal("test&quot;");
			expect(escape("test'")).to.deep.equal("test&#039;");
			expect(escape("test&")).to.deep.equal("test&amp;");
			expect(escape("test<")).to.deep.equal("test&lt;");
			expect(escape("test>")).to.deep.equal("test&gt;");
		});
		it("should replace multiple single character",function() {
			expect(escape('"test""')).to.deep.equal("&quot;test&quot;&quot;");
			expect(escape("'test''")).to.deep.equal("&#039;test&#039;&#039;");
			expect(escape("&test&&")).to.deep.equal("&amp;test&amp;&amp;");
			expect(escape("<test<<")).to.deep.equal("&lt;test&lt;&lt;");
			expect(escape(">test>>")).to.deep.equal("&gt;test&gt;&gt;");
		});
		it("should replace multiple character",function() {
			expect(escape("&Te\"stova' 'v<eta>.")).to.deep.equal("&amp;Te&quot;stova&#039; &#039;v&lt;eta&gt;.");
		});
	});
});
