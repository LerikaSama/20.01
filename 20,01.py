#Срез строки
#
#
#
myStr="Python-cool!"
print(myStr[1:3]) #yt
print(myStr[-5:-2]) #coo
print(myStr[-5:11]) #cool
print(myStr[:6]) #Python
print(myStr[:-1]) #Python-cool
print(myStr[6:]) #-cool!
print(myStr[-5:]) #cool!

myStr="1234567890"
print(myStr[2:8:2]) #357
print(myStr[8:2:-2]) #975
print(myStr[::-1]) #0987654321
print(myStr[5::2]) #680
print(myStr[-1::-2]) #08642
print(myStr[:len(myStr):3]) #1470





#Экранированные последовательности


myStr="There is no shortage of material to learn Python.\nThe following books might serve as a starting point, in the order specified: \n'Python Programming: An Introduction to Computer Science' by John M. Zelle, Ph.D.\n'The Python Guide for Beginners' by Renan Moura.\n'Effective Python' by Brett Slatkin"
print(myStr)



print("Python books:")
print("\t'Python Programming: An Introduction to Computer Science'")
print("\t'The Python Guide for Beginners'")


myStr="\x2C"
print(myStr) # ,


myStr="\053"
print(myStr) # +


print('\'Python Programming: An Introduction to Computer Science\'')
print("\"Python Programming: An Introduction to Computer Science\"")
print("15\\2")


#«Сырые» строки


myStr="Backslash symbol: \\"
print(myStr) # Backslash symbol: \


myStr="In Python strings, the backslash '\\' is a special character. It is used in representing certain whitespace characters: '\\t' is a tab,'\\n' is a newline"
print(myStr)



normalStr = "This is a \nnormal string"
print(normalStr)
rawStr = r"This is a \n raw string"
print(rawStr)



normalText='''Python Arithmetic Operators:\n
 Arithmetic operators are used to perform
 mathematical operations like addition,
 subtraction, multiplication and division.\n
 \tThere are 7 arithmetic operators in Python:
 \t\tAddition +\n
 \t\tSubtraction -\n
 \t\tDivision /\n
 \t\tModulus %\n
 \t\tExponentiation **\n
 \t\tFloor division //\n'''
rawText=r'''Python Arithmetic Operators:\n
 Arithmetic operators are used to perform
 mathematical operations like addition,
 subtraction, multiplication and division.\n
 \tThere are 7 arithmetic operators in Python:
 \t\tAddition +\n
 \t\tSubtraction -\n
 \t\tDivision /\n
 \t\tModulus %\n
 \t\tExponentiation **\n
 \t\tFloor division //\n
 '''
print(normalText)
print(rawText)




errRawStr1 = r'\'
errRawStr2 = r'123\'
errRawStr3 = r'abc\\\'



#Форматированный вывод



userLogin=input("Your login: ")
print("Welcome,", userLogin, ". Let's start game!")
strMsg="Dear, "+userLogin+". Game over!"
print(strMsg)

print("Welcome,", userLogin,
 ". Let’s start game!", sep="")

userLogin=input("Your login: ")
strMsg="Welcome, {}. Let's start game!".format(userLogin)
print(strMsg)



strMsg = "My name is {}, I'm {}".format("Student",25)
print(strMsg) # My name is Student, I'm 25


strMsg = "My name is {}, I'm {}".format(25,"Student")
print(strMsg) # My name is 25, I'm Student


strMsg1 = "My name is {0}, I'm {1}"
format("Student",25)
print(strMsg1) # My name is Student, I'm 25
strMsg2 = "I'm {1}. My name is {0}".format("Student",25)
print(strMsg2) # I'm 25. My name is Student


strMsg3 = "My name is {name}, I'm {age}".format(name="Student",age=25)
print(strMsg3) # My name is Student, I'm 25
strMsg4 = "My name is {name}, I'm {age}".format(age=25,name="Student")
print(strMsg4) # My name is Student, I'm 25


strMsg = "Your salary is {0:9.2f}".format(200.846)
print(strMsg) # Your salary is 200.85

strMsg = "Your salary is {0:3.2f}".format(200.846)
print(strMsg) # Your salary is 200.85


