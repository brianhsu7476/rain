import json

name=['博翔 許', '天盛 鄭', '尚齊 吳', '哲瑋 張', '耿宏 朱', '冠賢 吳']

res=[]
with open('data', 'r') as fp:
	res=json.load(fp)

print('distance\tclimb', end='\t')
for i in range(len(name)):
	print('name', i+1, end='\t')
print('route')
for i in res:
	print(i[2]+'\t'+i[3], end='\t')
	rk=i[-1]
	cnt=0
	for j in range(len(rk)):
		if rk[j][1] in name:
			print(rk[j][1]+': time='+rk[j][2]+', rank='+str(j+1), end='\t')
			cnt+=1
	while cnt<len(name):
		print('', end='\t')
		cnt+=1
	print(i[1])
