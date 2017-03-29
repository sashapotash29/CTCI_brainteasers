# 1.1 is unique? - Determine if a string contains unique characters

def is_unique(string):
	comparison_list=[]
	for letter in string:
		if letter.lower() in comparison_list:
			return False
		comparison_list.append(letter.lower())
		if len(comparison_list) == len(string):
			return True
		else:
			pass
			

# # TESTING AREA
# print("sasha")
# output = is_unique("sasha")
# print(output)
# output = is_unique("cat")
# print("cat")
# print(output)
# # CLOSE TESTING AREA


# 1.2 Check Permutation? - Determine with two strings if one string is a permutation of the other

def is_perm(stringOne, stringTwo):
	if stringOne == stringTwo:
		return True
	if len(stringOne) == len(stringTwo):
		test_string = ""
		for letter in stringOne:
			if letter in stringTwo:
				test_string += letter
			else:
				return False
		return True
	else:
		return False


# # TESTING AREA
# print("bat and tab")
# output = is_perm("bat", "tab")
# print(output)
# print("sapplein and saplpien")
# output = is_perm("sapplein", "saplpien")
# print(output)
# # CLOSE TESTING AREA


# 1.3 Check Permutation? - Determine with two strings if one string is a permutation of the other

def urlify(string):
	url_string=""
	for letter in string:
		if letter == " ":
			url_string += "%20"
		else:
			url_string += letter
	return url_string


# # TESTING AREA
# print("Mr John Smith")
# output = urlify("Mr John Smith")
# print(output)
# print("the url for all urls")
# output = urlify("the url for all urls")
# print(output)
# # CLOSE TESTING AREA


# 1.4 Palindrome Permutation? - Determine if a string has the ability to form a palindrome

def pal_perm(string):
	if len(string)%2==0:
		print("even")
		word_dict = {}
		for letter in string:
			if letter in word_dict.keys():
				word_dict[letter] += 1
			else:
				word_dict[letter] = 1
		checker = 0
		for key, value in word_dict.items():
			if word_dict[key] == 2:
				checker += 1
			else:
				return False
		if checker%2==0:
			return True
		else:
			print(checker)
	else:
		print("odd")
		word_dict = {}
		for letter in string:
			if letter in word_dict.keys():
				word_dict[letter] += 1
			else:
				word_dict[letter] = 1
		checker = 0
		for key, value in word_dict.items():
			if checker == 2:
				print("checker caught it")
				return False
			elif value%2 == 0:
				pass
			elif value == 1:
				checker +=1
		if checker == 1:
			return True
		else:
			return False


# # # TESTING AREA
# print("abba")
# output = pal_perm("abba")
# print(output)
# print("ccall")
# output = pal_perm("ccall")
# print(output)
# # CLOSE TESTING AREA



# 1.5 One Away? - Determine if one string is a single character away from being the second string


def one_away(string, check):
	if string == check:
		return True
	elif len(string) == len(check):
		wrong = 0
		for letter in string:
			if letter in check:
				print("yes " + letter)
			if letter not in check:
				wrong += 1
		if wrong == 1:
			print(string)
			print(check)
			return True
		elif wrong >1:
			print(string)
			print(check)
			return False
	elif len(string)%len(check)==1 or len(check)%len(string) ==1:
		wrong = 0
		for letter in string:
			if letter in check:
				pass
			if letter not in check:
				wrong += 1
		if wrong <= 1:
			print(string)
			print(check)
			return True
		elif wrong >1:
			print(string)
			print(check)
			return False
	else:
		print("else")
		return False

# # TESTING AREA
# print("aaaa and aaa")
# output = one_away("aaaaa","aaa")
# print(output)
# print("pale and bake")
# output = one_away("pale", "bake")
# print(output)
# # CLOSE TESTING AREA


# 1.6 String Compression? - Determine the amount of each character in a row


def string_compr(string):
	final_string = ""
	counter = 1
	for index in range(0,len(string)):
		if index == len(string)-1:
			final_string += string[index] + str(counter)
		elif string[index] == string[index+1]:
			counter+=1
		elif string[index+1]:
			if string[index] != string[index+1]:
				final_string += string[index] + str(counter)
				counter=1
		else:
			print("in else")
			final_string += string[index] + str(counter)
			
	return final_string





# # TESTING AREA
# print("aaaabbbaaccdddjj")
# output = string_compr("aaaabbbaaccdddjj")
# print(output)
# print("abcd")
# output = string_compr("abcjjjkkaskaasasskkksd")
# print(output)
# # CLOSE TESTING AREA





