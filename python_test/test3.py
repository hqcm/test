class Retangle():
    def __init__(self,length=1,width=1):
        self.length=length
        self.width=width

       def __setattr__(self,name,value):
        if name=='square':
            self.length=value
            self.width=value
        else:
            super().__setattr__(name,value)
        
    def mianji(self):
        return self.length*self.width
