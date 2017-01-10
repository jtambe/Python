# Binary Search in python

import math

def BinarySearch(list, item):

	if len(list) == 0:
		return False

	start = 0	
	end = len(list) - 1
	found = False

	sortedList = sorted(list)

	while start <= end and not found:
		mid = math.floor(len(list)/2)		
		if sortedList[mid] == item:
			found = True
		else:
			if item < sortedList[mid]:
				return BinarySearch(sortedList[:mid-1], item)
			else:
				return BinarySearch(sortedList[mid+1:], item)


	return found



def main():
	a = [3, 2, 19, 4, 3, 12, 89, 45, 73, 19, 30]
	searchItem = 45
	print(BinarySearch(a, searchItem))

if __name__ == '__main__':
	main()
