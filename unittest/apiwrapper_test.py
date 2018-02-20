#!/usr/bin/env python3

"""Unit tests for ApiWrapper"""

import unittest
import requests_mock

from apiwrapper import ApiWrapper

API_URL = 'http://example.com'


@requests_mock.mock()
class ApiWrapperTest(unittest.TestCase):
    """Tests ApiWrapper"""

    def test_add_user(self, mock):
        wrapper = ApiWrapper(API_URL)

        mock.post(API_URL + '/users', status_code=401)
        with self.assertRaises(RuntimeError):
            wrapper.add_user('The', 'User')

        mock.post(API_URL + '/users', text='{"id": "1234"}', status_code=201)
        self.assertEqual('1234', wrapper.add_user('The', 'User'))

    def test_get_user(self, mock):
        wrapper = ApiWrapper(API_URL)

        mock.get(API_URL + '/users/1234', status_code=401)
        with self.assertRaises(RuntimeError):
            wrapper.get_user('1234')

        mock.get(API_URL + '/users/1234',
                 text='{"first_name": "The", "last_name": "User"}', status_code=200)
        self.assertEqual('The User', wrapper.get_user('1234'))


if __name__ == '__main__':
    unittest.main()
