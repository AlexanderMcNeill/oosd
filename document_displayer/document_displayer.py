__author__ = 'alexmcneill'

import displayer_factory


test_case = {'name': 'Alex',
             'role': 'student',
             'hobbies': ['Programming', 'Gaming', 'Sleeping'],
             'favorite_beer': {'brewer': 'Rodenbach', 'beer': 'Grand Cro'}}

factory = displayer_factory.DisplayerFacory()

displayer = factory.create_json()

print(displayer.convert_document(test_case))

displayer = factory.create_xml()

print(displayer.convert_document(test_case))

displayer = factory.create_yaml()

print(displayer.convert_document(test_case))
