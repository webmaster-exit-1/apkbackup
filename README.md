[![Python package](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-package.yml/badge.svg)](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-package.yml)
[![Python application](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-app.yml/badge.svg)](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-app.yml)
[![Pylint](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/pylint.yml/badge.svg)](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/pylint.yml)

>
        \     _ \  |  / __ )             |                
       _ \   |   | ' /  __ \   _` |  __| |  / |   | __ \  
      ___ \  ___/  . \  |   | (   | (      <  |   | |   | 
    _/    _\_|    _|\_\____/ \__,_|\___|_|\_\\__,_| .__/  
                                                    _|     


# APKBackup

A simple python module  to find, compress, and create an archive or backup of all the apk's on your phone via adb Android DeBug Bridge.

## Installation

```bash
pip install apkbackup
```

### Usage: 

#### Here's how to get started with APKBackup: 

Assuming your phone is connected to your pc or via adb wifi

```bash
adb usb
```

or

```bash
adb connect 192.168.0.999:5555
```

From within the python IDE

```py
from apkbackup import backup
backup.do_your_thing()
```

or as a command

```bash
apkbackup
```

### Contributing

If you wanna tweak my code, go for it! Here's how:

* Fork it 
* Create your feature branch (`git checkout -b feature/fooBar`)
* Commit your changes (`git commit -am 'Add some fooBar'`)
* Push to the branch (`git push origin feature/fooBar`)
* Create a new pull request
