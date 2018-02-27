#!/usr/bin/python
import logging 

logging.basicConfig(level=logging.WARNING,format="%(msg)s")
					
if 1:
    logging.getLogger().setLevel(logging.DEBUG)
	
LOG = logging.getLogger('logtest')

LOG.debug('Running main')
LOG.info('Everything is okay')
LOG.warning('EVERYTHING HAS GONE WRONG!')

	