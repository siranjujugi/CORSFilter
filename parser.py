'''
Created on 04-Oct-2013

@author: siranj
'''

import re
def main():
    alist= [] 
    #num = ['0','1','2','3','4','5','6','7','8','9']
    f = open("D:/CTFWSPH2B/MainframeReportParser/rep.txt","r+")
    f1 =open("D:/CTFWSPH2B/MainframeReportParser/_vit/parser/res1.txt","w+")
    data = f.read()
    lines = data.split('\n')
    totalline = len(lines)
    #column = lines[0].split('\t')
    #totalcolumn = len(column)
    #print(totalcolumn)
    print(totalline)
    for index in range(totalline):
        lines[index] = lines[index].strip()
        column = lines[index].split(' ')
        totalcolumn = len(column)
        #print(totalcolumn)
        a = len(lines[index])
        if a > 120 :
            matchObj = re.match(r'date',lines[index],re.M|re.I)
            matchObj1 = re.match(r'Transaction',lines[index],re.M|re.I)
            matchObj2 = re.match(r'cash',lines[index],re.M|re.I)
            matchObj3 = re.match(r'--------',lines[index],re.M|re.I)
            matchObj4 = re.match( r'(.*) Total (.*?) .*', lines[index], re.M|re.I)
            if matchObj:
                print("not valid");
            elif matchObj1 :
                print("invalid_2");
            elif matchObj2 :
                print("invalid_3");
            elif matchObj3 :
                print("invalid_4");
            elif matchObj4 :
                print("invalid_5");        
        #if len(column) != 0:
        #if column[0,1] in num:
            #if column[7,1] in num:
            else:
                alist= column[0].strip('>')
                m = len(column[0])
                print(alist[1:m],column[totalcolumn-1]);
                f1.write(alist[1:m]);
                f1.write("\t\t\t");
                f1.write(column[totalcolumn-1]);
                f1.write("\n");
                                       
main()
