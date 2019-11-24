from math import log
import operator

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

def splitDataSet(dataSet,axis,value):#划分数据集，符合特征要求的，除了特征以外的所有信息都保存
	retDataSet=[]
	for featVec in dataSet:
		if featVec[axis]==value:
			reducedFeatVec=featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def bestSplit(dataSet):#寻找最好划分的特征
	numFeatures=len(dataSet[0])-1#计算除去最后一个标签，有多少特征
	baseEntropy=calcShannonEnt(dataSet)#计算原始的熵
	bestInfoGain=0.0#记录最优熵
	bestFeature=-1#记录最优划分的特征
	for i in range(numFeatures):#考察每个特征
		featList=[example[i] for example in dataSet]#第i个特征的所有值
		uniqueVals=set(featList)#集合中的值互不相同
		newEntropy=0.0
		for value in uniqueVals:#考察这个特征的所有值
			subDataSet=splitDataSet(dataSet,i,value)
			prob=len(subDataSet)/float(len(dataSet))#
			newEntropy+=prob*calcShannonEnt(subDataSet)
		infoGain=baseEntropy-newEntropy
		if(infoGain>bestInfoGain):
			bestInfoGain=infoGain
			bestFeature=i
	return bestFeature

def mahorityCnt(classList):#形参应该是所有标签列表
	classCount={}#存储每个类别出现的次数
	for vote in classList:#考察每一个类别
		if vote not in classCount.keys():
			classCount[vote]=0
		classCount[vote]+=1
	sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def createTree(dataSet,labels):
	classList=[example[-1] for example in dataSet]#所有标签
	if classList.count(classList[0])==len(classList):#都属于一个类，停止划分
		return classList[0]
	if len(dataSet[0])==1:#所有的标签都用过还是不能划分，就挑选出现次数最多的类型
		return majorityCnt(classList)
	bestFeat=bestSplit(dataSet)
	bestFeatLabel=labels[bestFeat]

	myTree={bestFeatLabel:{}}#
	del(labels[bestFeat])
	featValues=[example[bestFeat] for example in dataSet]
	uniqueVals=set(featValues)#存储最好特征的所有值
	for value in uniqueVals:
		subLabels=labels[:]
		myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)#递归
	return myTree

myDat,labels=createDataSet()
#print(bestSplit(myDat))
myTree=createTree(myDat,labels)
print(myTree)