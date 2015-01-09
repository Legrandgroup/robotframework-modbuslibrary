#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu

from rfmodbuslib.common import RfModbusError
from rfmodbuslib import __lib_version__

class RfModbusRTU(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __lib_version__

    def __init__(self):
        self.master = None
        self.logger = modbus_tk.utils.create_logger("console")
        self.serial = None

    def __del__(self):
        try:
            self.serial.close()
        except:
            pass

    def _format_error(self, except_object):
        return u"Error: %s - code: %d" % (except_object, except_object.get_exception_code())

    def _process_error(self, except_object, msg="Modbus error"):
        error = self._format_error(except_object=except_object)
        self.logger.error(error)
        raise RfModbusError(msg=msg, detail=error)

    def open_connection(self, port='/dev/ttyUSB0', timeout=0.5, verbose=False):
        try:
            self.serial = serial.Serial(port, baudrate=9600, bytesize=8, parity='E', stopbits=1, xonxoff=0)
            self.logger.debug("Opening modbus connection...")
            self.master = modbus_rtu.RtuMaster(self.serial)
            self.master.set_verbose(verbose)
            self.master.set_timeout(float(timeout))
            self.logger.info("Opened modbus connection.")
        except modbus_tk.modbus.ModbusError, error:
            self._process_error(except_object=error, msg="Could not open connection")

    def close_connection(self):
        try:
            try:
                self.logger.info("Closing modbus connection...")
                self.serial.close()
            except:
                self.logger.debug("Error when closing serial line connection.")
        finally:
            self.logger.debug("Closed modbus connection.")

    def read_holding_registers(self, slave, starting_address, quantity_of_x=0):
        try:
            slave = int(slave)
            starting_address = int(starting_address)
            quantity_of_x = int(quantity_of_x)
            result = self.master.execute(slave=slave, function_code=cst.READ_HOLDING_REGISTERS,
                                        starting_address=starting_address, quantity_of_x=quantity_of_x)
            return result
        except modbus_tk.modbus.ModbusError, error:
            self._process_error(except_object=error, msg="Could not read register: %d" % starting_address)

    def write_multiple_registers(self, slave, starting_address, datas):
        try:
            self.logger.debug("write multiple register")
            slave = int(slave)
            starting_address = int(starting_address)
            registers = list()
            registers = eval(datas)
            self.master.execute(slave=slave, function_code=cst.WRITE_MULTIPLE_REGISTERS,
                                starting_address=starting_address, output_value=registers)
        except modbus_tk.modbus.ModbusError, error:
            self._process_error(except_object=error,
                    msg="Could not write datas (%s) to register (%d)" % (datas, starting_address))

