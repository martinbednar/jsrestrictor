"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const webextensions_api_mock_1 = __importDefault(require("webextensions-api-mock"));
const apis_1 = __importDefault(require("./apis"));
class WebExtensionsApiFake {
    constructor(options = {}) {
        this.apis = apis_1.default(options);
    }
    createBrowser() {
        return webextensions_api_mock_1.default();
    }
    fakeApi(browser) {
        this.apis.alarms.fakeApi(browser);
        this.apis.contextualIdentities.fakeApi(browser);
        this.apis.cookies.fakeApi(browser);
        this.apis.extension.fakeApi(browser);
        this.apis.i18n.fakeApi(browser);
        this.apis.runtime.fakeApi(browser);
        this.apis.storage.fakeApi(browser);
        this.apis.tabs.fakeApi(browser);
        this.apis.windows.fakeApi(browser);
    }
}
exports.WebExtensionsApiFake = WebExtensionsApiFake;
exports.default = (options = {}) => {
    const webextensionApiFake = new WebExtensionsApiFake(options);
    const browser = (options.browser ||
        webextensionApiFake.createBrowser());
    webextensionApiFake.fakeApi(browser);
    return browser;
};
