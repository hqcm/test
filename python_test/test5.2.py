class Counlist(list):
    def __init__(self,*args):
        super().__init__(args)
        self.count=[0]*len(args)

    def __len__(self):
        return len(self.value)
    
    def __getitem__(self,key):
        self.count[key]+=1
        return  super().__getitem__(key)

    def __setitem__(self,key,value):
        self.count[key]+=1
        super().__setitem__(key,value)           
                    
    def counter(self,index):
        return self.count[index]
                    
    def append(self,value):
        super().append(value)
        self.count.append(0)          
                    
    def pop(self,key):
        self.value.pop(key)
        return super().pop(key)
                    
    def insert(self,key,value):
        super().insert(key,value)
        self.count.insert[key,0]=0

    def reverse(self):
        self.count.reverse()
        super().reverse()
#5.1中的value的列表元素存放在父类中
