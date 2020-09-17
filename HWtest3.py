import sys

# 糖果数目为m，宝宝数目为n
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
def fun(m, n):
	if n < 0:
		return 0
	elif m == 0 or n == 1:
		return 1
	elif n > m:
		# 当宝宝的数目比糖果多的时候，一定有n-m个宝宝是没有糖果的
		return fun(m, m)
	else:
		return fun(m, n - 1) + fun(m - n, n)
print(fun(a, b))