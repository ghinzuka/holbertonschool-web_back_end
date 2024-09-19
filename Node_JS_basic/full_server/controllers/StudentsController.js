// create a class named StudentsController. Add two static methods:
// The first one is getAllStudents:
// The method accepts request and response as argument
// It should return a status 200
// It calls the function readDatabase from the utils file, and display in the page:
// First line: This is the list of our students
// And for each field (order by alphabetic order case insensitive),
// a line that displays the number of students in the field, and the list of first names
// (ordered by appearance in the database file)
// with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
// If the database is not available, it should
// return a status 500 and the error message Cannot load the database
// The second one is getAllStudentsByMajor:
// The method accepts request and response as argument
// It should return a status 200
// It uses a parameter that the user can pass to the browser major.
// The major can only be CS or SWE. If the user is passing another parameter,
// the server should return a 500 and the error Major parameter must be CS or SWE
// It calls the function readDatabase from the utils file,
// and display in the page the list of first names for the students
// (ordered by appearance in the database file)
// in the specified field List: LIST_OF_FIRSTNAMES_IN_THE_FIELD
// If the database is not available, it should
// return a status 500 and the error message Cannot load the database

const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase('database.csv');
      let response = 'This is the list of our students\n';
      const fields = Object
        .keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      fields.forEach((field) => {
        const list = students[field].join(', ');
        response += `Number of students in ${field}: ${students[field].length}. List: ${list}\n`;
      });

      res.status(200).send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.query;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase('database.csv');
      const list = students[major] ? students[major].join(', ') : '';

      res.status(200).send(`List: ${list}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
