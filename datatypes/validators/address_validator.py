from voluptuous import Required, Optional, All, Length
from datatypes.core import DictionaryValidator
from datatypes.validators import postcode_validator, iso_country_code_validator

address_schema = {
    Required('line_one'): All(str, Length(max=40)),
    Optional('line_two'): All(str, Length(max=40)),
    Optional('line_three'): All(str, Length(max=40)),
    Optional('line_four'): All(str, Length(max=40)),
    Required('city'): All(str, Length(max=40)),
    Required('postcode'): postcode_validator.postcode_schema,
    Required('country'): iso_country_code_validator.country_schema
}

error_dictionary = {
    'line_one': 'line_one is a required string field and must be a maximum of 40 characters long'
}


class Address(DictionaryValidator):
    def define_schema(self):
        return address_schema

    def define_error_dictionary(self):
        return error_dictionary