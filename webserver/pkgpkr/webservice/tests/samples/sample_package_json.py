"""
Mock data used in unit tests
"""

SAMPLE_PACKAGE_JSON = """
{
    "name": "express",
    "description": "Fast, unopinionated, minimalist web framework",
    "version": "4.17.1",
    "author": "TJ Holowaychuk <tj@vision-media.ca>",
    "contributors": [
        "Aaron Heckmann <aaron.heckmann+github@gmail.com>",
        "Ciaran Jessup <ciaranj@gmail.com>",
        "Douglas Christopher Wilson <doug@somethingdoug.com>",
        "Guillermo Rauch <rauchg@gmail.com>",
        "Jonathan Ong <me@jongleberry.com>",
        "Roman Shtylman <shtylman+expressjs@gmail.com>",
        "Young Jae Sim <hanul@hanul.me>"
    ],
    "license": "MIT",
    "repository": "expressjs/express",
    "homepage": "http://expressjs.com/",
    "keywords": [
        "express",
        "framework",
        "sinatra",
        "web",
        "rest",
        "restful",
        "router",
        "app",
        "api"
    ],
    "dependencies": {
        "accepts": "~1.3.7",
        "array-flatten": "1.1.1",
        "body-parser": "1.19.0",
        "content-disposition": "0.5.3",
        "content-type": "~1.0.4",
        "cookie": "0.4.0",
        "cookie-signature": "1.0.6",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "~1.1.2",
        "fresh": "0.5.2",
        "merge-descriptors": "1.0.1",
        "methods": "~1.1.2",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.3",
        "path-to-regexp": "0.1.7",
        "proxy-addr": "~2.0.5",
        "qs": "6.7.0",
        "range-parser": "~1.2.1",
        "safe-buffer": "5.1.2",
        "send": "0.17.1",
        "serve-static": "1.14.1",
        "setprototypeof": "1.1.1",
        "statuses": "~1.5.0",
        "type-is": "~1.6.18",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
    },
    "devDependencies": {
        "after": "0.8.2",
        "connect-redis": "3.4.1",
        "cookie-parser": "~1.4.4",
        "cookie-session": "1.3.3",
        "ejs": "2.6.1",
        "eslint": "2.13.1",
        "express-session": "1.16.1",
        "hbs": "4.0.4",
        "istanbul": "0.4.5",
        "marked": "0.6.2",
        "method-override": "3.0.0",
        "mocha": "5.2.0",
        "morgan": "1.9.1",
        "multiparty": "4.2.1",
        "pbkdf2-password": "1.2.1",
        "should": "13.2.3",
        "supertest": "3.3.0",
        "vhost": "~3.0.2"
    },
    "engines": {
        "node": ">= 0.10.0"
    },
    "files": [
        "LICENSE",
        "History.md",
        "Readme.md",
        "index.js",
        "lib/"
    ],
    "scripts": {
        "lint": "eslint .",
        "test": "mocha --require test/support/env --reporter spec --bail --check-leaks test/ test/acceptance/",
        "test-ci": "istanbul cover node_modules/mocha/bin/_mocha --report lcovonly -- --require test/support/env --reporter spec --check-leaks test/ test/acceptance/",
        "test-cov": "istanbul cover node_modules/mocha/bin/_mocha -- --require test/support/env --reporter dot --check-leaks test/ test/acceptance/",
        "test-tap": "mocha --require test/support/env --reporter tap --check-leaks test/ test/acceptance/"
    }
}
"""