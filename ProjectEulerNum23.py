#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
#For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
#the smallest number that can be written as the sum of two abundant numbers is 24.
#By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
#However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math
import time
start = time.time()

list = [i for i in range(1,28124)]
abundant_nums = []
abundant_sums = []
answer = 0

def abundant_num(n): # determines if a number is abundant
    sum_divisors = 1
    do_not_check = []
    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if i in do_not_check:
            continue
        else:
            if i * i == n:
                sum_divisors += i
            elif n % i == 0:
                sum_divisors += i
                sum_divisors += int(n/i)
                do_not_check.append(int(n/i))
    if sum_divisors > n:
        abundant_nums.append(n)

for i in range(10, 28124):
    abundant_num(i)

for x in abundant_nums:
    for y in abundant_nums:
        if (x+y) < 28124:
            abundant_sums.append(x + y)

abundant_sums_sorted = set(abundant_sums)

for k in abundant_sums_sorted:
    list.remove(k)

for j in list:
    answer += j

print(answer)

stop = time.time()
print('Time: ', stop - start)