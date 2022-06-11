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

udev_rule = """
SUBSYSTEM=="tty", ATTRS:{product}=="USB2.0Serial", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", MODE:="0666"
"""

desktop_file = """[Desktop Entry]
Type=Application
Name=Launchpad
Exec=launchpad
Terminal=false
Icon=input-keyboard
Categories=Utilities;

"""

launch_testing_code = """
((10\\1)
(T2  D=3.175 CR=0 - ZMIN=4.182 - fl.//at end mill)
G90 G94
G17
G21

(2D Contour8)
G54
G1 X-197. Y0. F5000.
S10000 M3
G91
Y-307. F1000.
Y307.
X38.
Y-307.
Y307.
X38.
Y-307.
Y307.
M5
G90
X-197. 

M30
"""

feed_stop_command:str = '!\n'
air_stop_command:str = 'M5\n'
e_stop_command:str = '\x18'
reset_command:str = '$X\n'
zero_command:str = 'G10 L20 X0 Y0 Z0\n'
