# get input from user and reverse (string or integer)

value = input('enter value: ')

if value.isdigit():
	print(reverse_integer(int(value)))
else:
	print(reverse_string(value))

def reverse_string(s):
	tmp = ""
	for i in s:
		tmp = i + tmp
	return tmp

def reverse_integer(n: int):
	tmp = 0
	while(n > 0):
		a = n % 10
		tmp = tmp * 10 + a
		n = n // 10
	return tmp

