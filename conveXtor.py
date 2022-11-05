import os

hexTable = {
	0  : '0' ,
	1  : '1' , 
	2  : '2' , 
	3  : '3' , 
	4  : '4' , 
	5  : '5' , 
	6  : '6' , 
	7  : '7' , 
	8  : '8' , 
	9  : '9' , 
	10 : 'A' , 
	11 : 'B' , 
	12 : 'C' , 
	13 : 'D' , 
	14 : 'E' , 
	15 : 'F' , 
}	

base64Table = {
	0  :  'A' ,
	1  :  'B' ,
	2  :  'C' ,
	3  :  'D' ,
	4  :  'E' ,
	5  :  'F' ,
	6  :  'G' ,
	7  :  'H' ,
	8  :  'I' ,
	9  :  'J' ,
	10 :  'K' ,
	11 :  'L' ,
	12 :  'M' ,
	13 :  'N' ,
	14 :  'O' ,
	15 :  'P' ,
	16 :  'Q' ,
	17 :  'R' ,
	18 :  'S' ,
	19 :  'T' ,
	20 :  'U' ,
	21 :  'V' ,
	22 :  'W' ,
	23 :  'X' ,
	24 :  'Y' ,
	25 :  'Z' ,
	26 :  'a' ,
	27 :  'b' ,
	28 :  'c' ,
	29 :  'd' ,
	30 :  'e' ,
	31 :  'f' ,
	32 :  'g' ,
	33 :  'h' ,
	34 :  'i' ,
	35 :  'j' ,
	36 :  'k' ,
	37 :  'l' ,
	38 :  'm' ,
	39 :  'n' ,
	40 :  'o' ,
	41 :  'p' ,
	42 :  'q' ,
	43 :  'r' ,
	44 :  's' ,
	45 :  't' ,
	46 :  'u' ,
	47 :  'v' ,
	48 :  'w' ,
	49 :  'x' ,
	50 :  'y' ,
	51 :  'z' ,
	52 :  '0' ,
	53 :  '1' ,
	54 :  '2' ,
	55 :  '3' ,
	56 :  '4' ,
	57 :  '5' ,
	58 :  '6' ,
	59 :  '7' ,
	60 :  '8' ,
	61 :  '9' ,
	62 :  '+' ,
	63 :  '/' 
}

acsiiTable = {
	'20' : ' ',
	'21' : '!',
	'22' : '"',
	'23' : '#',
	'24' : '$',
	'25' : '%',
	'26' : '&',
	'27' : "'",
	'28' : '(',
	'29' : ')',
	'2A' : '*',
	'2B' : '+',
	'2C' : ',',
	'2D' : '-',
	'2E' : '.',
	'2F' : '/',
	'30' : '0',
	'31' : '1',
	'32' : '2',
	'33' : '3',
	'34' : '4',
	'35' : '5',
	'36' : '6',
	'37' : '7',
	'38' : '8',
	'39' : '9',
	'3A' : ':',
	'3B' : ';',
	'3C' : '<',
	'3D' : '=',
	'3E' : '>',
	'3F' : '?',
	'40' : '@',
	'41' : 'A',
	'42' : 'B',
	'43' : 'C',
	'44' : 'D',
	'45' : 'E',
	'46' : 'F',
	'47' : 'G',
	'48' : 'H',
	'49' : 'I',
	'4A' : 'J',
	'4B' : 'K',
	'4C' : 'L',
	'4D' : 'M',
	'4E' : 'N',
	'4F' : 'O',
	'50' : 'P',
	'51' : 'Q',
	'52' : 'R',
	'53' : 'S',
	'54' : 'T',
	'55' : 'U',
	'56' : 'V',
	'57' : 'W',
	'58' : 'X',
	'59' : 'Y',
	'5A' : 'Z',
	'5B' : '[',
	'5C' : '\\',
	'5D' : ']',
	'5E' : '^',
	'5F' : '_',
	'60' : '`',
	'61' : 'a',
	'62' : 'b',
	'63' : 'c',
	'64' : 'd',
	'65' : 'e',
	'66' : 'f',
	'67' : 'g',
	'68' : 'h',
	'69' : 'i',
	'6A' : 'j',
	'6B' : 'k',
	'6C' : 'l',
	'6D' : 'm',
	'6E' : 'n',
	'6F' : 'o',
	'70' : 'p',
	'71' : 'q',
	'72' : 'r',
	'73' : 's',
	'74' : 't',
	'75' : 'u',
	'76' : 'v',
	'77' : 'w',
	'78' : 'x',
	'79' : 'y',
	'7A' : 'z',
	'7B' : '{',
	'7C' : '|',
	'7D' : '}',
	'7E' : '~',
}



