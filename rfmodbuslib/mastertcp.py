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

import logging

import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp

from rfmodbuslib.master import RfModbusMaster

class RfModbusMasterTCP(RfModbusMaster):
    """
        RfModbusMasterTCP class implements a modbus master which can communicate with slaves
        through a socket
    """

    def __init__(self, debug_level=logging.NOTSET):
        super(RfModbusMasterTCP, self).__init__(debug_level=debug_level)

    def open_connection(self, host="127.0.0.1", port=502, timeout_in_sec=5.0):
        """
            Open a modbus connection over a socket
        """
        try:
            self.logger.debug("Opening modbus connection over TCP...")
            self.master = modbus_tcp.TcpMaster(host=host, port=port, timeout_in_sec=timeout_in_sec)
            self.logger.info("Opened modbus connection over TCP.")
        except (modbus_tk.modbus.ModbusError, OSError) as error:
            self._process_error(except_object=error, msg="Could not open connection")


