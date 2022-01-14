#输出正素数列表
nummin=int(input('请输入范围最小值\n'))
nummax=int(input('请输入范围最大值\n'))
if nummax<2 or nummin>nummax:
    print('无\n')
else:
    if nummin<=2:
        nummin=2
    if nummax>100000:
        c=int(input('请输入报告节点：'))
    else:
        c=1000
    num=[2]
    count=0
    b=[True]*(nummax+1)
    b[0]=False
    b[1]=False
    for i in range(3,nummax+1,2):
        count+=2
        if nummax>1000 and count%c==0:
            print('运算中,请稍候……\t运算次数：',count)
        if b[i]:
            num.append(i)
            for j in range(i*3,nummax+1,i*2):
                if b[j]:
                    b[j]=False
    for i in range(0,len(num)):
        if num[0]>=nummin:
             break
        else:
            del num[0]
            print('删除中……',num[0])                     
    print(nummin,'到',nummax,'以内的素数数量为\t',len(num),'\n最大为\t',max(num))
    boo=int(input('输入数字按位置进行输出,输入负数进行比较输出'))
    if (boo>=0):
        e=int(input('请输入终末值，小于等于原值默认为终止'))
        if (e<=boo):
            e=len(num)
        for i in range(boo,e):
            print(num[i])           	
    else:
        boo=-boo
        e=int(input('请输入终末值，小于等于原值默认为终止'))
        if (e<=boo) or (e>=max(num)):
            e=max(num)
        for t1 in range(len(num)):
            if (num[t1]>=boo):
                break
        for t2 in range(len(num)):
            if (num[t2]>=e):
                break        
        for i in range(t1,t2+1):
            print(num[i])    
                
    
        
