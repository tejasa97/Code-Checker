import re
import os
import sys

#file = open("fact.c", "r")
def initialize(file_name):
	global file_contents
	file = open(file_name, "r")
	spaces = ' ' * 8
	file_contents = file.read()
	#file_contents = re.sub('\t', spaces, file_contents)
	file.close()
	err_cnt = 0
	print(" \n---------------- \n")
	print(">>> Checking file '{}'...\n".format(f))

def make_arrow(st):
		#st = line[0:a]
		st = re.sub(r'\S', ' ', st)
		print(st + '^')

def indent_end_multiple_maxlength():
	err_cnt = 0
	lines = file_contents.split('\n')
	i = 1
	#print (lines)
	for line in lines:
		if line != '':
			#Check for indent error		
			if re.search(r'^\t*[^\s]', line) == None:
				try:
					a = re.search(r'\S', line).start()
					print("** Leading indent error on line {}".format(i))
					print(line)
					print(line[0:a-1] + '^')
					err_cnt += 1
				except AttributeError:
					pass

			#Check for interspersed tabs
			if re.search(r'[^\t].*[\t].*', line):
				print("** Interspersed tab found")
				print(line)
				#a = re.search(r'[^\t].*([\t]).*', line).group(1)
				a = re.search(r'(?<=[^\t])([\t]).*[^\t]', line).start()
				#print(a)
				err_cnt += 1
				make_arrow(line[0:a])

			#Check for trailing whitespace
			if re.search('\s$', line):
				a = re.search('\s$', line).start()
				err_cnt += 1
				print("** Whitespace found at end of line {}".format(i))
				print(line)
				make_arrow(line[0:a])

			#Check for max length of 80
			if(len(line) > 80):
				err_cnt += 1
				print("** Line {} exceeds length of 80 chars".format(i))
			#Check for multiple statements on a single line
			if re.search(r'.+;.*;.*', line):
				if not re.search(r'\(.+;.+\)', line):
					err_cnt += 1
					print("** Multiple statements on line {}".format(i))
					print(line)
		i=i+1

	#Give overfiew of file errors
	if err_cnt == 0:
		print(">>> No errors in file {}".format(f))
	else:
		print(">>> Mistakes found in file {}: {}".format(f,err_cnt))
	print(" \n----------------")

if __name__ == "__main__":
	files = []
	if len(sys.argv) >= 2:
		files.append(sys.argv[1])
	else:
		files = os.listdir()
	if len(files)>1:
		print(">>> Checking all programs in folder...")
	for f in files:
		try:
			if f[-2:] == '.c':
				initialize(f)
				indent_end_multiple_maxlength()
		except FileNotFoundError:
			print("\t\n{} file not found".format(f))