userNumber = int(input("Your number? ")) #255
myStrB = "The binary representation of a number {n} is {n:b}".format(n=userNumber)
print(myStrB) #The binary representation of a number 255 is 11111111
myStrO="The octal representation of a number {n} is {n:o}".format(n=userNumber)
print(myStrO) #The octal representation of a number 255 is 377
myStrH="The Hex representation of a number {n} is {n:x}".format(n=userNumber)
print(myStrH) #The Hex representation of a number 255 is ff



myStr1="The number1 range from {0:-} to {1:-}".format(-10,10)
print(myStr1) #The number1 range from -10 to 10
myStr2="The number2 range from {0:+} to {1:+}".format(-20,50)
print(myStr2) #The number2 range from -20 to +50
myStr3="The number3 range from {0: } to {1:}".format(-30,30)
print(myStr3) #The number3 range from -30 to 30


#установим доступное пространство для значения до 10 символов.
myStr1 = "You have {:<10} points."
print(myStr1.format(12)) #You have 12 points.
myStr2 = "You have {:>10} points."
print(myStr2.format(12)) #You have 12 points.
myStr3 = "You have {:^10} points."
print(myStr3.format(12)) #You have 12 points.


#При выравнивании чисел после типа форматирования можно указывать спецификатор
myStr1 = "Number is {:<10.2f}!"
print(myStr1.format(34.8256)) #Number is 34.83 !
myStr2 = "Number is {:>10.2f}!"
print(myStr2.format(34.8256)) #Number is 34.83!
myStr3 = "Number is {:^10.2f}!"
print(myStr3.format(34.8256)) #Number is 34.83 !

#Рассмотренные типы форматирования также полезны при выравнивании строк:
myStr1 = "Your login is {:<20}!"
print(myStr1.format("Admin")) #Your login is Admin !
myStr2 = "Your password is {:>20}!"
print(myStr2.format("12345")) #Your password is 12345!
myStr3 = "Your secret word is {:^15}!"
print(myStr3.format("IT")) #Your secret word is IT !



#Модуль string



import string

import string
import random
userLogin = "".join(random.sample((string.ascii_lowercase),6))
userPass = "".join(random.sample((string.ascii_letters +
 string.digits), 8))
print("login:",userLogin)
print("password:",userPass)


import string
myStr = " We have BEEN happy\n to welcome\n\n back OLD friends, \n\n\nand to make new ones "
#We Have Been Happy To Welcome Back Old Friends,And To Make New Ones
print(string.capwords(myStr))



from string import Formatter
formatter = Formatter()
print(formatter.format('{userLog}',
 userLog = 'Admin')) #Admin
print(formatter.format('{} {userLog}', 'Welcome, ',
 userLog = 'Admin')) #Welcome, Admin
print('{} {userLog}'.format('Welcome, ',
 userLog = 'Admin')) #Welcome, Admin




from string import Template
t = Template('$userName has the rights to $userRights in the $appName')




resStr = t.substitute(userName='Admin',
 userRights = 'edit',
appName='SuperApp.')
print(resStr) #Admin has the rights to edit in the SuperApp.



#Регулярные выражения, модуль re



import re
userStr="abcd abc efgh"
match = re.search(r'\w{4}', userStr)


print(match.group()) # abcd
print(match.group(0)) # abcd


import re
userStr="abcd abc 123 efgh 456"
match = re.search(r'\d{3}', userStr)
print(match.group()) # 123




import re
userStr="My cell phone numbers: Vodafone +38(095)1234567;Cellcom +38(067)9875612";
match1 = re.search(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)', userStr)




print(match1.group()) # Vodafone +38(095)1234567;Cellcom +38(067)9875612
print(match1.group(0)) # Vodafone +38(095)1234567;Cellcom +38(067)9875612


print(match1.group(1)) # 1234567
print(match1.group(2)) # 9875612



print(match1.group(1,2)) # ('1234567', '9875612')



print(match1.start(), match1.end()) #23 73
print(match1.start(0), match1.end(0)) #23 73
print(match1.start(1), match1.end(1)) #40 47
print(match1.start(2), match1.end(2)) #66 73


print(match1.span()) #(23, 73)
print(match1.span(0)) #(23, 73)
print(match1.span(1)) #(40, 47)
print(match1.span(2)) #(66, 73)




