import sys
line=sys.stdin.readline().split('],[')
width=list(map(int,line[0][1:].split(',')))
height=list(map(int,line[1][:-2].split(',')))
height_new=[]
res=0
# 非法条件的判断
if len(width)!=len(height) or len(width)==0 or len(height)==0\
	or min(width)<1 or min(height)<1\
	or max(width)>100 or max(height)>100:
	print(0)
else:
	for i in range(len(width)):
		while width[i]>0:
			height_new.append(height[i])
			width[i]=width[i]-1
	height_mul=height_new[:]
	height_new=list(set(height_new))
	for val in height_new:
		tmp,max_val=0,0
		for i in range(len(height_mul)):
			if height_mul[i]>=val:
				tmp=tmp+val
				max_val=max(tmp, max_val)
			else:
				tmp=0
		res=max(res,max_val)
print(res)