def get_keys_from_value(d, val):
    return [k for (k,v) in d.items() if v == val][0]



def d2b(desimalNum):
	#Desimal to Binary

	binaryNum = ''

	while (True):

		binaryNum = str(desimalNum%2) + binaryNum
		desimalNum //= 2

		if (desimalNum == 1 or desimalNum == 0):
			binaryNum = str(desimalNum) + binaryNum
			break

	return binaryNum


def f2b(num):
	#float to Binary

	if ('.' not in num):
		num += '.0'

	binary1 = binary2 =  ''

	num = str(num).split('.')
	intNum = int(num[0])
	floatNum = float(str(0)+'.'+num[1])


	while not(floatNum == 0.0):

		floatNum *= 2

		if (floatNum == 1.0):
			binary2 += str(1)
			break

		elif (floatNum > 1.0):
			floatNum -= 1.0
			binary2 += str(1)

		elif (floatNum < 1.0):
			binary2 += str(0)



	while (True):

		binary1 = str(intNum%2) + binary1
		intNum //= 2

		if (intNum == 1 or intNum == 0):
			binary1 = str(intNum) + binary1
			break

	binaryNum = float(binary1 + '.' + binary2)

	return binaryNum


def d2fc(desimalNum):
	# Desimal to first complement

	binaryNum = ''

	if (desimalNum < 0):
		
		desimalNum = 0 - desimalNum
		temp = d2b(desimalNum)

		for x in temp:
			if (x=='1'):
				binaryNum += '0'
			elif (x=='0'):
				binaryNum += '1'

		while (len(binaryNum)<8):
			binaryNum = str('1') + binaryNum

	else:

		binaryNum = d2b(desimalNum)

		while (len(binaryNum)<8):
			binaryNum = str('0') + binaryNum

	return binaryNum
			


def o2fc(octalNum):
	# Octal to first complement

	if ( octalNum[0] == '-'):
		octalNum = -int(octalNum)
		binaryNum = d2fc(-int(o2d(octalNum)))
	else:
		binaryNum = d2fc(int(o2d(octalNum)))

	return binaryNum


def h2fc(hexNum):
	# Hexa Desimal to first complement

	if ( hexNum[0] == '-'):
		temp = list(hexNum)
		temp.pop(0)
		hexNum = ''

		for charactor in temp:
			hexNum += charactor
		binaryNum = d2fc(-int(h2d(hexNum)))

	else:
		binaryNum = d2fc(int(h2d(hexNum)))

	return binaryNum



def d2sc(desimalNum):
	# Desimal to second compliment

	binaryNum = ''

	if (desimalNum < 0):
	

		if (desimalNum > -2**8):
			desimalNum = 2**8 + desimalNum
			temp = d2b(desimalNum)

			while ( len(temp) < 8 ):
				temp = str(1) + temp
			binaryNum = temp


		elif (desimalNum > -2**16):

			desimalNum = 2**16 + desimalNum
			temp = d2b(desimalNum)

			while ( len(temp) < 16 ):
				temp = str(1) + temp
			binaryNum = temp


		elif (desimalNum > -2**32):

			desimalNum = 2**32 + desimalNum
			temp = d2b(desimalNum)

			while ( len(temp) < 16 ):
				temp = str(1) + temp
			binaryNum = temp



		elif (desimalNum > -2**64):

			desimalNum = 2**64 + desimalNum
			temp = d2b(desimalNum)

			while ( len(temp) < 16 ):
				temp = str(1) + temp
			binaryNum = temp

		else:
			return 'ERROR : required number must be under the 64 bits'



	else:

		temp = d2b(desimalNum)
		
		if (len(temp)<8):
			while (len(temp)<8):
				temp = str(0) + temp
		
		elif (len(temp)<16):
			while (len(temp)<16):
				temp = str(0) + temp
		
		elif (len(temp)<32):
			while (len(temp)<32):
				temp = str(0) + temp
		
		elif (len(temp)<64):
			while (len(temp)<64):
				temp = str(0) + temp
		
		else:
			return 'ERROR : required number must be under the 64 bits'

		binaryNum = temp

	return binaryNum
			



def o2sc(octalNum):
	# Octal to first complement

	if ( octalNum[0] == '-'):
		octalNum = -int(octalNum)
		binaryNum = d2sc(-int(o2d(octalNum)))
	else:
		binaryNum = d2sc(int(o2d(octalNum)))

	return binaryNum


