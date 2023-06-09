# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PhysicalAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address_name_part: str=None, address_street_part: str=None, address_town_part: str=None, address_state_part: str=None, address_postcode_part: str=None, address_country_part: str=None):  # noqa: E501
        """PhysicalAddress - a model defined in Swagger

        :param address_name_part: The address_name_part of this PhysicalAddress.  # noqa: E501
        :type address_name_part: str
        :param address_street_part: The address_street_part of this PhysicalAddress.  # noqa: E501
        :type address_street_part: str
        :param address_town_part: The address_town_part of this PhysicalAddress.  # noqa: E501
        :type address_town_part: str
        :param address_state_part: The address_state_part of this PhysicalAddress.  # noqa: E501
        :type address_state_part: str
        :param address_postcode_part: The address_postcode_part of this PhysicalAddress.  # noqa: E501
        :type address_postcode_part: str
        :param address_country_part: The address_country_part of this PhysicalAddress.  # noqa: E501
        :type address_country_part: str
        """
        self.swagger_types = {
            'address_name_part': str,
            'address_street_part': str,
            'address_town_part': str,
            'address_state_part': str,
            'address_postcode_part': str,
            'address_country_part': str
        }

        self.attribute_map = {
            'address_name_part': 'addressNamePart',
            'address_street_part': 'addressStreetPart',
            'address_town_part': 'addressTownPart',
            'address_state_part': 'addressStatePart',
            'address_postcode_part': 'addressPostcodePart',
            'address_country_part': 'addressCountryPart'
        }
        self._address_name_part = address_name_part
        self._address_street_part = address_street_part
        self._address_town_part = address_town_part
        self._address_state_part = address_state_part
        self._address_postcode_part = address_postcode_part
        self._address_country_part = address_country_part

    @classmethod
    def from_dict(cls, dikt) -> 'PhysicalAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The physicalAddress of this PhysicalAddress.  # noqa: E501
        :rtype: PhysicalAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_name_part(self) -> str:
        """Gets the address_name_part of this PhysicalAddress.

        The part of the address that is descriptive of the name of the property  # noqa: E501

        :return: The address_name_part of this PhysicalAddress.
        :rtype: str
        """
        return self._address_name_part

    @address_name_part.setter
    def address_name_part(self, address_name_part: str):
        """Sets the address_name_part of this PhysicalAddress.

        The part of the address that is descriptive of the name of the property  # noqa: E501

        :param address_name_part: The address_name_part of this PhysicalAddress.
        :type address_name_part: str
        """

        self._address_name_part = address_name_part

    @property
    def address_street_part(self) -> str:
        """Gets the address_street_part of this PhysicalAddress.

        The part of the address where we talk about the street  # noqa: E501

        :return: The address_street_part of this PhysicalAddress.
        :rtype: str
        """
        return self._address_street_part

    @address_street_part.setter
    def address_street_part(self, address_street_part: str):
        """Sets the address_street_part of this PhysicalAddress.

        The part of the address where we talk about the street  # noqa: E501

        :param address_street_part: The address_street_part of this PhysicalAddress.
        :type address_street_part: str
        """

        self._address_street_part = address_street_part

    @property
    def address_town_part(self) -> str:
        """Gets the address_town_part of this PhysicalAddress.

        The part of the address that refers to the suburb or town  # noqa: E501

        :return: The address_town_part of this PhysicalAddress.
        :rtype: str
        """
        return self._address_town_part

    @address_town_part.setter
    def address_town_part(self, address_town_part: str):
        """Sets the address_town_part of this PhysicalAddress.

        The part of the address that refers to the suburb or town  # noqa: E501

        :param address_town_part: The address_town_part of this PhysicalAddress.
        :type address_town_part: str
        """

        self._address_town_part = address_town_part

    @property
    def address_state_part(self) -> str:
        """Gets the address_state_part of this PhysicalAddress.

        The part of the address that refers to the state, or territory, or province, or county, or jangwat, etcetera  # noqa: E501

        :return: The address_state_part of this PhysicalAddress.
        :rtype: str
        """
        return self._address_state_part

    @address_state_part.setter
    def address_state_part(self, address_state_part: str):
        """Sets the address_state_part of this PhysicalAddress.

        The part of the address that refers to the state, or territory, or province, or county, or jangwat, etcetera  # noqa: E501

        :param address_state_part: The address_state_part of this PhysicalAddress.
        :type address_state_part: str
        """

        self._address_state_part = address_state_part

    @property
    def address_postcode_part(self) -> str:
        """Gets the address_postcode_part of this PhysicalAddress.

        I think we all know what a postcode is.  The Yanks, of course, will call it something else.  # noqa: E501

        :return: The address_postcode_part of this PhysicalAddress.
        :rtype: str
        """
        return self._address_postcode_part

    @address_postcode_part.setter
    def address_postcode_part(self, address_postcode_part: str):
        """Sets the address_postcode_part of this PhysicalAddress.

        I think we all know what a postcode is.  The Yanks, of course, will call it something else.  # noqa: E501

        :param address_postcode_part: The address_postcode_part of this PhysicalAddress.
        :type address_postcode_part: str
        """

        self._address_postcode_part = address_postcode_part

    @property
    def address_country_part(self) -> str:
        """Gets the address_country_part of this PhysicalAddress.

        The part of the address that specifies the country  # noqa: E501

        :return: The address_country_part of this PhysicalAddress.
        :rtype: str
        """
        return self._address_country_part

    @address_country_part.setter
    def address_country_part(self, address_country_part: str):
        """Sets the address_country_part of this PhysicalAddress.

        The part of the address that specifies the country  # noqa: E501

        :param address_country_part: The address_country_part of this PhysicalAddress.
        :type address_country_part: str
        """

        self._address_country_part = address_country_part
