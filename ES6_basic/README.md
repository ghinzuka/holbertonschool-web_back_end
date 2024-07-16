# ES6 Basics

![08806026ef621f900121](https://github.com/user-attachments/assets/e247bbd2-379f-4e58-8529-e4e2296d6d8d)

**Novice**

**By:** Johann Kerbrat, Engineering Manager at Uber Works

**Weight:** 1

**Migrated to checker v2:** Your score will be updated as you progress.

## Concepts

For this project, we expect you to look at this concept:

- **Software Linter**

## Resources

**Read or watch:**

- [ECMAScript 6 - ECMAScript 2015](https://link_to_resource)
- [Statements and declarations](https://link_to_resource)
- [Arrow functions](https://link_to_resource)
- [Default parameters](https://link_to_resource)
- [Rest parameter](https://link_to_resource)
- [Javascript ES6 — Iterables and Iterators](https://link_to_resource)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

## Requirements

**General:**

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension
- Your code will be tested using the Jest Testing Framework
- Your code will be analyzed using the linter ESLint along with specific rules that we’ll provide
- All of your functions must be exported

## Setup

### Install NodeJS 12.11.x

In your home directory:

```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
# v12.11.1
npm -v
# 6.11.3
```
### Install Jest, Babel, and ESLint
in your project directory:

- Install Jest using: `npm install --save-dev jest`
- Install Babel using: `npm install --save-dev babel-jest @babel/core @babel/preset-env`
- Install ESLint using: `npm install --save-dev eslint`

## Configuration files
Please create the following 3 files (with the provided contents) in the project directory:

## `package.json`

```bash

{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```
## `babel.config.js`
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
## `.eslintrc.js`
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

## Finally…

Don’t forget to run npm install from the terminal of your project folder to install all necessary project dependencies.


| Number | Name                          | Short Description                                                                       | Name of the File                  |
|--------|-------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------|
| 0      | Const or let?                | Modify to use `const` and `let` for variable instantiation.                          | `0-constants.js`                 |
| 1      | Block Scope                   | Prevent variable overwriting in the conditional block.                                | `1-block-scoped.js`              |
| 2      | Arrow functions               | Rewrite standard function to use ES6 arrow syntax.                                   | `2-arrow.js`                     |
| 3      | Parameter defaults            | Condense function to one line using default parameter values.                          | `3-default-parameter.js`         |
| 4      | Rest parameter syntax         | Use rest parameter syntax to count the number of arguments.                           | `4-rest-parameter.js`            |
| 5      | The wonders of spread syntax  | Concatenate arrays and string characters using spread syntax.                         | `5-spread-operator.js`           |
| 6      | Take advantage of template literals | Rewrite return statement using template literals for string interpolation.           | `6-string-interpolation.js`      |
| 7      | Object property value shorthand | Use shorthand syntax for object properties in the budget object.                     | `7-getBudgetObject.js`           |
| 8      | No need to create empty objects | Use ES6 computed property names for the budget object.                               | `8-getBudgetCurrentYear.js`      |
| 9      | ES6 method properties          | Rewrite function to use ES6 method properties in the full budget object.             | `9-getFullBudget.js`             |
| 10     | For...of Loops               | Rewrite to use ES6’s `for...of` operator instead of `var`.                           | `10-loops.js`                    |
| 11     | Iterator                       | Create a function that returns an object with department names and employees.        | `11-createEmployeesObject.js`    |
| 12     | Let's create a report object   | Write a function to create a report object with employee counts by department.       | `12-createReportObject.js`       |

Baptiste Pouquerou