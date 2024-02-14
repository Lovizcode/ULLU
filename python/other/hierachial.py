class papa:
    def l1(self):
        print("1st owner-")
class child(papa):
    def l2(self):
        print("2nd owner-")
class child2(papa):
    def l3(self):
        print("2nd owner-") 
class child3(child):
    def l4(self):
        print("3rd owner-")                       
class child4(child):
    def l5(self):
        print("3rd owner-")  
class child5(child2):
    def l6(self):
        print("4th owner-") 
class child6(child2):
    def l7(self):
        print("4th owner-")   
p1=child3()
p2=child4()        
p3=child5()
p4=child6()
p1.l4()
p1.l2()
p2.l5()
p3.l6()
p4.l7()
                       