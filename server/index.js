var express = require('express');
var app = express();

var GPhoto = require('./gphoto.js');

var gphoto = new GPhoto();

app.use(express.static('dist'));

app.get('/connect', async function (req, res) {
    try {
        await gphoto.connect();
    }
    catch {
        res.sendStatus(500);
        return;
    }

    res.sendStatus(200);
});

app.listen(3000, function () {
    console.log('Listening on :3000...');
});