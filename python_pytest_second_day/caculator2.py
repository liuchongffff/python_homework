
class Calculator_two :
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result= 0

    def add(self,a,b):
        self.a = a
        self.b = b
        self.result = self.a + self.b
        return self.result

    def div(self,a,b):
        if b == 0:
            raise Exception
        else:
            self.a = a
            self.b = b
            self.result = self.a / self.b
            return self.result
