array = [1, 4, 5, 7, 9, 12, 15, 18, 19, 22, 25, 29, 40, 50]

def binary_search(array, target):
	left = 0
	right = len(array) - 1
	
	while(left <= right):
		mid = (left + right) // 2
		
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
		
	return - 1
	
print(f'Index of 9: {binary_search(array, 9)}')
