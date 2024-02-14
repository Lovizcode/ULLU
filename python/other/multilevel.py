class papa:
    def l1(self):
        print("1st land owner-")
class child(papa):
    def l2(self):
        print("2nd land owner-")
class child2(child):
    def l3(self):
        print("3rd owner-")
cl=child2()
cl.l1()
cl.l2()
cl.l3()

                
                