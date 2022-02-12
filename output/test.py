# THIS IS A GENERATED FILE! DO NOT EDIT!
import json
import PythonJSONUtilities
import pydantic
import typing


class OtherTestObject :


    # [[GENERATED_OBJECT]] This is another test object

    def __init__(self, In_count: int) :
        self.count = In_count



    # Number of items
    count: int

    # JSON Encoders/Decoders
    @staticmethod
    def to_json(InOtherTestObject: typing.Any) :
        if InOtherTestObject == None: return None
        OutOtherTestObjectJSON: PythonJSONUtilities.JsonUtilities = PythonJSONUtilities.JsonUtilities()

        OutOtherTestObjectJSON.set_integer_field("count", InOtherTestObject.count)
        return OutOtherTestObjectJSON


    @staticmethod
    def from_json(InOtherTestObjectJSON: PythonJSONUtilities.JsonUtilities) :
        if InOtherTestObjectJSON == None: return None

        return OtherTestObject(InOtherTestObjectJSON.get_integer_field("count"))



class TestObject :


    # [[GENERATED_OBJECT]] This is a test object

    def __init__(self, In_variableB: str, In_variableC: OtherTestObject, In_variableD: str, In_variableE: int, In_variableA: int = 24) :
        self.variableB = In_variableB
        self.variableC = In_variableC
        self.variableD = In_variableD
        self.variableE = In_variableE
        self.variableA = In_variableA



    class VARIABLED :

        ABC: str = "ABC"
        XYZ: str = "XYZ"


    class VARIABLEE :

        LOW: int = 2
        HIGH: int = 4


    # This property represents an integer. It is not
    # required
    variableA: int = 24

    # This property is a string. It is required
    variableB: str

    # This is an object variable
    variableC: OtherTestObject

    # enum-like value
    variableD: str

    # enum-like value int
    variableE: int

    # JSON Encoders/Decoders
    @staticmethod
    def to_json(InTestObject: typing.Any) :
        if InTestObject == None: return None
        OutTestObjectJSON: PythonJSONUtilities.JsonUtilities = PythonJSONUtilities.JsonUtilities()

        OutTestObjectJSON.set_integer_field("variableA", InTestObject.variableA)
        OutTestObjectJSON.set_string_field("variableB", InTestObject.variableB)
        OutTestObjectJSON.set_object_field("variableC", OtherTestObject.to_json(InTestObject.variableC))
        OutTestObjectJSON.set_string_field("variableD", InTestObject.variableD)
        OutTestObjectJSON.set_integer_field("variableE", InTestObject.variableE)
        return OutTestObjectJSON


    @staticmethod
    def from_json(InTestObjectJSON: PythonJSONUtilities.JsonUtilities) :
        if InTestObjectJSON == None: return None

        return TestObject(InTestObjectJSON.get_string_field("variableB"),
         OtherTestObject.from_json(InTestObjectJSON.get_object_field("variableC")),
         InTestObjectJSON.get_string_field("variableD"),
         InTestObjectJSON.get_integer_field("variableE"),
         InTestObjectJSON.get_integer_field("variableA"))



