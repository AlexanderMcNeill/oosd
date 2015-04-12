__author__ = 'alexmcneill'
import waiting_state


class VendingMachine:

    def __init__(self):
        self.state = waiting_state.WaitingState()