
# 欧几里得算法的普通实现
m = int(input("m = "))
n = int(input("n = "))

if m > n:
	m, n = n, m

# while n % m != 0:
# 	p = n % m
# 	n = m
# 	m = p
# print("所求最小公约数是： %d" % m)

# 优化实现：同时计算最小公约数和最小公倍数



def func(m,n):
	# while p != 0::
	if m > n:
		m, n = n, m
	while n % m != 0:
		p = n % m
		n = m
		m = p
	return m
most_common_divisor = func(m, n)
least_common_multiple = m * n // most_common_divisor

print("所求最大公约数是： %d " % most_common_divisor)
print("所求最小倍数是： %d " % least_common_multiple)

