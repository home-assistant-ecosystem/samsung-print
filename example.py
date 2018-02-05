"""
Copyright (c) 2017-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio

import aiohttp

from samsung_print import Printer

IP_PRINTER = '192.168.0.25'


@asyncio.coroutine
def main():
    with aiohttp.ClientSession() as session:
        printer = Printer(IP_PRINTER, loop, session)
        yield from printer.async_get_data()

        # Show the printer status
        print("Printer status:", printer.status('hrDeviceStatus'))
        # Show details about the printer
        print("Printer details:")
        for key, value in printer.identity().items():
            print(key, ':', value)
        # Get the details of a cartridge
        print("Toner Cyan details:", printer.toner('cyan'))
        # Get the details about tray 2
        print("Tray 2 details:", printer.tray(2))
        # Check if Wifi is on
        print("Is WiFI active?", bool(printer.options()['wlan']))
        # Get the raw response from the printer
        print(printer.raw())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