import re
userStr="2021-2022 Competition Calendar:30.11.2021 —2021 Grand Prix Series; 14.01.2022 —Grand Pemio D'Italia"
match2=re.findall(r'\d{2}\.\d{2}\.\d{4}', userStr)
print(match2) # ['30.11.2021', '14.01.2022']





import re
userStr1="My cell phone numbers: Vodafone+38(095)1234567; Cellcom +38(067)9875612";
userStr2="Vodafone +38(095)1234567; Cellcom+38(067)9875612 — my cell phone numbers";
match3 = re.match(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)', userStr1)
match4 = re.match(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)', userStr2)
print(match3) #None
print(match4.group()) # Vodafone +38(095)1234567;Cellcom +38(067)9875612



import re
userStr="2021-2022 Competition Calendar:30.11.2021 — 2021 Grand Prix Series;14.12.2021 — Grand Pemio D'Italia"
newStr=re.sub(r'[-;]', '/',userStr)
print(newStr) #2021/2022 CompetitionCalendar:30.11.2021 /2021 Grand Prix Series/ 14.12.2021 /Grand Pemio D'Italia





import re
userStr="30.11.2021 — 2021 Grand Prix Series,14.12.2021 — Grand Pemio D'Italia;27.12.2021 — Cup of Austria by IceChallenge"
strList=re.split(r'[,;]+', userStr)
print(strList) #['30.11.2021 — 2021 Grand Prix Series',
#' 14.12.2021 — Grand Pemio D'Italia',
#' 27.12.2021 — Cup of Austria by IceChallenge']




#Понятие классического массива


#Понятие коллекции объектов


#Ссылочный тип данных list


#Создание списков



category =["Drama", "Comedy", "Fantasy"]



courses =list(("Math", "Algorithms", "Databases"))



print(category) #['Drama', 'Comedy', 'Fantasy']
print(courses) #['Math', 'Algorithms', 'Databases']




studentScores=[]
students=list()
print(studentScores) #[]
print(students) #[]




myCourses= ["Algorithms", 2345, 7009, "Networks",
 "Databases"]
print(myCourses) #['Algorithms', 2345, 7009,'Networks', 'Databases']


#Также элементом списка может быть другой список:
nestedList=[1,2.5,[45, "Example"]]
print(nestedList) #[1, 2.5, [45, 'Example']]


#Элементы списка могут повторяться:
customers=['Bob','Anna','Joe','Bob','Nick']




#Также, если передать функции list() строку, то результатом ее работы будет список, состоящий из символовстроки:

mySymbols=list("abcdef")
print(mySymbols) #['a', 'b', 'c', 'd', 'e', 'f']



#Генераторы списков


list1=[i*i for i in range(6)]
print(list1) #[0, 1, 4, 9, 16, 25]



#Предположим, что у нас есть строка «example», из элементов которой нужно создать список, присоединяя ним символ *.
list2=[i+"*" for i in "example"]
print(list2) #['e*', 'x*', 'a*', 'm*', 'p*', 'l*', 'e*']


#Или, например, нужно создать список из продублированных 5 раз символов строки:
list3=[i*5 for i in "abcdtf"]
print(list3) #['aaaaa', 'bbbbb', 'ccccc', 'ddddd','ttttt', 'fffff']



#Допустим, что нам необходимо сгенерировать список из квадратов четных чисел в диапазоне от 1 до 10:
list4=[i*i for i in range(1,11) if i%2==0]
print(list4) #[4, 16, 36, 64, 100]



#Или выбрать из уже имеющегося списка всех клиентов, кроме Bob и Joe:
customers=['Bob','Anna','Joe','Bob','Nick']
list5=[i for i in customers if i!='Bob' and i!='Joe']
print(list5) #['Anna', 'Nick']



#В Python также предусмотрена возможность создания генератора с несколькими циклами.
list6 = [x*y for x in range(1, 4) for y in range(1, 4)]
print(list6) #[1, 2, 3, 2, 4, 6, 3, 6, 9]



#Генераторы списков также полезны, если необходимо создать вложенный список. Например, чтобы представить ту же таблицу умножения на три в виде матрицы:
list7 = [[x*y for x in range(1, 4)] for y in range(1, 4)]
print(list7) #[[1, 2, 3], [2, 4, 6], [3, 6, 9]]


