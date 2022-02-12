// Copyright 2022 Aiden Soedjarwo

#pragma once

#include "Dom/JsonObject.h"
#include "JsonObjectWrapper.h"

#define RETURN_NULL_JSONOBJECT_IF_NOT_EXIST(val) if (!val.IsSet())return TOptional<TSharedPtr<FJsonObject>>{};
#define RETURN_NULL_OBJECT_IF_NOT_EXIST(val) if (!val.IsSet())return {};
#define FIELD_REQUIRED(json_object, field) ensure(json_object->HasField(field));
class UJson {
public:

	// Conversions
	static FString JsonToString(const TSharedPtr<FJsonObject>& InJsonObject) {
		FJsonObjectWrapper Wrapper;
		Wrapper.JsonObject = InJsonObject;
		FString Result;
		Wrapper.JsonObjectToString(Result);

		return Result;
	}

	static TOptional<TSharedPtr<FJsonObject>> StringToJson(const FString& InJsonString) {
		FJsonObjectWrapper Wrapper;
		if (!Wrapper.JsonObjectFromString(InJsonString)) {
			return {};
		}
		return Wrapper.JsonObject;
	}

	// Setters
	static void SetNumberField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const double& Value) {
		InJsonObject->SetNumberField(FieldName, Value);
	}

	static void SetNumberField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TOptional<double>& Value) {
		if (Value.IsSet()) {
			InJsonObject->SetNumberField(FieldName, *Value);
		}
	}

	static void SetIntegerField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const int64& Value) {
		InJsonObject->SetNumberField(FieldName, static_cast<double>(Value));
	}

	static void SetIntegerField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TOptional<int64>& Value) {
		if (Value.IsSet()) {
			InJsonObject->SetNumberField(FieldName, static_cast<double>(*Value));
		}
	}

	static void SetStringField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const FString& Value) {
		InJsonObject->SetStringField(FieldName, Value);
	}

	static void SetStringField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TOptional<FString>& Value) {
		if (Value.IsSet()) {
			InJsonObject->SetStringField(FieldName, *Value);
		}
	}

	static void SetBoolField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const bool& Value) {
		InJsonObject->SetBoolField(FieldName, Value);
	}

	static void SetBoolField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TOptional<bool>& Value) {
		if (Value.IsSet()) {
			InJsonObject->SetBoolField(FieldName, *Value);
		}
	}

	static void SetObjectField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TSharedPtr<FJsonObject>& Value) {
		InJsonObject->SetObjectField(FieldName, Value);
	}

	static void SetObjectField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TOptional<TSharedPtr<FJsonObject>>& Value) {
		if (Value.IsSet()) {
			InJsonObject->SetObjectField(FieldName, *Value);
		}
	}

	// Getters

	static double GetNumberField(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
        FIELD_REQUIRED(InJsonObject, FieldName)
		return InJsonObject->GetNumberField(FieldName);
	}

	static TOptional<double> GetNumberFieldOpt(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
		if (InJsonObject->HasTypedField<EJson::Number>(FieldName)) {
			return InJsonObject->GetNumberField(FieldName);
		} return TOptional<double>{};
	}

	static int64 GetIntegerField(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
        FIELD_REQUIRED(InJsonObject, FieldName)
		return static_cast<int64>(InJsonObject->GetNumberField(FieldName));
	}

	static TOptional<int64> GetIntegerFieldOpt(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
		if (InJsonObject->HasTypedField<EJson::Number>(FieldName)) {
			return static_cast<int64>(InJsonObject->GetNumberField(FieldName));
		} return TOptional<int64>{};
	}

	static FString GetStringField(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
        FIELD_REQUIRED(InJsonObject, FieldName)
		return InJsonObject->GetStringField(FieldName);
	}

	static TOptional<FString> GetStringFieldOpt(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
		if (InJsonObject->HasTypedField<EJson::String>(FieldName)) {
			return InJsonObject->GetStringField(FieldName);
		} return TOptional<FString>{};
	}

	static bool GetBoolField(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
        FIELD_REQUIRED(InJsonObject, FieldName)
		return InJsonObject->GetBoolField(FieldName);
	}

	static TOptional<bool> GetBoolFieldOpt(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
		if (InJsonObject->HasTypedField<EJson::Boolean>(FieldName)) {
			return InJsonObject->GetBoolField(FieldName);
		} return TOptional<bool>{};
	}

	static TSharedPtr<FJsonObject> GetObjectField(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
        FIELD_REQUIRED(InJsonObject, FieldName)
		return InJsonObject->GetObjectField(FieldName);
	}

	static TOptional<TSharedPtr<FJsonObject>> GetObjectFieldOpt(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		const auto& InJsonObject = (*InJsonObjectOpt);
		if (InJsonObject->HasTypedField<EJson::Object>(FieldName)) {
			return InJsonObject->GetObjectField(FieldName);
		} return TOptional<TSharedPtr<FJsonObject>>{};
	}
};