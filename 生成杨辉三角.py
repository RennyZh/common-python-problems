'''【题目描述】杨辉三角就是一个用数排列起来的三角形，杨辉三角规则如下：
1）每行第一个数和最后一个数都为1，其它每个数等于它左上方和右上方的两数之和；
2）第n行有n个数。
注意：“列”指的是斜列。
                1
             1    1
          1    2    1
        1   3     3   1
     1    4    6    4    1
   1   5    10    10  5   1
       ...     ...     ...    '''
#N表行数
N = int(input())
PTls =[[1],
    [1,1]]
for i in range(2,N):
    #nls表每行的内容
    nls = [1]
    for z in range(i-1) :
        nls.append(PTls[i-1][z]+PTls[i-1][z+1])
    nls.append(1)
    PTls.append(nls)
print(PTls)