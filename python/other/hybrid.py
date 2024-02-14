class papa:
    def l1(self):
        print("1st owner land-")
class child(papa):
    def l2(self):
        print("2nd owner land-")
class child2(papa):
    def l3(self):
        print("2nd owner land-") 
class child3(child,child2):
    def l4(self):
        print("5th land owner")  
p1=child3()
p1.l4()   
p1.l3()
p1.l2() 
p1.l1()              
              