def h2sc(hexNum):
	# Hexa Desimal to first complement

	if ( hexNum[0] == '-'):
		temp = list(hexNum)
		temp.pop(0)
		hexNum = ''

		for charactor in temp:
			hexNum += charactor
		binaryNum = d2sc(-int(h2d(hexNum)))

	else:
		binaryNum = d2sc(int(h2d(hexNum)))

	return binaryNum





def d2o(desimalNum):
	# Desimal to Octal

	octalNum = ''

	while (True):
		
		octalNum = str(desimalNum % 8) + octalNum
		desimalNum //= 8

		if (desimalNum < 8):
			octalNum = str(desimalNum) + octalNum
			break

	return octalNum



def d2h(desimalNum):
	# Desimal to Hexa desimal

	hexNum = ''

	while (True):
		
		hexNum = str(hexTable[ desimalNum % 16 ]) + hexNum
		desimalNum //= 16

		if (desimalNum < 16):
			hexNum = str(desimalNum) + hexNum
			break

	return hexNum




def b2d(binaryNum):
	# Binary to Desimal

	desimalNum = 0
	i = 1 

	while ( i < len( str(binaryNum) )+1 ) :	
		desimalNum += int(str(binaryNum)[-i]) * (2** (i-1) )
		i += 1
		
	return desimalNum



def b2f(binaryNum):
	# Binary to float

	if ('.' not in binaryNum):
		binaryNum += '.0'

	floatNum = 0.0
	float1 = 0.0
	float2 = 0.0
	binaryNum = str(binaryNum).split('.')
	binary1 = binaryNum[0]
	binary2 = binaryNum[1]


	float1 = float(b2d( binary1))

	i = 0
	while ( i < len(binary2) ):
		float2 += float(str(binary2)[i]) * ( (1/2) ** (i+1) )
		i += 1

	floatNum = float1 + float2

	return floatNum




def o2d(octalNum):
	# Octal to Desimal

	desimalNum = 0
	i = 1

	while (i < len( str(octalNum) )+1 ):
		desimalNum += int( str(octalNum)[-i]) * (8** (i-1) )
		i += 1

	return desimalNum



def h2d(hexNum):
	# Hexa desimal to desimal
	
	desimalNum = 0
	i = 1

	while (i < len( str(hexNum) )+1 ) :
		desimalNum += get_keys_from_value(hexTable,str(hexNum)[-i]) * (16** (i-1))
		i += 1

	return desimalNum


def b2o(binaryNum):
	# Binary to Octal

	octalNum =  d2o(b2d(binaryNum))
	return octalNum


def b2h(binaryNum):
	# Binary to Hexa desimal

	hexNum = d2h(b2d(binaryNum))
	return hexNum


def o2b(octalNum):
	# Octal to Binary

	binaryNum = d2b(o2d(octalNum))
	return binaryNum


def h2b(hexNum):
	# Hexa desimal to Binary

	binaryNum = d2b(h2d(hexNum))
	return binaryNum


def o2h(octalNum):
	# Octal to Hexa desimal

	hexNum = d2h(o2d(octalNum))
	return hexNum


def h2o(hexNum):
	# Hexa desimal to Octal

	octalNum = d2o(h2d(hexNum))
	return octalNum




def ieee754_32bit(floatNum):
	# IEEE754 Single precision (32Bit)
	
	floatNum = float(floatNum)

	if ( floatNum < 0 ):
		floatNum = -floatNum
		sign = '1'
	else:
		sign = '0'

	binaryNum = f2b(str(floatNum))

	i = 0
	while (str(binaryNum)[i] != '.') :
		i += 1
	else:
		n = i-1

		temp = str(binaryNum).split('.')
		temp = temp[0] + temp[1]

		mantissa = temp[1::]
		while (len(mantissa) < 23):
			mantissa += '0'

		exponent = d2b( (127+n) )

		ieee754 = sign+exponent+mantissa

		return ieee754,sign,exponent,mantissa


def ieee754_64bit(floatNum):
	# IEEE754 Double precision (64Bit)
	
	floatNum = float(floatNum)

	if ( floatNum < 0 ):
		floatNum = -floatNum
		sign = '1'
	else:
		sign = '0'

	binaryNum = f2b(str(floatNum))

	i = 0
	while (str(binaryNum)[i] != '.') :
		i += 1
	else:
		n = i-1

		temp = str(binaryNum).split('.')
		temp = temp[0] + temp[1]

		mantissa = temp[1::]
		while (len(mantissa) < 52):
			mantissa += '0'

		exponent = d2b( (1023+n) )

		ieee754 = sign+exponent+mantissa

		return ieee754,sign,exponent,mantissa

	


