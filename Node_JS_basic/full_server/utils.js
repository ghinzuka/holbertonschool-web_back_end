// create a function named readDatabase that accepts a path and returns a Promise
// When the file is not accessible, it should reject the promise with the error
// if file can be read, it should return an object of arrays of the firstname of students per fields
// It should read the database asynchronously

const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    const lines = data.trim().split('\n').filter((line) => line.length > 0);
    lines.shift();

    if (lines.length === 0) {
      throw new Error('No data in the database');
    }

    const studentFields = {};

    lines.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!studentFields[field]) {
        studentFields[field] = [];
      }
      studentFields[field].push(firstname);
    });

    return studentFields;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

export default readDatabase;
