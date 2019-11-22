from math import log

def createDataSet():
	dataSet=[[1,1,'yes'],
	[1,1,'yes'],
	[1,0,'no'],
	[0,1,'no'],
	[0,1,'no']
	]
	labels=['no surfacing','flippers']
	return dataSet,labels

def calcShannonEnt(dataSet):
	num=len(dataSet)
	labelCounts={}#数据字典
	for featVec in dataSet:
		currentLabel=featVec[-1]#每一个数据的标签
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel]=0
		labelCounts[currentLabel]+=1#记录每个类别的次数
	shannonEnt=0.0
	for key in labelCounts:
		prob=float(labelCounts[key])/num#发生频率
		shannonEnt-=prob*log(prob,2)#以2为底求对数
	return shannonEnt

myDat,labels=createDataSet()
tt=calcShannonEnt(myDat)
print(tt)