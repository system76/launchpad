#!/usr/bin/env python3

""" launchpad - basic tool for testing System76 Launch Keyboards

Copyright (c) 2022 Ian Santopietro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import subprocess
from pathlib import Path

from . import gui
from . import data

def run():
    win = gui.LaunchpadWindow()
    gui.Gtk.main()

def setup():
    desktop_path = Path(
        Path.home(),
        '.local',
        'share',
        'applications',
        'com.system76.launchpad.desktop'
    )
    with open(desktop_path, mode='w') as desktop_file:
        desktop_file.write(data.desktop_file)
    
    subprocess(
        [
            'pkexec',
            'mv',
            '/usr/lib/udev/rules.d/85-brltty.rules',
            '/usr/lib/udev/rules.d/85-brltty.disabled'
        ]
    )

    with open('/tmp/udevrule', mode='w') as udev_rule_file:
        udev_rule_file.write(data.udev_rule)
    subprocess.run(
        [
            'pkexec',
            'cp',
            '/tmp/udevrule',
            '/usr/lib/udev/rules.d/'
        ]
    )