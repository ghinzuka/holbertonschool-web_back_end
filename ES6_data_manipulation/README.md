# ES6 Data Manipulation
![6ab7bec4727cb5c91257](https://github.com/user-attachments/assets/7f2fa239-dbf2-4ce4-85b2-33179711ae8f)

**Level**: Amateur  
**By**: Johann Kerbrat, Engineering Manager at Uber Works  
**Weight**: 1  
**Migrated to checker v2**: Your score will be updated as you progress.

## Resources
Read or watch:
- [Array](#)
- [Typed Array](#)
- [Set Data Structure](#)
- [Map Data Structure](#)
- [WeakMap](#)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The Set, Map, and Weak link data structures

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, Visual Studio Code
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest and the command `npm run test`
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`
- All of your functions must be exported

## Setup
### Install NodeJS 20.x.x  
(in your home directory):

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```

### Install Jest, Babel, and ESLint

in your project directory:

* Install Jest using: ```npm install --save-dev jest```
* Install Babel using: ```npm install --save-dev babel-jest @babel/core @babel/preset-env```
* Install ESLint using: ```npm install --save-dev eslint```

### Configuration Files

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
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
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

## `eslintrc.js`

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
## and…
Don’t forget to run `$ npm install` when you have the `package.json`

---

## Tasks

| Number | Name                       | Short Description                                                                                  | Name of the File                |
|--------|----------------------------|----------------------------------------------------------------------------------------------------|---------------------------------|
| 0      | Basic list of objects      | Create a function named `getListStudents` that returns an array of objects with `id`, `firstName`, and `location`. | `0-get_list_students.js`        |
| 1      | More mapping               | Create a function `getListStudentIds` that returns an array of ids from a list of objects.          | `1-get_list_student_ids.js`     |
| 2      | Filter                     | Create a function `getStudentsByLocation` that returns an array of objects located in a specific city. | `2-get_students_by_loc.js`      |
| 3      | Reduce                     | Create a function `getStudentIdsSum` that returns the sum of all the student ids.                   | `3-get_ids_sum.js`              |
| 4      | Combine                    | Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade. | `4-update_grade_by_city.js`     |
| 5      | Typed Arrays               | Create a function `createInt8TypedArray` that returns a new ArrayBuffer with an Int8 value at a specific position. | `5-typed_arrays.js`             |
| 6      | Set data structure         | Create a function `setFromArray` that returns a Set from an array.                                  | `6-set.js`                      |
| 7      | More set data structure    | Create a function `hasValuesFromArray` that returns a boolean if all the elements in the array exist within the set. | `7-has_array_values.js`         |
| 8      | Clean set                  | Create a function `cleanSet` that returns a string of all the set values that start with a specific string. | `8-clean_set.js`                |
| 9      | Map data structure         | Create a function `groceriesList` that returns a map of groceries with specified items and quantities. | `9-groceries_list.js`           |
| 10     | More map data structure    | Create a function `updateUniqueItems` that returns an updated map for all items with initial quantity at 1. | `10-update_uniq_items.js`       |

baptiste pouquerou
