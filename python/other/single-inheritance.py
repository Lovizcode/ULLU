class parent:
    def l1(self):
        print("1st land-")
        
class child(parent):
    def l2(self):
        print("2nd land-")        
h1=child()
h1.l2()
h1.l1()        