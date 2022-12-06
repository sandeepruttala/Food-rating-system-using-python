class Error(Exception):
    pass
class InvalidEntryforSolidsError(Error):
    pass
class InvalidEntryforLiquidsError(Error):
    pass
class InvalidEntryforSemiLiquidsError(Error):
    pass
class ItemNotFoundError(Error):
    pass
#functions

def solids():
    print("\n(Input your rating in terms of Best,Good,Average,Poor)\n")
def semi_liquids():
    print("\n(Input your rating in terms of one,two,three,four,five)\n")
def liquids():
    print("\n(Input your rating in terms of 1,2,3,4,5)\n")
def biryani(s,solids_food_rating):
    solids()
    while True:
        try:
            n = input("Enter rating for biryani: ")
            if n in s:
                solids_food_rating.update({'biryani':n})
                break
            else:
                raise InvalidEntryforSolidsError
        except InvalidEntryforSolidsError:
            print("\nError: not a valid rating term i.e(Best,Good,Average,Poor)\n")
def noodles(s,solids_food_rating):
    solids()
    while True:
        try:
            n = input("Enter rating for noodles: ")
            if n in s:
                solids_food_rating.update({'noodles':n})
                break
            else:
                raise InvalidEntryforSolidsError
        except InvalidEntryforSolidsError:
            print("\nError: not a valid rating term i.e(Best,Good,Average,poor)\n")
def manchuria(s,solids_food_rating):
    solids()
    while True:
        try:
            n = input("Enter rating for manchuria: ")
            if n in s:
                solids_food_rating.update({'manchuria':n})
                break
            else:
                raise InvalidEntryforSolidsError
        except InvalidEntryforSolidsError:
            print("\nError: not a valid rating term i.e(Best,Good,Average,poor)\n")
def icecream(sl,semiliquids_food_rating):
    semi_liquids()
    while True:
        try:
            n = input("Enter rating for icecream: ")
            if n in sl:
                semiliquids_food_rating.update({'ice cream':n})
                break
            else:
                raise InvalidEntryforSemiLiquidsError
        except InvalidEntryforSemiLiquidsError:
            print("\nError: not a valid rating term i.e(one,two,three,four,five)\n")
def soups(sl,semiliquids_food_rating):
    semi_liquids()
    while True:
        try:
            n = input("Enter rating for soups: ")
            if n in sl:
                semiliquids_food_rating.update({'soups':n})
                break
            else:
                raise InvalidEntryforSemiLiquidsError
        except InvalidEntryforSemiLiquidsError:
            print("\nnot a valid rating term i.e(one,two,three,four,five)\n")
def fruit_juices(l,liquids_food_rating):
    liquids()
    while True:
        try:
            n = input("Enter rating for fruit juices: ")
            if n in l:
                liquids_food_rating.update({'fruit juices':n})
                break
            else:
                raise InvalidEntryforLiquidsError
        except InvalidEntryforLiquidsError:
            print("\nError: not a valid rating term i.e(1,2,3,4,5)\n")
def cool_drinks(l,liquids_food_rating):
    liquids()
    while True:
        try:
            n = input("Enter rating for fruit cool drinks: ")
            if n in l:
                liquids_food_rating.update({'cool drinks':n})
                break
            else:
                raise InvalidEntryforLiquidsError
        except InvalidEntryforLiquidsError:
            print("\nError: not a valid rating term i.e(1,2,3,4,5)\n")

#functions

#main

solid_food =['biryani','noodles','manchuria']
semiliquid_food =['ice cream','soups']
liquid_food=['fruit juices','cool drinks']
s = ['Best','Good','Average','Poor']
sl = ['one','two','three','four','five']
l = ['1','2','3','4','5']
item=[1,2,3,4,5,6,7]
solids_food_rating = {'biryani':0,'noodles':0,'manchuria':0}
semiliquids_food_rating = {'ice cream':0,'soups':0}
liquids_food_rating={'fruit juices':0,'cool drinks':0}
order=[]

#main

#interface

print("\n*************WELCOME*************\n")
print("\nMENU:\n")
print("\nSOLIDS:\n")
print('1. Biryani\n2. Noodles\n3.Manchuria\n')
print("\nSemi-iquids:\n")
print('4. Ice-cream\n5. Soups\n')
print("\nLiquids:\n")
print('6. FRuit Juices\n7. Cool-drinks\n')
print("\n")

print("Order Here: ")
while True:
    try:
        n = int(input("\nEnter number of items you want to order: "))
        break
    except ValueError:
        print("\nEnter an integer to continue")
while n:
    while True:
        try:
            inp = int(input("\nEnter your item number: "))
            if inp in item:
                order.append(inp)
                n-=1
                break
            else:
                raise ItemNotFoundError
        except ItemNotFoundError:
            print("\nItem not found, Enter Correct Item number. Please Try again!\n")
        except ValueError:
            print("\nEnter correct item number(i.e 1,2,3,4,5) Try again!\n")

#interface

#processing
           
for i in order:
    if i==1:
        biryani(s,solids_food_rating)
    elif i==2:
        noodles(s,solids_food_rating)
    elif i==3:
        manchuria(s,solids_food_rating)
    elif i==4:
        icecream(sl,semiliquids_food_rating)
    elif i==5:
        soups(sl,semiliquids_food_rating)
    elif i==6:
        fruit_juices(l,liquids_food_rating)
    elif i==7:
        cool_drinks(l,liquids_food_rating)

#processing

#print

p1=[]
p2=[]
p3=[]
print("\n**************************************************************\n")
for k,v in solids_food_rating.items():
    if v == 'Best':
        p1.append(k)
if not(p1):
    for k,v in solids_food_rating.items():
        if v == 'Good':
            p1.append(k)
if not(p1):
    for k,v in solids_food_rating.items():
        if v == 'Average':
            p1.append(k)
if not(p1):
    for k,v in solids_food_rating.items():
        if v == 'Poor':
            p1.append(k)
print("\nThe Solid-food item(s) got highest rating are",end=' ')
print(*p1,sep=",")
print("\n")
for k,v in semiliquids_food_rating.items():
    if v == 'one':
        p2.append(k)
if not(p2):
    for k,v in semiliquids_food_rating.items():
        if v == 'two':
            p2.append(k)
if not(p2):
    for k,v in semiliquids_food_rating.items():
        if v == 'three':
            p2.append(k)
if not(p2):
    for k,v in semiliquids_food_rating.items():
        if v == 'four':
            p2.append(k)
if not(p2):
    for k,v in semiliquids_food_rating.items():
        if v == 'five':
            p2.append(k)
print("The Semi-liquid-food item(s) got highest rating are",end=' ')
print(*p2,sep=",")
print("\n")
for k,v in liquids_food_rating.items():
    if v == '1':
        p2.append(k)
if not(p3):
    for k,v in liquids_food_rating.items():
        if v == '2':
            p3.append(k)
if not(p3):
    for k,v in liquids_food_rating.items():
        if v == '3':
            p3.append(k)
if not(p3):
    for k,v in liquids_food_rating.items():
        if v == '4':
            p3.append(k)
if not(p3):
    for k,v in liquids_food_rating.items():
        if v == '5':
            p3.append(k)
print("The liquid-food item(s) got highest rating are",end=' ')
print(*p3,sep=",")
print("\n")

#print

#plot


