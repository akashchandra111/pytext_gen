from sys import argv, exit

delimiter = -1
fileName = -1
times = -1
expression = ''

# Read command-line argument
def parseCommand():
	global expression
	global delimiter
	global fileName
	global times

	for i in range(len(argv)):
		if i == 0:
			continue
		else:
			if argv[i] == '-d':
				delimiter = argv[i+1]
			elif argv[i] == '-f':
				fileName = argv[i+1]
			elif argv[i] == '-h':
				# Call help
				help()
			elif argv[i] == '-t':
				times = int(argv[i+1])
			else:
				if argv[i-1] != '-d' or argv[i-1] != '-f' or argv[i-1] != '-h' or argv[i-1] != '-t':
					expression = argv[i]
				else:
					print('Expression not found in the argument list')
					exit(1)

# checks for errors and assigns proper value
def checkForErrors():
	global delimiter
	global fileName
	global times
	global expression

	# Check if delimiter is None
	if delimiter == -1:
		delimiter = '?'

	# Check if fileName is None
	if fileName == -1:
		fileName = 'textgen.csv'

	# Check if time is None
	if times == -1 and expression == '':
		times = 1
	elif times == -1:
		times = 10

# prints help message on -h option
def help():
	print('''
	Usage:	text_gen.py [-d delimiter] [-f filename] [-t times] expression
	Expression example:-
						\
						abc?,12?,h?ell
	Output:
			abc1,121,h1ell
			abc2,122,h2ell
	''')


# text_gen engine
def expressionEval():
	global expression
	file = open(str(fileName), "w")
	for i in range(times):
		newexpr = expression.replace(delimiter, str(i+1))
		file.write(newexpr + '\n')
	file.close()

# debug function
def printlocals(message, checkargs=0):
	global expression
	global delimiter
	global fileName
	global times
	print("Before " + str(message))
	print("expression: " + str(expression))
	print("delimiter: " + str(delimiter))
	print("fileName: " + str(fileName))
	print("times: " + str(times) + '\n')

	if checkargs == 1:
		print("argv: " + str(argv))

# main program starts here
if __name__ == "__main__":
#		printlocals('parseCommand()')
		parseCommand()

#		printlocals('checkForErrors()')
		checkForErrors()

#		printlocals('expressionEval()', 1)
		expressionEval()
