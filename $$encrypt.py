
import os
import sys

def readFile(filename):
    with open(filename,'r', encoding='utf-8') as f:
        global inputext
        print(filename)
        inputext=f.read()

def getPW():
    global passw
    try:
        f=open('IMPORTANT','r',encoding='utf-8')
        passw=f.read()
        f.close()
    except:        
        passw=input('请输入密码：\n')
        with open('IMPORTANT','w',encoding='utf-8') as f:
            f.write(passw)
            os.system('attrib +s +h +r +a IMPORTANT')   


def encrypt(outfile):
    '''turn string into number string  every word takes one lines'''        
    listin=list(inputext)
    listp=list(passw)
    p=[ord(x) for x in listp]
    pw=1
    for x in p:
        pw=x*pw
    pw=str(pw)
    pw=pw[-18:]
    pws='0.'+pw
    pw=float(pws)
    texto=''                           
    for x in listin:
        pw=pw*(1-pw)*3.93699989893668722729139042
        pws=str(pw)
        pivot= int(pws[-6:-3])
        texto=texto+str(ord(x)^pivot)+' '
    with open(outfile,'w',encoding='utf-8') as f:
        f.write(texto)
    pass

if __name__ == "__main__":
    os.chdir(sys.path[0])
    from pathlib import Path as p
    try:
        with open('filename.txt','r',encoding='utf-8') as f:
            ss=f.read().strip()
    except:
        ss=input('请输入github对应仓库名！\n')
        with open('filename.txt','w',encoding='utf-8') as f:
            f.write(ss)
    try:
        p('./'+ss).mkdir()
    except:
        pass
    for x in p('.').iterdir():
        if x.is_file():
            plist=['*.py', '*.txt', '*.js', '*.cpp', '*.c', '*.html','*.json', '*.bat','*.sql']
            match=False
            for m in plist:
                if x.match(m):
                    match=True
                    break
            if match:
                readFile(str(x))
                getPW()
                encrypt('./'+ss+'/'+str(x))

                