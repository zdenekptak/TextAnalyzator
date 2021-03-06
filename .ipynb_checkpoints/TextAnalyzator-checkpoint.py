logins = {"bob" : "bob123", "ann" : "ann123", "mike" : "mike123", "liz" : "liz123"}
pozdrav = 'Welcome to the app. Please log in: '
oddelovac = '-'
delkaOddelovace = 50 * oddelovac
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print(delkaOddelovace)
print(pozdrav)
userName = input("USERNAMRE: ")
password = input("PASSWORD: ")
print(delkaOddelovace)
if logins.get(userName) == password:
    print('You are logged on!')
    print(delkaOddelovace)
else:
    print('Password or username incorrect')
    print(delkaOddelovace)

    

print("We have 3 texts to be analyzed.")
cisloClanku = int(input("Enter a number btw. 1 and 3 to select: "))
print(delkaOddelovace)

titleCase = 0
lowerCase = 0
upperCase = 0
numeric = 0
soucetCisel = 0

splitText = TEXTS[cisloClanku-1].split()
pocetSlov = len(splitText)
print(f"There are {pocetSlov} words in the selected text.")

for st in splitText:
    if st.istitle():
        titleCase = titleCase + 1
    elif st.islower():
        lowerCase = lowerCase + 1
    elif st.isupper():
        upperCase = upperCase + 1
    elif st.isnumeric():
        numeric = numeric + 1 
        soucetCisel = soucetCisel + int(st)

        
        
print(f"There are {titleCase} titlecase words")
print(f"There are {lowerCase} lowercase words")
print(f"There are {upperCase} uppercase words")
print(f"There are {numeric} numeric words")
print(delkaOddelovace)


cetnostSlovPodleDelky = {}
while splitText:
    slovo = splitText.pop()
    delkaSlova = len(slovo)
    if delkaSlova not in cetnostSlovPodleDelky:
        cetnostSlovPodleDelky[delkaSlova] = 1
    else:
        cetnostSlovPodleDelky[delkaSlova] = cetnostSlovPodleDelky[delkaSlova] + 1


for delkaSlova, pocet in sorted(cetnostSlovPodleDelky.items()):
    znak = "*"
    print(f"{delkaSlova} {pocet*znak} {pocet}")

print(delkaOddelovace)
print(f"If we summed all the numbers in this text we would get: {soucetCisel}")
print(delkaOddelovace)