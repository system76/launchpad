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

import gi

gi.require_versions({
    'Gtk': '3.0',
})

from gi.repository import Gtk

from .selma import Selma
from . import data

class LaunchpadWindow(Gtk.Window):

    def __init__(self) -> None:
        super().__init__()

        self.connect('destroy', Gtk.main_quit)

        self.selma = Selma()
        self.set_title("Launchpad")
        
        layout_grid = Gtk.Grid()
        layout_grid.props.margin = 36
        layout_grid.set_row_spacing(6)
        layout_grid.set_column_spacing(6)
        self.add(layout_grid)

        connect_button = Gtk.Button.new_with_label("Connect")
        self.status_text = Gtk.Label.new('Disconnected')

        connect_button.connect('clicked', self.toggle_connection)
        
        layout_grid.attach(connect_button, 0, 0, 1, 1)
        layout_grid.attach(self.status_text, 1, 0, 1, 1)

        helper_label = Gtk.Label.new("Select a product below for Selma testing")

        launch_button = Gtk.Button.new_with_label("Launch")
        lite_button = Gtk.Button.new_with_label("Launch Lite")
        heavy_button = Gtk.Button.new_with_label("Launch Heavy")
        heavy_button.set_sensitive(False)

        for button in (launch_button, lite_button, heavy_button):
            Gtk.StyleContext.add_class(
                button.get_style_context(),
                'suggested-action'
            )

        estop_button = Gtk.Button.new_with_label("STOP")
        estop_button.set_size_request(-1, 76)
        Gtk.StyleContext.add_class(
            estop_button.get_style_context(),
            'destructive-action'
        )

        layout_grid.attach(helper_label, 0, 1, 2, 1)
        layout_grid.attach(launch_button, 0, 2, 1, 1)
        layout_grid.attach(lite_button, 1, 2, 1, 1)
        layout_grid.attach(heavy_button, 0, 3, 1, 1)

        layout_grid.attach(estop_button, 0, 4, 2, 1)

        reset_button = Gtk.Button.new_with_label('RESET')
        reset_button.connect('clicked', self.do_reset)
        layout_grid.attach(reset_button, 0, 5, 2, 1)

        self.show_all()

        launch_button.connect('clicked', self.do_test, data.launch_testing_code)
        lite_button.connect('clicked', self.do_test, data.launch_testing_code)

        estop_button.connect('clicked', self.do_estop)
    
    def do_test(self, widget, data):
        self.selma.start_test(data)
    
    def do_estop(self, widget):
        self.selma.e_stop()
    
    def do_reset(self, widget):
        self.selma.reset()

    def toggle_connection(self, widget):
        if self.selma.port_open:
            self.selma.close_port()
        else:
            self.selma.open_port()
        
        if self.selma.port_open:
            widget.set_label("Disconnect")
            self.status_text.set_label(
                f'Connected to port {self.selma.serial_port.port}'
            )
        else:
            widget.set_label("Connect")
            self.status_text.set_label('Disconnected')

def run():
    win = LaunchpadWindow()
    Gtk.main()