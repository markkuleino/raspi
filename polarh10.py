# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:55:25 2020

@author: MarkkuLeino
"""

#bluetoothctl
# agent on 
# scan on
#[NEW] Device EF:B7:AA:FC:96:73 Polar H10 690A1321
#
# pair EF:B7:AA:FC:96:73
# trust EF:B7:AA:FC:96:73
# EF:B7:AA:FC:96:73: Polar H10 690A1321


import asyncio
from bleak import discover

async def run():
    devices = await discover()
    for d in devices:
        print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

#
#
#
#
#
#


import asyncio
from bleak import BleakClient

address = "EF:B7:AA:FC:96:73"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))


#
#
#
#
#

https://github.com/polarofficial/create-mobile-app-for-polar-sensors
 Sensor is measuring heart rate value once in a second and sends HR value (uint8) as 
 a Heart Rate Measurement Notification. In addition, Polar H10 Sensor support 
 RR Intervals (unit of 1/1024 seconds), 
 but not energy expenditure value in Heart Rate Characteristic. 
 In case of the skin contact is absent for 20-30 seconds, 
 the Sensor will start termination of BLE connection and switches back to standby mode to save power.


https://github.com/polarofficial/polar-ble-sdk
 H10 Heart rate sensor
 Most accurate Heart rate sensor in the markets. The H10 is used in the 
 Getting started section of this page. Store page

 H10 heart rate sensor available data types
 -From version 3.0.35 onwards.
 -Heart rate as beats per minute. RR Interval in ms and 1/1024 format.
 -Electrocardiography (ECG) data in µV. Default epoch for timestamp is 1.1.2000
 -Accelerometer data with samplerates of 25Hz, 50Hz, 100Hz and 200Hz and 
  range of 2G, 4G and 8G. Axis specific acceleration data in mG. 
  Default epoch for timestamp is 1.1.2000
 -Start and stop of internal recording and request for internal recording status. 
  Recording supports RR, HR with one second sampletime or HR with five second sampletime.
 -List, read and remove for stored internal recording 
  (sensor supports only one recording at the time).


#
#
#
#
#








Get Services...

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service004c
        0000feee-0000-1000-8000-00805f9b34fb
        Polar Electro Oy

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service004c/char0053
        fb005c53-02e7-f387-1cad-8acd2d8df0c8
        Unknown

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service004c/char0050
        fb005c52-02e7-f387-1cad-8acd2d8df0c8
        Unknown

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service004c/char0050/desc0052
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service004c/char004d
        fb005c51-02e7-f387-1cad-8acd2d8df0c8
        Unknown

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service004c/char004d/desc004f
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0045
        fb005c80-02e7-f387-1cad-8acd2d8df0c8
        Unknown

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0045/char0049
        fb005c82-02e7-f387-1cad-8acd2d8df0c8
        Unknown

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0045/char0049/desc004b
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0045/char0046
        fb005c81-02e7-f387-1cad-8acd2d8df0c8
        Unknown

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0045/char0046/desc0048
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service003f
        6217ff4b-fb31-1140-ad5a-a45545d7ecf3
        Unknown

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service003f/char0042
        6217ff4d-91bb-91d0-7e2a-7cd3bda8a1f3
        Unknown

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service003f/char0042/desc0044
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service003f/char0040
        6217ff4c-c8ec-b1fb-1380-3ad986708e2d
        Unknown

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c
        0000180a-0000-1000-8000-00805f9b34fb
        Device Information

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char0039
        00002a23-0000-1000-8000-00805f9b34fb
        System ID

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char0037
        00002a28-0000-1000-8000-00805f9b34fb
        Software Revision String

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char0035
        00002a26-0000-1000-8000-00805f9b34fb
        Firmware Revision String

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char0033
        00002a27-0000-1000-8000-00805f9b34fb
        Hardware Revision String

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char0031
        00002a25-0000-1000-8000-00805f9b34fb
        Serial Number String

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char002f
        00002a24-0000-1000-8000-00805f9b34fb
        Model Number String

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service002c/char002d
        00002a29-0000-1000-8000-00805f9b34fb
        Manufacturer Name String

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014
        0000181c-0000-1000-8000-00805f9b34fb
        User Data

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char002a
        00002aa2-0000-1000-8000-00805f9b34fb
        Language

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0028
        00002a8e-0000-1000-8000-00805f9b34fb
        Height

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0026
        00002a98-0000-1000-8000-00805f9b34fb
        Weight

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0024
        00002a8c-0000-1000-8000-00805f9b34fb
        Gender

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0022
        00002a80-0000-1000-8000-00805f9b34fb
        Age

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char001f
        00002a90-0000-1000-8000-00805f9b34fb
        Last Name

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char001f/desc0021
        00002900-0000-1000-8000-00805f9b34fb
        Characteristic Extended Properties

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char001c
        00002a8a-0000-1000-8000-00805f9b34fb
        First Name

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char001c/desc001e
        00002900-0000-1000-8000-00805f9b34fb
        Characteristic Extended Properties

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0019
        00002a9f-0000-1000-8000-00805f9b34fb
        User Control Point

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0019/desc001b
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0017
        00002a9a-0000-1000-8000-00805f9b34fb
        User Index

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service0014/char0015
        00002a99-0000-1000-8000-00805f9b34fb
        Database Change Increment

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e
        0000180d-0000-1000-8000-00805f9b34fb
        Heart Rate  <-----  NOT FOUND??????

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char0012
        00002a38-0000-1000-8000-00805f9b34fb
        Body Sensor Location

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f
        00002a37-0000-1000-8000-00805f9b34fb
        Heart Rate Measurement     <------

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f/desc0011
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration

Primary Service
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000a
        00001801-0000-1000-8000-00805f9b34fb
        Generic Attribute Profile

Characteristic
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000a/char000b
        00002a05-0000-1000-8000-00805f9b34fb
        Service Changed

Descriptor
        /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000a/char000b/desc000d
        00002902-0000-1000-8000-00805f9b34fb
        Client Characteristic Configuration



# -*- coding: utf-8 -*-
"""
Notifications
-------------
Example showing how to add notifications to a characteristic and handle the responses.
Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>
"""

import logging
import asyncio
import platform

from bleak import BleakClient
from bleak import _logger as logger


CHARACTERISTIC_UUID = (
    "00002a37-0000-1000-8000-00805f9b34fb"
)  # <--- Change to the characteristic you want to enable notifications from.


#0000feee-0000-1000-8000-00805f9b34fb


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    print("{0}: {1}".format(sender, data))

async def run(address, loop, debug=False):
    if debug:
        import sys

        # loop.set_debug(True)
        l = logging.getLogger("asyncio")
        l.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        l.addHandler(h)
        logger.addHandler(h)

    async with BleakClient(address, loop=loop) as client:
        x = await client.is_connected()
        logger.info("Connected: {0}".format(x))

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        await asyncio.sleep(5.0, loop=loop)
        await client.stop_notify(CHARACTERISTIC_UUID)

if __name__ == "__main__":
    import os

    os.environ["PYTHONASYNCIODEBUG"] = str(1)
    address = (
        "EF:B7:AA:FC:96:73"  # <--- Change to your device's address here if you are using Windows or Linux
        if platform.system() != "Darwin"
        else "243E23AE-4A99-406C-B317-18F1BD7B4CBE"  # <--- Change to your device's address here if you are using macOS
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop, True))




#
#
#
#
#
#
#



from pygatt.util import uuid16_to_uuid
from pygatt.exceptions import NotConnectedError, NotificationTimeout
import binascii
import time
import logging

MAC = 'EF:B7:AA:FC:96:73'   # MAC address of the Polar H10 belt
HR = 0
RRi1 = 0
RRi2 = 0

logging.basicConfig(filename='/home/pi/python/debug.log',filemode='w',level=logging.DEBUG)
logging.getLogger('pygatt').setLevel(logging.DEBUG)

def callback(handle, measure):
    global HR, RRi1, RRi2

    if handle == 16:
        for i in range(len(measure)):
            if i == 1:
                print('Heart rate = ',measure[1],' bpm')
                HR = measure[1]
            if i == 2:
                RRi1 = round((measure[2] + 256*measure[3])/1024,2)
                print('RR intervall = %.2f' % RRi1,' s')
            if i == 4:
                RRi2 = round((measure[4] + 256*measure[5])/1024,2)
                print('RR intervall = %.2f' % RRi2,' s')


def Init():

    adapter = pygatt.GATTToolBackend()
    adapter.start()

    try:
        """ connect to bluetooth MAC addres with 5 seconds timeout"""
        device = adapter.connect(MAC, address_type=pygatt.BLEAddressType.random)
        device.bond()

        """ generate characteristics uuid's  """
        uuid_heart_service = uuid16_to_uuid(0x2A37)
        """ discover all characteristics uuid's"""
        device.discover_characteristics()


        device.subscribe(uuid_heart_service, callback, True)

    except NotConnectedError:
        print('No connection established ')
        quit()



