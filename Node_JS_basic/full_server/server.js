const express = require('express');
const routes = require('./routes/index');

const app = express();
const PORT = 1245;
const dbFile = process.argv[2];

app.set('dbFile', dbFile);

app.use('/', routes);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.export = app;
