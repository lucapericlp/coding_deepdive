import os
from Solution import Solution
class TestRansomNote():
	def test_input_vs_outputs():
		input_output_dict = {}
		for root,dirs,files in os.walk("input"):
			for filename in files:
				with open(os.path.join("input",filename)) as f:
					input_output_dict[filename[-6:]] = []
					input_output_dict[filename[-6:]].append(f.read())

		for root,dirs,files in os.walk("output"):
			for filename in files:
				with open(os.path.join("output",filename)) as f:
					input_output_dict[filename[-6:]].append(f.read())
		
			

		
