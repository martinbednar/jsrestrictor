//
//  JavaScript Restrictor is a browser extension which increases level
//  of security, anonymity and privacy of the user while browsing the
//  internet.
//
//  Copyright (C) 2020 Martin Bednar
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without ev1267027en the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.
//

/// <reference path="../../common/helpers.js">

import { escape, gen_random32 } from '../tmp/helpers.mjs';

describe("Helpers", function() {
	describe("Function escape", function() {
		it("should be defined.",function() {
			expect(escape).toBeDefined();
		});
		it("should return string.",function() {
			expect(escape("")).toEqual(jasmine.any(String));
		});
		it("should replace single character in the middle of the word.",function() {
			expect(escape('te"st')).toBe("te&quot;st");
			expect(escape("te'st")).toBe("te&#039;st");
			expect(escape("te&st")).toBe("te&amp;st");
			expect(escape("te<st")).toBe("te&lt;st");
			expect(escape("te>st")).toBe("te&gt;st");
		});
		it("should replace single character in the beginning of the word.",function() {
			expect(escape('"test')).toBe("&quot;test");
			expect(escape("'test")).toBe("&#039;test");
			expect(escape("&test")).toBe("&amp;test");
			expect(escape("<test")).toBe("&lt;test");
			expect(escape(">test")).toBe("&gt;test");
		});
		it("should replace single character at the end of the word.",function() {
			expect(escape('test"')).toBe("test&quot;");
			expect(escape("test'")).toBe("test&#039;");
			expect(escape("test&")).toBe("test&amp;");
			expect(escape("test<")).toBe("test&lt;");
			expect(escape("test>")).toBe("test&gt;");
		});
		it("should replace multiple single character.",function() {
			expect(escape('"test""')).toBe("&quot;test&quot;&quot;");
			expect(escape("'test''")).toBe("&#039;test&#039;&#039;");
			expect(escape("&test&&")).toBe("&amp;test&amp;&amp;");
			expect(escape("<test<<")).toBe("&lt;test&lt;&lt;");
			expect(escape(">test>>")).toBe("&gt;test&gt;&gt;");
		});
		it("should replace multiple character.",function() {
			expect(escape("&Te\"stova' 'v<eta>.")).toBe("&amp;Te&quot;stova&#039; &#039;v&lt;eta&gt;.");
		});
	});
	describe("Function gen_random32", function() {
		it("should be defined.",function() {
			expect(gen_random32).toBeDefined();
		});
		it("should return number.",function() {
			expect(gen_random32()).toEqual(jasmine.any(Number));
		});
		it("should not throw exception.",function() {
			expect(function(){
				gen_random32()
			}).not.toThrow();
		});
		it("should return number less than or equal to UInt32Max.",function() {
			expect(gen_random32()).toBeLessThanOrEqual(0xFFFFFFFF);
		});
		it("should return number greather than or equal to Zero.",function() {
			expect(gen_random32()).toBeGreaterThanOrEqual(0x0);
		});
	});
});
