import sys
import re
import crayons
import os


""" PRE-PROCESSING OF FILE """

def initialize(file_name):
	global lines_raw, lines, err_cnt, indent, no_of_lines_raw
	err_cnt = 0
	lines_raw, indent = ([] for i in range(2))

	with open(file_name) as f:
		for line in f:
			lines_raw.append(line.rstrip('\n'))
	no_of_lines_raw = len(lines_raw)
	print(" \n---------------- \n")
	print(crayons.yellow(">>> Checking file '{}'...\n".format(file_name), bold = True))

def comment_detected(index):
	if re.search(r'^\s*\/\*', lines_raw[index]):
		return 2

	elif re.search(r'([^:]|^)\/\/.*$', lines_raw[index]):
		return 1

	else:
		return 0

def comments_skip(index):
	for i in range(index, no_of_lines_raw):
 		if re.search(r'[*][/]', lines_raw[i]):
 			return i+1

def line_append(string, i):
	lines.append(string)
	index_lines.append(i)

def pre_process():
	global lines, index_lines, no_of_lines
	lines, index_lines = ([] for i in range(2))
	
	i = 0	
	while i < no_of_lines_raw:
		a = comment_detected(i)
		if a == 2:
			i = comments_skip(i)
			if lines_raw[i] != '':
				line_append(lines_raw[i], i)

		elif a == 1 :
			string = re.sub(r'([^:]|^)\/\/.*$', '', lines_raw[i])
			if re.search(r'[\S]', string):
				line_append(string, i)

		elif lines_raw[i] == '':
			pass

		else:
			line_append(lines_raw[i], i)
		i = i + 1
		
	no_of_lines = len(lines)


""" END OF PRE-PROCESSING """


""" LEADING AND TRAILING WHITESPACES, MAX LENGTH, MULITPLE STATEMENTS """

def indent_end_multiple_maxlength():
	global indent_flag
	indent_flag = 0
	global err_cnt
	i = 0 
	indent_err = 0
	while i < no_of_lines:

		#Check for indent error	
		if re.search(r'^\t*[^\s]', lines[i]) == None:
			try:
				a = re.search(r'\S', lines[i]).start()
				print_err("** Leading indent error on line {}".format(index_lines[i] + 1))
				print(lines[i])
				print(lines[index_lines[i]][0:a-1] + '^')
				indent_err +=1
			except AttributeError:
				pass

		#Check for interspersed tabs
		if re.search(r'[^\t].*([\t]).*[^\t]$', lines[i]):
			print_err("** Interspersed tab found on line {}".format((index_lines[i] + 1)))
			print(lines[i])
			a = re.search(r'(?<=[^\t])([\t]).*[^\t]', lines[i]).start()
			indent_err +=1
			make_arrow(lines[i][0:a])

		#Check for trailing whitespace
		if re.search('\s$', lines[i]):
			a = re.search('\s$', lines[i]).start()
			indent_err +=1
			print_err("** Whitespace found at end of line {}".format((index_lines[i] + 1)))
			print(lines[i])
			make_arrow(lines[i][0:a])

		#Check for max length of 80
		if len(lines[i]) > 80:
			indent_err +=1
			print_err("** Line {} exceeds length of 80 chars".format((index_lines[i] + 1)))
			make_arrow(lines[i][0])

		#Check for multiple statements on a single line
		if re.search(r'.+;.*;.*', lines[i]):
			if not re.search(r'\(.+;.+\)', lines[i]):
				indent_err +=1
				print_err("** Multiple statements on line {}".format((index_lines[i] + 1)))
				print(lines[i])

		i = i + 1
	if indent_err > 0:
		print_err("** {} indent and spacing error(s) found. Correct them and run the program again.\n".format(indent_err), color = 'yellow')
		indent_flag = 1


""" END OF LEADING AND TRAILING WHITESPACES, MAX LENGTH, MULITPLE STATEMENTS """


