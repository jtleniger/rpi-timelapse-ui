var express = require('express');
var cors = require('cors');
var bodyParser = require('body-parser');
var app = express();
var debug = require('debug')('raspberry-nikon:server');

var GPhoto = require('./gphoto.js');
var SHUTTER_SPEEDS = require('./shutters.js');

var gphoto = new GPhoto();

app.use(bodyParser.json());
app.use(cors());
app.use(express.static('dist'));

app.post('/api/connect', async function(req, res) {
    try {
        await gphoto.connect();
    } catch (error) {
        debug(error);
        res.status(500);
        res.send('Could not connect to camera.');
        return;
    }

    res.sendStatus(200);
});

app.post('/api/interval', async function(req, res) {
    const { count, speed, delay, useBulb } = req.body;
    
    if (useBulb) {
        gphoto.runBulb(count, speed, delay);
    } else {
        gphoto.runTime(count, speed, delay);
    }

    res.sendStatus(200);
});

app.get('/api/status', function(req, res) {

});

app.get('/api/speeds', function(req, res) {
    res.json(Object.entries(SHUTTER_SPEEDS)
        .map(([key, value]) => ({ text: value, value: key }))
        .sort((a, b) => a.value - b.value));
});

app.listen(3000, function() {
    console.log('Listening on :3000...');
});
