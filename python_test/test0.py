def main():  
    try:
        #"w"方式写时的'\n'会在被系统自动替换为'\r\n'
        #with open("test1.txt", "w") as f:
        with open("test1.txt", "wb") as f:
            for i in range(5):  
                f.write((str(i)+'\n').encode())   
    except IOError as reason:  
        print ("Error: open file failed.")  
        return  
if __name__ == "__main__":  
    main()  


#一：
#Python从文件中读取和写入的一般是字符串类型数据。因此，为了处理二进制数据，需要一种二进制数据到字符串数据的变换工具
#方法一：
#encode（编码），可以将str类型编码为bytes。 
#decode（译码），可以将bytes类型转换为str类型。
#方法二：
#使用struct模块。struct模块中最重要的三个函数是pack、unpack和calcsize。
#二：
#在字符串模式下换行符会在读写中自动换为\r\n（Windows平台），而二进制则不改变

