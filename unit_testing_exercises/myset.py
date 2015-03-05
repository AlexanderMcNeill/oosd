class MySet:

    def __init__(self, items):
        """Takes a list of items and builds a set with them, removing
           duplicates if necessary.
        """
        self.myset = []
        self.myset = [self.add_item() for i in items]

    def add_item(self, item):
        """ Adds an item to the set if it is not already present. If the
            item is present, do nothing.
        """

        if item not in self.myset:
            self.myset.append(item)

    def remove_item(self, item):
        """ Removes item from the set.  Does nothing if item is not
            in the set.
        """

        if item in self.set:
            self.myset.remove(item)

    def is_empty(self):
        """Returns True is the set has no members."""
        
        if len(self.set) < 1:
            return True
        else:
            return False

    def has_item(self, item):
        """returns True if item is in the set, False otherwise."""
        
        if item in self.myset:
            return True
        else:
            return False

    def intersection(self, otherset):
        """Returns a new set that is the intersection of self
           and otherset.
           """
        pass

    def union(self, otherset):
        """"Returns a new set that is the union of self and otherset"""
        pass

    def is_subset_of(self, otherset):
        """Returns True if self is a subset of otherset."""
        pass

    def is_equal_to(self, otherset):
        """Returns True if self and otherset are equal, i.e.,
           they have the exact same members.
        """
        pass

    def is_proper_subset_of(self, otherset):
        """Returns True is self is a *proper* subset of otherset."""
        pass
