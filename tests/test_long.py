import unittest
from apa import LongA

class TestLong(unittest.TestCase):
    def test_mult(self):
        args = [["2","3"], ["222", "333"], ["6767454454524", "2345454124455"]]
        res = ["6", "73926", "15872753962424678033784420"]
        for arg, res in list(zip(args, res)):
            a = LongA(arg[0])
            b = LongA(arg[1])
            res_test = a*b
            res_test = str(res_test)
            self.assertEqual(res, res_test)
    
    def test_add(self):
        args = args = [["2","3"], ["222", "333"], ["67", "23"], ["6767454454524", "2345454124455"]]
        res = ["5", "555", "90", "9112908578979"]
        for arg, res in list(zip(args, res)):
            a = LongA(arg[0])
            b = LongA(arg[1])
            res_test = a+b
            res_test = str(res_test)
            self.assertEqual(res, res_test)
    
    def test_pow(self):
        args = args = [["45","14"], ["22", "33"], ["3", "3"]]
        res = ["139628860198736572265625", "199502557355935975909450298726667414302359552", "27"]
        for arg, res in list(zip(args, res)):
            a = LongA(arg[0])
            b = LongA(arg[1])
            res_test = a**b
            res_test = str(res_test)
            self.assertEqual(res, res_test)
 
#if __name__ == '__main__':
#    unittest.main()