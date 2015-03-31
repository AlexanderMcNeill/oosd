__author__ = 'alexmcneill'

import json_displayer
import xml_displayer
import yaml_displayer

class DisplayerFacory():

    def get_displayer(self, type):
        displayer_switch = {'xml': self.create_xml, 'yaml': self.create_yaml, 'json': self.create_json}

        return displayer_switch[type]()

    def create_xml(self):
        return xml_displayer.XmlDisplayer()

    def create_yaml(self):
        return yaml_displayer.YamlDisplayer()

    def create_json(self):
        return json_displayer.JsonDisplayer()