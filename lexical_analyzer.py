import re
Operation=['*','-','/','=','>','<','>=','==','<=','%','+','+=','-=','*=','/=','%=','!','!=']#运算符
Delimiter=['(',')',',',';',':','{','}','<','>','"','','[',']'] #词法分析器中分别界符
#python关键字
KeyWord=['False','None','True','and','as','assert','async','await','break','class','continuct',
         'def','del','elif','else','except','finally','for','from','global','if','import','in',
         'is','lambda','nonlocal','not','or','pass','raise','return','try','while','with','yield']

def filterResource(file):

    f1 = open(file, 'r', encoding="UTF-8").read()
    f1 = re.sub(r"(\\\")|(\\\')","@1@",f1) #删除字符串中\"对于"的印象
    f1 = re.sub(r"(\".*?\")|(\'.*?\')|(r\'.*?\')|(r\".*?\")","Null_str",f1) #将字符串全部转化为一个特殊的字
    f1 = re.sub("#.*","",f1,re.DOTALL) #将注释删掉
    return f1
    #list_f1 = re.split(" |=|\n",f1) #按空格或者=号切分源代码
    #list_f2 = [j.strip() for j in list_f1]#彻底删除多余的空格

def codeHandling(s):
    l = ""
    l2 = []
    for i in s:
        if i not in Delimiter and i not in Operation and i not in [' ','\n']:
            l += i
        else:
            t = l #l是累加的字符串,
            l = ""
            s = i #i是当前字符串

            if s in Operation:
                print("<运算符:%s>"%(s))
            elif s in Delimiter:
                print("<分割符:%s>"%(s))

            if t in KeyWord:
                print("<关键字:%s>"%(t))
            elif t == 'Null_str':
                pass
            elif t.find('.')>=0:
                if re.match('\d+.\d',t)!=None:
                    print("<常量:%s>"%(t))
                else:
                    for k in t.split('.'):
                        if k != "":
                            print("<标识符:%s>"%(k))
            elif re.match('\d+',t)!=None:
                print("<常量:%s>"%(t))
            else:
                if re.match("^\w[\w\d]*",t)!=None:
                    print("<标识符:%s>"%(t))
                elif t not in["","[]"]:
                    print(t)
                    print("变量定义错误！") #查错，非法变量名，因代码能执行，应该不会抱这个问题

strs =filterResource('lexical_analyzer.py')
codeHandling(strs)

