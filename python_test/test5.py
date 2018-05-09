class Counlist():
    def __init__(self,*args):
        self.value=args
        #fromkeys()函数用于创建一个字典，以序列中元素做字典的键，value为字典所有键对应的初始值。
        self.count=dict.fromkeys(range(len(self.value)),0)

    def __len__(self):
        return len(self.value)
    
    def __getitem__(self,key):
        self.count[key]+=1
        return self.value[key]

#元组，列表，字典以及这个序列都是通过[]来访问元素
