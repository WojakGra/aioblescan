#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# This file deals with INode #4 formatted messages
#
# Copyright (c) 2021 Jakub Wojdziak
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE


def parse(packet):
    peer = packet.retrieve("peer")
    rssi = packet.retrieve("rssi")
    #svc_data = packet.retrieve("Manufacturer Specific Data")
    #adv_payload = packet.retrieve("Adv Payload")
    if peer and rssi:
        mac = peer[0].val
        #uuid = svc_data[0].val
        #if "38034" == uuid:
        return parse_payload(mac, rssi[0].val)


def parse_payload(mac, rssi):
    #temp = int.from_bytes(payload[6:8], "big", signed=True) / 10.0
    #humidity = int.from_bytes(payload[8:9], "big")
    #battery = int.from_bytes(payload[9:10], "big")
    #battery_volts = int.from_bytes(payload[10:12], "big") / 1000.0
    #counter = int.from_bytes(payload[12:13], "big")
    return {
        "mac address": mac,
        #"temperature": temp,
        #"humidity": humidity,
        #"battery": battery,
        #"battery_volts": battery_volts,
        #"counter": counter,
        "rssi": rssi,
    }


class INode4(object):
    """Class defining the content of an INode4 advertisement."""

    def decode(self, packet):
        # Look for INode4 custom firmware advertisements
        result = parse(packet)
        return result
