from abc import ABC
class vivek(ABC):
    def land(self):
        pass
class beta(vivek):
    def land(self):
        print("i have a hotel-")
class beti(vivek):
    def land(self):
        print("i have a hospital-")
be=beta()
be.land()
bi=beti()
bi.land()                    