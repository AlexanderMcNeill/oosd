__author__ = 'mcnear1'


class Account():

    def __init__(self, subject):
        self.subject = subject
        self.feed = []
        self.observers = []
        self.status = ""

        if self.subject is not None:
            self.subject.add_observer(self)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status
        self.update_observers()

    def update(self, new_status):
        self.feed.append(new_status)

    def update_observers(self):
        for o in self.observers:
            o.update(self.status)

    def remove_observer(self, o):
        self.observers.remove(o)

    def add_observer(self, o):
        self.observers.append(o)