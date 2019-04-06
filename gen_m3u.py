#!/usr/bin/python
#-*- coding: utf-8 -*-

import codecs
import gzip
import json
import os
import re
import sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

CURR_PATH = os.path.dirname(os.path.realpath(__file__))
WHITE_CATS = [line.decode('utf-8').rstrip('\n') for line
              in open(CURR_PATH + '/whitecats.txt') if not line.startswith('#')]
BLACK_REGEX = [line.decode('utf-8').rstrip('\n') for line
               in open(CURR_PATH + '/blacklist.txt') if not line.startswith('#')]

if (len(sys.argv) != 2):
    raise Exception("Not enough arguments!!")
else:
    with gzip.open(sys.argv[1], 'rb') as chanFile:
        chanJson = json.load(chanFile)
        filteredChanJson = [
            x for x in chanJson["channels"] if
            (x['cat'] in WHITE_CATS)
            and not any(r for r in BLACK_REGEX
                        if re.search(r, x['name'], re.IGNORECASE))]
#        print(filteredChanJson)
        if (filteredChanJson):
            print("#EXTM3U\n\n")
            for itm in filteredChanJson:
                itm['tvg_name'] = itm['name'].replace(' ', '_')
                print(u"""#EXTINF:-1 group-title="{cat:s}" tvg-name="{tvg_name:s}",{name:s}
http://127.0.0.1:6878/ace/getstream?id={url:s}&.mp4""".format(**itm))
