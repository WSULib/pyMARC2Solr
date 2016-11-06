
import time

from multiprocessing.pool import ThreadPool as Pool

pool_size = 5  # your "parallelness"
pool = Pool(pool_size)


def worker(item):
    try:
        x = item
    except:
        print('error with item')

print "beginning threaded test"
stime = time.time()
for item in range(0,100000):
    pool.apply_async(worker, (item,))
print "multi-threaded / elapsed: %s" % str(time.time() - stime)

pool.close()
pool.join()

print "beginning single-thread test"
stime = time.time()
for item in range(0,100000):
	x = item
print "single thread / elapsed: %s" % str(time.time() - stime)

