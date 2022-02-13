# THIS IS A GENERATED FILE! DO NOT EDIT!
import json
import PythonJSONUtilities
import pydantic
import typing


class OtherTestObject:
    # This is another test object

    # Number of items
    count: int

    def __init__(self, in_count: int):
        self.count = in_count


    # JSON Encoders/Decoders
    @staticmethod
    def to_json(InOtherTestObject: typing.Any):
        if InOtherTestObject == None: return None
        OutOtherTestObjectJSON: PythonJSONUtilities.JsonUtilities = PythonJSONUtilities.JsonUtilities()

        OutOtherTestObjectJSON.set_integer_field("count", InOtherTestObject.count)
        return OutOtherTestObjectJSON


    @staticmethod
    def from_json(InOtherTestObjectJSON: PythonJSONUtilities.JsonUtilities):
        if InOtherTestObjectJSON == None: return None

        return OtherTestObject(InOtherTestObjectJSON.get_integer_field("count"))



