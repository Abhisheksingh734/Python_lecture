def game():
    return 1500
newscore=game()



f=open("files/highScore.txt","r")
score=f.read()
if score=='':
    with open("files/highScore.txt","r") as f:
        f.write(str(newscore))
elif newscore>int(score):
    f=open("files/highScore.txt","w")
    f.write(str(newscore))
    print("new highscore is set \n The new highScore is",newscore)
else:
    print("newscore is",newscore)
f.close()