Init()
t = time.time()    # Initialite with a reasonable value
while(1):
    time.sleep(max(0, 60/max(HR,30) - (time.time() - t)))    
    t = time.time()





CHARACTERISTIC_UUID = (
    "00002a37-0000-1000-8000-00805f9b34fb"
) #Heart Rate Measurement     <------
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Notifying': True}
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 57, 201, 3]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 57, 201, 3]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x109\xc9\x03')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 58, 192, 3]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 58, 192, 3]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x10:\xc0\x03')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 58, 227, 3]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 58, 227, 3]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x10:\xe3\x03')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 59, 236, 3]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 59, 236, 3]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x10;\xec\x03')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 59, 236, 3]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 59, 236, 3]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x10;\xec\x03')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Notifying': False}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Notifying': False}, []]
Disconnecting from BLE device...
Removing rule PropChanged, ID: 1

DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Notifying': True}
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 54, 193, 3]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 54, 193, 3]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x106\xc1\x03')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 55, 12, 4]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 55, 12, 4]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x107\x0c\x04')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [0, 55]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [0, 55]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x007')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 56, 3, 4]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 56, 3, 4]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x108\x03\x04')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Value': [16, 56, 110, 4]}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Value': [16, 56, 110, 4]}, []]
00002a37-0000-1000-8000-00805f9b34fb: bytearray(b'\x108n\x04')
DBUS: path: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f, domain: org.bluez.GattCharacteristic1, body: {'Notifying': False}
GATT Char Properties Changed: /org/bluez/hci0/dev_EF_B7_AA_FC_96_73/service000e/char000f | [{'Notifying': False}, []]
Disconnecting from BLE device...