""" 'IF' STATEMENT RELATED """

	
def if_for_while(i, clause):
	global err_cnt
	#Store index of line
	incoming = i
	b = r"\s*if\s*\(.+\)" if clause == 'if' else r'\s*for\s*\([^;]*;[^;]*;[^;]*\)' if clause == 'for' else r'\s*while\s*\(.+\)' if clause == 'while' else 0
	
	if re.search(r';$', lines[i]):
		return

	if clause != 'do':

		#Check if there's no '{' neither on the IF statement line, or on the next, thus implying it's a single statement 
		if re.search(r'{$', lines[i]) == None and re.search(r'{$', lines[i+1]) == None:
			searcher = r'.*if([^\s]|[\s]{2,})?.+\)' if clause == 'if' else r'.*for([^\s]|[\s]{2,})?.+\)' if clause == 'for' else r'.*while([^\s]|[\s]{2,})?.+\)' if clause =='while' else 0
			paranthesis = re.search(searcher, lines[i])
			if paranthesis.group(1) != None:
				a = paranthesis.start(1)
				print_err("** '{}' statement indent error on line {}".format(clause,(index_lines[i] + 1)))
				print(lines[i])
				make_arrow(lines[i][:a])
				err_cnt += 1

	#Check if statement has '{' trailing on IF statement line
	if re.search(r'({)$', lines[i]):
		searcher = r".*if([^\s]|[\s]{2,})?.+\)([^\s]|[\s]{2,})?" if clause == 'if' else r".*for([^\s]|[\s]{2,})?.+\)([^\s]|[\s]{2,})?" if clause == 'for' else r".*while([^\s]|[\s]{2,})?.+\)([^\s]|[\s]{2,})?" if clause == 'while' else r".*do([^\s]|[\s]{2,})?" if clause == 'do' else 0
		match = re.search(searcher, lines[i])
		if len(match.groups()) > 0:
			for j in range(1, len(match.groups()) + 1):
				if match.group(j) != None:
					print_err("** '{}' statement indent error on line {}".format(clause, (index_lines[i] + 1)))
					print(lines[i])
					make_arrow(lines[i][0:match.start(j)])
					err_cnt += 1
		if_lines = match_paranthesis(i, 0, clause)
		if if_lines == 1:
			b = re.search(r'({)', lines[i]).start(1)
			print_err("** '{0}' statement on line {1} contains a single statement and shouldn't have braces".format(clause, (index_lines[i] + 1)))
			print(lines[i])
			make_arrow(lines[i][0:b])
			err_cnt += 1

	#Check if statement has '{' trailing on line after IF statement	
	elif re.search(r'\s*({)\s*', lines[i+1]):
			print_err("** Opening brace \'{{\' should be after '{}' clause on line {}".format(clause, (index_lines[i] + 1)))
			searcher = r'.*if\s*\(.+(\))' if clause == 'if' else r'.*for\s*\(.+(\))' if clause == 'for' else r'.*while\s*\(.+(\))' if clause == 'while' else r'\s*do(\s*)'
			a = re.search(searcher, lines[i]).start(1)
			print(lines[i])
			make_arrow(lines[i][:a])
			if_lines = match_paranthesis(i+1, 1, clause)
			if if_lines == 1:
				b = re.search(r'.*({).*', lines[i+1]).start(1)
				print_err("** '{0}' statement on line {1} contains a single statement and shouldn't have braces".format(clause, (index_lines[i] + 1)))
				print(lines[i+1])
				make_arrow(lines[i+1][0:b])
				err_cnt += 1


