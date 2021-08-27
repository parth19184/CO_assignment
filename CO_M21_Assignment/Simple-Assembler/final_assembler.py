import sys
import shutil

def main():
	lines = []
	
	#original = 
	#this part of the code is used so that blank lines are removed from lines list
	'''with open('sample_text.txt') as f:	#we will later format the text files as variables to run them easily
		for line in f:					#have been converted so that \n is removed and does not cause problems in the string parsing
			if not line.isspace():
				line_added = line.replace('\n', '')
				lines.append(line_added)'''
	

	for mem_instruction in sys.stdin:
		if mem_instruction == '\n':
			break
		line_added = mem_instruction.replace('\n', '')
		lines.append(line_added)
		

	def convert_to_8bit_binary(number: int) -> str:        
		bnr = bin(number).replace('0b','')
		x = bnr[::-1] #this reverses an array
		while len(x) < 8:
			x += '0'
			bnr = x[::-1]
		return bnr

	#labels have been updated in this function itself
	#this function returns a new string which is like the input instruction but easier to operate with
	def encode_instruction(instruction_string: str, instruction_number: int, has_var_ended: bool, final_instruction_length: int) -> str:
		instruction_line_parsed = instruction_string.split(' ')
		if(instruction_string == 'hlt' and instruction_number != final_instruction_length - 1):
			sys.exit("hlt instruction at line {} before the end of the instruction [ERROR]".format(instruction_number))

		elif(instruction_line_parsed[0] == 'var' and has_var_ended):
			sys.exit("var assigned at line {} after assignment ended in the beginning".format(instruction_number))
		
		elif(instruction_line_parsed[0] == 'mov'):
			if instruction_line_parsed[2][0] == '$':
				return 'mov_imm ' + instruction_string[instruction_string.find(instruction_line_parsed[1]): ]
			elif instruction_line_parsed[2] in register_dict:
				return 'mov_reg ' + instruction_string[instruction_string.find(instruction_line_parsed[1]) - 1: ]
			else:
				sys.exit("wrong instruction syntax at line {} corresponding to mov".format(instruction_number))
		elif(instruction_line_parsed[0] in opcode_dict):
			return instruction_string
		elif(instruction_line_parsed[0][-1] == ':'):
			label_dict.update({instruction_line_parsed[0][: -1] : instruction_number})
			return encode_instruction(instruction_string[instruction_string.find(":") + 2: ], instruction_number, has_var_ended, final_instruction_length)
		else:
			sys.exit("wrong instruction syntax at line {}".format(instruction_number))

	def encode_5(instruction_string_encoded: str) -> str:
		command = instruction_string_encoded.split(' ')
		return opcode_dict[command[0]]

	def encode_11(instruction_string_encoded: str, instruction_number: int) -> str:
		instruction_line_parsed = instruction_string_encoded.split()
		instruction_type = type_dict[instruction_line_parsed[0]]

		#if statements to be started from here
		if instruction_type == 'A':
			
			if instruction_line_parsed[1] in register_dict and instruction_line_parsed[2] in register_dict and instruction_line_parsed[3] in register_dict :
				return '00' + register_dict[instruction_line_parsed[1]] + register_dict[instruction_line_parsed[2]] + register_dict[instruction_line_parsed[3]]
			else:
				sys.exit('wrong syntax at line number {} for type A instruction'.format(instruction_number))

		elif instruction_type == 'B':
			if instruction_line_parsed[2][0] == '$' and instruction_line_parsed[1] in register_dict:
				return register_dict[instruction_line_parsed[1]] + convert_to_8bit_binary(int(instruction_line_parsed[2][1: ]))
			else:
				sys.exit('wrong syntax at line {} for type B instruction'.format(instruction_number))

		elif instruction_type == 'C':
			if instruction_line_parsed[1] in register_dict and instruction_line_parsed[2] in register_dict:
				return '00000' + register_dict[instruction_line_parsed[1]] + register_dict[instruction_line_parsed[2]]
			else:
				return sys.exit('wrong syntax at line {} for type C instruction'.format(instruction_number))

		elif instruction_type == 'D':
			if instruction_line_parsed[1] in register_dict and instruction_line_parsed[2] in var_storing_dict:
				return register_dict[instruction_line_parsed[1]] + convert_to_8bit_binary(var_storing_dict[instruction_line_parsed[2]])
			#elif instruction_line_parsed[1] in register_dict and 
			else:
				sys.exit('wrong syntax at line {} for type D instruction'.format(instruction_number))

		elif instruction_type == 'E':
			if instruction_line_parsed[1] in register_dict and instruction_line_parsed[2] in label_dict:
				return register_dict[instruction_line_parsed[1]] + convert_to_8bit_binary(label_dict[instruction_line_parsed[2]])
			else:
				sys.exit('wrong syntax at line {} for type E instruction'.format(instruction_number))

		elif instruction_type == 'F':
			return '00000000000'
	opcode_dict = {
    	'add': '00000',
    	'sub': '00001',
    	'mov_imm': '00010',
    	'mov_reg': '00011',
    	'ld': '00010',
    	'st': '00101',
    	'mul': '00110',
    	'div': '00111',
    	'rs': '01000',
    	'ls': '01001',
    	'xor': '01010',
    	'or': '01011',
    	'and': '01100',
    	'not':'01101',
    	'cmp': '01110',
    	'jmp': '01111',
    	'jlt': '10000',
    	'jgt': '10001',
    	'je': '10010',
    	'hlt': '10011'
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
    	'hlt': 'F',
        'var': 'G'
    }
	register_dict = {
		'R0':'000',
		'R1':'001',
		'R2':'010',
		'R3':'011',
		'R4':'100',
		'R5':'101',
		'R6':'110',
		'FLAGS':'111'
	}

	label_dict = {}
	var_storing_dict = {}
	var_storing_list = []
	encoded_instruction_list = []
	final_assembly_code = []
    #halt check statement:
	if lines[-1] != 'hlt':
		sys.exit("last line is not a halt instruction [ERROR]")

    #get length of the total instructions:
	initial_instruction_length = len(lines)
	

	#throw error when instruction length > 256
	if initial_instruction_length > 256:
		sys.exit("instruction length is greater than 256 and cannot be stored in the memory")

	#this part of the code adds all the variable assignments in a dictionary
	var_loop_counter = 0
	has_var_ended = False
	while(var_loop_counter < initial_instruction_length and has_var_ended == False):
		instruction_line_parsed = lines[var_loop_counter].split(' ')
		if instruction_line_parsed[0] == 'var':
			try:
				#var_storing_dict.update({instruction_line_parsed[1]: var_loop_counter})
				var_storing_list.append(instruction_line_parsed[1])
				var_loop_counter += 1					#add the corresponding memory address to the variable (initially added the order of declaration)
			except:
				sys.exit("wrong variable assignment syntax at the beginning [no line number to be given]")
		else:
			has_var_ended = True
			break

	final_instruction_length = initial_instruction_length - var_loop_counter

	instruction_counter = 0

	dictionary_counter = final_instruction_length
	#print(final_instruction_length)

	for variable in var_storing_list:
		var_storing_dict.update({variable: dictionary_counter})
		dictionary_counter += 1

	#print(var_storing_dict)
	#print(var_storing_list)
	while(instruction_counter < final_instruction_length):
		
								
		instruction_string = lines[instruction_counter + var_loop_counter]
		
		encoded_instruction = encode_instruction(instruction_string, instruction_counter, has_var_ended, final_instruction_length)
		#print(encoded_instruction)
		encoded_instruction_list.append(encoded_instruction)
		'''first_5_bits = encode_5(encoded_instruction)
		#print(encoded_instruction)
		
		#print(first_5_bits)

		second_11_bits = encode_11(encoded_instruction, instruction_counter)
		#print(second_11_bits)
		instruction_binary = first_5_bits + second_11_bits
		final_assembly_code.append(instruction_binary)'''
		instruction_counter += 1
		
	#print(final_assembly_code)
	#print(encoded_instruction_list)

	instruction_counter = 0

	while(instruction_counter < final_instruction_length):
		
								
		'''instruction_string = lines[instruction_counter + var_loop_counter]
		
		encoded_instruction = encode_instruction(instruction_string, instruction_counter, has_var_ended, final_instruction_length)
		#print(encoded_instruction)
		encoded_instruction_list.append(encoded_instruction)'''
		first_5_bits = encode_5(encoded_instruction_list[instruction_counter])
		#print(encoded_instruction)
		
		#print(first_5_bits)

		second_11_bits = encode_11(encoded_instruction_list[instruction_counter], instruction_counter)
		#print(second_11_bits)
		instruction_binary = first_5_bits + second_11_bits
		final_assembly_code.append(instruction_binary)
		instruction_counter += 1

	for i in final_assembly_code :
		print(i)
if __name__ == "__main__":
	main()
