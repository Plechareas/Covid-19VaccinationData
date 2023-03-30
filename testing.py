import unittest
from Main import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(1,3,5,7,13)d(15,9,11)'),"B")
		self.assertEqual(minFunc(2,'(0,1)d(2,3)'),"1")
                
if __name__=='__main__':
	unittest.main()