__author__ = 'alexmcneill'


class XmlDisplayer():

    def convert_document(self, doc):
        return self.convert_to_xml(doc)

    def convert_to_xml(self, doc):
        output = ""
        for key, value in doc.items():
            output += "\n<" + key + ">"

            if isinstance(value, list):
                output += self.get_items(value, key)
            elif isinstance(value, dict):
                output += self.convert_to_xml(value)
            else:
                output += "\n   " + value

            output += "\n</" + key + ">"

        return output

    def get_items(self, items, parent_name):
        output = ""

        for i in items:
            output += "\n<" + parent_name + "_Item>"
            output += "\n" + i
            output += "\n</" + parent_name + "_Item>"

        return output;