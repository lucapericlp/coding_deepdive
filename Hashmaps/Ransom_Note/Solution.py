import os
dirname = os.path.dirname(__file__)
input_path = os.path.join(dirname, 'input')
output_path = os.path.join(dirname, 'output')

def Solution(m,n,source,target):
	if n > m or n > 30000 or m > 30000:
		return False

	available_words = {}
	for word in source.split():
		if len(word) > 5:
			return False

		available_words[word] = True

	for target_word in target.split():
		if target_word not in available_words or len(target_word) > 5:
			return False

	return True

if __name__ == '__main__':
	print(Solution(6,4,"give me one grand today night","give one grand today"))