def else_(i, clause):
	global err_cnt
	#Store index of line
	incoming = i
	check_ = r'}\s*else\s*' if clause == 'else' else r'}\s*else\s+if\s*\(.+\)'

	#Check if it follows the IF statement correctly
	if re.search(check_, lines[i]) == None and re.search('}$', lines[i-1]) == None:
		pass

	elif re.search(check_, lines[i]) == None and re.search('}$', lines[i-1]):
		print_err("** '{}' clause on line {} has to follow \'{{\' of 'if' statement".format(clause, (index_lines[i] + 1)))
		print(lines[i])
		make_arrow(lines[i][0])
		err_cnt += 1

	else :
		a = re.search(r'}([^\s]|[\s]{2,})?e?lse', lines[i])
		if a and a.groups(1):
			print_err("** '{}' statement indent error on line {}".format(clause, (index_lines[i] + 1)))
			print(lines[i])
			make_arrow(lines[i][0:a.start(1)])
			err_cnt += 1

	#Check if there's no '{', neither on the ELSE (IF) statement line, or on the next, thus implying it's a single statement 
	if re.search(r'{$', lines[i]) == None and re.search(r'{$', lines[i+1]) == None:
		paranthesis = re.search(r'else([^\s]|[\s]{2,})?', lines[i]) if clause == 'else' else re.search(r'.*else\s{1,}if([^\s]|[\s]{2,})?.+\)', lines[i])
		if paranthesis.group(1) != None:
			a = paranthesis.start(1)
			print_err("** '{}' statement indent error on line {}".format(clause, (index_lines[i] + 1)))
			print(lines[i])
			make_arrow(lines[i][:a])
			err_cnt += 1
	
	#Check if statement has '{' trailing on ELSE (IF) statement line
	elif re.search(r'({)$', lines[i]):
		paranthesis = r'.*else([^\s]|[\s]{2,})?' if clause == 'else' else r'.*else\s+if([^\s]|[\s]{2,})?.+\)([^\s]|[\s]{2,})?'
		match = re.search(paranthesis, lines[i])
		if len(match.groups()) > 0:
			for j in range(1, len(match.groups()) + 1):
				if match.group(j) != None:
					print_err("** '{}' statement indent error on line {}".format(clause,(index_lines[i] + 1)))
					print(lines[i])
					make_arrow(lines[i][0:match.start(j)])
					err_cnt += 1

		if_lines = match_paranthesis(i, 0)
		if if_lines == 1:
			b = re.search(r'({)', lines[i]).start(1)
			print_err("** '{}' statement on line {} contains a single statement and shouldn't have braces".format(clause,(index_lines[i] + 1)))
			print(lines[i])
			make_arrow(lines[i][0:b])
			err_cnt += 1
	
	#Check if statement has '{' trailing on line after ELSE (IF) statement	
	elif re.search(r'\s*({)\s*', lines[i+1]):
			print_err("** Opening \'{{\' should be after '{}' clause on line {}".format(clause,(index_lines[i] + 1)))
			paranthesis = r'.*else\s+if\s*\(.+(\))' if clause == 'else if' else r'.*else(\s*)'
			a = re.search(paranthesis, lines[i]).start(1)
			print(lines[i])
			make_arrow(lines[i][:a])
			err_cnt += 1

			if_lines = match_paranthesis(i+1, 1)
			if if_lines == 1:
				b = re.search(r'.*({).*', lines[i+1]).start(1)
				print_err("** '{}' statement on line {} contains a single statement and shouldn't have braces".format(clause, (index_lines[i] + 1)))
				print(lines[i+1])
				make_arrow(lines[i+1][0:b])
				err_cnt += 1

def cond_loop_search():

	# IF searcher regex
	_if = r"^\s*if\s*\(.+\)"
	_for = r"^\s*for\s*\([^;]*;[^;]*;[^;]*\)"
	_while = r"^\s*while\s*\(.+\)"
	_do = r"^\s*do\s*"
	i = 0
	while i < no_of_lines:

		#Look for if statements
		if re.search(_if, lines[i]):
			if_for_while(i, 'if')

		elif re.search(_for, lines[i]):
			if_for_while(i, 'for')

		elif re.search(_while, lines[i]):
			if_for_while(i, 'while')

		elif re.search(_do, lines[i]):
			if_for_while(i, 'do')

		i = i + 1

def else_search():

	#ELSE (IF) searcher regex 
	_else = r'else'
	_else_if = r'else\s+if\s*\(.+\)'
	j = 0

	while j < no_of_lines:
		match1 = re.search(_else, lines[j])
		match2 = re.search(_else_if, lines[j])
		if match2 :
			else_(j, 'else if')
		elif match1:
			else_(j, 'else')
		j += 1


