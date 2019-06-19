const { spawn } = require('child_process');
const SHUTTER_SPEEDS = require('./shutters.js');

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
        console.log('running interval')
        debugger;
        if (shutterSpeed == 52) {
            runBulb(count, shutterSpeed, delay)
        } else {
            runTime(count, shutterSpeed, delay)
        }
    }

    async runBulb(count, shutterSpeed, delay) {
        await runCommand([CFG_FLAG, 'shutterspeed=52'])

        for(var i = 0; i < count; i++) {
            await runCommand([
                CFG_FLAG,
                'bulb=1',
                `--wait-event=${duration}s`,
                CFG_FLAG,
                'bulb=0',
                `--wait-event=${spacing}s`
            ])
        }
    }

    async runTime(count, shutterSpeed, delay) {
        console.log('Starting interval');
        await runCommand([CFG_FLAG, `shutterspeed=${SHUTTER_SPEEDS[shutterSpeed]}`])

        for(var i = 0; i < count; i++) {
            await runCommand(['--capture-image'])
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
                    reject();
                }
            });
        })
    }
}