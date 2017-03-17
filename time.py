import datetime 
from dateutil.relativedelta import *

## get the input
## input or raw_input
string = input("Give the text:")

## convert inpurt to lower case
string = string.lower()

## split the input into words(list)
words = string.split(" ")

## give final date and time after parsing by changing current date-time
def change_datetime ( c="0", y=0,  mt=0, w=0,  d=0,  h=0,  m=0,  s=0):

	#mt = mt + 12*y
	#d = d + 30*mt

	now = datetime.datetime.now()
	change = relativedelta( years =+ y, months =+ mt, weeks =+ w, days =+ d, hours =+ h, minutes =+ m, seconds =+ s)
	#print (now + change)

	if c == "date":
		return (now + change).date()

	elif c == "time":
		return (now + change).time()

## make separate date and time functions

#def change_date (y=0, m=0, w=0, d=0):
#def change_time (h=0, m=0, s=0):



## make separate functions for setting date and time and print -- if not provided the data
## give final date and time after parsing by setting date-time
def set_datetime (y=0, mt=0, d=0, h=0, m=0, s=0, c="0"):

	a = ""
	if d!=0:
		a = a + str(d) + "/"
	if mt!=0:
		a = a + str(mt) + "/"
	if y!=0:
		a = a + str(y)   

	#a = a + " "

	if h!=0:
		a = a + str(h) + ":"
	if m!=0:
		a = a + str(m) + ":"
	if s!=0:
		a = a + str(s)

	if c!="0":
		a = a + " "
		a = a + str(c)
		#print (a, "a")

	return a

## make function for am/pm


## categories of words (dictionaries or associative arrays)
# you cannot use or for strings, find another better way
Date = {"aaj":[0,"day"], "kal":[1,"day"], "parson":[2,"day"], "narson":[3,"day"], "dashak":[10,"year"], "tarikh":0, "mahine":[0,"months"], "mahina":[0,"months"], "hafte":[0,"week"], "din":[0,"day"], "divas":[0,"day"], "dino":[0,"day"], "saal":0, "varsh":0, "monday":[MO,"weekday"], "tuesday":["TU","weekday"], "wednesday":["WE","weekday"], "thursday":["TH","weekday"], "friday":["FR","weekday"], "saturday":["SA","weekday"], "sunday":["SU","weekday"], "somvar":["MO","weekday"], "mangalvar":["TU","weekday"], "budhvar":["WE","weekday"], "guruvar":["TH","weekday"], "shukravar":["FR","weekday"], "shanivar":["SA","weekday"], "ravivar":["SU","weekday"], "january":[1,"month"], "february":[2,"month"], "march":[3,"month"], "april":[4,"month"], "may":[5,"month"], "june":[6,"month"], "july":[7,"month"], "august":[8,"month"], "september":[9,"month"], "october":[10,"month"], "november":[11,"month"], "december":[12,"month"]}
Time = {"abhi":0, "baje":0, "baj":0, "ghante":0, "ghanta":1, "ghanton":1, "subah":0, "shaam":0, "sandhya":0, "dopahar":0, "raat":0, "minutes":0, "minute":1, "seconds":0, "second":1}
DateTime = {"baad":[1,-1], "is":[0,1], "pahle":[-1,-1], "pichle":[-1,1], "agle":[1,1], "aadhe":[0.5,1], "aadha":[0.5,1], "dedh":[1.5,1], "dhaai":[2.5,1], "saade":[0.5,1]}
Numbers = {'1':[1,1], 'ek':[1,1], 'pahla':[1,1], '2':[2,1], 'do':[2,1], 'doosra':[2,1], '3':[3,1], 'teen':[3,1], 'teesra':[3,1], '4':[4,1], 'chaar':[4,1], 'choutha':[4,1], '5':[5,1], 'paanch':[5,1], 'paanchva':[5,1], '6':[6,1], 'chhe':[6,1], 'chhata':[6,1], '7':[7,1], 'saat':[7,1], 'saatva':[7,1], '8':[8,1], 'aath':[8,1], 'aathva':[8,1], '9':[9,1], 'nau':[9,1], 'nahla':[9,1], '10':[10,1], 'das':[10,1], 'dasva':[10,1], '11':[11,1], 'gyarah':[11,1], 'gyarva':[11,1], '12':[12,1], 'barah':[12,1], 'barvan':[12,1], '13':[13,1], 'terah':[13,1], '14':[14,1], 'chaudah':[14,1], '15':[15,1], 'pandrah':[15,1], '16':[16,1], 'solah':[16,1], '17':[17,1], 'satrah':[17,1], '18':[18,1], 'atharah':[18,1], '19':[19,1], 'unnish':[19,1], '20':[20,1], 'bees':[20,1], '21':[21,1], 'ikkish':[21,1], '22':[22,1], 'baaish':[22,1], '23':[23,1], 'teish':[23,1], '24':[24,1], 'chaubish':[24,1], '25':[25,1], 'pachhish':[25,1], '26':[26,1], 'chhabish':[26,1], '27':[27,1], 'sattaish':[27,1], '28':[28,1], 'atthaish':[28,1], '29':[29,1], 'untish':[29,1], '30':[30,1], 'teesh':[30,1], '31':[31,1], 'ikattish':[31,1]}
Separators = {"se":0, "ke":0, "aur":0, "evam":0, "lekin":0, "par":0, "magar":0, "kintu":0, "parantu":0, "ya":0, "kyunki":0, "isliye":0}

