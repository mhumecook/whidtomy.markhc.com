# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.home import Home  # noqa: E501
from swagger_server.models.particle import Particle  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCurrentHomeController(BaseTestCase):
    """CurrentHomeController integration test stubs"""

    def test_create_current_home(self):
        """Test case for create_current_home

        Create the default home
        """
        body = Home()
        response = self.client.open(
            '/home',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_particle(self):
        """Test case for create_particle

        Create a particle in the home
        """
        body = Particle()
        response = self.client.open(
            '/home/particles',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_particles(self):
        """Test case for get_all_particles

        Retrieve the particles of the home
        """
        response = self.client.open(
            '/home/particles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_current_home(self):
        """Test case for get_current_home

        Retrieve information about the home
        """
        response = self.client.open(
            '/home',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_particle_with_id(self):
        """Test case for get_particle_with_id

        Retrieve a given particle of the home
        """
        response = self.client.open(
            '/home/particles/{particleId}'.format(particle_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_particle_with_id(self):
        """Test case for update_particle_with_id

        Update a particle in the home
        """
        body = Particle()
        response = self.client.open(
            '/home/particles',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
