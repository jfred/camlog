import os
import sys
import datetime

from PIL import Image

if len(sys.argv) == 1:
    _cmds = [
        './isightcapture -t png user.png',
        'screencapture screen.png',
    ]

    from subprocess import call
    for cmd in _cmds:
        # keep calling until its successful
        while call(cmd, shell=True):
            pass

screen = Image.open('screen.png')
user = Image.open('user.png')

overlay_size = map(lambda x: int(x * .75), user.size)
user = user.resize(overlay_size, Image.ANTIALIAS)

paste_coords = tuple([screen.size[0] - overlay_size[0], screen.size[1] - overlay_size[1]])
screen.paste(user, paste_coords)

final_size = tuple(map(lambda x: int(x * .75), screen.size))
screen = screen.resize(final_size, Image.ANTIALIAS)

file_name = datetime.datetime.now().strftime('%Y%m%d-%H%M')
screen.save('data/%s.png' % file_name)
