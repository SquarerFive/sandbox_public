# THIS IS A GENERATED FILE! DO NOT EDIT!
import json


class OtherTestObject :


    # [[GENERATED_OBJECT]] This is another test object

    def __init__(self, Incount: int) :
        count = Incount



    # Number of items
    count: int

    # JSON Encoders/Decoders
    @staticmethod
    def ToJSON(InOtherTestObject: OtherTestObject) :
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InOtherTestObject)
        OutOtherTestObjectJSON: TSharedPtr<FJsonObject> = MakeShareable(new FJsonObject)

        UJson::SetIntegerField(OutOtherTestObjectJSON,"count", InOtherTestObject.count)
        return OutOtherTestObjectJSON


    @staticmethod
    def FromJSON(InOtherTestObjectJSON: TSharedPtr<FJsonObject>) :
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InOtherTestObjectJSON)

        return def __init__(self,
         UJson::GetIntegerFieldOpt(InOtherTestObjectJSON,"count"))



class TestObject :


    # [[GENERATED_OBJECT]] This is a test object

    def __init__(self, InvariableB: str, InvariableC: OtherTestObject, InvariableD: str, InvariableE: int, InvariableA: int = 24) :
        variableB = InvariableB
        variableC = InvariableC
        variableD = InvariableD
        variableE = InvariableE
        variableA = InvariableA



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
    def ToJSON(InTestObject: TestObject) :
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObject)
        OutTestObjectJSON: TSharedPtr<FJsonObject> = MakeShareable(new FJsonObject)

        UJson::SetIntegerField(OutTestObjectJSON,"variableA", InTestObject.variableA)
        UJson::SetStringField(OutTestObjectJSON, "variableB", InTestObject.variableB)
        UJson::SetObjectField(OutTestObjectJSON,"variableC", OtherTestObject::ToJSON(InTestObject.variableC))
        UJson::SetStringField(OutTestObjectJSON, "variableD", InTestObject.variableD)
        UJson::SetIntegerField(OutTestObjectJSON,"variableE", InTestObject.variableE)
        return OutTestObjectJSON


    @staticmethod
    def FromJSON(InTestObjectJSON: TSharedPtr<FJsonObject>) :
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObjectJSON)

        return def __init__(self, UJson::GetStringField(InTestObjectJSON,"variableB"),
         OtherTestObject::FromJSON(UJson::GetObjectFieldOpt(InTestObjectJSON,
         "variableC")), UJson::GetStringField(InTestObjectJSON,"variableD"),
         UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableE"),
         UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableA"))



