text=open('record.txt')
i=1
f1=open('girl_1.txt','w')
f2=open('boy_1.txt','w')
#读入一行字符串
for eachline in text:
    if eachline[0:6]!='======':
        if eachline[0:3]=='小客服':
            f1.write(eachline[4:])
        else:
            f2.write(eachline[4:])
    else:
        f1.close()
        f2.close()
        i+=1
		#注意字符的拼接方式，尤其是数值变量的拼接
        name='girl_'+str(i)+'.txt'
        f1=open(name,'w')
        name='boy_'+str(i)+'.txt'
        f2=open(name,'w')
f1.close()
f2.close()
text.close()
        
