import express from 'express';
import controllerRouting from './routes/index';

const app = express();
const PORT = 1245;

controllerRouting(app);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

export default app;