def a2h(text):
	# ACSSI to HEX
	
	convText = ''

	for charactor in text:
		convText += get_keys_from_value(acsiiTable,charactor) + ' '

	return convText


def a2b(text):
	# ACSII to Binary

	convText = ''
	hexCodeLst = a2h(text).split(' ')
	hexCodeLst.pop()

	for hexCode in hexCodeLst:
		convText += str(h2b(hexCode)) + ' '

	return convText

	

def a2o(text):
	# ACSII to Octal

	convText = ''
	hexCodeLst = a2h(text).split(' ')
	hexCodeLst.pop()

	for hexCode in hexCodeLst:
		convText += str(h2o(hexCode)) + ' '

	return convText

			

def a2d(text):
	# ACSII to Desimal

	convText = ''
	hexCodeLst = a2h(text).split(' ')
	hexCodeLst.pop()

	for hexCode in hexCodeLst:
		convText += str(h2d(hexCode)) + ' '

	return convText



def base64_encode(text):
	# BASE64 encode
	convText = ''
	temp = ''
	

	binaryNumLst = a2b(text).split(' ')
	binaryNumLst.pop()

	for binaryNum in binaryNumLst:

		if (len(binaryNum) < 9):
			while (len(binaryNum) != 8):
				binaryNum = str(0) + binaryNum

		temp += binaryNum

	temp = list(temp)
	binaryNum = ''
	binaryNumLst = []
	i = 1
	
	for charactor in temp:
		binaryNum += charactor


		if (len(binaryNum) == 6):
			binaryNumLst.append(binaryNum)
			binaryNum = ''

		i += 1

	if (len(binaryNum) > 0):

		if (len(binaryNum) < 6):
			while (len(binaryNum) < 6):
				binaryNum += str(0)
		binaryNumLst.append(binaryNum)

	del(binaryNum)
	del(temp)

	numLst = []
	for binaryNum in binaryNumLst:
		numLst.append(b2d(binaryNum))
		i += 1

	for num in numLst:
		convText += base64Table[num]

	if not ( len(convText) % 4 == 0):
		while (True):
			convText += '='
			if (len(convText) % 4 == 0):
				break
	del(numLst)

	return convText


def base64_decode(text):

	convText = ''
	text = list(text)
	i = text.count('=')

	for j in range (0, len(text)-i ):
		if (text[j] == '='):
			return 'Incorrect format for BASE64'
		if (text[j] not in base64Table.values()):
			return 'Incorrect format for BASE64'

	for j in range (i):
		text.pop(-1)
	del(i)

	temp = ''
	for charactor in text:
		binaryNum = d2b( get_keys_from_value(base64Table,charactor) )

		if (len(binaryNum) <6 ):
			while (len(binaryNum) < 6):
				binaryNum = str(0) + binaryNum
		temp += binaryNum

	binaryNum = ''
	binaryNumLst = []

	for charactor in temp:
		binaryNum += charactor

		if (len(binaryNum)==8):
			binaryNumLst.append(binaryNum)
			binaryNum = ''

	if binaryNum:
		if not(int(binaryNum) == 0):
			return 'Incorrect format for BASE64'

	numLst = []

	for binaryNum in binaryNumLst:
		if(b2h(binaryNum) not in acsiiTable.keys()):
			return 'Incorrect format for BASE64'
		convText += acsiiTable[ b2h(binaryNum) ]

	return convText



def banner():

	os.system('cls')
	
	print('\n\n')
	print('\t #####  ###    ###   #  ##    #  #####   ###    ##### #######  ###   ######  ')
	print('\t##     ##   #  ## #  #  ##    #  #         ##  ##       ###   ##   #  ##    #')
	print('\t##     ##   #  ##  # #  ##    #  ###        ####         #    ##   #  ##    #')
	print('\t##     ##   #  ##   ##  ##   #   ###        ####         #    ##   #  ## ### ')
	print('\t##     ##   #  ##    #   ## #    #         ##  ##        #    ##   #  ##    #')   
	print('\t #####  ###    ##    #    ##     ##### #####    ###      #     ###    ##    #\n\n')

