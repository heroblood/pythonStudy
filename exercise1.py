'''
http://wenku.baidu.com/link?url=mxcmfQxbV2I1_XX0oZBtzetQAb6FxyFr2WkMvI6fpw2rmVf754xeSVuDxLfIGFv8R-LwVheT8wnEA05Hq9rJ7w5WP4X47-ZwcHwYPN2r6Bm
【程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
import copy
a=['1','2','3','4']
set3=[]
for i in range(len(a)):
    b=copy.deepcopy(a)
    b.pop(i)
    for j in range(len(b)):
        c=copy.deepcopy(b)
        c.pop(j)
        for k in range(len(c)):
            set3.append(a[i]+b[j]+c[k])
print('个数：',len(set3),'\n分别是：',set3)

