class papa:
    def l1(self):
        print("1st land-")
        
class child(papa):
    def l2(self):
        print("2nd land-") 

class child2(papa):
    def l3(self):
        print("3nd land-")         

class child3(papa):
    def l4(self):
        print("4nd land-") 
                       
h1=child2()
# h1.l2()
# h1.l1() 
h1.l3() 
h1.l1()      