def main ():

	os.system('color 3')
	os.system('mode 90')


	while (True):
	
		banner()
		print('='*90,'\n',' '*34,'CONVEXTOR MAIN MENU\n')
		print('='*90)
		choise_mainMenu = input(

			"\n 1 - ACSII Convertor \n"
			" 2 - Base Convertor \n"
			" 3 - IEEE_754 Convertor \n"
			" 4 - BASE_64 Encode and Decode \n"
			" 5 - Credits \n\n"
			" Please enter the number of your choise or '0' to Exit => " 
			)
		if (not choise_mainMenu.isnumeric()): continue
		
		elif (choise_mainMenu == '0'): break

		elif (choise_mainMenu == '1'):

			while (True):
			
				banner()

				print('='*37, 'ACSII CONVERTOR', '='*36,'\n')

				choise_subMenu = input(

					" 1 - ACSII to Hexa Desimal Convertor \n"
					" 2 - ACSII to Octal Convertor \n"
					" 3 - ACSII to Desimal Convertor \n"
					" 4 - ACSII to Binary Convertor \n\n"
					# " 5 - Hexa Desimal to ACSII Convertor \n"
					# " 6 - Octal to ACSII Convertor \n"
					# " 7 - Desimal to ACSII Convertor \n"
					# " 8 - Binary to ACSII Convertor \n\n"
					" Please enter the number of your choise or '0' to back => " 
					)
			
				if ( not choise_subMenu.isnumeric() ): continue

				elif ( choise_subMenu == '0'): break

				elif (choise_subMenu == '1'):
				
					while (True):
						banner()
						print('-'*28, 'ACSII TO HEXA DESIMAL CONVERTOR', '-'*29,'\n')

						text = input(" Enter your text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						else :
							result = a2h(text)
							input("\n\n Entered text :- \n\n %s \n\n\n Converted text :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))

				elif (choise_subMenu == '2'):
				
					while (True):
						banner()
						print('-'*32, 'ACSII TO OCTAL CONVERTOR', '-'*32,'\n')

						text = input(" Enter your text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						else :
							result = a2o(text)
							input("\n\n Entered text :- \n\n %s \n\n\n Converted text :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))

				elif (choise_subMenu == '3'):
				
					while (True):
						banner()
						print('-'*31, 'ACSII TO DESIMAL CONVERTOR', '-'*31,'\n')

						text = input(" Enter your text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						else :
							result = a2d(text)
							input("\n\n Entered text :- \n\n %s \n\n\n Converted text :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))

				elif (choise_subMenu == '4'):
				
					while (True):
						banner()
						print('-'*32, 'ACSII TO BINARY CONVERTOR', '-'*31,'\n')

						text = input(" Enter your text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						else :
							result = a2b(text)
							input("\n\n Entered text :- \n\n %s \n\n\n Converted text :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))





		elif (choise_mainMenu == '2'):

			while (True):
			
				banner()
				print('='*37, 'BASE CONVERTOR', '='*37,'\n')

				choise_subMenu = input(

				" 1  - Binary to Hexa Desimal Convertor \n"
				" 2  - Binary to Octal Convertor \n"
				" 3  - Binary to Desimal(Intiger) Convertor \n"
				" 4  - Binary to Desimal(Float) Convertor \n\n"
			
				" 5  - Desimal to Hexa Desimal Convertor \n"
				" 6  - Desimal to Octal Convertor \n"
				" 7  - Desimal(Intiger) to Binary Convertor \n"
				" 8  - Desimal(Float) to Binary Convertor \n"
				" 9  - Desimal(Intiger) to first complement \n"
				" 10 - Desimal(Intiger) to second complement \n\n"
			
				" 11 - Octal to Hexa Desimal Convertor \n"
				" 12 - Octal to Desimal Convertor \n"
				" 13 - Octal to Binary Convertor \n"
				" 14 - Octal to first complement \n"
				" 15 - Octal to second complement \n\n"

			
				" 16 - Hexa Desimal to Octal Convertor \n"
				" 17 - Hexa Desimal to Desimal Convertor \n"
				" 18 - Hexa Desimal to Binary Convertor \n"
				" 19 - Hexa Desimal to first complement \n"
				" 20 - Hexa Desimal to second complement \n\n\n"


				" Please enter the number of your choise or '0' to back : " 
				)
			
				if ( not choise_subMenu.isnumeric() ): continue

				elif ( choise_subMenu == '0'): break

				elif (choise_subMenu == '1'):
				
					while (True):
						banner()
						print('-'*27, 'BINARY TO HEXA DESIMAL CONVERTOR', '-'*29,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor == '0' or charactor == '1'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in BINARY(BASE 2) format !")
							continue

						else:
							result = b2h(text)
							input("\n\n Binary number :- \n\n %s \n\n\n Hexa Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '2'):
				
					while (True):
						banner()
						print('-'*31, 'BINARY TO OCTAL CONVERTOR', '-'*32,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor == '0' or charactor == '1'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in BINARY(BASE 2) format !")
							continue

						else:
							result = b2o(text)
							input("\n\n Binary number :- \n\n %s \n\n\n Octal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '3'):
				
					while (True):
						banner()
						print('-'*26, 'BINARY TO DESIMAL(INTIGER) CONVERTOR', '-'*26,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor == '0' or charactor == '1'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in BINARY(BASE 2) format !")
							continue

						else:
							result = b2d(text)
							input("\n\n Binary number :- \n\n %s \n\n\n Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '4'):
				
					while (True):
						banner()
						print('-'*27, 'BINARY TO DESIMAL(Float) CONVERTOR', '-'*27,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor == '0' or charactor == '1' or charactor == '.'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in BINARY(BASE 2) format !")
							continue

						else:
							result = b2f(text)
							input("\n\n Binary number :- \n\n %s \n\n\n Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '5'):
				
					while (True):
						banner()
						print('-'*28, 'DESIMAL TO HEXA DESIMAL CONVERTOR', '-'*27,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor.isnumeric()):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !  \n\n Please enter the number in DESIMAL(BASE 10) format !")
							continue

						else:
							result = d2h(int(text))
							input("\n\n Desimal number :- \n\n %s \n\n\n Hexa Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '6'):
				
					while (True):
						banner()
						print('-'*31, 'DESIMAL TO OCTAL CONVERTOR', '-'*31,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor.isnumeric()):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !  \n\n Please enter the number in DESIMAL(BASE 10) format !")
							continue

						else:
							result = d2o(int(text))
							input("\n\n Desimal number :- \n\n %s \n\n\n Octal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '7'):
				
					while (True):
						banner()
						print('-'*26, 'DESIMAL(INTIGER) TO BINARY CONVERTOR', '-'*26,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor.isnumeric()):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in DESIMAL(BASE 10) - INTIGER format !")
							continue

						else:
							result = d2b(int(text))
							input("\n\n Desimal number :- \n\n %s \n\n\n Binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '8'):
				
					while (True):
						banner()
						print('-'*27, 'DESIMAL(FLOAT) TO BINARY CONVERTOR', '-'*26,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break
					
						elif (text.count('.') > 1):
							input ("\n ERROR: MALFORMED INPUT !  \n\n\t( There are %d '.' in the input ) \n\n Please enter the number in DESIMAL(BASE 10) - FLOAT format !"%text.count('.'))
							continue


#						elif (len(text) > 16):
#							input("\n ERROR: The input must be under the 16 digits\n\n press 'Enter' to continue ")
#							continue
#
						ok = True
						for charactor in text:
							if not (charactor.isnumeric() or charactor == '.'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !    \n\n Please enter the number in DESIMAL(BASE 10) - FLOAT format !")
							continue

						else:
							result = f2b(text)
							input("\n\n Desimal number :- \n\n %s \n\n\n Binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '9'):
				
					while (True):
						banner()
						print('-'*21, 'DESIMAL(INTIGER) TO FIRST COMPLEMENT CONVERTOR', '-'*21,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor.isnumeric() or charactor == '-'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in DESIMAL(BASE 10) - INTIGER format !")
							continue

						else:
							result = d2fc(int(text))
							input("\n\n Desimal number :- \n\n %s \n\n\n First complement binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '10'):
				
					while (True):
						banner()
						print('-'*21, 'DESIMAL(INTIGER) TO SECOND COMPLEMENT CONVERTOR', '-'*20,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if not (charactor.isnumeric() or charactor == '-'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in DESIMAL(BASE 10) - INTIGER format !")
							continue

						else:
							result = d2sc(int(text))
							input("\n\n Desimal number :- \n\n %s \n\n\n Second complement binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))




				elif (choise_subMenu == '11'):
				
					while (True):
						banner()
						print('-'*28, 'OCTAL TO HEXA DESIMAL CONVERTOR', '-'*28,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if (not (charactor.isnumeric() ) or charactor == '8' or charactor == '9' ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in OCTAL(BASE 8) format !")
							continue

						else:
							result = o2h(int(text))
							input("\n\n Octal number :- \n\n %s \n\n\n Hexa Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))



				elif (choise_subMenu == '12'):
				
					while (True):
						banner()
						print('-'*31, 'OCTAL TO DESIMAL CONVERTOR', '-'*31,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if (not (charactor.isnumeric() ) or charactor == '8' or charactor == '9' ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in OCTAL(BASE 8) format !")
							continue

						else:
							result = o2d(int(text))
							input("\n\n Octal number :- \n\n %s \n\n\n Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))



				elif (choise_subMenu == '13'):
				
					while (True):
						banner()
						print('-'*31, 'OCTAL TO BINARY CONVERTOR', '-'*31,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if (not (charactor.isnumeric() ) or charactor == '8' or charactor == '9' ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in OCTAL(BASE 8) format !")
							continue

						else:
							result = o2b(int(text))
							input("\n\n Octal number :- \n\n %s \n\n\n Binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))



				elif (choise_subMenu == '14'):
				
					while (True):
						banner()
						print('-'*26, 'OCTAL TO FIRST COMPLEMENT CONVERTOR', '-'*26,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if (not (charactor.isnumeric() or charactor == '-') or charactor == '8' or charactor == '9' ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in OCTAL(BASE 8) format !")
							continue

						else:
							result = o2fc(text)
							input("\n\n Octal number :- \n\n %s \n\n\n First complement binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '15'):
				
					while (True):
						banner()
						print('-'*25, 'OCTAL TO SECOND COMPLEMENT CONVERTOR', '-'*26,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						for charactor in text:
							if (not (charactor.isnumeric() or charactor == '-') or charactor == '8' or charactor == '9' ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in OCTAL(BASE 8) format !")
							continue

						else:
							result = o2fc(text)
							input("\n\n Octal number :- \n\n %s \n\n\n Second complement binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '16'):
				
					while (True):
						banner()
						print('-'*28, 'HEXA DESIMAL TO OCTAL CONVERTOR', '-'*28,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						text = text.upper()
						for charactor in text:
							if ( charactor not in hexTable.values() ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in HEXA DESIMAL(BASE 16) format !")
							continue

						else:
							result = h2o(text)
							input("\n\n Hexa Desimal number :- \n\n %s \n\n\n Octal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '17'):
				
					while (True):
						banner()
						print('-'*28, 'HEXA DESIMAL TO DESIMAL CONVERTOR', '-'*27,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						text = text.upper()
						for charactor in text:
							if ( charactor not in hexTable.values() ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in HEXA DESIMAL(BASE 16) format !")
							continue

						else:
							result = h2d(text)
							input("\n\n Hexa Desimal number :- \n\n %s \n\n\n Desimal number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))

				elif (choise_subMenu == '18'):
				
					while (True):
						banner()
						print('-'*28, 'HEXA DESIMAL TO BINARY CONVERTOR', '-'*28,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						text = text.upper()
						for charactor in text:
							if ( charactor not in hexTable.values() ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in HEXA DESIMAL(BASE 16) format !")
							continue

						else:
							result = h2b(text)
							input("\n\n Hexa Desimal number :- \n\n %s \n\n\n Binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))

				elif (choise_subMenu == '19'):
				
					while (True):
						banner()
						print('-'*23, 'HEXA DESIMAL TO FIRST COMPLEMENT CONVERTOR', '-'*23,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						text = text.upper()
						for charactor in text:
							if not ( charactor == '-' or  charactor in hexTable.values() ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in HEXA DESIMAL(BASE 16) format !")
							continue

						else:
							result = h2fc(text)
							input("\n\n Hexa Desimal number :- \n\n %s \n\n\n First complement binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


				elif (choise_subMenu == '20'):
				
					while (True):
						banner()
						print('-'*22, 'HEXA DESIMAL TO SECOND COMPLEMENT CONVERTOR', '-'*22,'\n')

						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						ok = True
						text = text.upper()
						for charactor in text:
							if not ( charactor == '-' or  charactor in hexTable.values() ):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !   \n\n Please enter the number in HEXA DESIMAL(BASE 16) format !")
							continue

						else:
							result = h2sc(text)
							input("\n\n Hexa Desimal number :- \n\n %s \n\n\n Second complement binary number :- \n\n %s \n\n\n\n Press 'Enter' to continue " %(text,result))


		elif(choise_mainMenu == '3'):
			
			while (True):
				banner()
				print('='*36, 'IEEE754 CONVERTOR', '='*35,'\n')

				choise_subMenu = input(

					"\n 1 - IEEE754 single precision (32Bit) convertor \n"
					" 2 - IEEE754 double precision (64Bit) convertor \n\n"
					" Please enter the number of your choise or '0' to back => " 
					)
			
				if ( not choise_subMenu.isnumeric() ): continue

				elif ( choise_subMenu == '0'): break

				elif (choise_subMenu == '1'):

					while (True):
						banner()
						print('-'*22, 'IEEE754 SINGLE PRECISION (32BIT) CONVERTOR', '-'*22,'\n')
						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						elif (text.count('.') > 1):
							input ("\n ERROR: MALFORMED INPUT !  \n\n\t( There are %d '.' in the input ) \n\n Please enter the number in DESIMAL(BASE 10) - FLOAT format !"%text.count('.'))
							continue

						elif not(float(text) < 65535.0 and float(text) > -65535.0 ):
							input("\n ERROR: The input must be in the range of -65535.0 and 65535.0 \n\n press 'Enter' to continue ")
							continue

						ok = True
						for charactor in text:
							if not (charactor.isnumeric() or charactor == '.' or charactor == '-'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !    \n\n Please enter the number in DESIMAL(BASE 10) - FLOAT format !")
							continue

						else:
							result = ieee754_32bit(text)
							input("\n\n Desimal number :- \n\n %s \n\n\n IEEE754 Single precision (32bit) number :- \n\n\t\t\t%s\n\n Sign\t  = %s\n Exponent = %s\n Mantissa = %s\n\n\n Press 'Enter' to continue  " %(text,result[0],result[1],result[2],result[3]))


				elif (choise_subMenu == '2'):

					while (True):

						banner()
						print('-'*22, 'IEEE754 DOUBLE PRECISION (64BIT) CONVERTOR', '-'*22,'\n')
						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						elif (text.count('.') > 1):
							input ("\n ERROR: MALFORMED INPUT !  \n\n\t( There are %d '.' in the input ) \n\n Please enter the number in DESIMAL(BASE 10) - FLOAT format !"%text.count('.'))
							continue

						elif not(float(text) < 65535.0 and float(text) > -65535.0 ):
							input("\n ERROR: The input must be in the range of -65535.0 and 65535.0 \n\n press 'Enter' to continue ")
							continue

						ok = True
						for charactor in text:
							if not (charactor.isnumeric() or charactor == '.' or charactor == '-'):
								ok = False

						if ( ok == False):		
							input ("\n ERROR: MALFORMED INPUT !    \n\n Please enter the number in DESIMAL(BASE 10) - FLOAT format !")
							continue

						else:
							result = ieee754_64bit(text)
							input("\n\n Desimal number :- \n\n %s \n\n\n IEEE754 Double precision (64bit) number :- \n\n\t\t%s\n\n Sign\t  = %s\n Exponent = %s\n Mantissa = %s\n\n\n Press 'Enter' to continue  " %(text,result[0],result[1],result[2],result[3]))



		elif(choise_mainMenu == '4'):
			
			while (True):
				banner()
				print('='*31, 'BASE64 ENCODER AND DECODER ', '='*30,'\n')

				choise_subMenu = input(

					"\n 1 - BASE64 Encoder \n"
					" 2 - BASE64 Decoder \n\n"
					" Please enter the number of your choise or '0' to back => " 
					)
			
				if ( not choise_subMenu.isnumeric() ): continue

				elif ( choise_subMenu == '0'): break

				elif (choise_subMenu == '1'):

					while (True):
						banner()
						print('-'*37, 'BASE64 Encoder', '-'*36,'\n')
						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						else:
							result = base64_encode(text)
							input ("\n\n Entered text :- \n\n %s \n\n\n BASE64 Encoded text :-\n\n %s  \n\n\n\n Press 'Enter' to continue "%(text,result))


				elif (choise_subMenu == '2'):

					while (True):
						banner()
						print('-'*37, 'BASE64 Decoder', '-'*36,'\n')
						text = input(" Enter the text below or press 'Enter' button without a text to go to the previous menu \n\n >>> ")

						if (text == ''): break

						else:
							result = base64_decode(text)

							if (result == 'Incorrect format for BASE64'):
								input ("\n\n ERROR: MALFORMED INPUT ! \n\n Please enter the input in correct BASE64 format \n\n\n Press 'Enter' to continue ")

							else:
								input ("\n\n Entered text :- \n\n %s \n\n\n BASE64 Decoded text :-\n\n %s  \n\n\n\n Press 'Enter' to continue "%(text,result))



		elif (choise_mainMenu == '5'):
			banner()
			print('-'*41, 'CREDITS', '-'*40,'\n\n')

			input ( '\t\t\t\t         DEVELOPER             \n'
					'\t\t\t\t     ________________          \n\n'
					'\t\t\t\t     Tharusha Piyumal          \n\n\n'

					'\t\t\t\t          GITHUB               \n'
					'\t\t\t\t __________________________    \n\n'
					'\t\t\t\t https://github.com/thxrxsh    \n\n\n\n'

					'\t\t\t\t                               \n\n'


					' Press "Enter" to continue ')



	os.system('cls')


main()