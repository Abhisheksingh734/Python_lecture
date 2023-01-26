# import math
# class Parent():
#     def number(self,n):
#         self.n=n
#         num=n**(1/5)
#         if math.ceil(num)!=math.floor(num) and n>0:
#             print("positive and Nonperfect")
#         if math.ceil(num)!=math.floor(num) and n<0:
#             print("negative and Nonperfect")

# class Child(Parent):
#     def number(self, n):
#         self.n=n
#         num=n**(1/5)
#         if math.ceil(num)==math.floor(num) and n>0:
#             print("positive and perfect")
#         if math.ceil(num)==math.floor(num) and n<0:
#             print("negative and perfect")
            

# n=int(input("enter the number : "))
# num1 = Child()
# num1.number(n)



class Parent():
    def number(self,n):
        self.n=n
        if n>0:
            if int(n**(1/5))**5!=n:
                print("positive and Nonperfect")
        else:
            if int(abs(n)**(1/5))**5!=abs(n):
                print("negative and Nonperfect")
class Child(Parent):
    def number(self,n):
        self.n=n
        if n>0:
            if int(n**(1/5))**5==n:
                print("positive and perfect")
            else:
                print("positive and Nonperfect")
        else:
            if int(abs(n)**(1/5))**5==abs(n):
                print("negative and perfect")
            else:
                print("negative and Nonperfect")

n=int(input("enter the number: "))
num=Child()
num.number(n)

# class Parent:
#     def number(self, n):
#         if n > 0:
#             if int(n ** (1/5)) ** 5 == n:
#                 print("positive and perfect")
#             else:
#                 print("positive and nonperfect")
#         elif n < 0:
#             if int(abs(n) ** (1/5)) ** 5 == abs(n):
#                 print("negative and perfect")
#             else:
#                 print("negative and nonperfect")

# n = int(input("Enter an integer: "))
# p = Parent()
# p.number(n)