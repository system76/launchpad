## Launchpad

A small utility to send built-in Gcode files through a serial port to a Selma 
Launch keyboard QC tester. 

## Installation

Easiest installation is via `pip` from git:

```shell
sudo apt install python3-pip python3-serial
sudo pip3 install git+https://github.com/system76/launchpad
```

Afterwards, set up the udev rules and Desktop file:

```shell
/usr/local/bin/launchpad_setup
```

You will be prompted several times for an authentication password. A reboot may
be required to ensure the udev rules take effect.


## Setup

Launchpad will load G-code for testing keyboards from the `~/Selma` folder. If
this folder does not exist, it will be created automatically. Each keyboard will 
need a G-code file in this folder for it to be testable. The files should be 
named as follows:

  * Launch - `launch.gcode`
  * Launch Lite - `launch_lite.gcode`
  * Launch Heavy - `launch_heavy.gcode`

Simply copy the file for each keyboard into the `Selma` folder within the home 
folder, and the button for that keyboard will be enabled for testing. 

Custom G-Code is also supported, however these will not be saveable. This is 
intended for testing experimental changes to G-Code before putting the updated 
testing code into production.

## Updates

To update Launchpad to the latest version, run `launchpad_update` from 
a terminal.