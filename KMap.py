
# K-Map Minimization 

import unittest
from Main import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(1,3,5,7,13)d(15,9,11)'),"B")
		self.assertEqual(minFunc(2,'(0,1)d(2,3)'),"1")
                
if __name__=='__main__':
	unittest.main()



def minFunc(numVar, stringIn):

	d_index=stringIn.find('d')

	q=stringIn[1:d_index-1]

	w=stringIn[d_index+2:len(stringIn)-1]


	if numVar==4:

		q1=q

		min_terms=[]
		dc=[]

		min_terms=q.split(',')
		dc=w.split(',')


		StringOut=''

		a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


		for x in range(len(min_terms)):
			if min_terms[x]=='0':
				q=a[0]
				q[0]=1

			elif min_terms[x]=='1':
				q=a[0]
				q[1]=1
				

			elif min_terms[x]=='2':
				q=a[0]
				q[3]=1
				

			elif min_terms[x]=='3':
				q=a[0]
				q[2]=1
				

			elif min_terms[x]=='4':
				q=a[1]
				q[0]=1
				

			elif min_terms[x]=='5':
				q=a[1]
				q[1]=1
				

			elif min_terms[x]=='6':
				q=a[1]
				q[3]=1
				

			elif min_terms[x]=='7':
				q=a[1]
				q[2]=1
				

			elif min_terms[x]=='8':
				q=a[3]
				q[0]=1
				

			elif min_terms[x]=='9':
				q=a[3]
				q[1]=1
								

			elif min_terms[x]=='10':
				q=a[3]
				q[3]=1
				

			elif min_terms[x]=='11':
				q=a[3]
				q[2]=1
				

			elif min_terms[x]=='12':
				q=a[2]
				q[0]=1
				

			elif min_terms[x]=='13':
				q=a[2]
				q[1]=1
				

			elif min_terms[x]=='14':
				q=a[2]
				q[3]=1
				

			else:
				q=a[2]
				q[2]=1






		for x in range(len(dc)):
			if dc[x]=='0':
				q=a[0]
				q[0]=5

			elif dc[x]=='1':
				q=a[0]
				q[1]=5
				

			elif dc[x]=='2':
				q=a[0]
				q[3]=5
				

			elif dc[x]=='3':
				q=a[0]
				q[2]=5
				

			elif dc[x]=='4':
				q=a[1]
				q[0]=5
				

			elif dc[x]=='5':
				q=a[1]
				q[1]=5
				

			elif dc[x]=='6':
				q=a[1]
				q[3]=5
				

			elif dc[x]=='7':
				q=a[1]
				q[2]=5
				

			elif dc[x]=='8':
				q=a[3]
				q[0]=5
				

			elif dc[x]=='9':
				q=a[3]
				q[1]=5
								

			elif dc[x]=='10':
				q=a[3]
				q[3]=5
				

			elif dc[x]=='11':
				q=a[3]
				q[2]=5
				

			elif dc[x]=='12':
				q=a[2]
				q[0]=5
				

			elif dc[x]=='13':
				q=a[2]
				q[1]=5
				

			elif dc[x]=='14':
				q=a[2]
				q[3]=5
				

			elif dc[x]=='15' :
				q=a[2]
				q[2]=5

			else:
				a=a


		# OCTET WALA

		# all 1

		count=0

		for i in a:
			for j in i:
				if j==1:
					count+=1

		if count==16:
			StringOut='1'



		# 0 and 1 row

		count1=0

		for i in a[0]:
			if i==1 or i==5:
				count1+=1



		for i in a[1]:
			if i==1 or i==5:
				count1+=1

		if count1==8:
			StringOut="A'"                
			a[0]=[5,5,5,5]
			a[1]=[5,5,5,5]


		# 1 and 2 row

		count2=0

		for i in a[1]:
			if i==1 or i==5:
				count2+=1

		for i in a[2]:
			if i==1 or i==5:
				count2+=1

		if count2==8:
			a[1]=[5,5,5,5]
			a[2]=[5,5,5,5]
			if StringOut == '':
				StringOut="B"
			else:
				StringOut+=" OR B"
				


		# 2 and 3 row

		count3=0

		for i in a[2]:
			if i==1 or i==5:
				count3+=1

		for i in a[3]:
			if i==1 or i==5:
				count3+=1


		if count3==8:
			a[2]=[5,5,5,5]
			a[3]=[5,5,5,5]
			if StringOut == '':
				StringOut="A"
			else:
				StringOut=" OR A"  
				


		# 0 and 3 row

		count4=0

		for i in a[0]:
			if i==1 or i==5:
				count4+=1

		for i in a[3]:
			if i==1 or i==5:
				count4+=1


		if count4==8:
			a[0]=[5,5,5,5]
			a[3]=[5,5,5,5]
			if StringOut == '':
				StringOut="B'"
			else:
				StringOut=" OR B'"
				

		# col octet

		                             		              

		row0=[]
		row1=[]
		row2=[]
		row3=[]

		                                          
		row0=a[0]
		row1=a[1]
		row2=a[2]
		row3=a[3]


		# column 0 and 1


		if (row0[0] == 1 or row0[0] == 5) and  (row0[1] == 1 or row0[1] == 5) and  (row1[0] == 1 or row1[0] == 5) and  (row1[1] == 1 or row1[1] == 5) and  (row2[0] == 1 or row2[0] == 5) and  (row2[1] == 1 or row2[1] == 5) and  (row3[0] == 1 or row3[0] == 5) and  (row3[1] == 1 or row3[1] == 5):
			row0[0] = 5 ; row0[1] = 5 ; row1[0] = 5 ; row1[1] = 5 ; row2[0] = 5 ; row2[1] = 5 ; row3[0] = 5 ; row3[1] = 5
			if StringOut == '':
				StringOut="C'"
			else:
				StringOut+= " OR C'"
			
		# column 1 and 2


		elif (row0[1] == 1 or row0[1] == 5) and  (row0[2] == 1 or row0[2] == 5) and  (row1[1] == 1 or row1[1] == 5) and  (row1[2] == 1 or row1[2] == 5) and  (row2[1] == 1 or row2[1] == 5) and  (row2[2] == 1 or row2[2] == 5) and  (row3[1] == 1 or row3[1] == 5) and  (row3[2] == 1 or row3[2] == 5):
			row0[1] = 5 ; row0[2] = 5 ; row1[1] = 5 ; row1[2] = 5 ; row2[1] = 5 ; row2[2] = 5 ; row3[1] = 5 ; row3[2] = 5
			if StringOut == '':
				StringOut="B"
			else:
				StringOut+= " OR D"	
			
		# column 2 and 3


		elif (row0[2] == 1 or row0[2] == 5) and  (row0[3] == 1 or row0[3] == 5) and  (row1[2] == 1 or row1[2] == 5) and  (row1[3] == 1 or row1[3] == 5) and  (row2[2] == 1 or row2[2] == 5) and  (row2[3] == 1 or row2[3] == 5) and  (row3[2] == 1 or row3[2] == 5) and  (row3[3] == 1 or row3[3] == 5):
			row0[2] = 5 ; row0[3] = 5 ; row1[2] = 5 ; row1[3] = 5 ; row2[2] = 5 ; row2[3] = 5 ; row3[2] = 5 ; row3[3] = 5
			if StringOut == '':
				StringOut="C"
			else:
				StringOut+= " OR C"
			
		# column 0 and 3


		elif (row0[0] == 1 or row0[0] == 5) and  (row0[3] == 1 or row0[3] == 5) and  (row1[0] == 1 or row1[0] == 5) and  (row1[3] == 1 or row1[3] == 5) and  (row2[0] == 1 or row2[0] == 5) and  (row2[3] == 1 or row2[3] == 5) and  (row3[0] == 1 or row3[0] == 5) and  (row3[3] == 1 or row3[3] == 5):
			row0[0] = 5 ; row0[3] = 5 ; row1[0] = 5 ; row1[3] = 5 ; row2[0] = 5 ; row2[3] = 5 ; row3[0] == 5 ; row3[3] = 5
			if StringOut == '':
				StringOut="D'"
			else:
				StringOut+= " OR D'"
				

		#  QUAD


		#  0 row 

		count_1=0
		count_5=0

		for i in row0:
			if i == 5:
				count_5+=1
			elif i == 1:
				count_1+=1
			
		if count_5 != 4 and count_5+count_1 == 4 :
			row0=[5,5,5,5]
			if StringOut == '':
				StringOut="A'B'"
			else:
				StringOut+= " OR A'B'"
				
		# 1 row

		count_1=0
		count_5=0

		for i in row1:
			if i == 5:
				count_5+=1
			elif i == 1:
				count_1+=1
			
		if count_5 != 4 and count_5+count_1 == 4 :
			row1=[5,5,5,5]
			if StringOut == '':
				StringOut="A'B"
			else:
				StringOut+= " OR A'B"
				

		# 2 row

		count_1=0
		count_5=0

		for i in row2:
			if i == 5:
				count_5+=1
			elif i == 1:
				count_1+=1
			
		if count_5 != 4 and count_5+count_1 == 4 :
			row2=[5,5,5,5]
			if StringOut == '':
				StringOut="AB"
			else:
				StringOut+= " OR AB"
				

		#  3 row

		count_1=0
		count_5=0

		for i in row3:
			if i == 5:
				count_5+=1
			elif i == 1:
				count_1+=1
			
		if count_5 != 4 and count_5+count_1 == 4 :
			row3=[5,5,5,5]
			if StringOut == '':
				StringOut="AB'"
			else:
				StringOut+= " OR AB'"
				


		# 0 column

		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		elif row0[0]==1:
			count_1+=1 

		if row1[0]==5:
			count_5+=1
		elif row1[0]==1:
			count_1+=1 

		if row2[0]==5:
			count_5+=1
		elif row2[0]==1:
			count_1+=1 

		if row3[0]==5:
			count_5+=1
		elif row3[0]==1:
			count_1+=1 

		if count_5 != 4 and count_5 + count_1 == 4:
			row0[0]=5 ; row1[0]=5 ; row2[0]=5 ; row3[0]=5
			if StringOut == '':
				StringOut="C'D'"
			else:
				StringOut+= " OR C'D'"
				

		# 1 column


		count_1=0
		count_5=0

		if row0[1]==5:
			count_5+=1
		elif row0[1]==1:
			count_1+=1 

		if row1[1]==5:
			count_5+=1
		elif row1[1]==1:
			count_1+=1 

		if row2[1]==5:
			count_5+=1
		elif row2[1]==1:
			count_1+=1 

		if row3[1]==5:
			count_5+=1
		elif row3[1]==1:
			count_1+=1 

		if count_5 != 4 and count_5 + count_1 == 4:
			row0[1]=5 ; row1[1]=5 ; row2[1]=5 ; row3[1]=5
			if StringOut == '':
				StringOut="C'D"
			else:
				StringOut+= " OR C'D"
			

		# 2 column

		count_1=0
		count_5=0

		if row0[2]==5:
			count_5+=1
		elif row0[2]==1:
			count_1+=1 

		if row1[2]==5:
			count_5+=1
		elif row1[2]==1:
			count_1+=1 

		if row2[2]==5:
			count_5+=1
		elif row2[2]==1:
			count_1+=1 

		if row3[2]==5:
			count_5+=1
		elif row3[2]==1:
			count_1+=1 

		if count_5 != 4 and count_5 + count_1 == 4:
			row0[2]=5 ; row1[2]=5 ; row2[2]=5 ; row3[2]=5
			if StringOut == '':
				StringOut="CD"
			else:
				StringOut+= " OR CD"
				

		# 3 column

		count_1=0
		count_5=0

		if row0[3]==5:
			count_5+=1
		elif row0[3]==1:
			count_1+=1 

		if row1[3]==5:
			count_5+=1
		elif row1[3]==1:
			count_1+=1 

		if row2[3]==5:
			count_5+=1
		elif row2[3]==1:
			count_1+=1 

		if row3[3]==5:
			count_5+=1
		elif row3[3]==1:
			count_1+=1 

		if count_5 != 4 and count_5 + count_1 == 4:
			row0[3]=5 ; row1[3]=5 ; row2[3]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="CD'"
			else:
				StringOut+= " OR CD'"
				

		# 3rd type ke quad 

		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		if row0[0]==1:
			count_1+=1
		if row0[1]==5:
			count_5+=1
		if row0[1]==1:
			count_1+=1
		if row1[0]==5:
			count_5+=1
		if row1[0]==1:
			count_1+=1
		if row1[1]==5:
			count_5+=1
		if row1[1]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[0]=5 ; row0[1]=5 ; row1[0]=5 ; row1[1]=5
			if StringOut == '':
				StringOut="A'C'"
			else:
				StringOut+= " OR A'C'"
				
		#################
			
		count_1=0
		count_5=0

		if row0[1]==5:
			count_5+=1
		if row0[1]==1:
			count_1+=1
		if row0[2]==5:
			count_5+=1
		if row0[2]==1:
			count_1+=1
		if row1[1]==5:
			count_5+=1
		if row1[1]==1:
			count_1+=1
		if row1[2]==5:
			count_5+=1
		if row1[2]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[1]=5 ; row0[2]=5 ; row1[1]=5 ; row1[2]=5
			if StringOut == '':
				StringOut="A'D"
			else:
				StringOut+= " OR A'D"

		#################

		count_1=0
		count_5=0

		if row0[2]==5:
			count_5+=1
		if row0[2]==1:
			count_1+=1
		if row0[3]==5:
			count_5+=1
		if row0[3]==1:
			count_1+=1
		if row1[2]==5:
			count_5+=1
		if row1[2]==1:
			count_1+=1
		if row1[3]==5:
			count_5+=1
		if row1[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[2]=5 ; row0[3]=5 ; row1[2]=5 ; row1[3]=5
			if StringOut == '':
				StringOut="A'C"
			else:
				StringOut+= " OR A'C"
				
		#################


		count_1=0
		count_5=0

		if row1[0]==5:
			count_5+=1
		if row1[0]==1:
			count_1+=1
		if row1[1]==5:
			count_5+=1
		if row1[1]==1:
			count_1+=1
		if row2[0]==5:
			count_5+=1
		if row2[0]==1:
			count_1+=1
		if row2[1]==5:
			count_5+=1
		if row2[1]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row1[0]=5 ; row1[1]=5 ; row2[0]=5 ; row2[1]=5
			if StringOut == '':
				StringOut="BC'"
			else:
				StringOut+= " OR BC'"
				

		#################


		count_1=0
		count_5=0

		if row1[1]==5:
			count_5+=1
		if row1[1]==1:
			count_1+=1
		if row1[2]==5:
			count_5+=1
		if row1[2]==1:
			count_1+=1
		if row2[1]==5:
			count_5+=1
		if row2[1]==1:
			count_1+=1
		if row2[2]==5:
			count_5+=1
		if row2[2]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row1[1]=5 ; row1[2]=5 ; row2[1]=5 ; row2[2]=5
			if StringOut == '':
				StringOut="BD"
			else:
				StringOut+= " OR BD"
				
		#################


		count_1=0
		count_5=0

		if row1[2]==5:
			count_5+=1
		if row1[2]==1:
			count_1+=1
		if row1[3]==5:
			count_5+=1
		if row1[3]==1:
			count_1+=1
		if row2[2]==5:
			count_5+=1
		if row2[2]==1:
			count_1+=1
		if row2[3]==5:
			count_5+=1
		if row2[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row1[2]=5 ; row1[3]=5 ; row2[2]=5 ; row2[3]=5
			if StringOut == '':
				StringOut="BC"
			else:
				StringOut+= " OR BC"
				

		#################


		count_1=0
		count_5=0

		if row2[0]==5:
			count_5+=1
		if row2[0]==1:
			count_1+=1
		if row2[1]==5:
			count_5+=1
		if row2[1]==1:
			count_1+=1
		if row3[0]==5:
			count_5+=1
		if row3[0]==1:
			count_1+=1
		if row3[1]==5:
			count_5+=1
		if row3[1]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row2[0]=5 ; row2[1]=5 ; row3[0]=5 ; row3[1]=5
			if StringOut == '':
				StringOut="AC'"
			else:
				StringOut+= " OR AC'"
				
		#################


		count_1=0
		count_5=0

		if row2[1]==5:
			count_5+=1
		if row2[1]==1:
			count_1+=1
		if row2[2]==5:
			count_5+=1
		if row2[2]==1:
			count_1+=1
		if row3[1]==5:
			count_5+=1
		if row3[1]==1:
			count_1+=1
		if row3[2]==5:
			count_5+=1
		if row3[2]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row2[1]=5 ; row2[2]=5 ; row3[1]=5 ; row3[2]=5
			if StringOut == '':
				StringOut="AD"
			else:
				StringOut+= " OR AD"
				
		#################


		count_1=0
		count_5=0

		if row2[2]==5:
			count_5+=1
		if row2[2]==1:
			count_1+=1
		if row2[3]==5:
			count_5+=1
		if row2[3]==1:
			count_1+=1
		if row3[2]==5:
			count_5+=1
		if row3[2]==1:
			count_1+=1
		if row3[3]==5:
			count_5+=1
		if row3[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row2[2]=5 ; row2[3]=5 ; row3[2]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="AC"
			else:
				StringOut+= " OR AC"
				
		##############



		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		if row0[0]==1:
			count_1+=1
		if row1[0]==5:
			count_5+=1
		if row1[0]==1:
			count_1+=1
		if row0[3]==5:
			count_5+=1
		if row0[3]==1:
			count_1+=1
		if row1[3]==5:
			count_5+=1
		if row1[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[0]=5 ; row0[3]=5 ; row1[0]=5 ; row1[3]=5
			if StringOut == '':
				StringOut="A'D'"
			else:
				StringOut+= " OR A'D'"
				

		#############



		count_1=0
		count_5=0

		if row1[0]==5:
			count_5+=1
		if row1[0]==1:
			count_1+=1
		if row2[0]==5:
			count_5+=1
		if row2[0]==1:
			count_1+=1
		if row1[3]==5:
			count_5+=1
		if row1[3]==1:
			count_1+=1
		if row2[3]==5:
			count_5+=1
		if row2[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row1[0]=5 ; row1[3]=5 ; row2[0]=5 ; row2[3]=5
			if StringOut == '':
				StringOut="BD'"
			else:	
				StringOut+= " OR BD'"
				


		############


		count_1=0
		count_5=0

		if row2[0]==5:
			count_5+=1
		if row2[0]==1:
			count_1+=1
		if row2[3]==5:
			count_5+=1
		if row2[3]==1:
			count_1+=1
		if row3[0]==5:
			count_5+=1
		if row3[0]==1:
			count_1+=1
		if row3[3]==5:
			count_5+=1
		if row3[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row2[0]=5 ; row2[3]=5 ; row3[0]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="AD'"
			else:
				StringOut+= " OR AD'"
				


		#############



		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		if row0[0]==1:
			count_1+=1
		if row0[1]==5:
			count_5+=1
		if row0[1]==1:
			count_1+=1
		if row3[0]==5:
			count_5+=1
		if row3[0]==1:
			count_1+=1
		if row3[1]==5:
			count_5+=1
		if row3[1]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[0]=5 ; row0[1]=5 ; row3[0]=5 ; row3[1]=5
			if StringOut == '':
				StringOut="B'C'"
			else:
				StringOut+= " OR B'C'"
				

		############



		count_1=0
		count_5=0

		if row0[1]==5:
			count_5+=1
		if row0[1]==1:
			count_1+=1
		if row0[2]==5:
			count_5+=1
		if row0[2]==1:
			count_1+=1
		if row3[1]==5:
			count_5+=1
		if row3[1]==1:
			count_1+=1
		if row3[2]==5:
			count_5+=1
		if row3[2]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[1]=5 ; row0[2]=5 ; row3[1]=5 ; row3[2]=5
			if StringOut == '':
				StringOut="B'D"
			else:
				StringOut+= " OR B'D"
				


		############


		count_1=0
		count_5=0

		if row0[2]==5:
			count_5+=1
		if row0[2]==1:
			count_1+=1
		if row0[3]==5:
			count_5+=1
		if row0[3]==1:
			count_1+=1
		if row3[2]==5:
			count_5+=1
		if row3[2]==1:
			count_1+=1
		if row3[3]==5:
			count_5+=1
		if row3[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[2]=5 ; row0[3]=5 ; row3[2]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="B'C"
			else:
				StringOut+= " OR B'C"
				


		###########


		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		if row0[0]==1:
			count_1+=1
		if row0[3]==5:
			count_5+=1
		if row0[3]==1:
			count_1+=1
		if row3[0]==5:
			count_5+=1
		if row3[0]==1:
			count_1+=1
		if row3[3]==5:
			count_5+=1
		if row3[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[0]=5 ; row0[3]=5 ; row3[0]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="B'D'"
			else:
				StringOut+= " OR B'D'"
				


		############################################################  all quads over

		#  DUALS 

		## row 0

		if (row0[0]==5 and row0[1]==1) or (row0[0]==1 and row0[1]==5) or (row0[0]==1 and row0[1]==1):
			row0[0]=5 ; row0[1]=5
			if StringOut == '':
				StringOut="A'B'C'"
			else:
				StringOut+= " OR A'B'C'"
				

		if (row0[1]==5 and row0[2]==1) or (row0[1]==1 and row0[2]==5) or (row0[1]==1 and row0[2]==1):
			row0[1]=5 ; row0[2]=5
			if StringOut == '':
				StringOut="A'B'D"
			else:
				StringOut+= " OR A'B'D"
				


		if (row0[2]==5 and row0[3]==1) or (row0[2]==1 and row0[3]==5) or (row0[2]==1 and row0[3]==1):
			row0[2]=5 ; row0[3]=5
			if StringOut == '':
				StringOut="A'B'C"
			else:
				StringOut+= " OR A'B'C"
				


		## row 1

		if (row1[0]==5 and row1[1]==1) or (row1[0]==1 and row1[1]==5) or (row1[0]==1 and row1[1]==1):
			row1[0]=5 ; row1[1]=5
			if StringOut == '':
				StringOut="A'BC'"
			else:
				StringOut+= " OR A'BC'"
				


		if (row1[1]==5 and row1[2]==1) or (row1[1]==1 and row1[2]==5) or (row1[1]==1 and row1[2]==1):
			row1[1]=5 ; row1[2]=5
			if StringOut == '':
				StringOut="A'BD"
			else:
				StringOut+= " OR A'BD"  
				


		if (row1[2]==5 and row1[3]==1) or (row1[2]==1 and row1[3]==5) or (row1[2]==1 and row1[3]==1):
			row1[2]=5 ; row1[3]=5
			if StringOut == '':
				StringOut="A'BC"
			else:
				StringOut+= " OR A'BC"
				


		##  row 2

		if (row2[0]==5 and row2[1]==1) or (row2[0]==1 and row2[1]==5) or (row2[0]==1 and row2[1]==1):
			row2[0]=5 ; row2[1]=5
			if StringOut == '':
				StringOut="ABC'"
			else:
				StringOut+= " OR ABC'"
				


		if (row2[1]==5 and row2[2]==1) or (row2[1]==1 and row2[2]==5) or (row2[1]==1 and row2[2]==1):
			row2[1]=5 ; row2[2]=5
			if StringOut == '':
				StringOut="ABD"
			else:
				StringOut+= " OR ABD"
				


		if (row2[2]==5 and row2[3]==1) or (row2[2]==1 and row2[3]==5) or (row2[2]==1 and row2[3]==1):
			row2[2]=5 ; row2[3]=5
			if StringOut == '':
				StringOut="ABC"
			else:
				StringOut+= " OR ABC"
				


		##  row 3

		if (row3[0]==5 and row3[1]==1) or (row3[0]==1 and row3[1]==5) or (row3[0]==1 and row3[1]==1):
			row3[0]=5 ; row3[1]=5
			if StringOut == '':
				StringOut="AB'C'"
			else:
				StringOut+= " OR AB'C'"
				


		if (row3[1]==5 and row3[2]==1) or (row3[1]==1 and row3[2]==5) or (row3[1]==1 and row3[2]==1):
			row3[1]=5 ; row3[2]=5
			if StringOut == '':
				StringOut="AB'D"
			else:
				StringOut+= " OR AB'D"
				


		if (row3[2]==5 and row3[3]==1) or (row3[2]==1 and row3[3]==5) or (row3[2]==1 and row3[3]==1):
			row3[2]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="AB'C"
			else:
				StringOut+= " OR AB'C"
				


		########   col 0

		if (row0[0]==5 and row1[0]==1) or (row0[0]==1 and row1[0]==5) or (row0[0]==1 and row1[0]==1):
			row0[0]=5 ; row1[0]=5
			if StringOut == '':
				StringOut="A'C'D'"
			else:
				StringOut+= " OR A'C'D'"
				


		if (row1[0]==5 and row2[0]==1) or (row1[0]==1 and row2[0]==5) or (row1[0]==1 and row2[0]==1):
			row1[0]=5 ; row2[0]=5
			if StringOut == '':
				StringOut="BC'D'"
			else:
				StringOut+= " OR BC'D'"
				


		if (row2[0]==5 and row3[0]==1) or (row2[0]==1 and row3[0]==5) or (row2[0]==1 and row3[0]==1):
			row2[0]=5 ; row3[0]=5
			if StringOut == '':
				StringOut="AC'D'"
			else:
				StringOut+= " OR AC'D'"
				

		##  col 1


		if (row0[1]==5 and row1[1]==1) or (row0[1]==1 and row1[1]==5) or (row0[1]==1 and row1[1]==1):
			row0[1]=5 ; row1[1]=5
			if StringOut == '':
				StringOut="A'C'D"
			else:
				StringOut+= " OR A'C'D"
				



		if (row1[1]==5 and row2[1]==1) or (row1[1]==1 and row2[1]==5) or (row1[1]==1 and row2[1]==1):
			row1[1]=5 ; row2[1]=5
			if StringOut == '':
				StringOut="BC'D"
			else:
				StringOut+= " OR BC'D"
				



		if (row2[1]==5 and row3[1]==1) or (row2[1]==1 and row3[1]==5) or (row2[1]==1 and row3[1]==1):
			row0[0]=5 ; row1[0]=5
			if StringOut == '':
				StringOut="AC'D"
			else:
				StringOut+= " OR AC'D"
				


		##  Col 2


		if (row0[2]==5 and row1[2]==1) or (row0[2]==1 and row1[2]==5) or (row0[2]==1 and row1[2]==1):
			row0[2]=5 ; row1[2]=5
			if StringOut == '':
				StringOut="A'CD"
			else:
				StringOut+= " OR A'CD"
				



		if (row1[2]==5 and row2[2]==1) or (row1[2]==1 and row2[2]==5) or (row1[2]==1 and row2[2]==1):
			row1[2]=5 ; row2[2]=5
			if StringOut == '':
				StringOut="BCD"
			else:
				StringOut+= " OR BCD"
				



		if (row2[2]==5 and row3[2]==1) or (row2[2]==1 and row3[2]==5) or (row2[2]==1 and row3[2]==1):
			row2[2]=5 ; row3[2]=5
			if StringOut == '':
				StringOut="ACD"
			else:
				StringOut+= " OR ACD"
				


		##  col 3



		if (row0[3]==5 and row1[3]==1) or (row0[3]==1 and row1[3]==5) or (row0[3]==1 and row1[3]==1):
			row0[3]=5 ; row1[3]=5
			if StringOut == '':
				StringOut="A'CD'"
			else:
				StringOut+= " OR A'CD'"
				



		if (row1[3]==5 and row2[3]==1) or (row1[3]==1 and row2[3]==5) or (row1[3]==1 and row2[3]==1):
			row1[3]=5 ; row2[3]=5
			if StringOut == '':
				StringOut="BCD'"
			else:
				StringOut+= " OR BCD'"



		if (row2[3]==5 and row3[3]==1) or (row2[3]==1 and row3[3]==5) or (row2[3]==1 and row3[3]==1):
			row2[3]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="ACD'"
			else:
				StringOut+= " OR ACD'"
				


		####  bakki bache hue 8 dual:

		## 4 row wale

		if (row0[0]==5 and row0[3]==1) or (row0[0]==1 and row0[3]==5) or (row0[0]==1 and row0[3]==1):
			row0[0]=5 ; row0[3]=5
			if StringOut == '':
				StringOut="A'C'D'"
			else:
				StringOut+= " OR A'C'D'"
				


		if (row1[0]==5 and row1[3]==1) or (row1[0]==1 and row1[3]==5) or (row1[0]==1 and row1[3]==1):
			row1[0]=5 ; row1[3]=5
			if StringOut == '':
				StringOut="A'BD'"
			else:
				StringOut+= " OR A'BD'"
				


		if (row2[0]==5 and row2[3]==1) or (row2[0]==1 and row2[3]==5) or (row2[0]==1 and row2[3]==1):
			row2[0]=5 ; row2[3]=5
			if StringOut == '':
				StringOut="ABD'"
			else:
				StringOut+= " OR ABD'"
				


		if (row3[0]==5 and row3[3]==1) or (row3[0]==1 and row3[3]==5) or (row3[0]==1 and row3[3]==1):
			row3[0]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="AB'D'"
			else:
				StringOut+= " OR AB'D'"
				

		## 4 col wale


		if (row0[0]==5 and row3[0]==1) or (row0[0]==1 and row3[0]==5) or (row0[0]==1 and row3[0]==1):
			row0[0]=5 ; row3[0]=5
			if StringOut == '':
				StringOut="B'C'D'"
			else:
				StringOut+= " OR B'C'D'"
				


		if (row0[1]==5 and row3[1]==1) or (row0[1]==1 and row3[1]==5) or (row0[1]==1 and row3[1]==1):
			row0[1]=5 ; row3[1]=5
			if StringOut == '':
				StringOut="B'C'D"
			else:
				StringOut+= " OR B'C'D"
				


		if (row0[2]==5 and row3[2]==1) or (row0[2]==1 and row3[2]==5) or (row0[2]==1 and row3[2]==1):
			row0[2]=5 ; row3[2]=5
			if StringOut == '':
				StringOut="B'CD"
			else:
				StringOut+= " OR B'CD"
				


		if (row0[3]==5 and row3[3]==1) or (row0[3]==1 and row3[3]==5) or (row0[3]==1 and row3[3]==1):
			row0[3]=5 ; row3[3]=5
			if StringOut == '':
				StringOut="B'CD'"
			else:
				StringOut+= " OR B'CD'"
				


		###  individual


		if q1.find('0') != -1 and row0[0]==1:
			if StringOut == '':
				StringOut="A'B'C'D'"
			else:
				StringOut+= " OR A'B'C'D'"

		if q1.find('1') != -1 and row0[1]==1:
			if StringOut == '':
				StringOut="A'B'C'D"
			else:
				StringOut+= " OR A'B'C'D"

		if q1.find('2') != -1 and row0[3]==1:
			if StringOut == '':
				StringOut="A'B'CD'"
			else:
				StringOut+= " OR A'B'CD'"

		if q1.find('3') != -1 and row0[2]==1:
			if StringOut == '':
				StringOut="A'B'CD"
			else:
				StringOut+= " OR A'B'CD"

		####

		if q1.find('4') != -1 and row1[0]==1:
			if StringOut == '':
				StringOut="A'BC'D'"
			else:
				StringOut+= " OR A'BC'D'"

		if q1.find('5') != -1 and row1[1]==1:
			if StringOut == '':
				StringOut="A'BC'D"
			else:
				StringOut+= " OR A'BC'D"

		if q1.find('6') != -1 and row1[3]==1:
			if StringOut == '':
				StringOut="A'BCD'"
			else:
				StringOut+= " OR A'BCD'"

		if q1.find('7') != -1 and row1[2]==1:
			if StringOut == '':
				StringOut="A'BCD"
			else:
				StringOut+= " OR A'BCD"

		####

		if q1.find('8') != -1 and row3[0]==1:
			if StringOut == '':
				StringOut="AB'C'D'"
			else:
				StringOut+= " OR AB'C'D'"
		 
		if q1.find('9') != -1 and row3[1]==1:
			if StringOut == '':
				StringOut="AB'C'D"
			else:
				StringOut+= " OR AB'C'D"

		if q1.find('10') != -1 and row3[3]==1:
			if StringOut == '':
				StringOut="AB'CD'"
			else:
				StringOut+= " OR AB'CD'"

		if q1.find('11') != -1 and row3[2]==1:
			if StringOut == '':
				StringOut="AB'CD"
			else:
				StringOut+= " OR AB'CD"

		####

		if q1.find('12') != -1 and row2[0]==1:
			if StringOut == '':
				StringOut="ABC'D'"
			else:
				StringOut+= " OR ABC'D'"

		if q1.find('13') != -1 and row2[1]==1:
			if StringOut == '':
				StringOut="ABC'D"
			else:
				StringOut+= " OR ABC'D"

		if q1.find('14') != -1 and row2[3]==1:
			if StringOut == '':
				StringOut="ABCD'"
			else:
				StringOut+= " OR ABCD'"

		if q1.find('15') != -1 and row2[2]==1:
			if StringOut == '':
				StringOut="ABCD"
			else:
				StringOut+= " OR ABCD"

	
	#### for 3 variable

	elif numVar==3:
		q1=q

		min_terms=[]
		dc=[]

		min_terms=q.split(',')
		dc=w.split(',')

		StringOut=''

		a=[[0,0,0,0],[0,0,0,0]]


		for x in range(len(min_terms)):
			if min_terms[x]=='0':
				q=a[0]
				q[0]=1

			elif min_terms[x]=='1':
				q=a[0]
				q[1]=1
				

			elif min_terms[x]=='2':
				q=a[0]
				q[3]=1
				

			elif min_terms[x]=='3':
				q=a[0]
				q[2]=1
				

			elif min_terms[x]=='4':
				q=a[1]
				q[0]=1
				

			elif min_terms[x]=='5':
				q=a[1]
				q[1]=1
				

			elif min_terms[x]=='6':
				q=a[1]
				q[3]=1
				

			else:
				q=a[1]
				q[2]=1




		for x in range(len(dc)):
			if dc[x]=='0':
				q=a[0]
				q[0]=5

			elif dc[x]=='1':
				q=a[0]
				q[1]=5
				

			elif dc[x]=='2':
				q=a[0]
				q[3]=5
				

			elif dc[x]=='3':
				q=a[0]
				q[2]=5
				

			elif dc[x]=='4':
				q=a[1]
				q[0]=5
				

			elif dc[x]=='5':
				q=a[1]
				q[1]=5
				

			elif dc[x]=='6':
				q=a[1]
				q[3]=5
				

			elif dc[x]=='7':
				q=a[1]
				q[2]=5
				
			else:
				a=a


		# OCTET WALA

		# all 1

		count=0

		for i in a:
			for j in i:
				if j==1:
					count+=1

		if count==8:
			StringOut=1



		#  QUAD

		row0=[]
		row1=[]

		row0=a[0]
		row1=a[1]

		#  0 row 

		count_1=0
		count_5=0

		for i in row0:
			if i == 5:
				count_5+=1
			elif i == 1:
				count_1+=1
					
		if count_5 != 4 and count_5+count_1 == 4 :
			row0=[5,5,5,5]
			if StringOut == '':
				StringOut="A'"
			else:
				StringOut+= " OR A'"
						
		# 1 row

		count_1=0
		count_5=0

		for i in row1:
			if i == 5:
				count_5+=1
			elif i == 1:
				count_1+=1
					
		if count_5 != 4 and count_5+count_1 == 4 :
			row1=[5,5,5,5]
			if StringOut == '':
				StringOut="A"
			else:
				StringOut+= " OR A"

		# 3rd type ke quad 

		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		if row0[0]==1:
			count_1+=1
		if row0[1]==5:
			count_5+=1
		if row0[1]==1:
			count_1+=1
		if row1[0]==5:
			count_5+=1
		if row1[0]==1:
			count_1+=1
		if row1[1]==5:
			count_5+=1
		if row1[1]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[0]=5 ; row0[1]=5 ; row1[0]=5 ; row1[1]=5
			if StringOut=='':
				StringOut="C'"
			else:
				StringOut+=" OR C'"
		#################
			
		count_1=0
		count_5=0

		if row0[1]==5:
			count_5+=1
		if row0[1]==1:
			count_1+=1
		if row0[2]==5:
			count_5+=1
		if row0[2]==1:
			count_1+=1
		if row1[1]==5:
			count_5+=1
		if row1[1]==1:
			count_1+=1
		if row1[2]==5:
			count_5+=1
		if row1[2]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[1]=5 ; row0[2]=5 ; row1[1]=5 ; row1[2]=5
			if StringOut=='':
				StringOut="D"
			else:
				StringOut+=" OR D"

		#################

		count_1=0
		count_5=0

		if row0[2]==5:
			count_5+=1
		if row0[2]==1:
			count_1+=1
		if row0[3]==5:
			count_5+=1
		if row0[3]==1:
			count_1+=1
		if row1[2]==5:
			count_5+=1
		if row1[2]==1:
			count_1+=1
		if row1[3]==5:
			count_5+=1
		if row1[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[2]=5 ; row0[3]=5 ; row1[2]=5 ; row1[3]=5
			if StringOut=='':
				StringOut="C"
			else:
				StringOut+=" OR C"


		##############



		count_1=0
		count_5=0

		if row0[0]==5:
			count_5+=1
		if row0[0]==1:
			count_1+=1
		if row1[0]==5:
			count_5+=1
		if row1[0]==1:
			count_1+=1
		if row0[3]==5:
			count_5+=1
		if row0[3]==1:
			count_1+=1
		if row1[3]==5:
			count_5+=1
		if row1[3]==1:
			count_1+=1				
		else:
			count_1=count_1

		if count_5 != 4 and (count_5+count_1) == 4:
			row0[0]=5 ; row0[3]=5 ; row1[0]=5 ; row1[3]=5
			if StringOut=='':
				StringOut="D'"
			else:
				StringOut+=" OR D'"



		#  DUALS 

		## row 0

		if (row0[0]==5 and row0[1]==1) or (row0[0]==1 and row0[1]==5) or (row0[0]==1 and row0[1]==1):
			row0[0]=5 ; row0[1]=5
			if StringOut=='':
				StringOut="A'C'"
			else:
				StringOut+=" OR A'C'"


		if (row0[1]==5 and row0[2]==1) or (row0[1]==1 and row0[2]==5) or (row0[1]==1 and row0[2]==1):
			row0[1]=5 ; row0[2]=5
			if StringOut=='':
				StringOut="A'D"
			else:
				StringOut+=" OR A'D"


		if (row0[2]==5 and row0[3]==1) or (row0[2]==1 and row0[3]==5) or (row0[2]==1 and row0[3]==1):
			row0[2]=5 ; row0[3]=5
			if StringOut=='':
				StringOut="A'C"
			else:
				StringOut+=" OR A'C"


		## row 1

		if (row1[0]==5 and row1[1]==1) or (row1[0]==1 and row1[1]==5) or (row1[0]==1 and row1[1]==1):
			row1[0]=5 ; row1[1]=5
			if StringOut=='':
				StringOut="AC'"
			else:
				StringOut+=" OR AC'"


		if (row1[1]==5 and row1[2]==1) or (row1[1]==1 and row1[2]==5) or (row1[1]==1 and row1[2]==1):
			row1[1]=5 ; row1[2]=5
			if StringOut=='':
				StringOut="AD"
			else:
				StringOut+=" OR AD"


		if (row1[2]==5 and row1[3]==1) or (row1[2]==1 and row1[3]==5) or (row1[2]==1 and row1[3]==1):
			row1[2]=5 ; row1[3]=5
			if StringOut=='':
				StringOut="AC"
			else:
				StringOut+=" OR AC"

		########   col 0

		if (row0[0]==5 and row1[0]==1) or (row0[0]==1 and row1[0]==5) or (row0[0]==1 and row1[0]==1):
			row0[0]=5 ; row1[0]=5
			if StringOut=='':
				StringOut="C'D'"
			else:
				StringOut+=" OR C'D'"

		##  col 1


		if (row0[1]==5 and row1[1]==1) or (row0[1]==1 and row1[1]==5) or (row0[1]==1 and row1[1]==1):
			row0[1]=5 ; row1[1]=5
			if StringOut=='':
				StringOut="C'D"
			else:
				StringOut+=" OR C'D"

		##  Col 2

		if (row0[2]==5 and row1[2]==1) or (row0[2]==1 and row1[2]==5) or (row0[2]==1 and row1[2]==1):
			row0[2]=5 ; row1[2]=5
			if StringOut=='':
				StringOut="CD"
			else:
				StringOut+=" OR CD"

		##  col 3

		if (row0[3]==5 and row1[3]==1) or (row0[3]==1 and row1[3]==5) or (row0[3]==1 and row1[3]==1):
			row0[3]=5 ; row1[3]=5
			if StringOut=='':
				StringOut="CD'"
			else:
				StringOut+=" OR CD'"


		## bakki 2

		if (row0[0]==5 and row0[3]==1) or (row0[0]==1 and row0[3]==5) or (row0[0]==1 and row0[3]==1):
			row0[0]=5 ; row0[3]=5
			if StringOut=='':
				StringOut="A'D'"
			else:
				StringOut+=" OR A'D'"


		if (row1[0]==5 and row1[3]==1) or (row1[0]==1 and row1[3]==5) or (row1[0]==1 and row1[3]==1):
			row1[0]=5 ; row1[3]=5
			if StringOut=='':
				StringOut="AD'"
			else:
				StringOut+=" OR AD'"


		###  individual


		if q1.find('0') != -1 and row0[0]==1:
			if StringOut=='':
				StringOut="A'C'D'"
			else:
				StringOut+=" OR A'C'D'"


		if q1.find('1') != -1 and row0[1]==1:
			if StringOut=='':
				StringOut="A'C'D"
			else:
				StringOut+=" OR A'C'D"

		if q1.find('2') != -1 and row0[3]==1:
			if StringOut=='':
				StringOut="A'CD'"
			else:
				StringOut+=" OR A'CD'"

		if q1.find('3') != -1 and row0[2]==1:
			if StringOut=='':
				StringOut="A'CD"
			else:
				StringOut+=" OR A'CD"

		####

		if q1.find('4') != -1 and row1[0]==1:
			if StringOut=='':
				StringOut="AC'D'"
			else:
				StringOut+=" OR AC'D'"

		if q1.find('5') != -1 and row1[1]==1:
			if StringOut=='':
				StringOut="AC'D"
			else:
				StringOut+=" OR AC'D"

		if q1.find('6') != -1 and row1[3]==1:
			if StringOut=='':
				StringOut="ACD'"
			else:
				StringOut+=" OR ACD'"

		if q1.find('7') != -1 and row1[2]==1:
			if StringOut=='':
				StringOut="ACD"
			else:
				StringOut+=" OR ACD"

		
	#####   for 2 variables 

	else:
		
		q1=q

		min_terms=[]
		dc=[]

		min_terms=q.split(',')
		dc=w.split(',')

		StringOut=''

		a=[[0,0],[0,0]]

		for x in range(len(min_terms)):
			if min_terms[x]=='0':
				q=a[0]
				q[0]=1

			elif min_terms[x]=='1':
				q=a[0]
				q[1]=1

			elif min_terms[x]=='2':
				q=a[1]
				q[0]=1
				

			elif min_terms[x]=='3':
				q=a[1]
				q[1]=1

			else:
				a=a


		for x in range(len(dc)):
			if dc[x]=='0':
				q=a[0]
				q[0]=5

			elif dc[x]=='1':
				q=a[0]
				q[1]=5

			elif dc[x]=='2':
				q=a[1]
				q[0]=5
				

			elif dc[x]=='3':
				q=a[1]
				q[1]=5
				

		row0=[]
		row1=[]

		row0=a[0]
		row1=a[1]

		# all 1

		count1=0
		count5=0

		for i in a:
			for j in i:
				if j==1:
					count1+=1
				if j==5:
					count5+=1
		if (count5 != 4) and ((count5 + count1) == 4):
			StringOut='1'
			row0[0]='5' ; row0[1]='5' ; row1[0]='5' ; row1[1]='5'

		#  DUALS 

		## row 0

		if (row0[0]==5 and row0[1]==1) or (row0[0]==1 and row0[1]==5) or (row0[0]==1 and row0[1]==1):
			row0[0]=5 ; row0[1]=5
			if StringOut=='':
				StringOut="A'"
			else:
				StringOut+=" OR A'"

		## row 1

		if (row1[0]==5 and row1[1]==1) or (row1[0]==1 and row1[1]==5) or (row1[0]==1 and row1[1]==1):
			row1[0]=5 ; row1[1]=5
			if StringOut=='':
				StringOut="A"
			else:
				StringOut+=" OR A"

		########   col 0

		if (row0[0]==5 and row1[0]==1) or (row0[0]==1 and row1[0]==5) or (row0[0]==1 and row1[0]==1):
			row0[0]=5 ; row1[0]=5
			if StringOut=='':
				StringOut="B'"
			else:
				StringOut+=" OR B'"

		##  col 1


		if (row0[1]==5 and row1[1]==1) or (row0[1]==1 and row1[1]==5) or (row0[1]==1 and row1[1]==1):
			row0[1]=5 ; row1[1]=5
			if StringOut=='':
				StringOut="B"
			else:
				StringOut+=" OR B"

		###  individual


		if q1.find('0') != -1 and row0[0]==1:
			if StringOut=='':
				StringOut="A'B'"
			else:
				StringOut+=" OR A'B'"

		if q1.find('1') != -1 and row0[1]==1:
			if StringOut=='':
				StringOut="A'B"
			else:
				StringOut+=" OR A'B"

		if q1.find('2') != -1 and row1[0]==1:
			if StringOut=='':
				StringOut="AB'"
			else:
				StringOut+=" OR AB'"

		if q1.find('3') != -1 and row1[1]==1:
			if StringOut=='':
				StringOut="AB"
			else:
				StringOut+=" OR AB"

	return StringOut

    
#### function ends here
