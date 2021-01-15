# coding: utf-8

"""
    Aerpaw Gateway

    This is Aerpaw gateway service to interact with Emulab  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ericafu@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Userkey(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user': 'str',
        'pubkey': 'str'
    }

    attribute_map = {
        'user': 'user',
        'pubkey': 'pubkey'
    }

    def __init__(self, user=None, pubkey=None):  # noqa: E501
        """Userkey - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._pubkey = None
        self.discriminator = None
        self.user = user
        if pubkey is not None:
            self.pubkey = pubkey

    @property
    def user(self):
        """Gets the user of this Userkey.  # noqa: E501


        :return: The user of this Userkey.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Userkey.


        :param user: The user of this Userkey.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def pubkey(self):
        """Gets the pubkey of this Userkey.  # noqa: E501


        :return: The pubkey of this Userkey.  # noqa: E501
        :rtype: str
        """
        return self._pubkey

    @pubkey.setter
    def pubkey(self, pubkey):
        """Sets the pubkey of this Userkey.


        :param pubkey: The pubkey of this Userkey.  # noqa: E501
        :type: str
        """

        self._pubkey = pubkey

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Userkey, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Userkey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other