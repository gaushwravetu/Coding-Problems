def timeadd(x, y, xxx):
	y+=xxx
	if y>59:
		y-=60
		y+=1
	if y>23:
		y-=24
	return x, y


x,y=map(int,input().split('.'))

if x<0 or x>23:
	print('INVALID INPUT')

elif y<0 or y>59:
	print('INVALID INPUT')

else:
	list1=[4,5,6,4,3]
	result=''
	for xxx in list1:
		x,y=timeadd(x,y,xxx)
		days=''
		if x==0: days+='00'
		elif len(str(x))==1: days+='0'+str(x)
		else: days+=str(x)
		days+='.'
		if y==0: days+='00'
		elif len(str(y))==1: days+='0'+str(y)
		else: days+=str(y)
		result=result+days+' '
	print(result)