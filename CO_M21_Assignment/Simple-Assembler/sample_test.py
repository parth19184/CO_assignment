lines = []
with open('sample_text.txt') as f:	#we will later format the text files as variables to run them easily
	for line in f:
		if not line.isspace():
			line_added = line.replace('\n', '')
			lines.append(line_added)

'''for i in lines:
	if i == '\n':
		lines.remove('\n')
	print(lines)'''

print(lines)

testing_list = [0, 1, 2, 3, 4]
if 0 in testing_list and 2 in testing_list:
	print("tested")