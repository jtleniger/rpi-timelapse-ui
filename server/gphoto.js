const { spawn } = require('child_process');

const CMD = 'gphoto2';
const CFG_FLAG = '--set-config';

module.exports = class GPhoto {
    constructor() {
        this.busy = false;
        this.runningCmd = null;
    }

    connect() {
        return new Promise((resolve, reject) => {
            const childProc = spawn(CMD, [CFG_FLAG, 'capturetarget=1']);

            childProc.stdout.on('data', data => {
                console.log(data.toString());
            });
            
            childProc.on('exit', (code) => {
                if (code === 0) {
                    resolve();
                } else {
                    reject();
                }
            });
        })
    }

    runInterval(count, shutterSpeed, delay) {
        
    }
}