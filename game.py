X = "X"
O = "O"
EMP = " "
NULL = "NULL"

def IsZog(x):
	if(x%2 == 0):
		return True
	else:
		return False

class plane:
	def __init__(self):
		self.homes = []
		for i in range(0,9):
			self.homes.append(EMP)
	def show(self):
			print("--------------------------------------")
			print("   "+self.homes[0]+"    |     "+self.homes[1]+"       |     "+self.homes[2]+"    ")
			print("--------------------------------------")
			print("   "+self.homes[3]+"    |     "+self.homes[4]+"       |     "+self.homes[5]+"    ")
			print("--------------------------------------")
			print("   "+self.homes[6]+"    |     "+self.homes[7]+"       |     "+self.homes[8]+"    ")
			print("--------------------------------------")
	def IsWin(self):
		if(self.homes[0]==self.homes[4]==self.homes[8]==X or self.homes[2]==self.homes[4]==self.homes[6]==X or self.homes[0]==self.homes[1]==self.homes[2]==X or self.homes[3]==self.homes[4]==self.homes[5]==X or self.homes[6]==self.homes[7]==self.homes[8]==X or self.homes[0]==self.homes[3]==self.homes[6]==X or self.homes[1]==self.homes[4]==self.homes[7]==X or self.homes[2]==self.homes[5]==self.homes[8]==X):
			return X
		elif(self.homes[0]==self.homes[4]==self.homes[8]==O or self.homes[2]==self.homes[4]==self.homes[6]==O or self.homes[0]==self.homes[1]==self.homes[2]==O or self.homes[3]==self.homes[4]==self.homes[5]==O or self.homes[6]==self.homes[7]==self.homes[8]==O or self.homes[0]==self.homes[3]==self.homes[6]==O or self.homes[1]==self.homes[4]==self.homes[7]==O or self.homes[2]==self.homes[5]==self.homes[8]==O):
			return O
		else:
			return 0
class branch():
	def __init__(self):
		self.childrens = []
		self.data = NULL
		self.father = NULL
		self.lvl = NULL
		self.score = 0



playground = plane()

root = branch()
root.data = playground

def addscore(node):
	if(node.father == root):
		node.score = node.score + 1
	else:
		addscore(node.father)

def makeTree(root,lvl):
	for i in range(0,9):
		if(root.data.homes[i] == EMP):
			node = branch()
			state = plane()
			node.father = root
			#set homes from last
			#cant set directly (this loop do it)"
			for c in range(0,9):
				state.homes[c] = root.data.homes[c]
			#ok
			node.data = state
			if(IsZog(lvl)):
				node.data.homes[i] = X
			else:
				node.data.homes[i] = O
			node.lvl = lvl
			root.childrens.append(node)
			#Ok
	for x in range(0,len(root.childrens)):
		if(root.childrens[x].data.IsWin() !=0):
			if(root.childrens[x].data.IsWin() == X):
				addscore(root.childrens[x])
		else:
			makeTree(root.childrens[x],lvl+1)


def decision(root):
	scores = []
	for b in range(0,len(root.childrens)):
		scores.append(root.childrens[b].score)
	maxim = max(scores);
	print (maxim)
	for n in range(0,len(root.childrens)):
		if(root.childrens[n].score == maxim):
			for j in range(0,len(root.data.homes)):
				root.data.homes[j] = root.childrens[n].data.homes[j]
				break
			break



"""
for test
root.data.homes[5] = X
root.data.homes[4] = O
makeTree(root,0)
root.data.show()
for i in range(0,len(root.childrens)):
	print(root.childrens[i].score)
decision(root)
root.data.show()
"""
