class Celsius():
    def __init__(self,value=26):
        self.value=value

    def __get__(self,instance,owner):
        return self.value
    
    def __set__(self,instance,value):
        self.value=value
    
    def __del__(self,instance,owner):
        self.fdel(instance)

class Fahrenheit():
    def __get__(self,instance,owner):
        return instance.c*1.8+32
    
    def __set__(self,instance,value):
        instance.c=(value-32)/1.8
    
    def __del__(self,instance,owner):
        self.fdel(instance)
        
class Temperature():
    c=Celsius()
    f=Fahrenheit()
    
#class Temperature要放在描述符后，否则其中的描述符属性无法识别
#instance指代的是Teperature这个实例，instance值的改变会引起value变化然后引起self.value变化
#set中的value指的是赋值语句右边的值
