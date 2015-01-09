#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2015 Legrand Group
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import serial
import logging

import modbus_tk
import modbus_tk.modbus_rtu as modbus_rtu

from rfmodbuslib.master import RfModbusMaster

class RfModbusMasterRTU(RfModbusMaster):
    """
        RfModbusMasterRTU class implements a modbus master which can communicate with slaves
        through a serial line
    """

    def __init__(self, debug_level=logging.NOTSET):
        super(RfModbusMasterRTU, self).__init__(debug_level=debug_level)
        self.serial = None

    def open_connection(self, port='/dev/ttyUSB0', timeout=0.5, verbose=False):
        """
            Open a modbus connection over a serial line
        """
        try:
            self.logger.debug("Creating serial interface...")
            self.serial = serial.Serial(port, baudrate=9600, bytesize=8, parity='E', stopbits=1, xonxoff=0)
            self.logger.debug("Opening modbus connection...")
            self.master = modbus_rtu.RtuMaster(self.serial)
            self.master.set_verbose(verbose)
            self.master.set_timeout(float(timeout))
            self.logger.info("Opened modbus connection.")
        except (modbus_tk.modbus.ModbusError, OSError) as error:
            self._process_error(except_object=error, msg="Could not open connection")

