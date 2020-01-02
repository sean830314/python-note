import multiprocessing
manager = multiprocessing.Manager()
temp_dict = manager.dict()
lock = manager.Lock()
temp_dict['test'] = 0
temp_dict['test2'] = 100
def test(test_dict, lock):
    lock.acquire()
    test_dict['test'] = test_dict['test'] + 1
    temp_dict['test2'] = temp_dict['test2'] - 1
    lock.release()
jobs = [multiprocessing.Process(target=test, args=(temp_dict, lock)),multiprocessing.Process(target=test, args=(temp_dict, lock)) ]
print(jobs)
for job in jobs:
    job.start()
for job in jobs:
    job.join()
print(temp_dict)
