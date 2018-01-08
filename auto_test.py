#!/usr/bin/env python
import os
import unittest
import json
# import rdflib
from os.path import join, dirname
from app import app

class SingleSiteViewTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client() 
        # cvf = json.load(open(join(dirname(__file__), 'controller/views_formats.json')))
        # Get root register information from 'localhost/minimal/register'. After project finish, this should be changed to 'localhost/minimal'
        response = self.client.get('/register')
        json_data = json.loads(response.data)[0]
        self.categories = set(json_data.get(json_data.get('default')).get('containedItemClass'))

        self.formats = set(['text/html', 
                            'text/turtle', 
                            'text/ntriples', 
                            'text/nt', 
                            'text/n3', 
                            'application/rdf+xml', 
                            'application/xml',
                            'application/rdf+json', 
                            'application/json', 
                            'abcdef'])

    # def get_instance(self, cls):
    #     # rdf query like %s a cls limit 1
    #     response = self.client.get('/register')
    # def test_register():
    #     response = self.client.get('/register')

    def test_category_register(self):
        for category in self.categories:
            ca = category.split('#')[1].lower()
            with self.subTest(category):
                # from alternates application/json view get JSON style register views and formats info.
                response = self.client.get('/'+ca+'/?_view=alternates&_format=application/json')
                
                self.assertEqual(200, response.status_code)
                self.assertIn('application/json', response.headers.get('Content-Type'))

                # From response json data, get this register supported views and formats, and start test
                # print(response.data)
                data = json.loads(response.data)
                print(data)
                views = data.keys()
                for view in views:
                    if view != 'default' != 'subreg' != 'renderer':
                        formats = data[view]['mimetypes']
                        print(formats)


    def test_category_class(self):
        for category in self.categories:
            ca = category.split('#')[1].lower()
            with self.subTest(category):
                 #access register and pick up an instance
                response = self.client.get('/'+ca+'/?_view=reg&_format=text/turtle')



    # def class_test(self, cls, random_instance):
    #     for key in reg.keys:
    #         if key != 'renderer' != 'default':
    #             # Process views
    #             view = key
    #             mimetypes = reg.get(key).get('mimetypes')
    #             for format in mimetypes:
    #                 response = self.client.get()
    #     pass
    def tearDown(self):
        pass

    def test_nothing(self):
        pass
    # Test unvalid site no
    # def test_unvalid_site_no_view(self):

if __name__ == '__main__':
    unittest.main(verbosity=2)