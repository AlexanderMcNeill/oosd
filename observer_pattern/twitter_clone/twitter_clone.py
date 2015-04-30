__author__ = 'mcnear1'

import sys
import time
from PyQt4 import QtCore, QtGui, uic
import twitter_account

qtCreatorFile = "twitterClone.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class TwitterApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.subject_account = twitter_account.Account(None)
        self.follower_one = twitter_account.Account(self.subject_account)
        self.follower_two = twitter_account.Account(self.subject_account)
        self.txtInput.editingFinished.connect(self.update_followers)

    def update_followers(self):
        new_status = time.strftime("%H:%M:%S") + ": " + self.txtInput.text()
        self.subject_account.status = new_status
        self.subject_account.update_observers()

        self.fill_feed(self.txtAccountOne, self.follower_one)
        self.fill_feed(self.txtAccountTwo, self.follower_two)



    def fill_feed(self, feed_text_edit, account):
        feed_text_edit.setText("")
        for message in account.feed:
            feed_text_edit.append(message + "\n")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = TwitterApp()
    window.show()
    sys.exit(app.exec_())