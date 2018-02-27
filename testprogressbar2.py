#!/usr/bin/python
from progressbar import *
import time

progress = ProgressBar()
for i in progress(range(80)):
    time.sleep(0.01)
	
