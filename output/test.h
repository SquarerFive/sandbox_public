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
