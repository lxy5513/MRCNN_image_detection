import sys


post_path = '/home/ferryliu/data'
sys.path.append(post_path)
from image_post import post_fun

time.sleep(0.1)
post_time = 0
post_time = post_fun(post_time)
print('post time ', post_time)

print('over')