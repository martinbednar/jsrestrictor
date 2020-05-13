const { default: browserFake } = require('webextensions-api-fake');
global.browser = browserFake();

global.chai = require("chai");
global.asserttype = require('chai-asserttype');
chai.use(asserttype);
global.expect = chai.expect;

global.rewire = require('rewire');
