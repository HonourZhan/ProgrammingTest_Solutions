# class Solution:
# 	def maxCandies(self , candies , coin , n ):
candies,coin=[3,5,7,2,8,8,15,3],[1,0,1,0,1,0,1,0]
n=3
candies_nomag=[]
for i in range(len(candies)):
	candies_nomag.append(candies[i]*(1-coin[i]))
candies_res=[]
for i in range(len(coin)):
	candies_res.append(sum(candies_nomag[:i])+sum(candies[i:n+i])+sum(candies_nomag[n+i:]))
print(max(candies_res))
