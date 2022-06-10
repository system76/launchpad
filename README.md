## Launchpad

A small utility to send built-in Gcode files through a serial port to a Selma 
Launch keyboard QC tester. 

## Installation

Easiest installation is via `pip` from git:

```shell
pip3 install git+https://github.com/system76/launchpad
```

Afterwards, set up the udev rules and Desktop file:

```shell
~/.local/bin/launchpad_setup
```

You will be prompted several times for an authentication password. A reboot may
be required to ensure the udev rules take effect.

