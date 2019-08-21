#!/usr/bin/python3
import urllib.request
import os


count = 0
#f.write(page.read().decode("utf-8"))
while (count == 0):
    try:
         urllib.request.urlretrieve("http://results.vtu.ac.in/vitaviresultcbcs/index.php", "vtu.html")
         count=1
         os.system('firefox results.vtu.ac.in')
    except:
          print('error')

