import time
class MyTimer():    
    def start(self):
        t=list(time.localtime())
        self.starttime=t[3]*3600+t[4]*60+t[5]
        print('计时开始...')

    def stop(self):
        try:
            self.starttime
        except AttributeError:
            print ('请先调用start()开始计时！')
        else:
            t=list(time.localtime())
            self.stoptime=t[3]*3600+t[4]*60+t[5]
            print('计时结束')

    def __repr__(self):
        try:
            self.stoptime
        except AttributeError:
            return '未开始计时！'
        else:
            self.runtime=self.stoptime-self.starttime
            return '总共运行了%d秒'%self.runtime
        
    def __str__(self):
        print ('总共运行了%d秒' % int.__add__(self.runtime,other))
 
#各def要对齐，否则会无法识别
#list得到的是数组，用中括号获取其中的元素
                

            
