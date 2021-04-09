import threading
import time
import boto3
from codeguru_profiler_agent import Profiler

if __name__ == "__main__":
    custom_session = boto3.session.Session(profile_name='dev', region_name='ap-southeast-1')
    Profiler(profiling_group_name="first", aws_session=custom_session).start()
    start_application()

def lw1():
	while True:
		print("a")
		time.sleep(1)

def lw2():
	while True:
		print("z")
		time.sleep(3)

db=[]
def lw3():
	for i in range(100000):
		db.append(i)
		time.sleep(2)



t1 = threading.Thread(target=lw1, args=())
t2 = threading.Thread(target=lw3, args=())
t3 = threading.Thread(target=lw2, args=())

t1.start()
t2.start()
t3.start()