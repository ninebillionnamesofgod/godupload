#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import ftplib
import yaml
import re
import datetime

# The template for each new week
TEMPLATE = """
      <tr>
        <td><audio controls>
 <source src="sound/{filename}"
         type='audio/mp3'>
 <!-- The next two lines are only executed if the browser doesn't support MP4 files -->
 <source src="sound/{filename}"
         type='audio/mp3; codecs=vorbis'>
 <!-- The next line will only be executed if the browser doesn't support the <audio> tag-->
 <p>Your user agent does not support the HTML5 Audio element.</p>
</audio> </td>
        <td><div align="center"><span class="bodytext">{date}</span></div></td>
        <td><div align="center"><span class="bodytext">{count}</span></div></td>
      </tr>
"""

# Read configuration file
with open("conf.yaml") as f:
    conf = yaml.load(f)

with open(conf['count']) as fc:
    count = fc.read()

with open("index.html") as f:
    index = f.read()

f = open(conf['master'], "rb")

session = ftplib.FTP(conf['server'], conf['username'], conf['password'])

filename = datetime.datetime.now().strftime("OMG-%Y-%m-%d.mp3")
session.storbinary("STOR /www/sound/{}".format(filename), f)
parts = re.split(r"</tbody>\s*</table>\s*<!--- clip -->", index)
newindex = parts[0] + TEMPLATE.format(filename=filename, date=datetime.datetime.now().strftime("%d %B %Y"), count=count) + "\n</tbody>\n</table>\n<!--- clip -->\n" + parts[1]

f.close()

with open("index.html", "w") as f:
    f.write(newindex)

f = open("index.html", "rb")

session.storbinary("STOR /www/index42.html", f)
f.close()

session.quit()