#Работа со списками



myList =["user", 12, 200.34, False, True]
print(myList [1]) #12
print(myList [-1]) #True
print(myList [len(L)-1]) #True
print(myList [-2]) #False


#Рассмотрим работу с различными вариантами срезов
#списка на примерах.
myCourses= ["Algorithms", 2345, 7009, "Networks",
 "Databases"]
print(myCourses[1:3]) #[2345, 7009]
print(myCourses[-4:-2]) #[2345, 7009]
print(myCourses[1:-1]) #[2345, 7009, 'Networks']
print(myCourses[:-1]) #['Algorithms', 2345, 7009,'Networks']
print(myCourses[3:]) #['Networks', 'Databases']
print(myCourses[::2]) #['Algorithms', 7009,'Databases']
print(myCourses[::-1]) #['Databases', 'Networks',7009, 2345, 'Algorithms']
print(myCourses[-4::-1]) #[2345, 'Algorithms']


#с использованием индекса мы можем изменять
#значение элемента:
category =["Drama", "Comedy", "Fantasy"]
print(category) #['Drama', 'Comedy', 'Fantasy']
category[-1]="Action"
print(category) #['Drama', 'Comedy', 'Action']



#Возможно также и изменение значений целых фрагментов списка, используя срезы.

userLogs=["admin","student","teacher","HR","user"]
print(userLogs) #['admin', 'student', 'teacher','HR', 'user']
userLogs[::2]=["newUser1","newUser2","newUser3"]
print(userLogs) #['newUser1', 'student', 'newUser2','HR', 'newUser3']



userLogs = ["admin","student","teacher","hr","user"]
print(len(userLogs)) #5
print(sorted(userLogs)) #['admin', 'hr', 'student','teacher', 'user']
prices = [100, 250.45, 1200, 20.78]
print(sum(prices)) #1571.23
print(max(prices)) #1200
print(min(prices)) #20.78
print(sorted(prices)) #[20.78, 100, 250.45, 1200]



category1 =["Drama", "Comedy"]
category2 =["Action", "Fantasy"]
print(category1+category2) #['Drama', 'Comedy','Action', 'Fantasy']
print(category1*2) #['Drama', 'Com





#Методы списков



#Например, выведем значение каждого элемента списка:
category =["Drama", "Comedy", "Mystery","Romance"]
for film in category:
 print(film)

#Также можно организовать цикл с использованиемфункцииrange(), используя длину цикла:
 category = ["Drama", "Comedy", "Mystery", "Romance"]
for i in range(len(category)):
 print(category[i])

#Метод listObj.append(item) позволяет добавить еще один элемент(аргумент метода, item) в конец списка listObj.
 category1 = ["Drama", "Comedy"]
 print(category1)  # ['Drama', 'Comedy']
 category1.append("Fantasy")
 print(category1)  # ['Drama', 'Comedy', 'Fantasy']




category1 =["Drama", "Comedy"]
category2=['Action','Fantasy']
print(category1) #['Drama', 'Comedy']
category1.extend(category2)
print(category1) #['Drama', 'Comedy', 'Action','Fantasy']
category1.extend(["Mystery","Romance"])
print(category1) #['Drama', 'Comedy', 'Action','Fantasy', 'Mystery', 'Romance']




category1 =["Drama", "Comedy"]
print(category1) #['Drama', 'Comedy']
category1.insert(1,"Fantasy")
print(category1) #['Drama', 'Fantasy', 'Comedy']
category1.insert(2,"Action")
print(category1) #['Drama', 'Fantasy', 'Action','Comedy']
category1.insert(-1,"Romance")
print(category1) #['Drama', 'Fantasy', 'Action','Romance', 'Comedy']




category =["Drama", "Comedy", "Mystery", "Romance",
 "Comedy"]
print(category) #['Drama', 'Comedy', 'Mystery','Romance', 'Comedy']
category.remove("Comedy")
print(category) #['Drama', 'Mystery', 'Romance','Comedy']
category.pop(2)
print(category) #['Drama', 'Mystery', 'Comedy']
category.pop()
print(category) #['Drama', 'Mystery']



#Метод listObj.clear() удаляет все элементы из списка listObj.
category=["Drama", "Comedy", "Mystery", "Romance",
 "Comedy"]
