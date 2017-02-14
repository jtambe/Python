
def IsPowerOfTwo (inputNUmber):
	num = inputNUmber
	if num == 1:
		return True
	elif(((num != 1) and (num & (num - 1)))):
		return False
	else:
		return True


def main():
	print(IsPowerOfTwo(2))
	print(IsPowerOfTwo(8))
	print(IsPowerOfTwo(10))
	print(IsPowerOfTwo(16))
	print(IsPowerOfTwo(22))
	print(IsPowerOfTwo(32))
	print(IsPowerOfTwo(80))
	print(IsPowerOfTwo(512))



if __name__ == "__main__":
	main()


# power of two example, second condition
# 1000 =  (8)
# &
# 0111 = (8-1)
# results as follows
# 0000 = 0

# not power of two example, second condition
# 1010 = 10
# &
# 1001 = 9

# 1000 = 8