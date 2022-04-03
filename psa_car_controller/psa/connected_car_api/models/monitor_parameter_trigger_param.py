# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MonitorParameterTriggerParam(object):
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
        'bool_exp': 'str',
        'data_triggers': 'list[DataTrigger]',
        'time_zone_triggers': 'TimeZoneTrigger',
        'triggers': 'list[MonitorTrigger]'
    }

    attribute_map = {
        'bool_exp': 'bool.exp',
        'data_triggers': 'dataTriggers',
        'time_zone_triggers': 'timeZoneTriggers',
        'triggers': 'triggers'
    }

    def __init__(self, bool_exp=None, data_triggers=None, time_zone_triggers=None, triggers=None):  # noqa: E501
        """MonitorParameterTriggerParam - a model defined in Swagger"""  # noqa: E501

        self._bool_exp = None
        self._data_triggers = None
        self._time_zone_triggers = None
        self._triggers = None
        self.discriminator = None

        self.bool_exp = bool_exp
        if data_triggers is not None:
            self.data_triggers = data_triggers
        if time_zone_triggers is not None:
            self.time_zone_triggers = time_zone_triggers
        self.triggers = triggers

    @property
    def bool_exp(self):
        """Gets the bool_exp of this MonitorParameterTriggerParam.  # noqa: E501

        A boolean expression that allow defining a logical relationship between triggers. Used Operands with this expression should only be the names of the defined triggers.   Grammar: ``` exp ::= exp '&' exp        | exp '|' exp        | (exp)        | !exp ```  * **example**: having two-zone trigger (two towns) named z1 an z2, one time-trigger (8h00 to 20h00) named t1 and finally three data triggerd named as follow: f(fuel), a(autonomy) , o(odometer).      we can have a boolean expression such as: : ``` ((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2))) ```   # noqa: E501

        :return: The bool_exp of this MonitorParameterTriggerParam.  # noqa: E501
        :rtype: str
        """
        return self._bool_exp

    @bool_exp.setter
    def bool_exp(self, bool_exp):
        """Sets the bool_exp of this MonitorParameterTriggerParam.

        A boolean expression that allow defining a logical relationship between triggers. Used Operands with this expression should only be the names of the defined triggers.   Grammar: ``` exp ::= exp '&' exp        | exp '|' exp        | (exp)        | !exp ```  * **example**: having two-zone trigger (two towns) named z1 an z2, one time-trigger (8h00 to 20h00) named t1 and finally three data triggerd named as follow: f(fuel), a(autonomy) , o(odometer).      we can have a boolean expression such as: : ``` ((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2))) ```   # noqa: E501

        :param bool_exp: The bool_exp of this MonitorParameterTriggerParam.  # noqa: E501
        :type: str
        """
        if bool_exp is None:
            raise ValueError("Invalid value for `bool_exp`, must not be `None`")  # noqa: E501

        self._bool_exp = bool_exp

    @property
    def data_triggers(self):
        """Gets the data_triggers of this MonitorParameterTriggerParam.  # noqa: E501

        Compound data triggers (will be evaluated with an AND relationship)  *Note*: ```dataTriggers``` is depricated according the new monitor spec. Please use the new data schema.   # noqa: E501

        :return: The data_triggers of this MonitorParameterTriggerParam.  # noqa: E501
        :rtype: list[DataTrigger]
        """
        return self._data_triggers

    @data_triggers.setter
    def data_triggers(self, data_triggers):
        """Sets the data_triggers of this MonitorParameterTriggerParam.

        Compound data triggers (will be evaluated with an AND relationship)  *Note*: ```dataTriggers``` is depricated according the new monitor spec. Please use the new data schema.   # noqa: E501

        :param data_triggers: The data_triggers of this MonitorParameterTriggerParam.  # noqa: E501
        :type: list[DataTrigger]
        """

        self._data_triggers = data_triggers

    @property
    def time_zone_triggers(self):
        """Gets the time_zone_triggers of this MonitorParameterTriggerParam.  # noqa: E501


        :return: The time_zone_triggers of this MonitorParameterTriggerParam.  # noqa: E501
        :rtype: TimeZoneTrigger
        """
        return self._time_zone_triggers

    @time_zone_triggers.setter
    def time_zone_triggers(self, time_zone_triggers):
        """Sets the time_zone_triggers of this MonitorParameterTriggerParam.


        :param time_zone_triggers: The time_zone_triggers of this MonitorParameterTriggerParam.  # noqa: E501
        :type: TimeZoneTrigger
        """

        self._time_zone_triggers = time_zone_triggers

    @property
    def triggers(self):
        """Gets the triggers of this MonitorParameterTriggerParam.  # noqa: E501

        Compound monitor triggers (will be evaluated using boolean expresion :```boo.exp```)   # noqa: E501

        :return: The triggers of this MonitorParameterTriggerParam.  # noqa: E501
        :rtype: list[MonitorTrigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this MonitorParameterTriggerParam.

        Compound monitor triggers (will be evaluated using boolean expresion :```boo.exp```)   # noqa: E501

        :param triggers: The triggers of this MonitorParameterTriggerParam.  # noqa: E501
        :type: list[MonitorTrigger]
        """
        if triggers is None:
            raise ValueError("Invalid value for `triggers`, must not be `None`")  # noqa: E501

        self._triggers = triggers

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
        if issubclass(MonitorParameterTriggerParam, dict):
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
        if not isinstance(other, MonitorParameterTriggerParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other