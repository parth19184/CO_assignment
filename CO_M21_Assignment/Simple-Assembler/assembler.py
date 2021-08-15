#import random_text.txt

import sys
def main():

    with open('random_text.txt') as f:	#we will later format the text files as variables to run them easily
    	lines = f.readlines()

    #print(lines)
    def convert_to_8bit_binary(number: int) -> str:
        

        bnr = bin(number).replace('0b','')
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        return bnr
    
    def encoding_5(instruction: str) ->str:
        return opcode_dict[instruction]
    
    def get_char_type(instruction: str) -> str:
        return type_dict[instruction]
    
    def encoding_11(type1 :str, inst_list: list) -> int:
        #code the if else statements here:
        

        if type1 == 'A':
            return '00' + register_dict[inst_list[1]] + register_dict[inst_list[2]]+ register_dict[inst_list[3][:2]]
        elif type1 == 'B':
            if inst_list[2] in memory_dict:
                return register_dict[inst_list[1]] + convert_to_8bit_binary(int(memory_dict[inst_list[2]]))
            else:
                return register_dict[inst_list[1]] + convert_to_8bit_binary(int(inst_list[2][1: ]))
        elif type1 == 'C':
            
            return '00000' + register_dict[inst_list[1]] + register_dict[inst_list[2]]
        elif type1 == 'D':
            if inst_list[2] in memory_dict:
                return register_dict[inst_list[1]] + convert_to_8bit_binary(int(memory_dict[inst_list[2]]))
            else:
                return register_dict[inst_list[1]] + convert_to_8bit_binary(int(inst_list[2][1: ]))

        elif type1 == 'E':
            if inst_list[1] in memory_dict:
                return '000' + convert_to_8bit_binary(int(memory_dict[inst_list[1]]))
            else:
                return '000' + convert_to_8bit_binary(int(inst_list[1][1: ]))
        else:
            sys.exit('wrong instruction1')
        pass
    def encoding_mov(instruction : str) ->str:
        opcode_fun = instruction.split(' ')

        try:
            opcode = opcode_fun[0]
            
        except:
            print("wrong instruction2")
            sys.exit("Error message")

        if opcode == 'mov':
            if opcode_fun[2][0] == '$':
                return 'mov_imm'

            elif opcode_fun[2][0] == 'R':
                return 'mov_reg'
            else:
                raise Exception("wrong instruction3")
        elif opcode == 'var':
            raise Exception("var cannot be in the middle of the instructions")
            sys.exit('Error message')
        elif opcode in type_dict:
            return opcode
        elif opcode == 'hlt':
            sys.exit('program has ended')
        elif(opcode[-1] == ':'):
            
            
            return encoding_mov(instruction[instruction.find(':') + 2: ])
            
        else:
            sys.exit('program has ended due to halting or wrong instruction')

    

    #the follwing are the different flags, they are set to boolean
    """overflow_flag = False
    lessthan_flag = False
    greaterthan_flag = False
    equal_flag = False"""
    
    FLAG_register = [0]*16

    #print(FLAG_register)
    
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


    #iter = len(lines)

    #instruction block for opcode
    instructions = []
    first_keyword_arr = []
    memory_dict = {}
    for instruction_num in lines:
        instructions.append(instruction_num)
        

    looping_count = 0
    random_count = 0
    total_instruction_length =len(first_keyword_arr)
    for iteration in instructions:
        key_element = iteration.split(' ')
        first_keyword_arr.append(key_element[0])
        if(looping_count< total_instruction_length and first_keyword_arr[looping_count] == 'var' and random_gen == True):
            memory_dict.update({random_count: memorykey_element[1]})
            random_count += 1 
            looping_count += 1
    #print(encoding_mov(instructions[5]))

    
    
    
    
    
    #block for instruction count
    if(total_instruction_length >256):
        raise Exception("instruction length greater than 256")
        sys.exit("error")
    
    


        

    final_instruction_length = total_instruction_length - looping_count
    #print(final_instruction_length)
#instruction dictionary to set the lines:
    number_dict = {}
    final_instruction_dict ={}
    dict_loop = 0
    
    for i in range(final_instruction_length):
        number_dict.update({i:first_keyword_arr[looping_count]})
        if (first_keyword_arr[looping_count] not in type_dict) and (first_keyword_arr[looping_count] != 'mov'):
            final_instruction_dict.update({first_keyword_arr[looping_count]: i})
        
        
        looping_count += 1

                
    
    
        
    #finally running the instructions:
    instruction_count = 0

    while instruction_count in range(len(instructions)):
        opcode_final = ''
        final_11 = ''
        this_list = instructions[instruction_count].split(' ')
        if instructions[instruction_count].split(' ')[0] == 'hlt':
            opcode_final = 'hlt'
        else:
            opcode_final = encoding_mov(instructions[instruction_count])
        #print(opcode_final)
        first_5 = encoding_5(opcode_final)

        char_type = get_char_type(opcode_final)
        if(char_type == 'F'):
            final_11 = '0'*11
            print(first_5 + final_11)
            sys.exit("assembly over")
        else:
            instruction_parameter = instructions[instruction_count].split(' ')
            if(instruction_parameter[0] == 'mov'):
                instruction_parameter[0] = opcode_final
            elif(instruction_parameter[0][-1] == ':'):
                instruction_parameter = instruction_parameter[1:]
                print(instruction_parameter)
            final_11 = encoding_11(char_type, instruction_parameter)
        print((first_5 + final_11) + '\n')
        instruction_count += 1

if __name__ == "__main__":
	main()
