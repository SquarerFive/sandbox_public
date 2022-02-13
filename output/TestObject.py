# THIS IS A GENERATED FILE! DO NOT EDIT!
import json
import PythonJSONUtilities
import pydantic
import typing
from OtherTestObject import *

class VARIABLED:
    ABC: str = "ABC"
    XYZ: str = "XYZ"


class VARIABLEE:
    LOW: int = 2
    HIGH: int = 4


class TestObject:
    # This is a test object

    # This property represents an integer. It is not
    # required
    variableA: int = 24

    # This property is a string. It is required
    variableB: str

    # This is an object variable
    variableC: OtherTestObject

    # enum-like value
    variableD: str = VARIABLED.ABC

    # enum-like value int
    variableE: int = VARIABLEE.LOW

    # This is an array of integers
    arrayVariable: typing.List[int]

    # This is an array of arrays of integers
    arrayOfArrays: typing.List[typing.List[int]]

    # This is an array of objects
    arrayOfObjects: typing.List[OtherTestObject]

    def __init__(self, in_variableB: str, in_variableC: OtherTestObject, in_arrayVariable: typing.List[int], in_arrayOfArrays: typing.List[typing.List[int]], in_arrayOfObjects: typing.List[OtherTestObject], in_variableA: int = 24, in_variableD: str = VARIABLED.ABC, in_variableE: int = VARIABLEE.LOW):
        self.variableB = in_variableB
        self.variableC = in_variableC
        self.arrayVariable = in_arrayVariable
        self.arrayOfArrays = in_arrayOfArrays
        self.arrayOfObjects = in_arrayOfObjects
        self.variableA = in_variableA
        self.variableD = in_variableD
        self.variableE = in_variableE

        self.validate()


    # JSON Encoders/Decoders
    @staticmethod
    def to_json(InTestObject: typing.Any):
        if InTestObject == None: return None
        OutTestObjectJSON: PythonJSONUtilities.JsonUtilities = PythonJSONUtilities.JsonUtilities()

        OutTestObjectJSON.set_integer_field("variableA", InTestObject.variableA)
        OutTestObjectJSON.set_string_field("variableB", InTestObject.variableB)
        OutTestObjectJSON.set_object_field("variableC", OtherTestObject.to_json(InTestObject.variableC))
        OutTestObjectJSON.set_string_field("variableD", InTestObject.variableD)
        OutTestObjectJSON.set_integer_field("variableE", InTestObject.variableE)
        OutTestObjectJSON.set_array_field("arrayVariable", InTestObject.arrayVariable)
        OutTestObjectJSON.set_array_field("arrayOfArrays", InTestObject.arrayOfArrays)
        OutTestObjectJSON.set_array_field("arrayOfObjects", InTestObject.arrayOfObjects)
        return OutTestObjectJSON


    @staticmethod
    def from_json(InTestObjectJSON: PythonJSONUtilities.JsonUtilities):
        if InTestObjectJSON == None: return None

        return TestObject(InTestObjectJSON.get_string_field("variableB"),
             OtherTestObject.from_json(InTestObjectJSON.get_object_field("variableC")),
             InTestObjectJSON.get_array_field("arrayVariable"),
             InTestObjectJSON.get_array_field("arrayOfArrays"),
             InTestObjectJSON.get_array_field("arrayOfObjects"),
             InTestObjectJSON.get_integer_field("variableA"),
             InTestObjectJSON.get_string_field("variableD"),
             InTestObjectJSON.get_integer_field("variableE"))


    def validate(self, ):
        if ( not (self.variableD == VARIABLED.ABC or self.variableD == VARIABLED.XYZ)):
            raise ValueError("Failed to validate field variableD!")

        if ( not (self.variableE == VARIABLEE.LOW or self.variableE == VARIABLEE.HIGH)):
            raise ValueError("Failed to validate field variableE!")




