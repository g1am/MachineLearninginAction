import matplotlib.pyplot as plt

decisionNode=dict(boxstyle="sawtooth",fc="0.8")
leafNode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")#定义文本框和箭头格式

def retrieveTree(i):
	listOfTrees=[{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},\
	{'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}]
	return listOfTrees[i]

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',\
		xytext=centerPt,textcoords='axes fraction',va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)

def createPlot():
	fig=plt.figure(1,facecolor='white')#新建图形区
	fig.clf()#清空绘图区
	createPlot.ax1=plt.subplot(111,frameon=False)
	plotNode('decisionNode',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('leafNode',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()

def getNumLeafs(myTree):#获取叶节点的数目
	numLeafs=0
	firstStr=list(myTree.keys())[0]#第一次划分数据集的类别标签
	secondDict=myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':#判断子类型是不是字典
			numLeafs+=getNumLeafs(secondDict[key])
		else:
			numLeafs+=1
	return numLeafs

def getTreeDepth(myTree):#树的层数
	maxDepth=0
	firstStr=list(myTree.keys())[0]
	secondDict=myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':#判断子类型是不是字典
			thisDepth=1+getTreeDepth(secondDict[key])
		else:
			thisDepth=1
		if thisDepth>maxDepth:maxDepth=thisDepth
	return maxDepth

# createPlot()
myTree=retrieveTree(0)
print(getNumLeafs(myTree))
print(getTreeDepth(myTree))