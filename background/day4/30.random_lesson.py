# randint
# uniform
# random
# choice
# shuffle

from random import *

random_num = randint(1,50)
print(random_num)

random_num = uniform(1,5)
print(round(random_num,1))

random_num = random()
print(round(random_num,2))

colors = ["blue","red","green","yellow"]
random_num = choice(colors)
print(random_num)

nums = list(range(5,51,5))
shuffle(nums)
print(nums)