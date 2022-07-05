from datetime import datetime

name=input("Enter Your Name:")
phonenumber=int(input("Enter your number:"))
#LISTS OF ITEMS
lists='''
Rice    Rs 80/kg
sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 90/litre
paneer  Rs 200/kg
Maggi   Rs 50/each
Boost   Rs90/each
colgate Rs 60/packet
dal     Rs 80/kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':80,'sugar':30,'salt':20,'oil':90,'paneer':200,'Maggi':50,'Boost':90,'colgate':60,'dal':80}
option=int(input("for list of items press 1:"))
#conditions
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","Orange supermarket",25*"=")
            print(28*" ","Vinukonda")
            print("Name:",name,30*" ","Date:",datetime.now())
            print("phonenumber:",phonenumber)
            print(75*"-")
            print("S.No",8*" ",'items',8*" " ,"quantity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,8*' ',3*' ',ilist[i],10*' ',qlist[i],11*' ',plist[i])
            print(75*"-")
            print(50*" ","Totalamount:",'Rs',totalprice)
            print("gst amount",50*" ","Rs",gst)
            print(75*"-")
            print(50*" ","finalamount:","Rs",finalamount)
            print(75*"-")
            print(30*" ","Thanks for visiting")
            print(75*"-")
