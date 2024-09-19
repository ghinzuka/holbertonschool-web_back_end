// Create a class named AppController. Add a static method named getHomepage
// The method accepts request and response as argument.
// It returns a 200 status and the message Hello Holberton School!

class AppController {
  static getHomepage(req, res) {
    res.status(200);
    res.send('Hello Holberton School!');
  }
}
module.exports = AppController;
