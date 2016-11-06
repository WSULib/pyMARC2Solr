# marc binary iterate

from pymarc import MARCReader
import sys
import time
from multiprocessing.pool import Pool

count = 0
stime= time.time()
with open(sys.argv[1], 'rb') as fh:
	
	reader = MARCReader(fh)

	# serial
	if sys.argv[2] == 'serial':
		for record in reader:
			count += 1
			if count % 1000 == 0:
				print count, time.time() - stime
			if count == 10000:
				break


	# multi-processes
	elif sys.argv[2] == 'multip':

		def read_binary(record):
			count += 1
			if count == 10000:
				exit()

		pool = Pool()
		pool.map(read_binary, reader)






