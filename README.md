# sandbox_public
various CLI utils for my projects

## json schema code-generator

This tool is used to generate a data structure with the relevant serializer/deserializers for a programming language.

The syntax is defined using a config file,
languages already supported are: 
- Python 3: `python.json`
- UE4 C++: `ue_cpp_config.json`
- Typescript: `typescript.json`

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
    # This is another test object


    # Number of items
    count: int

    def __init__(self, In_count: int) :
        self.count = In_count


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
    # This is a test object

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

    def __init__(self, In_variableB: str, In_variableD: str, In_variableC: OtherTestObject, In_variableE: int, In_variableA: int = 24) :
        self.variableB = In_variableB
        self.variableD = In_variableD
        self.variableC = In_variableC
        self.variableE = In_variableE
        self.variableA = In_variableA


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
         InTestObjectJSON.get_string_field("variableD"),
         OtherTestObject.from_json(InTestObjectJSON.get_object_field("variableC")),
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
    // This is another test object


    // Number of items
    TOptional<int64> count;

    OtherTestObject(const TOptional<int64>& In_count) {
        this->count = In_count;
    }

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
    // This is a test object

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

    // This is an array of integers
    TOptional<TArray<int64>> arrayVariable;

    TestObject(const FString& In_variableB, const FString& In_variableD, const TOptional<OtherTestObject>& In_variableC, const TOptional<int64>& In_variableE, const TOptional<TArray<int64>>& In_arrayVariable, const TOptional<int64>& In_variableA = 24) {
        this->variableB = In_variableB;
        this->variableD = In_variableD;
        this->variableC = In_variableC;
        this->variableE = In_variableE;
        this->arrayVariable = In_arrayVariable;
        this->variableA = In_variableA;
    }

    // JSON Encoders/Decoders
    static TOptional<TSharedPtr<FJsonObject>> ToJSON(const TOptional<TestObject>& InTestObject) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObject)
        const TSharedPtr<FJsonObject> OutTestObjectJSON = MakeShareable(new FJsonObject);

        UJson::SetIntegerField(OutTestObjectJSON,"variableA", InTestObject->variableA);
        UJson::SetStringField(OutTestObjectJSON, "variableB", InTestObject->variableB);
        UJson::SetObjectField(OutTestObjectJSON,"variableC", OtherTestObject::ToJSON(InTestObject->variableC));
        UJson::SetStringField(OutTestObjectJSON, "variableD", InTestObject->variableD);
        UJson::SetIntegerField(OutTestObjectJSON,"variableE", InTestObject->variableE);
        UJson::SetArrayField(OutTestObjectJSON,"arrayVariable", InTestObject->arrayVariable);
        return OutTestObjectJSON;
    }

    static TOptional<TestObject> FromJSON(const TOptional<TSharedPtr<FJsonObject>>& InTestObjectJSON) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObjectJSON)

        return TestObject(UJson::GetStringField(InTestObjectJSON,"variableB"),
         UJson::GetStringField(InTestObjectJSON,"variableD"),
         OtherTestObject::FromJSON(UJson::GetObjectFieldOpt(InTestObjectJSON,
         "variableC")), UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableE"),
         UJson::GetArrayFieldOpt<TArray<int64>>(InTestObjectJSON,"arrayVariable"),
         UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableA"));
    }
};
```

Generate Typescript:

```
python .\src\json_schema\json_schema.py -i .\data\testObject.SANDBOX.schema.json -o ./output/test.ts -c .\src\json_schema\typescript.json  
```
Resuts in:
```ts
// THIS IS A GENERATED FILE! DO NOT EDIT!


export class OtherTestObject {
    // [[GENERATED_OBJECT]] This is another test object


    // Number of items
    count?: number;

    constructor(In_count?: number) {
        this.count = In_count;
    }

}

export class VARIABLED {
    static ABC: string = "ABC";
    static XYZ: string = "XYZ";
}

export class VARIABLEE {
    static LOW: number = 2;
    static HIGH: number = 4;
}

export class TestObject {
    // [[GENERATED_OBJECT]] This is a test object


    // This property represents an integer. It is not
    // required
    variableA?: number = 24;

    // This property is a string. It is required
    variableB: string;

    // This is an object variable
    variableC?: OtherTestObject;

    // enum-like value
    variableD: string;

    // enum-like value int
    variableE?: number;

    constructor(In_variableB: string, In_variableD: string, In_variableC?: OtherTestObject, In_variableE?: number, In_variableA: number = 24) {
        this.variableB = In_variableB;
        this.variableD = In_variableD;
        this.variableC = In_variableC;
        this.variableE = In_variableE;
        this.variableA = In_variableA;
    }

}
```