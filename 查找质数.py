'''编程实现∶质数是指这个数只能被1和它自己本身整除的数，
实现输入一个整数，判断它是否为质数。'''
def zhishu(n):
    if int(n)== 1:
        return False
    for i in range(2, n):
        if int(n) % i == 0:
            return False
    return True
n = int(input())
print(zhishu(n))