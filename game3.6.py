X = "X"
O = "O"
EMP = " "
NULL = "NULL"
import random

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
	def CheckAllHomeIsFUll(self):
		for i in range(0,9):
			if(self.homes[i] == EMP):
				return False
		return True

	def IsWin(self):
		if(self.homes[0]==self.homes[4]==self.homes[8]==X or self.homes[2]==self.homes[4]==self.homes[6]==X or self.homes[0]==self.homes[1]==self.homes[2]==X or self.homes[3]==self.homes[4]==self.homes[5]==X or self.homes[6]==self.homes[7]==self.homes[8]==X or self.homes[0]==self.homes[3]==self.homes[6]==X or self.homes[1]==self.homes[4]==self.homes[7]==X or self.homes[2]==self.homes[5]==self.homes[8]==X):
			return X
		elif(self.homes[0]==self.homes[4]==self.homes[8]==O or self.homes[2]==self.homes[4]==self.homes[6]==O or self.homes[0]==self.homes[1]==self.homes[2]==O or self.homes[3]==self.homes[4]==self.homes[5]==O or self.homes[6]==self.homes[7]==self.homes[8]==O or self.homes[0]==self.homes[3]==self.homes[6]==O or self.homes[1]==self.homes[4]==self.homes[7]==O or self.homes[2]==self.homes[5]==self.homes[8]==O):
			return O
		elif(self.CheckAllHomeIsFUll()):
			return 1
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

def addscore(node,sc):
	if(node.father == root):
		node.score = node.score + sc
	else:
		addscore(node.father,sc)

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
				addscore(root.childrens[x],1)
			elif(root.childrens[x].data.IsWin() == O):
				addscore(root.childrens[x],-1)

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
			print(root.childrens[n].data.homes)
			for j in range(0,9):
				root.data.homes[j] = root.childrens[n].data.homes[j]
			break


print(" You Are O and your Oppenent(Computer) Is X")
print("--------------house numbers --------------")
print("     1       |       2      |        3    ")
print("------------------------------------------")
print("     4       |       5      |        6    ")
print("------------------------------------------")
print("     7       |       8      |        9    ")
print("------------------------------------------")
print(" ")
fpstart = int(input("Enter Who First Start 1:Computer 2:you : "))
if(fpstart == 1):
	fpstart = X
if(fpstart == 2):
	fpstart = O
if(fpstart == X):
	root.data.homes[random.randint(0,8)] = X
	root.data.show()
while True:
	if(root.data.IsWin() != 0):
				if(root.data.IsWin() == X):
					print("Computer Win The Game")
					break
				elif(root.data.IsWin() == O):
					print("You Win The Game")
					break
				elif(root.data.IsWin() == 1):
					print("Wow You and Computer Equals")
					break


	place = int(input("Is Your Turn Select Place:"))
	place = place-1
	if(place>9):
			print("WTF? Select Smaller ")
	else:
		if(root.data.homes[place]!= EMP):
			print("This House Is Full Select Another")
		else:
			root.data.homes[place] = O
			root.data.show()
			if(root.data.IsWin() != 0):
				if(root.data.IsWin() == X):
					print("Computer Win The Game")
					break
				elif(root.data.IsWin() == O):
					print("You Win The Game")
					break
				elif(root.data.IsWin() == 1):
					print("Wow You and Computer Equals")
					break
			else:
				print("Computers Turn Let him thinking...")
				makeTree(root,0)
				decision(root)
				root.data.show()
				root.childrens = []


