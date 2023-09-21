[![Python package](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-package.yml/badge.svg)](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-package.yml)
[![Python application](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-app.yml/badge.svg)](https://github.com/webmaster-exit-1/apkbackup/actions/workflows/python-app.yml)

>
        \     _ \  |  / __ )             |                
       _ \   |   | ' /  __ \   _` |  __| |  / |   | __ \  
      ___ \  ___/  . \  |   | (   | (      <  |   | |   | 
    _/    _\_|    _|\_\____/ \__,_|\___|_|\_\\__,_| .__/  
                                                    _|     


# APKBackup

A simple python module to find every **APK** file on your phone and save it to your PC via **ADB**.

## Installation

```bash
git clone https://github.com/webmaster-exit-1/apkbackup
cd apkbackup
pip install -e .
```

### Usage: 

Assuming your phone is connected to your PC either by cable or wifi and you have the software installed to run the `adb` command.
With debug mode enabled and you have accepted/trusted the network you are connected to.
All you'll need to do is to execute `apkbackup` and every apk file in your phone will now be in a folder called `backups` wherever you run the command from.

### Contributing

If you wanna tweak my code, go for it! Here's how:

* Fork it 
* Create your feature branch (`git checkout -b feature/fooBar`)
* Commit your changes (`git commit -am 'Add some fooBar'`)
* Push to the branch (`git push origin feature/fooBar`)
* Create a new pull request
