#!/usr/bin/env python3

"""Class that wraps some REST API"""

import requests


class ApiWrapper(object):
    """Class that wraps some REST API"""

    def __init__(self, api_url: str):
        self._api_url = api_url

    def add_user(self, first_name: str, last_name: str) -> str:
        """Adds a new user to the system and returns its ID"""
        params = {'first_name': first_name,
                  'last_name': last_name}
        response = requests.post(self._api_url + '/users', json=params)
        if response.status_code != 201:
            raise RuntimeError

        return response.json()['id']

    def get_user(self, userid: str) -> str:
        """Retrieves a user from the system and returns its Full Name"""
        response = requests.get(self._api_url + '/users/' + userid)
        if response.status_code != 200:
            raise RuntimeError

        return response.json()['first_name'] + ' ' + response.json()['last_name']
