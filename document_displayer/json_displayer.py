__author__ = 'alexmcneill'

import json


class JsonDisplayer(json.JSONDecoder):

    def convert_document(self, doc):
        self.decode(doc)