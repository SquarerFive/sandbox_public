# sandbox_public
various CLI utils for my projects

## json schema code-generator

This tool is used to generate a data structure with the relevant serializer/deserializers for a programming language.

The syntax is defined using a config file,
examples here are: `python.json` and `ue_cpp_config.json`.

Array data types are not supported yet!

Generate Python code:

```
python .\src\json_schema\json_schema.py -i .\data\testObject.SANDBOX.schema.json -o ./output/test.py -c .\src\json_schema\python.json    
```
Results in:

```py
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




```

Generate UE4-compatible C++ code:

```
python .\src\json_schema\json_schema.py -i .\data\testObject.SANDBOX.schema.json -o ./output/test.h -c .\src\json_schema\ue_cpp_config.json
```

Results in:

```cpp
// THIS IS A GENERATED FILE! DO NOT EDIT!

#pragma once

#include "CoreMinimal.h" 
#include "Dom/JsonObject.h" 
#include "UnrealJSONUtilities.h" 


struct OtherTestObject {

    // [[GENERATED_OBJECT]] This is another test object

    OtherTestObject(const TOptional<int64>& In_count) {
        this->count = In_count;
    }

    // Number of items
    TOptional<int64> count;

    // JSON Encoders/Decoders
    static TOptional<TSharedPtr<FJsonObject>> ToJSON(const TOptional<OtherTestObject>& InOtherTestObject) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InOtherTestObject)
        const TSharedPtr<FJsonObject> OutOtherTestObjectJSON = MakeShareable(new FJsonObject);

        UJson::SetIntegerField(OutOtherTestObjectJSON,"count", InOtherTestObject->count);
        return OutOtherTestObjectJSON;
    }

    static TOptional<OtherTestObject> FromJSON(const TOptional<TSharedPtr<FJsonObject>>& InOtherTestObjectJSON) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InOtherTestObjectJSON)

        return OtherTestObject(UJson::GetIntegerFieldOpt(InOtherTestObjectJSON,"count"));
    }
};

struct TestObject {

    // [[GENERATED_OBJECT]] This is a test object

    TestObject(const FString& In_variableB, const TOptional<OtherTestObject>& In_variableC, const FString& In_variableD, const TOptional<int64>& In_variableE, const TOptional<int64>& In_variableA = 24) {
        this->variableB = In_variableB;
        this->variableC = In_variableC;
        this->variableD = In_variableD;
        this->variableE = In_variableE;
        this->variableA = In_variableA;
    }

    struct VARIABLED {

        inline static const FString ABC = "ABC";
        inline static const FString XYZ = "XYZ";
    };

    struct VARIABLEE {

        inline static const int64 LOW = 2;
        inline static const int64 HIGH = 4;
    };

    // This property represents an integer. It is not
    // required
    TOptional<int64> variableA = 24;

    // This property is a string. It is required
    FString variableB;

    // This is an object variable
    TOptional<OtherTestObject> variableC;

    // enum-like value
    FString variableD;

    // enum-like value int
    TOptional<int64> variableE;

    // JSON Encoders/Decoders
    static TOptional<TSharedPtr<FJsonObject>> ToJSON(const TOptional<TestObject>& InTestObject) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObject)
        const TSharedPtr<FJsonObject> OutTestObjectJSON = MakeShareable(new FJsonObject);

        UJson::SetIntegerField(OutTestObjectJSON,"variableA", InTestObject->variableA);
        UJson::SetStringField(OutTestObjectJSON, "variableB", InTestObject->variableB);
        UJson::SetObjectField(OutTestObjectJSON,"variableC", OtherTestObject::ToJSON(InTestObject->variableC));
        UJson::SetStringField(OutTestObjectJSON, "variableD", InTestObject->variableD);
        UJson::SetIntegerField(OutTestObjectJSON,"variableE", InTestObject->variableE);
        return OutTestObjectJSON;
    }

    static TOptional<TestObject> FromJSON(const TOptional<TSharedPtr<FJsonObject>>& InTestObjectJSON) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObjectJSON)

        return TestObject(UJson::GetStringField(InTestObjectJSON,"variableB"),
         OtherTestObject::FromJSON(UJson::GetObjectFieldOpt(InTestObjectJSON,
         "variableC")), UJson::GetStringField(InTestObjectJSON,"variableD"),
         UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableE"),
         UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableA"));
    }
};
```