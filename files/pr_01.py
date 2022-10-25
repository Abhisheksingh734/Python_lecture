# write a program to read the text from a given
# file "poem.txt" and find out whether it contains
#  the word "twinkle" 

f=open("files/poems.txt","r")
text=f.read()
if "twinkle" in text:
    print("Yes it is")
else:
    print("No ")
f.close()