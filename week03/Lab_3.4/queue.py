# program that puts 10 random mumbers in to a queue(list) then outputs all values in the queue
# then take the numbers from the queue one at a time and prints it and the current number in the queue
# helen o'shea
# 20210206
# 1 https://www.geeksforgeeks.org/generating-random-number-list-in-python/

import random
i=0
queue = [random.randrange(0, 100) for i in range(10)] # based on the reference 1 above
print("queue is ",queue)
while len(queue) > 0:
  for q in queue:
    print("current Number is {} and the queue is {}".format(q,queue))
    queue.pop(0)