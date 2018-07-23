import jieba
import jieba.analyse
seg_list=jieba.cut("我来到了西安交通大学",cut_all=True)
print("Full Mode: " + "/".join(seg_list)) 
seg_list=jieba.cut("我来到了西安交通大学",cut_all=False)
print("Default Mode: " + "/".join(seg_list)) 
seg_list=jieba.cut("我来到了西安交通大学")
print("/".join(seg_list)) 
#提取关键词
with open (r'C:\Users\Administrator\Desktop\全部消息记录.txt','r', encoding='UTF-8') as f:
    #read读取所有内容成为，返回一个字符串
    #readline()每次只读取一行，返回一个字符串
    #readlines()按行读取整个文件，返回一个列表
    content=f.read()
keywords = jieba.analyse.extract_tags(content, topK=5, withWeight=True, allowPOS=('n','nr','ns'))
for item in keywords:
    print(item[0],item[1])