print(category) #['Drama', 'Comedy', 'Mystery','Romance', 'Comedy']
category.clear()
print(category) #[]



category =["Drama", "Comedy", "Mystery", "Romance",
 "Comedy"]
print(category.index("Mystery")) #2
print(category.index("Comedy")) #1




category =["Drama", "Comedy",
"Mystery","Romance","Comedy"]
print(category.count("Comedy")) #2


#Метод listObj.reverse() меняет порядок сортировки
#элементов на обратный.
category=["Drama", "Comedy", "Mystery", "Romance",
 "Comedy"]
category.sort()
print(category) #['Comedy', 'Comedy', 'Drama','Mystery', 'Romance']
category.sort(reverse=True)
print(category) #['Romance', 'Mystery', 'Drama','Comedy', 'Comedy']
prices=[100, 250.45, 1200, 20.78]
prices.sort()
print(prices) #[20.78, 100, 250.45, 1200]
prices.sort(reverse=True)
print(prices) #[1200, 250.45, 100, 20.78]
prices.reverse()
print(prices) #[20.78, 100, 250.45, 1200]


#Оператор принадлежности in



customers=['Bob','Anna','Joe','Bob','Nick']
print('Bob' in customers) #True



customers=['Bob','Anna','Joe','Bob','Nick']
if ('Bob' in customers):
 print("Bob is our customer")
else:
 print("Sorry")



 #Особенности списков, ссылки и клонирование

 list1 = [1, 2, 3, 4, 5]
 print(list1)  # [1, 2, 3, 4, 5]
 list2 = list1
 print(list2)  # [1, 2, 3, 4, 5]
 list2[1] = "Hello"
 print(list2)  # [1, 'Hello', 3, 4, 5]
 print(list1)  # [1, 'Hello', 3, 4, 5]


list1=[1,2,3,4,5]
list2=list1
list3=[6,7,8]
print(list2 is list1) #True
print(list3 is list1) #False




list1=[1,2,3,4,5]
print(list1) #[1, 2, 3, 4, 5]
list2=list1.copy()
list2[1]="Hello"
print(list2) #[1, 'Hello', 3, 4, 5]
print(list1) #[1, 2, 3,


list1[-1]=0
print(list1) #[1, 2, 3, 4, 0]
print(list2) #[1, 'Hello', 3, 4, 5]
print(list3) #[1, 2, 'Hello', 4, 5]
print(list4) #[1, 2, 3, 'Hello', 5]



#Поиск элемента


customers=['Bob','Anna','Joe','Nick']
print(customers.index('Joe')) #2
category=["Drama", "Comedy", "Mystery", "Romance",
 "Comedy"]
print(category.index('Comedy')) #1




#Если же нам необходимо выбрать все элементы, равные указанному, то поиск можно организовать вручную,
#перебирая список.
customers=['Bob','Anna','Joe','Bob','Nick']
for i in range(len(customers)):
 if customers[i]=='Bob':
  print(i)
#0
#3


#Матрицы




myTbl=[[111,112,113],[221,222,223]]
print(myTbl[1][1]) #222
print(myTbl[0]) #[111, 112, 113]



#Для перебора всех элементов таких списков можно
#использовать вложенные циклы:
for i in range(2):
 for j in range(3):
  print(myTbl[i][j])
#111
#112
#113
#221
#222
#223


for i in range(len(myTbl)):
 for j in range(len(myTbl[i])):
  print(myTbl[i][j])


 #Для создания матриц также можно использовать генераторы списков:
  myTbl2 = [[j for j in range(2)] for i in  range(3)]
print(myTbl2) #[[0, 1], [0, 1], [0, 1]]

studScores = [['Bob',11,8,10,12],
 ['Jane',12,11,11,11], ['Kate',7,8,9,9]]
for student in studScores:
 print(student)

 for student in studScores:
     print(student[0], max(student[1:]))





#Рассмотрим еще один пример. Допустим, что у нас
#есть данные, к какой категории относится определенный фильм.
films=[['Catch Me If You Can', 'Biography', 'Crime', 'Drama'],
 ['Mrs. Doubtfire', 'Comedy', 'Drama', 'Family']]


userCategory=input("Input film category: ")
for film in films:
 if userCategory in film[1:]:
  print(film[0])