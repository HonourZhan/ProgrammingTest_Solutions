import sys
# 输入数据读取
line=sys.stdin.readline().split(' ')
num_in=list(map(int,line))

tmp_fin=''
for tmp in num_in:
	tmp_change = ''
	tmp_str=''
	# 十进制数据转化为二进制并去掉‘0b’
	tmp_bin=str(bin(tmp))[2:]
	# 将其补全为32位数据
	if len(tmp_bin)!=32:
		tmp_str='0'*(32-len(tmp_bin))+tmp_bin
	# print(tmp_str)
	# 每两个bit进行交换
	for i in range(0,len(tmp_str),2):
		tmp_change=tmp_change+tmp_str[i+1]+tmp_str[i]
	# print(tmp_change)
	tmp_fin=tmp_fin+tmp_change
# 数字向右移位
tmp_val=tmp_fin[len(num_in)*32-2:]+tmp_fin[:len(num_in)*32-2]
res=[]
# 转化为2进制进行输出
for i in range(len(num_in)):
	res.append(int(tmp_val[32*i:32*(i+1)],2))
for num in res:
	print(num,end=' ')
# print(tmp_fin)
# print(tmp_val)
