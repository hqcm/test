class Counlist(list):
    def __init__(self,*args):
        self.value=list(args)
        self.count=[0]*len(self.value)

    def __len__(self):
        return len(self.value)
    
    def __getitem__(self,key):
        self.count[key]+=1
        return self.value[key]

    def __setitem__(self,key,value):
        self.value[key]=value
        self.count[key]=0           

    def __delitem__(self,key):
        del self.value[key]
        del self.count[key]
                    
    def counter(self,index):
        return self.count[index]
                    
    def append(self,value):
        self.value.append(value)
        self.count.append(0)          
                    
    def pop(self,key):
        self.value.pop(key)
        self.count.pop(key)
                    
    def insert(self,key,value):
        self.value.insert[key]=value
        self.count.insert[key]=0

    def reverse(self):
        self.value.reverse()
        self.count.reverse()
