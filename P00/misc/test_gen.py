#!/bin/python3
import random
import time

random.seed(time.time())
num_iter = int(input("Please enter the number of numbers you want: "))
max_num = int(input("Please enter the max entry number you want: "))
if num_iter < 1:
	print("You must have at least one number!")
	exit(-1)

gen_str = str(random.randint(0, max_num))
signs = []
for i in range(num_iter - 1):
	gen_str = gen_str + ' ' + str(random.randint(1, max_num))

	sign_val = random.randint(0, 2)
	sign = ''
	if sign_val == 0:
		sign = '+'
	elif sign_val == 1:
		sign = '*'
	#Took out subtraction because sometimes the numbers would line up such that they'd make 0, then be divided by 0 somewhere down the line.
	#elif sign_val == 2:
	#	sign = '-'
	else:
		sign = '/'

	if random.randint(0, 5) > 4:
		signs.append(sign)
	else:
		gen_str = gen_str + ' ' + sign

for sign in signs:
	gen_str = gen_str + ' ' + sign
		
print(gen_str)

fp = open("new_test.in", "w")
fp.write(gen_str + '\n')
fp.close()

print("Written to new_test.in")
