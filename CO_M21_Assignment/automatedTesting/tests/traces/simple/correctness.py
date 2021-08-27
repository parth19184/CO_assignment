with open('test5') as f:	#we will later format the text files as variables to run them easily
    	lines = f.readlines()

with open('test5_output.txt') as f2:
        lines2 = f2.readlines()
        
for i in range(len(lines)):
    if lines[i] != lines2[i]:
        print('error at ', i)