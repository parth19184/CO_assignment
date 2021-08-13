#import random_text.txt

def main():

    with open('random_text.txt') as f:	#we will later format the text files as variables to run them easily
    	lines = f.readlines()

    #print(lines)

    opcode_dict = {
    	'add': 00000,
    	'sub': 00001,
    	'mov_imm': 00010,
    	'mov_reg': 00011,
    	'ld': 00010,
    	'st': 00101,
    	'mul': 00110,
    	'div': 00111,
    	'rs': 01000,
    	'ls': 01001,
    	'xor': 01010,
    	'or': 01011,
    	'and': 01100,
    	'not':01101,
    	'cmp': 01110,
    	'jmp': 01111,
    	'jlt': 10000,
    	'jgt': 10001,
    	'je': 10010,
    	'hlt' 10011
    }

    type_dict = {
    	'add': 'A',
    	'sub': 'A',
    	'mov_imm': 'B',
    	'mov_reg': 'C',
    	'ld': 'D',
    	'st': 'D',
    	'mul': 'A',
    	'div': 'C',
    	'rs': 'B',
    	'ls': 'B',
    	'xor': 'A',
    	'or': 'A',
    	'and': 'A',
    	'not': 'C',
    	'cmp': 'C',
    	'jmp': 'E',
    	'jlt': 'E',
    	'jgt': 'E',
    	'je': 'E',
    	'hlt' 'F'
    }
if __name__ == "__main__":
	main()