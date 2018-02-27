#!/usr/bin/python
import glob

filelist = glob.glob("/var/log/apache2/access*")
filelist.sort()
print filelist
