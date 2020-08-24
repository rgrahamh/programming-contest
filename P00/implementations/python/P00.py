#!/bin/python3
import sys

def execute_op(stack, op):
	if op == '+':
		return stack[-2] + stack[-1]
	elif op == '-':
		return stack[-2] - stack[-1]
	elif op == '/':
		if stack[-1] != 0:
			return stack[-2] / stack[-1]
		else:
			return 0
	elif op == '*':
		return stack[-2] * stack[-1]

def calculate(formula):
	#For each character in the formula string
	stack = []
	num = 0
	add_num = False
	for c in formula:
		#Continue parsing number
		if c >= '0' and c <= '9':
			num *= 10
			num += int(c)
			add_num = True
		#Add the number to the stack
		elif c == ' ':
			if add_num:
				stack.append(num)
				num = 0
			add_num = False
		#Operators
		elif c == '+' or c == '-' or c == '*' or c == '/':
			if len(stack) <= 1:
				print("Invalid Input")
				return -1
			stack[-2] = execute_op(stack, c)
			if c == '/' and stack[-2] == 0:
				print("Invalid Input")
				return -1
			stack.pop()
		else:
			print("Invalid Input")
			return -1
	if len(stack) == 1 and add_num == 0:
		print("%.4f" % stack[0])
		return 0
	elif len(stack) > 1 or (len(stack) == 1 and add_num == 1):
		print("Invalid Input")
		return -1
	elif len(stack) == 0 and add_num == 1:
		print("%.4f" % num)
		return 0
	print("Invalid Input")
	return -1
			

#Get the text file input with no spaces
formula = sys.stdin.readline().rstrip()
calculate(formula)
