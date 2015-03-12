class MySet:

    def __init__(self, items):
        """Takes a list of items and builds a set with them, removing
           duplicates if necessary.
        """
        self.set = []

        if items != None:
            for i in items:
                 self.add_item(i)

    def add_item(self, item):
        """ Adds an item to the set if it is not already present. If the
            item is present, do nothing.
        """
        if item not in set:
            set.append(item)

    def remove_item(self, item):
        """ Removes item from the set.  Does nothing if item is not
            in the set.
        """
        if item in self.set:
            self.set.remove(item)

    def is_empty(self):
        """Returns True is the set has no members."""
        if len(self.set) < 1:
            return True
        else:
            return False

    def has_item(self, item):
        """returns True if item is in the set, False otherwise."""
        if item in self.set:
            return True
        else:
            return False

    def intersection(self, otherset):
        """Returns a new set that is the intersection of self
           and otherset.
           """
        intersectionSet = []

        for i in otherset:
            if i in self.set:
                intersectionSet.append(i)

        return intersectionSet

    def union(self, otherset):
        """"Returns a new set that is the union of self and otherset"""
        output = MySet(None)

        for i in otherset:
            output.add_item(i)

        for i in self.set:
            output.add_item(i)

        return otherset

    def is_subset_of(self, otherset):
        """Returns True if self is a subset of otherset."""
        output = True

        if len(otherset) < len(self.set):
            output = False
        else:
            count = 0

            while count < len(self.set) and output is True:
                if self.set[count] not in otherset:
                    output = False

                count += 1

        return output

    def is_equal_to(self, otherset):
        """Returns True if self and otherset are equal, i.e.,
           they have the exact same members.
        """
        output = True

        if len(otherset) != len(self.set):
            output = False
        else:
            count = 0
            while count < len(self.set) and output is True:
                if self.set[count] not in otherset:
                    output = False

                count += 1

        return output

    def is_proper_subset_of(self, otherset):
        """Returns True is self is a *proper* subset of otherset."""
        pass

    def get_size(self):
        return len(self.set)
