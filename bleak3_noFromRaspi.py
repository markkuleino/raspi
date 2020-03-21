# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:29:58 2020

@author: MarkkuLeino
"""

# -*- coding: utf-8 -*-
"""
Notifications
-------------
Example showing how to add notifications to a characteristic and handle the responses.
Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>


 python3 bleak3_notific.py >> data.log

 */2 * * * * pgrep -f bleak3_notific.py || nohup /usr/bin/python3 /home/pi/bleak3_notific.py >> data.log



"""

import logging
import asyncio
import platform
import datetime

from bleak import BleakClient
from bleak import _logger as logger


CHARACTERISTIC_UUID = (
    "00002a37-0000-1000-8000-00805f9b34fb"
)  # <--- Change to the characteristic you want to enable notifications from.


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
        print(datetime.datetime.now())

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        await asyncio.sleep(180.0, loop=loop)
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
    for i in range(3):
        loop.run_until_complete(run(address, loop, True))


