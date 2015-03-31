__author__ = 'alexmcneill'

class YamlDisplayer():

    def convert_document(self, doc):
        return self.convert_to_xml(doc)

    def convert_to_xml(self, doc):
        output =""
        for key, value in doc.items():
            output += "\n" + key + ":"

            if isinstance(value, list):
                output += self.get_items(value, key)
            elif isinstance(value, dict):
                output += self.convert_to_xml(value)
            else:
                output += value

        return output

    def get_items(self, items, parent_name):
        output = ""

        for i in items:
            output += "\n     " + i

        return output;