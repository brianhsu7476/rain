import json
import allSegments
import segmentClub

def clubRank(s):
	rk=[]
	t='table table-striped table-padded table-leaderboard'
	st=0
	while s[st:st+len(t)]!=t:
		st+=1
	t='href="/athletes/'
	for i in range(st, len(s)-len(t)+1):
		if s[i:i+len(t)]==t and s[i+len(t)].isdigit():
			res=[]
			j=i+len(t)
			while s[j].isdigit():
				j+=1
			res.append(s[i+len(t):j])
			j+=2
			k=j
			u='</a>'
			while s[k:k+len(u)]!=u:
				k+=1
			res.append(s[j:k])
			u='last-child'
			while s[k:k+len(u)]!=u:
				k+=1
			j=k+len(u)+2
			k=j
			u='</td>'
			v='<abbr class="unit" title="second">s</abbr>'
			while s[k:k+len(u)]!=u and s[k:k+len(v)]!=v:
				k+=1
			res.append(s[j:k])
			rk.append(res)
	return rk

def addSegments(s):
	seg=[]
	t='href="/segments/'
	for i in range(len(s)-len(t)+1):
		if s[i:i+len(t)]==t and s[i+len(t)].isdigit():
			res=[]
			j=i+len(t)
			while s[j].isdigit():
				j+=1
			res.append(s[i+len(t):j])
			j+=2
			k=j
			u='</a>'
			while s[k:k+len(u)]!=u:
				k+=1
			res.append(s[j:k])
			for l in range(2):
				u='<td>'
				while s[k:k+len(u)]!=u:
					k+=1
				j=k+len(u)
				k=j
				while s[k]!='<':
					k+=1
				res.append(s[j:k])
			res.append(clubRank(segmentClub.crawl(res[0])))
			seg.append(res)
			print(len(seg), 'segments done')
	return seg

res=addSegments(allSegments.crawl())
with open('data', 'w') as fp:
	json.dump(res, fp)

