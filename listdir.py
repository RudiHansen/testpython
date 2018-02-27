#!/usr/bin/python

import os, sys

# Open a file
path = "/var/log/apache2/"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file