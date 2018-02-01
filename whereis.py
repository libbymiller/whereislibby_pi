#!/usr/bin/env python
# based on https://github.com/pimoroni/inky-phat/blob/master/examples/hello.py

import sys
import json
import time
import urllib

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")


from PIL import ImageFont

import inkyphat

def get_location():
    res = requests.get('https://where.example.com/api/1/users/n/location.json?auth_token=ZZZZZZZZ')
    if(res.status_code == 200):
        json_data = json.loads(res.text)
        return json_data
    return {}


# Show the backdrop image

inkyphat.set_border(inkyphat.RED)
inkyphat.set_image("resources/hello-badge3.png")

# Partial update if using Inky pHAT display v1

if inkyphat.get_version() == 1:
    inkyphat.show()

# Add the text

font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 38)

name = "Where is Libby?"

w, h = font.getsize(name)

# Center the name text and align it with the name strip

x = (inkyphat.WIDTH / 2) - (w / 2)
y = 30 - (h / 2)

inkyphat.text((x, y), name, inkyphat.WHITE, font)

# get the data

data = get_location()
ds = data["description"]

# add it to the bottom of the badge

w1, h1 = font.getsize(ds)
x1 = (inkyphat.WIDTH / 2) - (w1 / 2)
y1 = 71 - (h1 / 2)

inkyphat.text((x1, y1), ds, inkyphat.BLACK, font)

# Partial update if using Inky pHAT display v1

if inkyphat.get_version() == 1:
    inkyphat.set_partial_mode(56, 96, 0, inkyphat.WIDTH)

inkyphat.show()
