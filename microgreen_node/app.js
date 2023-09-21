const express = require('express');

const app = express();

// Home route
app.get('/', (req, res) => {
    // return the index.html file
    res.sendFile(__dirname + '/views/index.html');
});

// Listen on port 3000
app.listen(3000, () => {
    console.log('Server listening on port 3000');
});