""" END 'IF' STATEMENT RELATED """


""" FUNCTIONS RELATED """

def functions_():
	func_ = r'^(\w+[*]*\s+){1,}\w+(\s)?\(.+\)[^;]'
	i = 0

	while i < no_of_lines:
		if re.search(func_, lines[i]):
			a = re.search(func_, lines[i])
			b = re.search(r'({)$', lines[i])
			if b.group(1):
				print_err("** Opening brace \'{{\' of function on line {} should be on next line".format((index_lines[i] + 1)))
				print(lines[i])
				make_arrow(lines[i][:b.start(1)])
			if a.group(2):
				print_err("** Indent error of function on line {}".format((index_lines[i] + 1)))
				print(lines[i])
				make_arrow(lines[i][:a.group(2)])
		i += 1


""" END FUNCTIONS RELATED """


""" MISCELLANEOUS """


def make_arrow(st):
		#Print required line with a marker
		st = re.sub(r'\S', ' ', st)
		print(crayons.green(st + '^', bold = True))

def match_paranthesis(i, c, clause = None):
	incoming = i - c

	cnt = 0
	while i < no_of_lines:
		if re.search(r'^[^\S]*}', lines[i]) and re.search(r'.+{', lines[i]):
			cnt = cnt + 1 if i == incoming + c else cnt - 1

		elif re.search(r'}', lines[i]):
			cnt -= 1

		elif re.search(r'{', lines[i]):
			cnt += 1
		if cnt == 0:
			break
		i += 1

	match = re.search(r'(})', lines[i])
	if match and re.search(r'\S+}', lines[i]):
		a = re.search(r'(})', lines[i])
		print_err("** Closing brace }} on line LINE should be on a line of its own".format(index_lines[i] + 1))
		print(lines[i])
		make_arrow(lines[i][:a.start(1)])

	if clause == 'do':
		if re.search(r'}\s*while\s*\(.+\)\s*;', lines[i]):
			a = re.search(r"}([^\s]|[\s]{2,})?\s?w?hile([^\s]|[\s]{2,})?.+\)\s*;", lines[i])

			for j in range(1,3):
				if a.group(j) != None:
					print_err("** Indent error on line {} of 'do while' statement".format(index_lines[i] + 1))
					print(lines[i])
					make_arrow(lines[i][0:a.start(j)])
		else:
			print_err("'while' clause required at end of 'do while' statement")
			print(lines[i])
			make_arrow(lines[i][0])

	lines_l = i - incoming - c - 1
	return lines_l

def print_err(error, color = 'red'):
	blue = re.search(r'(line \d+)', error)
	if blue:
		number = blue.group(1)
		error = error.split(number)
		print(getattr(crayons, color)(error[0], bold = True) + crayons.green(number, bold = True) + getattr(crayons, color)(error[1], bold = True))

	else:
		print(getattr(crayons, color)(error, bold = True))


""" END OF MISCALLANEOUS """

""" MAIN FUNCTION """


if __name__ == "__main__":
	files = []
	if len(sys.argv) >= 2:
		files.append(sys.argv[1])
	else:
		os.chdir('programs/')
		files = os.listdir()
	if len(files)>1:
		print_err(">>> Checking all programs in folder...", color = 'yellow')
	for f in files:
		try:
			if f[-2:] == '.c':
				initialize(f)

			else:
				continue
				
		except FileNotFoundError:
			print("\t\n{} file not found".format(f))
			exit()

		else:
			pre_process()
			indent_end_multiple_maxlength()
			if indent_flag == 1:
				continue
			cond_loop_search()
			else_search()
			functions_()

			print_err("No errors found in file {}!".format(f), color = 'blue') if err_cnt == 0 else print_err("{} errors found in file {}!".format(err_cnt, f), color = 'blue') if err_cnt > 0 else " "


""" END OF MAIN FUNCTION """
	
