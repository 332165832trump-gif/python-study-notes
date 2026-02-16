n = int(input())
total=0
for i in range(1,n+1):
    total+=i
print("The sum of the first", n, "natural numbers is:", total)

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter a positive integer: "))
result = sum_to_n(n)    
print("The sum of the first", n, "natural numbers is:", result)
#上面的是一个简单的程序，计算从1到n的自然数的和。用户输入一个正整数n，然后程序使用一个循环来累加从1到n的数字，最后输出结果。函数sum_to_n(n)也实现了同样的功能，可以被调用来计算任意正整数n的自然数之和。    
下面是一个更简洁的版本，使用了数学公式来计算从1到n的自然数之和：
n = int(input("Enter a positive integer: "))   