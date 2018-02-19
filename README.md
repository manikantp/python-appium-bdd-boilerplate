# Python boilerplate project for BDD using Appium

## Getting started

This boilerplate requires `python3` and `virtualenv`, you can install them by doing:

1. `brew update`
1. `brew install python3`
1. `pip3 install virtualenv`

For Appium to fully work on Android, you'll need:

1. Java JDK
1. Android Studio
1. [Android home configured](https://stackoverflow.com/questions/19986214/setting-android-home-enviromental-variable-on-mac-os-x)


To setup your environment to run the tests do:
1. `bash setup.sh`

To run the tests execute:
1. `cd tests`
1. `behave`

PyCharm:
1. Remember to add the boilerenv interpreter to your PyCharm

Saucelabs:
1. In case you push your access key, regenerate it (and don't push) with:  
    `curl -X POST -u USERNAME:ACCESS_KEY https://saucelabs.com/rest/v1/users/USERNAME/accesskey/change`

Appium Capabilities: https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md