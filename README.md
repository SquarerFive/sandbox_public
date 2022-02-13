# sandbox_public
various CLI utils for my projects

## json schema code-generator

This tool is used to generate a data structure with the relevant serializer/deserializers for a programming language.

Schema version: 2020-12

The syntax is defined using a config file,
languages already supported are: 
- Python 3: `python.json`
- UE4 C++17: `ue_cpp_config.json`
- Typescript: `typescript.json`

### Notes
- Only a small subset of the schema is currently supported.

### Examples

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


struct OtherTestObject : public BaseObject {
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

struct TestObject : public BaseObject {
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
    FString variableD = VARIABLED::ABC;

    // enum-like value int
    TOptional<int64> variableE = VARIABLEE::LOW;

    // This is an array of integers
    TOptional<TArray<int64>> arrayVariable;

    // This is an array of arrays of integers
    TOptional<TArray<TArray<int64>>> arrayOfArrays;

    // This is an array of objects
    TOptional<TArray<OtherTestObject>> arrayOfObjects;

    TestObject(const FString& In_variableB, const TOptional<OtherTestObject>& In_variableC, const TOptional<TArray<int64>>& In_arrayVariable, const TOptional<TArray<TArray<int64>>>& In_arrayOfArrays, const TOptional<TArray<OtherTestObject>>& In_arrayOfObjects, const TOptional<int64>& In_variableA = 24, const FString& In_variableD = VARIABLED::ABC, const TOptional<int64>& In_variableE = VARIABLEE::LOW) {
        this->variableB = In_variableB;
        this->variableC = In_variableC;
        this->arrayVariable = In_arrayVariable;
        this->arrayOfArrays = In_arrayOfArrays;
        this->arrayOfObjects = In_arrayOfObjects;
        this->variableA = In_variableA;
        this->variableD = In_variableD;
        this->variableE = In_variableE;

        this->Validate();
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
        UJson::SetArrayField(OutTestObjectJSON,"arrayOfArrays", InTestObject->arrayOfArrays);
        UJson::SetArrayField(OutTestObjectJSON,"arrayOfObjects", InTestObject->arrayOfObjects);
        return OutTestObjectJSON;
    }

    static TOptional<TestObject> FromJSON(const TOptional<TSharedPtr<FJsonObject>>& InTestObjectJSON) {
        RETURN_NULL_OBJECT_IF_NOT_EXIST(InTestObjectJSON)

        return TestObject(UJson::GetStringField(InTestObjectJSON,"variableB"),
             OtherTestObject::FromJSON(UJson::GetObjectFieldOpt(InTestObjectJSON,
             "variableC")),
             UJson::GetArrayFieldOpt<TArray<int64>>(InTestObjectJSON,"arrayVariable"),
             UJson::GetArrayFieldOpt<TArray<TArray<int64>>>(InTestObjectJSON,"arrayOfArrays"),
             UJson::GetArrayFieldOpt<TArray<OtherTestObject>>(InTestObjectJSON,"arrayOfObjects"),
             UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableA"),
             UJson::GetStringField(InTestObjectJSON,"variableD"),
             UJson::GetIntegerFieldOpt(InTestObjectJSON,"variableE"));
    }

    void Validate() {
        if (!(this->variableD==VARIABLED::ABC||this->variableD==VARIABLED::XYZ)) {
            UE_LOG(LogTemp, Fatal, TEXT("Failed to validate field variableD!"));
        }
        if (!(this->variableE==VARIABLEE::LOW||this->variableE==VARIABLEE::HIGH)) {
            UE_LOG(LogTemp, Fatal, TEXT("Failed to validate field variableE!"));
        }
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
    // This is another test object

    // Number of items
    count?: number;

    constructor(In_count?: number) {
        this.count = In_count;
    }

}

class VARIABLED {
    static ABC: string = "ABC";
    static XYZ: string = "XYZ";
}

class VARIABLEE {
    static LOW: number = 2;
    static HIGH: number = 4;
}

export class TestObject {
    // This is a test object

    // This property represents an integer. It is not
    // required
    variableA?: number = 24;

    // This property is a string. It is required
    variableB: string;

    // This is an object variable
    variableC?: OtherTestObject;

    // enum-like value
    variableD: string = VARIABLED.ABC;

    // enum-like value int
    variableE?: number = VARIABLEE.LOW;

    // This is an array of integers
    arrayVariable?: Array<number>;

    // This is an array of arrays of integers
    arrayOfArrays?: Array<Array<number>>;

    // This is an array of objects
    arrayOfObjects?: Array<OtherTestObject>;

    constructor(In_variableB: string, In_variableC?: OtherTestObject, In_arrayVariable?: Array<number>, In_arrayOfArrays?: Array<Array<number>>, In_arrayOfObjects?: Array<OtherTestObject>, In_variableA: number = 24, In_variableD: string = VARIABLED.ABC, In_variableE: number = VARIABLEE.LOW) {
        this.variableB = In_variableB;
        this.variableC = In_variableC;
        this.arrayVariable = In_arrayVariable;
        this.arrayOfArrays = In_arrayOfArrays;
        this.arrayOfObjects = In_arrayOfObjects;
        this.variableA = In_variableA;
        this.variableD = In_variableD;
        this.variableE = In_variableE;

        this.Validate()
    }


    Validate(): void {
        if (!(this.variableD==VARIABLED.ABC||this.variableD==VARIABLED.XYZ)) {
            console.error("Failed to validate field variableD!")
        }
        if (!(this.variableE==VARIABLEE.LOW||this.variableE==VARIABLEE.HIGH)) {
            console.error("Failed to validate field variableE!")
        }
    }
}
```