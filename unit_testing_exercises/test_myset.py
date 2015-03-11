import unittest
import myset


class TestMySet(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructor(self):
        incorrectItems = ["hi", "hi", "there", "tom"]
        correctItems = ["hi", "there", "tom"]

        test_set = myset.MySet(correctItems)

        self.assertEqual(test_set.get_size(), len(correctItems))

        test_set = myset.MySet(incorrectItems)

        self.assertEqual(test_set.get_size(), len(correctItems))

    def test_add_item(self):
        correctItems = ["hi", "there", "tom"]
        test_set = myset.MySet(correctItems)

        new_item = "howdy"
        expected_new_size = len(test_set.set) + 1

        test_set.add_item(new_item)
        self.assertEqual(len(test_set.set), expected_new_size)

        test_set.add_item(new_item)
        self.assertEqual(len(test_set.set), expected_new_size)

    def test_remove_item(self):
        items = ["hi", "there", "tom"]
        correctSize = len(items) - 1
        test_set = myset.MySet(items)

        test_set.remove_item("hi")

        self.assertEqual(test_set.get_size(), correctSize)

        test_set.remove_item("hi")

        self.assertEqual(test_set.get_size(), correctSize)

    def test_is_empty(self):
        test_set = myset.MySet(None)

        self.assertEqual(test_set.is_empty(), True)

        test_set.add_item("Test")

        self.assertEqual(test_set.is_empty(), False)

    def test_has_item(self):
        items = ["hi", "there", "tom"]
        test_set = myset.MySet(items)

        self.assertEqual(test_set.has_item("hi"), True);
        self.assertEqual(test_set.has_item("alex"), False);

    def test_intersection(self):
        pass

    def test_union(self):
        pass

    def test_is_subset_of(self):
        pass

    def test_is_equal_to(self):
        items = ["hi", "there", "tom"]
        test_set = myset.MySet(items)

        self.assertEqual(test_set.is_equal_to(items), True);

        items.append("Test")
        self.assertEqual(test_set.is_equal_to(items), False);

    def test_is_proper_subset_of(self):
        pass


if __name__ == '__main__':
    unittest.main()
