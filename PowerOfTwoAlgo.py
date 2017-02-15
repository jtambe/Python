
def IsPowerOfTwo (inputNUmber):
	num = inputNUmber
	if num == 1:
		return True
	elif(((num != 1) and (num & (num - 1)))):
		return False
	else:
		return True

def IsMultipleOfTwo(number):
	if( (number >> 1 << 1) == number ):
		return True
	else:
		return False


def main():
	print("2 power: "+str(IsPowerOfTwo(2)) )
	print("8 power: "+str(IsPowerOfTwo(8)) )
	print("10 power: "+str(IsPowerOfTwo(10)) )
	print("16 power: "+str(IsPowerOfTwo(16)) )
	print("22 power: "+str(IsPowerOfTwo(22)) )
	print("32 power: "+str(IsPowerOfTwo(32)) )
	print("80 power: "+str(IsPowerOfTwo(80)) )
	print("512 power: "+str(IsPowerOfTwo(512)) )


	print("8 multiple: "+str(IsMultipleOfTwo(8)) )
	print("10 multiple: "+str(IsMultipleOfTwo(10)) )
	print("16 multiple: "+str(IsMultipleOfTwo(16)) )
	print("22 multiple: "+str(IsMultipleOfTwo(22)) )

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