// Copyright 2022 Aiden Soedjarwo

#pragma once

#include "Dom/JsonObject.h"
#include "JsonObjectWrapper.h"

#define RETURN_NULL_JSONOBJECT_IF_NOT_EXIST(val) if (!val.IsSet())return TOptional<TSharedPtr<FJsonObject>>{};
#define RETURN_NULL_OBJECT_IF_NOT_EXIST(val) if (!val.IsSet())return {};
#define FIELD_REQUIRED(json_object, field) ensure(json_object->HasField(field));



class BaseObject {
public:
	static TOptional<TSharedPtr<FJsonObject>> ToJSON(const TOptional<BaseObject>& InObject) {};
	static TOptional<BaseObject> FromJSON(const TOptional<TSharedPtr<FJsonObject>>& InJsonObject) {};
};

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

	template <typename T>
	static TArray<TSharedPtr<FJsonValue>> SetArrayField_Internal(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TArray<T>& Values) {
		TArray<TSharedPtr<FJsonValue>> JsonValues;

		if constexpr (TIsSame<T, double>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueNumber(Value)
					)
				);
			}
		}

		else if constexpr (TIsSame<T, int64>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueNumber(static_cast<double>(Value))
					)
				);
			}
		}

		else if constexpr (TIsSame<T, FString>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueString(Value)
					)
				);
			}
		}

		else if constexpr (TIsSame<T, bool>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueBoolean(Value)
					)
				);
			}
		}

		else if constexpr (TIsSame<T, bool>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueBoolean(Value)
					)
				);
			}
		}

		else if constexpr (TIsSame<T, bool>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueBoolean(Value)
					)
				);
			}
		}

		else if constexpr (TIsTArray<T>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueArray(SetArrayField_Internal(InJsonObject, FieldName, Value))
					)
				);
			}
		}
		else if constexpr (TIsDerivedFrom<T, BaseObject>::Value) {
			for (const auto& Value : Values) {
				JsonValues.Add(
					MakeShareable(
						new FJsonValueObject(
							*T::ToJSON(Value)
						)
					)
				);
			}
		}
		else {
			// Is object
			for (const auto& Value : Values) {
				JsonValues.Add(
					Value
				);
			}
		}

		return JsonValues;
	}

	template<typename T>
	static void SetArrayField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TArray<T>& Values) {
		InJsonObject->SetArrayField(FieldName, SetArrayField_Internal(InJsonObject, FieldName, Values));
	}

	template<typename T>
	static void SetArrayField(const TSharedPtr<FJsonObject>& InJsonObject, const FString& FieldName, const TOptional<TArray<T>>& Values) {
		if (Values.IsSet()) {
			SetArrayField(InJsonObject, FieldName, *Values);
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

	template<typename T>
	static T GetArrayField_Internal(const TArray<TSharedPtr<FJsonValue>>& JsonArrayValues) {
		T Result;

		for (const auto& ArrayValue : JsonArrayValues) {
			if constexpr (TIsSame<T::ElementType, int64>::Value) {
				ensure(ArrayValue->Type == EJson::Number);
				Result.Add(static_cast<int64>(ArrayValue->AsNumber()));
			}
			else if constexpr (TIsSame<T::ElementType, double>::Value) {
				ensure(ArrayValue->Type == EJson::Number);
				Result.Add(ArrayValue->AsNumber());
			}
			else if constexpr (TIsSame<T::ElementType, FString>::Value) {
				ensure(ArrayValue->Type == EJson::String);
				Result.Add(ArrayValue->AsString());
			}
			else if constexpr (TIsSame<T::ElementType, bool>::Value) {
				ensure(ArrayValue->Type == EJson::Boolean);
				Result.Add(ArrayValue->AsBool());
			}
			else if constexpr (TIsTArray<T::ElementType>::Value) {
				ensure(ArrayValue->Type == EJson::Array);
				const auto& JsonArray = ArrayValue->AsArray();
				T::ElementType Res = GetArrayField_Internal<T::ElementType>(JsonArray);
				Result.Emplace(MoveTemp(Res));
			}
			else if constexpr (TIsDerivedFrom<T::ElementType, BaseObject>::Value) {
				ensure(ArrayValue->Type == EJson::Object);
				auto ResultObject = T::ElementType::FromJSON(ArrayValue->AsObject());
				if (ResultObject) {
					Result.Add(*ResultObject);
				}
			}
		}

		return Result;
	}

	template<typename T>
	static T GetArrayField(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		T Result;
		const auto& InJsonObject = (*InJsonObjectOpt);

		const auto& ArrayField = InJsonObject->GetArrayField(FieldName);

		Result = GetArrayField_Internal<T>(ArrayField);

		return Result;
	}

	template<typename T>
	static TOptional<T> GetArrayFieldOpt(const TOptional<TSharedPtr<FJsonObject>>& InJsonObjectOpt, const FString& FieldName) {
		T Result;
		const auto& InJsonObject = (*InJsonObjectOpt);

		if (InJsonObject->HasTypedField<EJson::Array>(FieldName)) {
			return GetArrayField<T>(InJsonObjectOpt, FieldName);

		} return {};
	}
};