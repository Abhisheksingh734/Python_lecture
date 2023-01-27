class Exception():
    pass

class SecondDivision(Exception):
    def __init__(self):
        print("exception raised this is second division")
class ThirdDivision(Exception):
    def __init__(self):
        print("exception raised this is third division ")
    
class Fail(Exception):
    def __init__(self):
        print("exception raised this is fail ")

avg_marks=65
try:     
    if 65<avg_marks<=75:
        raise SecondDivision()
    elif 55<avg_marks<=65:
        raise ThirdDivision()
    elif avg_marks<=55:
        raise Fail()
except:
    print()
