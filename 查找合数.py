'''合数：合数指自然数中除了能被1和本身整除外，还能被其它正整数整除的数。
例如4，4除了能被1和4整除，还可以被2整除。'''
def composite_quantity(n):
    for i in range(2, n):
        if int(n) % i == 0:
            return True
    return False
n = int(input())
print(composite_quantity(n))