## four stacks
Stack_Date = []
Stack_Time = []
Stack_Next = []
Stack_Prev = []

temp = []
check = 0

## list of lists
Stack_of_Stacks = []

Stack_Index = []

Final = {'Date':[], 'Time':[]}

Answer = {'Date':[], 'Time':[]}

## Algorithm to fill all the words in stack
for word in words:

	if word in Separators:

		#prev_word = words[words.index(word)-1]

		if check == 7:
			copy = Stack_Date[:]
			Stack_of_Stacks.append(copy)
			#print (Stack_Date, "Date Stack goes in Full Stack \n")
			#print (Stack_of_Stacks, "\n")
			Stack_Date.clear()
			Stack_Date = [x for x in Stack_Date if x]
			#print (Stack_Date, "Date Stack Cleared \n")
			#print (Stack_of_Stacks, "\n")
			Stack_Index.append("Date")
			Final['Date'].append(copy)
			
		if check == 8:
			copy = Stack_Time[:]
			Stack_of_Stacks.append(copy)
			#print (Stack_Time, "Time Stack goes in Full Stack \n")
			#print (Stack_of_Stacks, "\n")
			Stack_Time.clear()
			Stack_Time = [x for x in Stack_Time if x]
			#print (Stack_Time, "Time Stack Cleared \n")
			#print (Stack_of_Stacks, "\n")
			Stack_Index.append("Time")
			Final['Time'].append(copy)
			
		Stack_of_Stacks.append(word)
		#print(word, "goes in Full Stack \n")
		#print (Stack_of_Stacks, "\n")
		check = 0
		Stack_Index.append(word)
		
