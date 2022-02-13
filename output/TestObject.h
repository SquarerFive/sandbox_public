// THIS IS A GENERATED FILE! DO NOT EDIT!

#pragma once

#include "CoreMinimal.h" 
#include "Dom/JsonObject.h" 
#include "UnrealJSONUtilities.h" 
#include "OtherTestObject.h" 

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

