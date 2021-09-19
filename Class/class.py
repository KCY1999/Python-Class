import  class2
class abc():
    def __init__(self):
        self.a="testa"
        b="textb"
        print(self.a)
        print(b)

        self.a1=class2.num(1,2)
        self.a2=class2.num(3,4)
        print(self.a1.sum())

    def aaa(self):
        print(self.a1.num1)
        print(self.a2.num2)

'''     def bbb(self):
        x=5
        y=5
        num=self.sub.sub(x,y)
        print(num)
        

class sub():
    def sub1(self,num1,num2):
        num=num1+num2
        return num
'''
 #######################################################################################################'''

main=abc()