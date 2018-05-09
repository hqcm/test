import time
class Mytimer():
    def __init__(self):
        self.unit=['年','月','日','时','分','秒']
        self.promot='未开始计时!'
        self.starttime=0

    def __repr__(self):
        return self.promot
    
    def __add__(self,other):
        promot='总共运行了'
        for i in range(6):
            totaltime=self.runtime[i]+other.runtime[i]
            if totaltime:
                promot+=str(totaltime)+self.unit[i]
        return promot
            
    def start(self):
        self.starttime=time.localtime()
        print ('计时开始。。。')

    def stop(self):
        self.runtime=[]
        self.stoptime=time.localtime()
        if not self.starttime:
            print ('请先调用start()开始计时!')
        else:
            self.promot='总共运行了'
            for i in range(6):
                self.runtime.append(self.stoptime[i]-self.starttime[i])
                if self.runtime[i]:
                    self.promot+=str(self.runtime[i])+self.unit[i]
            print ('计时结束！')

#各def要对齐，否则会无法识别
#localtime得到的是数组，用中括号即可获取其中的元素
#注意在变量名前加上self.,否则在其他函数中无法识别此变量
#采用append的方法是给一个空数组赋值的好方法
#注意init方法赋初值的作用
#add方法后应该返回return
