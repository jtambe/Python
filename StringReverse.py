

def ReverseRecursive(stringObj):
	if len(stringObj) == 0 or len(stringObj) == 1:
		#print('got here')
		#print(stringObj)
		return stringObj
	else:
		while len(stringObj) > 1:
			# a = stringObj[0]
			# b = stringObj[len(stringObj)-1]
			# print( str(a) + ' ' + str(b))
			# stringObj[0] = b
			# stringObj[len(stringObj)-1] = a
			#print(stringObj[1:len(stringObj)-1])
			#return ReverseRecursive(stringObj[1:len(stringObj)-1]) 
			return stringObj[-1:] + ReverseRecursive(stringObj[:-1]) 



def main():
	astrObj = 'ABCDE'
	print(ReverseRecursive(astrObj))

	# a = [3, 2, 19, 4, 3, 12, 89, 45, 73, 19, 30]
	# print(ReverseRecursive(a))

if __name__ == '__main__':
	main()
