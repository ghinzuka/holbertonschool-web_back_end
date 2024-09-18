
# NodeJS Basics
 **Amateur**
 By: Johann Kerbrat, Engineering Manager at Uber Works
 Weight: 1
 Migrated to checker v2: 
 Your score will be updated as you progress.


## Resources
Read or watch:

[Node JS getting started](https://intranet.hbtn.io/rltoken/RqwwGmqIE4M3WwjqXusJ7w)
[Process API doc](https://intranet.hbtn.io/rltoken/TyodG31Rx3XIiGE7HnxNYw)
[Child process](https://intranet.hbtn.io/rltoken/Ic5-12q1xFd74_0psW4CdQ)
[Express getting started](https://intranet.hbtn.io/rltoken/Bi4zX1TeHY2RF5lLYgKspg)
[Mocha documentation](https://intranet.hbtn.io/rltoken/eBgT_wcT40RgCLtYXuRpvw)
[Nodemon documentation](https://intranet.hbtn.io/rltoken/rlx9PqRqSQkA6v6ZJmYKNw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- run javascript using NodeJS
- use NodeJS modules
- use specific Node JS module to read files
- use process to access command line arguments and the environment
- create a small HTTP server using Node JS
- create a small HTTP server using Express JS
- create advanced routes with Express JS
- use ES6 with Node JS with Babel-node
- use Nodemon to develop faster
- Requirements
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using node (version 20.x.x)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Your code will be tested using Jest and the command npm run test
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test
- All of your functions/classes must be exported by using this format: module.exports = myFunction;

## Provided files

### database.csv
```bash
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
```

### package.json
```bash
{
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
      "babel-cli": "^6.26.0",
      "babel-preset-env": "^1.7.0",
      "lint": "*",
      "eslint": "^6.8.0",
      "eslint-config-airbnb-base": "^14.2.1",
      "eslint-plugin-import": "^2.29.1",
      "eslint-plugin-jest": "^22.21.0",
      "nodemon": "^2.0.22",
      "chai": "^4.4.1",
      "mocha": "^6.2.3",
      "request": "^2.88.2",
      "sinon": "^7.5.0"
  }
}
```

### babel.config.js

```bash
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```

### .eslintrc.js

```bash
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
```

and…
Don’t forget to run $ npm install when you have the package.json