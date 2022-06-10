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

import serial

from . import data

SERIAL_DEVICE = '/dev/ttyUSB0'
BAUD_RATE = 115200
PARITY = serial.PARITY_NONE
DATA_BITS = serial.EIGHTBITS
STOP_BITS = serial.STOPBITS_ONE
TIMEOUT = 30

def enc(data:str) -> bytes:
    """
    Returns input data encoded as bytes compatible with GRBL/Serial/Selma.

    Primarily a convenience function.

    Arguments:
        data:str - The data to be encoded
    
    Returns:
        `bytes` encoded for transmission over the serial port
    """
    return data.encode('ascii')

class Selma:
    """
    Main interface for telling Selma to test a keyboard (or stop testing).
    """

    def __init__(self) -> None:
        """Initialize the class"""
        self.port_open = False
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = BAUD_RATE
        self.serial_port.port = SERIAL_DEVICE
        self.serial_port.timeout = TIMEOUT
        self.serial_port.parity = PARITY
        self.serial_port.bytesize = DATA_BITS
        self.serial_port.stopbits = STOP_BITS
    
    def open_port(self) -> bool:
        """
        Opens the serial port.
        
        Returns `True` if the port was opened successfully
        """
        try:
            self.serial_port.open()
        except serial.SerialException:
            return False
        self.port_open = self.serial_port.is_open
        return self.port_open
    
    def close_port(self) -> bool:
        """ Close the port"""
        try:
            self.serial_port.close()
        except serial.SerialException:
            return True
        self.port_open = self.serial_port.is_open
        return self.port_open
    
    def send(self, data:str) -> bool:
        """ Send data over serial"""
        b_data = enc(data)
        self.serial_port.write(b_data)
        return True

    def e_stop(self) -> bool:
        """ E-Stop """
        self.send(data.e_stop_command)
        self.send(data.reset_command)

    def home_axes(self) -> bool:
        """ Perform a "Homing" cycle.
        
        Note: because of how Selma is set up, this doesn't actually Home anything.
        """
        self.send(data.zero_x_command)
        self.send(data.zero_y_command)
    
    def start_test(self) -> bool:
        """
        Start running a test.
        
        Returns `True` if successfully started
        """
        if not self.port_open:
            return False
        
        test_data = enc(data.launch_lite_testing_code)
        
        self.serial_port.write(test_data)
