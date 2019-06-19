var express = require('express');
var n2f = require('num2fraction');
var cors = require('cors');
var app = express();

var GPhoto = require('./gphoto.js');
var SHUTTER_SPEEDS = require('./shutters.js');

var gphoto = new GPhoto();

app.use(cors());
app.use(express.static('dist'));

app.post('/api/connect', async function (req, res) {
    try {
        await gphoto.connect();
    } catch {
        res.sendStatus(500);
        return;
    }

    res.sendStatus(200);
});

app.post('/api/interval', async function (req, res) {
    const { count, shutterSpeed, delay } = req.body;

    try {
        gphoto.runInterval(count, shutterSpeed, delay);
    } catch {
        res.sendStatus(503);
        return;
    }

    res.sendStatus(200);
});

app.get('/api/speeds', function (req, res) {
    res.json(Object.entries(SHUTTER_SPEEDS)
        .map(([key, value]) => ({ text: key, value: value }))
        .sort((a, b) => a.value - b.value));
});

app.listen(3000, function () {
    console.log('Listening on :3000...');
});