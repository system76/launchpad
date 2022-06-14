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

