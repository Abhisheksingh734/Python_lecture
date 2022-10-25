list=["fuck","gandu","donkey","chutiya"]
with open("files/censorFile.txt","r") as f:
    text=f.read()
    for i in range(len(list)):
        text=text.replace(list[i],"#@$%!^&")

with open("files/censorFile.txt","w") as f:
    text = f.write(text)