## if next and prev stack is empty then fill accordingly
	if len(Stack_Next)==0 and len(Stack_Prev)==0:

		if (word in Date) or ((word.isdigit()) and (len(word)==4)):

			if(check == 8):
				copy = Stack_Time[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Time, "Time Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Time.clear()
				Stack_Time = [x for x in Stack_Time if x]
				#print (Stack_Time, "Time Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Time")
				Final['Time'].append(copy)

			Stack_Date.append(word)
			check = 7
			#print (word, "goes in Date \n")

		if word in Time:

			if(check == 7):
				copy = Stack_Date[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Date, "Date Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Date.clear()
				Stack_Date = [x for x in Stack_Date if x]
				#print (Stack_Date, "Date Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Date")
				Final['Date'].append(copy)

			Stack_Time.append(word)
			check = 8
			#print (word, "goes in Time \n")

		if word in DateTime:
			if DateTime[word][1]==1:
				Stack_Next.append(word)
				#print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				#print (word, "goes in Prev \n")

		elif word in Numbers:
			if Numbers[word][1]==1:
				Stack_Next.append(word)
				#print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				#print (word, "goes in Prev \n")

## if not empty then word in datetime(stack 3) is filled first in either of two stacks 
	elif len(Stack_Prev)!=0:

		temporary = Stack_Prev.pop()

		if check==7:
			Stack_Date.append(temporary)
			#print (temporary, "goes in Date from Prev\n")

		elif check==8:
			Stack_Time.append(temporary)
			#print (temporary, "goes in Time from Prev\n")

		if (word in Date) or ((word.isdigit()) and (len(word)==4)):

			if(check == 8):
				copy = Stack_Time[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Time, "Time Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Time.clear()
				Stack_Time = [x for x in Stack_Time if x]
				#print (Stack_Time, "Time Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Time")
				Final['Time'].append(copy)
		
			Stack_Date.append(word)
			#print (word, "goes in Date \n")
			check = 7

		if word in Time:

			if(check == 7):
				copy = Stack_Date[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Date, "Date Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Date.clear()
				Stack_Date = [x for x in Stack_Date if x]
				#print (Stack_Date, "Date Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Date")
				Final['Date'].append(copy)

			Stack_Time.append(word)
			#print (word, "goes in Time \n")
			check = 8

		if word in DateTime:

			Stack_Prev.append(temporary)

			if DateTime[word][1]==1:
				Stack_Next.append(word)
				#print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				#print (word, "goes in Prev \n")

		elif word in Numbers:

			Stack_Prev.append(temporary)

			if Numbers[word][1]==1:
				Stack_Next.append(word)
				#print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				#print (word, "goes in Prev \n")

	elif len(Stack_Next)!=0:

		#temp = []
		temp.append(Stack_Next.pop())

		#next_word = words[words.index(word)+1]

		if (word in Date) or ((word.isdigit()) and (len(word)==4)):
			Stack_Date.extend(temp)
			#print (temp, "goes in Date from Next\n")
			temp.clear()

			if(check == 8):
				copy = Stack_Time[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Time, "Time Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Time.clear()
				Stack_Time = [x for x in Stack_Time if x]
				#print (Stack_Time, "Time Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Time")
				Final['Time'].append(copy)

			Stack_Date.append(word)
			#print (Stack_Date)
			#print (word, "goes in Date \n")
			check = 7
		
		elif word in Time:
			Stack_Time.extend(temp)
			#print (temp, "goes in Time from Next\n")
			temp.clear()

			if(check == 7):
				copy = Stack_Date[:]
				Stack_of_Stacks.append(copy)
				#print (Stack_Date, "Date Stack goes in Full Stack \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Date.clear()
				Stack_Date = [x for x in Stack_Date if x]
				#print (Stack_Date, "Date Stack Cleared \n")
				#print (Stack_of_Stacks, "\n")
				Stack_Index.append("Date")
				Final['Date'].append(copy)

			Stack_Time.append(word)
			#print (word, "goes in Time \n")
			check = 8
		
		if word in DateTime:

			if DateTime[word][1]==1:
				Stack_Next.append(word)
				#print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				#print (word, "goes in Prev \n")

		elif word in Numbers:
			if Numbers[word][1]==1:
				Stack_Next.append(word)
				#print (word, "goes in Next \n")
			else :
				Stack_Prev.append(word)
				#print (word, "goes in Prev \n")

	if words.index(word) == len(words)-1:

		if len(Stack_Prev)!=0:

			temporary = Stack_Prev.pop()

			if check==7:
				Stack_Date.append(temporary)
				#print (temporary, "goes in Date from Prev\n")

			elif check==8:
				Stack_Time.append(temporary)
				#print (temporary, "goes in Time from Prev\n")	

		if len(Stack_Date)!=0:
			copy = Stack_Date[:]
			Stack_of_Stacks.append(copy)
			#print (Stack_Date, "Last Stack(Date) goes in Full Stack")
			#print (Stack_of_Stacks, "\n")
			Stack_Index.append("Date")
			Final['Date'].append(copy)

		elif len(Stack_Time)!=0:
			copy = Stack_Time[:]
			Stack_of_Stacks.append(copy)
			#print (Stack_Time, "Last Stack(Time) goes in Full Stack")
			#print (Stack_of_Stacks, "\n")
			Stack_Index.append("Time")
			Final['Time'].append(copy)



print (Stack_of_Stacks, "\n")
print (Stack_Index, "\n")
print (Final)

## empty function makes empty

##for date in Final['Date']:

#def dateparser(Stack = []):

#def timeparser(Stack = []):

for date in Final['Date']:

	fulldate = []
	y=0
	mt=0
	w=0
	d=0

	x = set(date).intersection(DateTime.keys())
	yx = set(date).intersection(Numbers.keys())

	if len(x)>0:

		if len(yx)>0:
			
			if ('din' in date) or ('divas' in date) or ('dino' in date):
				d = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

			#why not if ('ghanta' or 'ghante') in time:
			if ('mahine' in date) or ('mahina' in date):
				mt = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

			if ('saal' in date) or ('varsh' in date):
				y = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

			if ('hafta' in date) or ('hafte' in date):
				w = Numbers[list(yx)[0]][0] * DateTime[list(x)[0]][0]

		else:
			## eleiminate this step by use of above step (putting value = 1)

			if ('din' in date) or ('divas' in date) or ('dino' in date):
				d = DateTime[list(x)[0]][0]

			#why not if ('ghanta' or 'ghante') in time:
			if ('mahine' in date) or ('mahina' in date):
				mt = DateTime[list(x)[0]][0]

			if ('saal' in date) or ('varsh' in date):
				y = DateTime[list(x)[0]][0]

			if ('hafta' in date) or ('hafte' in date):
				w = DateTime[list(x)[0]][0]

			### Instead of using [0] use previous word for (aaj agle mahine pichle saal)

		## if weekday
		## and correspondigly agle is pichle set and pass weekday
		## pass in format of WE(+1) where WE is not string

		Answer['Date'].append(change_datetime("date",y,mt,w,d))


	else:
		
		if len(set(date).intersection(Numbers.keys()))>0:
			
			for word in date:

				if word in Numbers.keys():

					next_word = date[date.index(word)+1]

					if (next_word == 'mahina') or (next_word == 'mahine'): ## check if next_word == 'mahina' or 'mahine' works or not
						mt = Numbers[word][0]

					elif (next_word == 'saal') or (next_word == 'varsh'):
						y = Numbers[word][0]

					elif (next_word == 'tarikh') or (next_word == 'din'):
						d = Numbers[word][0]

					elif (next_word.isdigit()) and (len(next_word)==4):
						mt = Numbers[word][0]

					elif Date[next_word][1] == 'month':
						d = Numbers[word][0]
			
			fulldate.append(set_datetime(y,mt,d))

		for word in date:

			if (word in Date) and (Date[word][1] == 'month'):
				mt = Date[word][0]
			#obviously word is in Date

			if (word.isdigit()) and (len(word)==4):
				y = int(word)

			if (y!=0) and (mt!=0):
				fulldate[0] += (set_datetime(y, mt))

			if word == 'aaj':
				fulldate.append(change_datetime("date",0,0,0,0))

			if word == 'kal':
				fulldate.append(change_datetime("date",0,0,0,1))

			if word == 'parson':
				fulldate.append(change_datetime("date",0,0,0,2))

			if word == 'narson':
				fulldate.append(change_datetime("date",0,0,0,3))

			## Above 4 can be transformed into 1 just like done in above 4

			#if (word in Date) and (Date[word][1] == 'weekday'):
			# Difficult to implement without  DateTime words i.e. to set the day according to month and year
			## pseudocode
			## if (word in Date) and (Date[word][1] == 'weekday'):
			##     if (y!=0) and (mt!=0):
			##          call weekday function passing month and year to get the date	

		Answer['Date'].append(fulldate)

		

for time in Final['Time']:

	h=0
	m=0
	s=0
	c=0

	x = set(time).intersection(DateTime.keys())
	y = set(time).intersection(Numbers.keys())

	if len(y) == 0:
		y.add("1")

	#print (x)
	#print (y)

	if len(x)>0:

		if len(y)>0:

			if ('ghanta' in time) or ('ghante' in time) or ('ghanton' in time):
				h = Numbers[list(y)[0]][0] * DateTime[list(x)[0]][0]

			#why not if ('ghanta' or 'ghante') in time:
			if ('minute' in time) or ('minutes' in time):
				m = Numbers[list(y)[0]][0] * DateTime[list(x)[0]][0]

			if ('second' in time) or ('seconds' in time):
				s = Numbers[list(y)[0]][0] * DateTime[list(x)[0]][0]

		else:

			print ("waited for this example, thanks !!")

			# if pichle (ghante then , minute then, second then) else agle (same)

		Answer['Time'].append(change_datetime("time",0,0,0,0,h,m,s))

	else:

		if len(set(time).intersection(Numbers.keys()))>0:

			#print ("Number Exist")

			for word in time:

				if word in Numbers.keys():

					next_word = time[time.index(word)+1]

					if (next_word == 'baj') or (next_word == 'baje'): ## baje is not working
						h = Numbers[word][0]
						print (h, "h")

					elif (next_word == 'minute') or (next_word == 'minutes'): ## or ke baad wale main dikkar hai
						m = Numbers[word][0]
						print (m, "m")

					elif (next_word == 'second') or (next_word == 'seconds'):
						s = Numbers[word][0]
						print (s, "s")

			if 'subah' in time:
				c = "AM"

			elif 'dopahar' in time:
				c = "PM"

			elif 'shaam' or 'sandhya' in time: ## sandhya to aa hi nahi raha
				c = "PM"

			elif (('raat' in time) and (0 <= h < 6)):
				c = "AM"

			elif (('raat' in time) and (6 <= h < 12)):
				c = "PM"

			print (c, "c")
			Answer['Time'].append(set_datetime(0,0,0,h,m,s,c))

		else:

			#print ("Number doesn't Exist")

			duration = []
			
			for word in time:

				if word == 'abhi':
					duration.append(change_datetime("time"))

				if word == 'subah':
					duration.append("5 - 12 AM")

				elif word == 'dopahar':
					duration.append("12 - 5 PM")

				elif word == ('shaam' or 'sandhya'):
					duration.append("5 - 12 PM")

				elif word == 'raat':
					duration.append("10-12 PM & 12 - 5 AM")

			Answer['Time'].append(duration)
 

print (Answer)




