# Project Badge
![75862d67ca51a042003c](https://github.com/user-attachments/assets/b6a4fa7a-4022-486d-8f5f-45f7e5a89343)

## ES6 Promises

**Level:** Amateur  
**By:** Johann Kerbrat, Engineering Manager at Uber Works  
**Weight:** 1  
**Migrated to checker v2:**  
Your score will be updated as you progress.

---

## Resources

Read or watch:

- **Promise**
- **JavaScript Promise: An introduction**
- **Await**
- **Async**
- **Throw / Try**

---

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The `await` operator
- How to use an `async` function

---

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest and the command `npm run test`
- Your code will be verified against lint using ESLint
- All of your functions must be exported

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
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli

# Install ESLint
npm install --save-dev eslint
```
## Configuration Files

### `package.json`

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

### `babel.config.js`

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

### `utils.js`

```bash

export function uploadPhoto() {
  return Promise.resolve({
    status: 200,
    body: 'photo-profile-1',
  });
}


export function createUser() {
  return Promise.resolve({
    firstName: 'Guillaume',
    lastName: 'Salva',
  });
}

```

### `eslintrc.js`

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
### and…
Don’t forget to run `$ npm install` when you have the `package.json`

## Response Data Format

`uploadPhoto` returns a response with the format
```
{
  status: 200,
  body: 'photo-profile-1',
}
```
`createUser` returns a response with the format

```
{
  firstName: 'Guillaume',
  lastName: 'Salva',
}
```

---

## Tasks 

| Number | Name                        | Short Description                                                                                   | Name of the File               |
|--------|-----------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------|
| 0      | Keep every promise you make and only make promises you can keep | Return a Promise using the function prototype `getResponseFromAPI()`.                                 | `0-promise.js`                 |
| 1      | Don't make a promise...if you know you can't keep it | Return a promise based on a boolean value: resolve with an object or reject with an error message.    | `1-promise.js`                 |
| 2      | Catch me if you can!        | Handle a promise with resolve and reject cases, logging a specific message when the promise resolves. | `2-then.js`                    |
| 3      | Handle multiple successful promises | Use `uploadPhoto` and `createUser` functions to resolve promises and log specific information.       | `3-all.js`                     |
| 4      | Simple promise              | Return a resolved promise with an object containing `firstName` and `lastName`.                      | `4-user-promise.js`            |
| 5      | Reject the promises         | Return a promise rejecting with an error message based on the `fileName` argument.                   | `5-photo-reject.js`            |
| 6      | Handle multiple promises    | Call `signUpUser` and `uploadPhoto` and return an array with the status and value of each promise.    | `6-final-user.js`              |
| 7      | Load balancer               | Return the value from the promise that resolves first out of two provided promises.                  | `7-load_balancer.js`           |
| 8      | Throw an error              | Throw an error if the denominator is zero, otherwise return the division result.                     | `8-try.js`                     |
| 9      | Throw error / try catch     | Handle errors from a function and append results to an array with a final processing message.         | `9-try.js`                     |
| 10     | Await / Async               | Use async/await to handle promises from `uploadPhoto` and `createUser`, returning their responses.   | `100-await.js`                 |

