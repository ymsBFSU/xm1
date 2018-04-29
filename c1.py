import requests
from bs4 import BeautifulSoup
import re

def qiushibaike():
    content=requests.get('http://qiushibaike.com/').content
    soup=BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', {'class':'content'}):
        print div.text.strip()

def demo_string():
    stra='hello world'
    print stra.capitalize()
    stra.replace('world', 'nowcoder')
    print 1,'-'.join(['a','b','c'])
    print stra.split(" ")

def  demo_operation():
    print 1, 1+2,5/2,5*2,5-2
    print 2,True,not True

def demo_buildinfunction():
    print 1, max(2,1), min(5,3)
    print 2, len('xxx'),len([1,2,3])
    print 3,abs(-2)
    print 4,range(1,10,3)

def demo_controlflow():
    score=65
    if score>99:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print 3,'C'

    while score<100:
        print score
        score+=10

    #continue,break,pass
    for i in range(0,10,3):
        print 4,i

def demo_list():
    lista=[1,2,3]
    print 1,lista
    listb=['a',1,'c',1.1]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    tuple=(1,2,3) #read only

def add(a,b):
    return a+b

def sub(a,b):
    return a+b

def demo_dict():
    dicta={'+':add,'-':sub}
    print 1,dicta['+'](1,2)
    dicta['*']='x'
    print dicta

def demo_set():
    seta=set((1,2,3))
    print 1,seta
    setb=set((2,3,4))
    print 2,seta&setb
    seta.add(4)

def demo_re():
    str='dsjfkj12kj3432nj2'
    p1=re.compile('[\d]+')
    print 1,p1.findall(str)
    p2=re.compile('\d')
    print 2,p2.findall(str)
    str='a2@163.com;bds@sina.cn;meng@bfsu.edu,cn;7382@qq.com'
    p3=re.compile('[\w]+@[163|qq]+\.com')
    print p3.findall(str)
    str='<html><h>title</h><body>xxx</body></html>'
    p4=re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)
    p5=re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5,p5.findall(str)
    str='xxx2016-06-11yy'
    p5=re.compile('\d{4}-\d{2}-\d{2}')
    p6=re.compile('\d\d\d\d-\d\d-\d\d')
    print 6,p5.findall(str)
    print 6,p6.findall(str)

if __name__=='__main__':
    #print 'hello world'
    #comment
    #demo_string()
    #demo_operation()
    #demo_buildinfunction()
    #demo_controlflow()
    #demo_dict()
    #demo_set()
    demo_re()
