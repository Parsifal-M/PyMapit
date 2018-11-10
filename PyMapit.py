#!/usr/bin/env python3
# Easy Google Mapping
# From Automate the boring stuff
# Launches a map in the browser using an address from the command line or clipboard.

import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])
else:
    # Use the clipboard for address.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
