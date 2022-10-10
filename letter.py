name= input("enter name: ")
date=input("enter date: ")

# print("\'\'\' Dear <\\",name,"\\>\n your are selected ! \n <\\",date,"\\>\'\'\'")

letter= '''Dear <|NAME|>
Greetings from ABC coding house. i am happy to tell you about your selection
You are selected!
Have a  great day ahead!
Thanks and regards,
Jack
date: <|DATE|>
'''

letter= letter.replace("<|NAME|>",name)
letter= letter.replace("<|DATE|>",date)

if letter.find("  ")!= -1:
    a =letter.replace("  "," ")
    print(a)
else:
    print(letter)
