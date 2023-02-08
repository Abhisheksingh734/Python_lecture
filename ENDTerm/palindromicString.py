n=int(input())
words=[]

for i in range(n):
    word=input("enter the word: ")
    words.append(word.lower())

count=0
def palindromic(str):
    if str==str[::-1]:
        return True
for i in words:
    if palindromic(i):
        count+=1
print(count)