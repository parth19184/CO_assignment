import sys

halt=False
def main():
	#execute errors using sys.exit(<message>), if you are using try except, please run the code on sample cases
	#decide whether to change flags and registers in separate functions or do it in run()
	
	
	def convert_to_8bit_binary(number: int) -> str:                 
		bnr = bin(number).replace('0b','') #bin() returns string  
		x = bnr[::-1] #this reverses the string
		while len(x) < 8:
			x += '0'
		bnr = x[::-1]
		return bnr

	def convert_to_16bit_binary(number: int) -> str:                 
		bnr = bin(number).replace('0b','') #bin() returns string  
		x = bnr[::-1] #this reverses the string
		while len(x) < 16:
			x += '0'
		bnr = x[::-1]
		return bnr

	def convert_to_int(bi):
		return int(str(bi),2)

	def encode(binary_instruction: str) ->str:
		command = bit5_dict[binary_instruction[:5]] 
		
		if type_dict[command] == 'A':
			return command + ' ' + register_dict_rev[binary_instruction[7:10]] + ' ' + register_dict_rev[binary_instruction[10:13]] + ' ' + register_dict_rev[binary_instruction[13:]]
		elif type_dict[command] == 'B':
			return command + ' ' + register_dict_rev[binary_instruction[5:8]] + ' ' + binary_instruction[8:]
		elif type_dict[command] == 'C':
			return command + ' ' + register_dict_rev[binary_instruction[10:13]] + ' ' + register_dict_rev[binary_instruction[13:]]
		elif type_dict[command] == 'D':
			return command + ' ' + register_dict_rev[binary_instruction[5:8]] + ' ' + binary_instruction[8:]
		elif type_dict[command] == 'E':
			return command + ' ' + binary_instruction[8:]
		elif type_dict[command] == 'F':
			return command

	def executionEngine(i: str):
		#exclude the variables ion the beggining
		instruction=i.split()
		first_word = instruction[0] #get the first instruction ie (mov, cmp, etc)
		if first_word=='add':
			if convert_to_int(rf.dict_register_file[instruction[3]])+convert_to_int(rf.dict_register_file[instruction[2]])>(2**16)-1:
				rf.dict_register_file[instruction[1]]=bin(convert_to_int(rf.dict_register_file[instruction[2]])+convert_to_int(rf.dict_register_file[instruction[3]])).replace('0b','')[-16:]
				rf.dict_register_file['R7']='0000000000001000'
			else:
				rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])+convert_to_int(rf.dict_register_file[instruction[3]]))
				rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			rf.dump()
		elif first_word=='sub':
			if convert_to_int(rf.dict_register_file[instruction[3]])>convert_to_int(rf.dict_register_file[instruction[2]]):
				rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(0)
				rf.dict_register_file['R7']='0000000000001000'
			else:
				rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])-convert_to_int(rf.dict_register_file[instruction[3]]))
				rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='mov_imm':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(instruction[2]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='mov_reg':
			rf.dict_register_file[instruction[1]]=rf.dict_register_file[instruction[2]]
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='ld':
			rf.dict_register_file[instruction[1]]=mem.memory[convert_to_int(instruction[2])]
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='st':
			mem.memory[convert_to_int(instruction[2])]=rf.dict_register_file[instruction[1]]
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='mul':
			if convert_to_int(rf.dict_register_file[instruction[3]])*convert_to_int(rf.dict_register_file[instruction[2]])>(2**16)-1:
				rf.dict_register_file[instruction[1]]=bin(convert_to_int(rf.dict_register_file[instruction[2]])*convert_to_int(rf.dict_register_file[instruction[3]])).replace('0b','')[-16:]
				rf.dict_register_file['R7']='0000000000001000'
			else:
				rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])*convert_to_int(rf.dict_register_file[instruction[3]]))
				rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='div':
			rf.dict_register_file['R0']=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[1]])//convert_to_int(rf.dict_register_file[instruction[2]]))
			rf.dict_register_file['R1']=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[1]])%convert_to_int(rf.dict_register_file[instruction[2]]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='rs':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])>>convert_to_int(instruction[2]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='ls':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(~convert_to_int(rf.dict_register_file[instruction[2]])<<convert_to_int(instruction[2]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='xor':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])^convert_to_int(rf.dict_register_file[instruction[3]]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='or':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])|convert_to_int(rf.dict_register_file[instruction[3]]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='and':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(convert_to_int(rf.dict_register_file[instruction[2]])&convert_to_int(rf.dict_register_file[instruction[3]]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='not':
			rf.dict_register_file[instruction[1]]=convert_to_16bit_binary(~convert_to_int(rf.dict_register_file[instruction[2]]))
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='cmp':
			if convert_to_int(rf.dict_register_file[instruction[1]])>convert_to_int(rf.dict_register_file[instruction[2]]):
				rf.dict_register_file['R7']='0000000000000010'
			elif convert_to_int(rf.dict_register_file[instruction[1]])<convert_to_int(rf.dict_register_file[instruction[2]]):
				rf.dict_register_file['R7']='0000000000000100'
			else:
				rf.dict_register_file['R7']='0000000000000001'
			pc.dump()
			pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			
			rf.dump()
		elif first_word=='jmp':
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			pc.update(instruction[1])
			
			rf.dump()
		elif first_word=='jlt':
			if rf.dict_register_file['R7']=='0000000000000100':
				pc.dump()
				pc.update(instruction[1])
			else:
				pc.dump()
				pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			rf.dict_register_file['R7']='0000000000000000'
			
			rf.dump()
		elif first_word=='jgt':
			if rf.dict_register_file['R7']=='0000000000000010':
				pc.dump()
				pc.update(instruction[1])
			else:
				pc.dump()
				pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			rf.dict_register_file['R7']='0000000000000000'
			
			rf.dump()
		elif first_word=='je':
			if rf.dict_register_file['R7']=='0000000000000001':
				pc.dump()
				pc.update(instruction[1])
			else:
				pc.dump()
				pc.update(convert_to_8bit_binary(convert_to_int(pc.program_counter)+1))
			rf.dict_register_file['R7']='0000000000000000'
			
			rf.dump()
		elif first_word=='hlt':
			global halt 
			halt=True
			rf.dict_register_file['R7']='0000000000000000'
			pc.dump()
			rf.dump()







		#if first_word is a label:
			#append the label in a dictionary defined in main() with its corresponding curr_instruction top help in jump statements
			#also execute whats in the label
			#go to the next instruction 
	

		#if first_word is a regular instruction:
			#encode it 
			#decide whether assembly code should be generated or you can directly complete the actions and change the registers, flags 
			#and show the errors




#memory variable(made into a list with 512 elements)
	class MEM:
		memory = []
		
		def __init__(self):
			for i in range(256):                                   
				self.memory.append("0000000000000000")                          
		def dump(self):
			for i in range(256):
				print(self.memory[i])
	
	class RF:
		dict_register_file = {}

		def __init__(self):
			#append all register values with 8 bits to the dictionary
			for i in range(8):
				self.dict_register_file['R'+str(i)]='0000000000000000'

		def dump(self):
			#prints values of registers at that particular time
			for i in self.dict_register_file:
				print(self.dict_register_file[i],end=' ')
			print()
	#program counter initialised to 0
	class PC:
		program_counter='00000000'

		def update(self,i):                         
			#updates pc value
			self.program_counter=str(i)
		def dump(self):
			print(self.program_counter,end=' ')
	#halting instruction as bool

	
	inst = []
	#print('open_test')
	for mem_instruction in sys.stdin:
		if mem_instruction == '\n':
			break
		line_added = mem_instruction.replace('\n', '')
		inst.append(line_added)

	#print('end test')



	#all the variables, flags and registers are to be put in here:



	bit5_dict = {
		'00000': 'add',
		'00001': 'sub',
		'00010': 'mov_imm',
		'00011': 'mov_reg',
		'00100': 'ld',
		'00101': 'st',
		'00110': 'mul',
		'00111': 'div',
		'01000': 'rs',
		'01001': 'ls',
		'01010': 'xor',
		'01011': 'or',
		'01100': 'and',
		'01101': 'not',
		'01110': 'cmp',
		'01111': 'jmp',
		'10000': 'jlt',
		'10001': 'jgt',
		'10010': 'je',
		'10011': 'hlt'
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
		'000':'R1',
		'001':'R1',
		'010':'R2',
		'011':'R3',
		'100':'R4',
		'101':'R5',
		'110':'R6',
		'FLAGS':'111'
	}

	register_dict_rev = register_dict
	register_dict_rev = dict(reversed(list(register_dict.items())))
	

	mem=MEM()
	rf=RF()
	pc=PC()

	#inst=lines
	for i in range(len(inst)):
		mem.memory[i]=inst[i]

		
	while(halt==False):
		str_inst=encode(mem.memory[convert_to_int(pc.program_counter)])
		executionEngine(str_inst)

	mem.dump()


	

if __name__ == "__main__":
	main()
