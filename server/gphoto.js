const { spawn } = require('child_process');
const SHUTTER_SPEEDS = require('./shutters.js');
const debug = require('debug')('raspberry-nikon:gphoto');

const CMD = 'gphoto2';
const CFG_FLAG = '--set-config';

module.exports = class GPhoto {
    constructor() {
        this.busy = false;
    }

    async connect() {
        await this.runCommand([CFG_FLAG, 'capturetarget=1']);
    }

    runInterval(count, shutterSpeed, delay) {
        if (shutterSpeed === 52) {
            this.runBulb(count, shutterSpeed, delay);
        } else {
            this.runTime(count, shutterSpeed, delay);
        }
    }

    async runBulb(count, shutterSpeed, delay) {
        try {
            await this.runCommand([CFG_FLAG, 'shutterspeed=52']);
        } catch (error) {
            debug(error);
            return;
        }

        for (var i = 0; i < count; i++) {
            try {
                await this.runCommand([
                    CFG_FLAG,
                    'bulb=1',
                    `--wait-event=${shutterSpeed}s`,
                    CFG_FLAG,
                    'bulb=0',
                    `--wait-event=${delay}s`
                ]);
            } catch (error) {
                debug(error);
            }
        }
    }

    async runTime(count, shutterSpeed, delay) {
        try {
            await this.runCommand([CFG_FLAG, `shutterspeed=${SHUTTER_SPEEDS[shutterSpeed]}`]);
        } catch (error) {
            debug(error);
            return;
        }

        for (var i = 0; i < count; i++) {
            try {
                await this.runCommand(['--capture-image']);
            } catch (error) {
                debug(error);
            }
        }
    }

    runCommand(args) {
        return new Promise((resolve, reject) => {
            const proc = spawn(CMD, args);

            proc.stdout.on('data', data => {
                console.log(data.toString());
            });

            proc.on('exit', (code) => {
                if (code === 0) {
                    resolve();
                } else {
                    reject(new Error('gphoto exited with non-zero exit code.'));
                }
            });
        });
    }
};
