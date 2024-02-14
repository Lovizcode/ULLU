class first():
    def vk(self,a):
        print("hellow",a)
class second(first):
    def vk(self,a,b):
     super().vk(4)       
     print("hellow",a,b) 
class third(second):
    def vk(self,a,b,c):
     super().vk(3,4)
     print("hellow",a,b,c)
h1=third()
# h1.vk(4)
# h1.vk(4,5)
h1.vk(4,5,6)                