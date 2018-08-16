X = "X"
O = "O"
EMP = " "
NULL = "NULL"
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
		self.father = NULL
		self.childrens = []
		self.state = NULL



	