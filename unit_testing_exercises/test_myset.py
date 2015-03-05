import unittest
import myset

class TestMySet(unittest.TestCase):
    
    def setup(self):
    	items = ["hi", "there", "tom"]
    	self.myset = myset.MySet(items)
    	if(self.myset == None):
    		raise(Exception("Null"))

    def test_constructor(self):
    	incorrectItems = ["hi", "hi", "there", "tom"]


    def test_add_item(self):
    	#adding item and making sure that is added
    	newItem = "howdy"
    	expected_new_size = len(self.myset.myset) + 1
    	self.myset.add_item(newItem)

    	self.assertEqual(len(self.myset.set), expected_new_size)

    	#adding the same item again making sure that it is'nt added again
    	self.myset.add_item(newItem)

    	self.assertEqual(len(self.myset.myset), expected_new_size)

    def test_remove_item(self):
    	pass

    def test_is_empty(self):
    	pass

    def test_has_item(self):
    	pass

    def test_intersection(self):
    	pass

    def test_union(self):
    	pass

    def test_is_subset_of(self):
    	pass

    def test_is_equal_to(self):
    	pass

    def test_is_proper_subset_of(self):
    	pass



if __name__ == '__main__':
    unittest.main()
