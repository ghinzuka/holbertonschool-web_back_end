# ES6 Classes

![817248fb77fb5c2cef3f](https://github.com/user-attachments/assets/b785c2ba-bd58-479b-af65-1b6e8a6fb60f)

**Amateur**  
**By:** Johann Kerbrat, Engineering Manager at Uber Works  
**Weight:** 1  
**Migrated to checker v2:**   
Your score will be updated as you progress.

## Resources
**Read or watch:**
- [Classes](link-to-classes-resource)
- [Metaprogramming](link-to-metaprogramming-resource)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest and the command `npm run test`
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`

## Setup

### Install NodeJS 12.11.x
(in your home directory):
```sh
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
# v12.11.1
npm -v
# 6.11.3
```

### Install Jest, Babel, and ESLint
(In your project directory:)
```bash
# Install Jest
npm install --save-dev jest

# Install Babel
npm install --save-dev babel-jest @babel/core @babel/preset-env

# Install ESLint
npm install --save-dev eslint
```
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

# Tasks

| Number | Name                           | Short Description                                                                                         | File Name               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------|
| 0      | You used to attend a place like this at some point | Implement a `ClassRoom` class with an attribute `maxStudentsSize`                                           | `0-classroom.js`        |
| 1      | Let's make some classrooms     | Implement a function `initializeRooms` that returns an array of 3 `ClassRoom` objects                       | `1-make_classrooms.js`  |
| 2      | A Course, Getters, and Setters | Implement a `HolbertonCourse` class with attributes `name`, `length`, and `students`, and their getters/setters | `2-hbtn_course.js`      |
| 3      | Methods, static methods, computed methods names..... MONEY | Implement a `Currency` class with attributes `code` and `name`, and a method `displayFullCurrency`         | `3-currency.js`         |
| 4      | Pricing                        | Implement a `Pricing` class with attributes `amount` and `currency`, a method `displayFullPrice`, and a static method `convertPrice` | `4-pricing.js`          |
| 5      | A Building                     | Implement an abstract `Building` class with an attribute `sqft`, and a method `evacuationWarningMessage`    | `5-building.js`         |
| 6      | Inheritance                    | Implement a `SkyHighBuilding` class extending `Building` with attributes `sqft` and `floors`, and an overridden method `evacuationWarningMessage` | `6-sky_high.js`         |
| 7      | Airport                        | Implement an `Airport` class with attributes `name` and `code`, and a default string description returning the airport code | `7-airport.js`          |
| 8      | Primitive - Holberton Class    | Implement a `HolbertonClass` with attributes `size` and `location`, and custom type casting to `Number` and `String` | `8-hbtn_class.js`       |
| 9      | Hoisting                       | Fix the provided code to make it work correctly with the `HolbertonClass` and `StudentHolberton` classes   | `9-hoisting.js`         |
| 10     | Vroom                          | Implement a `Car` class with attributes `brand`, `motor`, and `color`, and a method `cloneCar`              | `10-car.js`             |
