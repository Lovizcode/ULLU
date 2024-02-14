# class vk:
#     def __init__(self,a,b):
#          print("hei",a+b)
# l1=vk(8,5)          
    
class first:
    def __init__(self,a,b,c):
                 self.a=a
                 self._b=b
                 self.__c=c
    def check(self):
        print("public",self.a)
        print("protect",self._b)
        print("private",self.__c)  
class second(first):
    def __init__(self, a, b, c):
        print(a,b,c)
        first.__init__(self,a,b,c)
    def printing(self):
        print("the value is",self.a)
        print("the value is",self._b)
        # print("the value is",self.__c)
s1=second(4,5,6)
s1.check()
s1.printing()                                  