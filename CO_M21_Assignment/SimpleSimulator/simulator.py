def main():
	#execute errors using sys.exit(<message>), if you are using try except, please run the code on sample cases
	#decide whether to change flags and registers in separate functions or do it in run()
	def encode(curr_instruction: list) -> str:
		#encode here
	def run(instructions: list) ->none:
		#exclude the variables ion the beggining
		instruction_size = len(instructions)
		for curr_instruction in range(instruction_size):
			first_word = get_first_word(curr_instruction) #get the first instruction ie (mov, cmp, etc)
			if first_word == var and var_true:
				#put the variable in a dictionary or list according to use
			elif first_word != var and var_true:
				var_true = False
			elif first_word == var and !var_true:
				#execute an error
			
			#if first_word is a label:
				#append the label in a dictionary defined in main() with its corresponding curr_instruction top help in jump statements
				#also execute whats in the label
				#go to the next instruction 
				pass

			#if first_word is a regular instruction:
				#encode it 
				#decide whether assembly code should be generated or you can directly complete the actions and change the registers, flags 
				#and show the errors

	#all the variables, flags and registers are to be put in here:
	var_true = True

	#memory variable(made into a list with 512 elements)
	class MEM:
		memory = []
		
		def initialise(self) -> none:
			for i in range(512):
				memory.append("00000000")

		def dump(self):
			for i in range(512):
				print(memory[i])
	
	class RF:
		dict_register_file = {}

		def initialise(self) -> none:
			#append all register values with 8 bits to the dictionary

		def dump(self) -> none:
			#prints values of registers at that particular time
	#program counter initialised to 0
	class PC:
		program_counter = 0

		def update(self) -> none:
			#updates pc value
	#halting instruction as bool
	halted = False

if __name__ = "__main__":
	main()
