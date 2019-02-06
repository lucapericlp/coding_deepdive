def reverse_enum(array):
	return ((index,array[index]) for index in reversed(range(len(array))))

def reverse_enum_full(array):
	for index in reversed(range(len(array))):
		yield index, array[index]

if __name__ == "__main__":
	array = [1,2,3,4]
	
	for index,item in reverse_enum(array):
		print(item,end="")

	print("\n")

	for index,item in reverse_enum_full(array):
		print(item,end="")

	print("\n")
