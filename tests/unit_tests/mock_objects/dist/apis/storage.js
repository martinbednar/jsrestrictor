"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const makeStorage = () => {
    let _storage = {};
    return {
        async get(key) {
            if (!key) {
                return _storage;
            }
            const result = {};
            if (Array.isArray(key)) {
                key.map(akey => {
                    if (typeof _storage[akey] !== 'undefined') {
                        result[akey] = _storage[akey];
                    }
                });
            }
            else if (typeof key === 'object') {
                // TODO support nested objects
                Object.keys(key).map(oKey => {
                    if (typeof _storage[oKey] !== 'undefined') {
                        result[oKey] = _storage[oKey];
                    }
                    else {
                        result[oKey] = key[oKey];
                    }
                });
            }
            else {
                result[key] = _storage[key];
            }
            return result;
        },
        async set(key, value) {
            if (typeof key === 'object') {
                // TODO support nested objects
                Object.keys(key).map(oKey => {
                    _storage[oKey] = key[oKey];
                });
            }
            else {
                _storage[key] = value;
            }
        },
        async remove(key) {
            if (Array.isArray(key)) {
                key.map(aKey => {
                    delete _storage[aKey];
                });
            }
            else {
                delete _storage[key];
            }
        },
        async clear() {
            _storage = {};
        },
    };
};
exports.default = () => {
    return {
        fakeApi(browser) {
            ['local', 'sync', 'managed'].map(storageType => {
                const storage = makeStorage();
                browser.storage[storageType].get.callsFake(storage.get);
                browser.storage[storageType]._get = storage.get;
                browser.storage[storageType].set.callsFake(storage.set);
                browser.storage[storageType]._set = storage.set;
                browser.storage[storageType].remove.callsFake(storage.remove);
                browser.storage[storageType]._remove = storage.remove;
                browser.storage[storageType].clear.callsFake(storage.clear);
                browser.storage[storageType]._clear = storage.clear;
            });
        },
    };
};
