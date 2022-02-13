# Copyright 2022 Aiden Soedjarwo

from optparse import Option
from pydantic import BaseModel, validator
from enum import Enum
from typing import *
import json
import os
import textwrap

import argparse


class EncoderDecoderConfig(BaseModel):
    json_object_typename: str = "TSharedPtr<FJsonObject>"
    json_object_assign_value: str = "MakeShareable(new FJsonObject)"
    json_object_variable_name: str = "_JsonObject_"

    json_encode_method_name = "ToJSON"
    json_decode_method_name = "FromJSON"

    json_object_set_string_field = """UJson::SetStringField({name}, "{variable_name}", {value})"""
    json_object_set_number_field = """UJson::SetNumberField({name},"{variable_name}", {value})"""
    json_object_set_integer_field = """UJson::SetIntegerField({name},"{variable_name}", {value})"""
    json_object_set_object_field = """UJson::SetObjectField({name},"{variable_name}", {value_typename}::{json_encode_method_name}({value}))"""
    json_object_set_boolean_field = """UJson::SetBooleanField({name},"{variable_name}", {value})"""
    json_object_set_array_field = """UJson::SetArrayField({name},"{variable_name}", {value})"""

    json_object_get_string_field = """UJson::GetStringField({name},"{variable_name}")"""
    json_object_get_number_field = """UJson::GetNumberField({name},"{variable_name}")"""
    json_object_get_integer_field = """UJson::GetIntegerField({name},"{variable_name}")"""
    json_object_get_object_field = """{value_typename}::{json_decode_method_name}(UJson::GetObjectFieldOpt({name}, "{variable_name}"))"""
    json_object_get_boolean_field = """UJson::GetBooleanField({name},"{variable_name}")"""
    json_object_get_array_field = """UJson::GetArrayField({name},"{variable_name}")"""

    json_object_get_opt_string_field = """UJson::GetStringFieldOpt({name},"{variable_name}")"""
    json_object_get_opt_number_field = """UJson::GetNumberFieldOpt({name},"{variable_name}")"""
    json_object_get_opt_integer_field = """UJson::GetIntegerFieldOpt({name},"{variable_name}")"""
    json_object_get_opt_object_field = """{value_typename}::{json_decode_method_name}(UJson::GetObjectFieldOpt({name}, "{variable_name}"))"""
    json_object_get_opt_boolean_field = """UJson::GetBooleanFieldOpt({name},"{variable_name}")"""
    json_object_get_opt_array_field = """UJson::GetArrayFieldOpt<{value_typename}>({name},"{variable_name}")"""

    json_object_has_field = """{name}->HasField("{variable_name}")"""

    return_null_object_if_not_exist: str = "RETURN_NULL_OBJECT_IF_NOT_EXIST({name})"


class DataTypeConfig(BaseModel):
    string_typename: str = "FString"
    number_typename: str = "double"
    integer_typename: str = "int64"
    object_typename: Optional[str] = None
    boolean_typename: str = "bool"
    array_typename: str = "TArray<{typename}>"
    void_typename: str = "void"


class CodeGenerationConfig(BaseModel):
    import_module_template: str = """#include "{module_name}" """
    imported_module_name_template: str = """{module_name}.h"""
    object_declaration_template: str = "struct {typename}"

    statement_close: str = ";"

    # Variables
    qualifier_const: str = "const"
    qualifier_inline: str = "inline"
    qualifier_static: str = "static"

    variable_declaration_template: str = "{qualifiers} {typename}{postfix} {name}"
    optional_variable_declaration_template: str = "{qualifiers} TOptional<{typename}>{postfix} {name}"
    variable_declaration_default_value_template: str = "{variable_declaration} = {value}"

    variable_postfix_reference_template: str = "&"
    variable_postfix_pointer_template: str = "*"

    # Naming
    input_argument_prefix: str = "In_"

    ## Enums & anyOf
    any_of_declaration_template: str = object_declaration_template
    declare_anyof_outside_self: bool = False

    # General

    access_member = "{object_name}.{member_name}"
    access_optional_member = "{object_name}->{member_name}"
    static_accessor = "{typename}::{member_name}"

    variable_declaration_close: str = statement_close

    variable_assignment_template: str = "{name} = {value}"
    variable_assignment_close: str = statement_close

    method_declaration_template: str = "{qualifiers} {typename} {name}({args})"
    static_method_declaration_template: str = "{qualifiers} {typename} {name}({args})"

    method_return_template: str = "return {name}"

    static_method_template: str = "static {method_declaration}"

    object_constructor_template: str = "{typename}({args})"
    construct_object_template: str = "{typename}({args})"

    scope_character_open: str = "{"
    scope_charater_close: str = "}"
    object_scope_character_open: str = "{\n"
    object_scope_character_close: str = "};"

    scope_indent_count: int = 4
    scope_indent_character: str = " "

    comment_character: str = "//"

    file_start = f"{comment_character} THIS IS A GENERATED FILE! DO NOT EDIT!\n\n#pragma once\n\n"

    module_imports: List[str] = [
        "CoreMinimal.h",
        "Dom/JsonObject.h",
        "UnrealJSONUtilities.h"
    ]

    allow_self_type_in_args: bool = True
    any_type: str = "std::any"

    self_access: str = "this->{member_name}"
    mark_as_optional_with_default_value_in_args: bool = True

    # Conditions
    conditional_or = "||"
    conditional_and = "&&"
    conditional_equal = "=="
    conditional_not = "!"
    conditional_if_template = "if ({condition})"

    # validation
    throw_error_template: str = 'UE_LOG(LogTemp, Fatal, TEXT("{message}"))'
    validate_method_name: str = "Validate"


class Config(BaseModel):
    include_serializers_and_deserializers: bool = True

    data_type_config: DataTypeConfig = DataTypeConfig()
    encoder_decoder_config: EncoderDecoderConfig = EncoderDecoderConfig()
    code_generation_config: CodeGenerationConfig = CodeGenerationConfig()


DataTypeAlias = object


class DataType:
    STRING = "STRING"
    NUMBER = "NUMBER"
    INTEGER = "INTEGER"
    OBJECT = "OBJECT"
    BOOLEAN = "BOOLEAN"
    ARRAY = "ARRAY"

    is_reference_to_object: bool = False
    child_data_type: DataTypeAlias = None

    value = None
    ref_value = None

    def __init__(self, value: str):
        self.value = value

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, DataType):
            return __o.value == self.value
        elif isinstance(__o, str) or __o == None:
            return __o == self.value

    def validate(other):
        return isinstance(other, DataType)

    @staticmethod
    def from_string(string: str):
        return {
            "string": DataType(DataType.STRING),
            "number": DataType(DataType.NUMBER),
            "integer": DataType(DataType.INTEGER),
            "object": DataType(DataType.OBJECT),
            "boolean": DataType(DataType.BOOLEAN),
            "array": DataType(DataType.ARRAY)
        }[string]

    @staticmethod
    def from_reference(string: str, spec):
        spec: Spec = spec
        dt = DataType(DataType.OBJECT)
        dt.is_reference_to_object = True
        dt.ref_value = spec.get_dependent_spec(
            string.split("$ref:")[1]).title_to_typename()
        return dt

    def resolve_data_type(self, spec) -> str:
        spec: Spec = spec

        result = None

        if self.value == DataType.STRING:
            result = spec.config.data_type_config.string_typename
        elif self.value == DataType.NUMBER:
            result = spec.config.data_type_config.number_typename
        elif self.value == DataType.INTEGER:
            result = spec.config.data_type_config.integer_typename
        elif self.value == DataType.OBJECT:
            if self.is_reference_to_object:
                result = self.ref_value
            else:
                result = spec.config.data_type_config.object_typename
        elif self.value == DataType.BOOLEAN:
            result = spec.config.data_type_config.boolean_typename
        elif self.value == DataType.ARRAY:
            result = spec.config.data_type_config.array_typename

        return result

        # return {
        #     DataType.STRING: spec.config.data_type_config.string_typename,
        #     DataType.NUMBER: spec.config.data_type_config.number_typename,
        #     DataType.INTEGER: spec.config.data_type_config.integer_typename,
        #     DataType.OBJECT: spec.config.data_type_config.object_typename,
        #     DataType.BOOLEAN: spec.config.data_type_config.boolean_typename,
        #     DataType.ARRAY: spec.config.data_type_config.array_typename
        # }[self]


class Variable(BaseModel):
    name: str
    description: str

    json_data_type: DataType
    reference_type: Optional[str]  # if we reference another schema object
    data_type: Optional[str]

    required: bool
    default_value: Any

    signature: Optional[str]

    @validator('json_data_type')
    def json_data_type_is_valid(cls, v):
        if not isinstance(v, DataType):
            raise ValueError("json_data_type must be of instance `DataType`!")
        return v

    class Config:
        arbitrary_types_allowed = True

    def resolve_typename(self, spec):
        if self.data_type == None:
            if self.reference_type:
                dependent_spec = spec.get_dependent_spec(self.reference_type)
                self.data_type = dependent_spec.title_to_typename()
            else:
                self.data_type = self.json_data_type.resolve_data_type(spec)

        typename = self.data_type

        has_no_child = self.json_data_type.child_data_type == None
        child = self.json_data_type.child_data_type
        while not has_no_child:
            child: DataType = child
            typename = typename.format(typename=child.resolve_data_type(spec))

            has_no_child = child.child_data_type == None
            if not has_no_child:
                child = child.child_data_type

        self.data_type = typename

    def resolve_signature(self,
                          spec,
                          const: bool = False,
                          reference: bool = False,
                          pointer: bool = False,
                          inline: bool = False,
                          static: bool = False,
                          close_declaration: bool = True,
                          include_assignment: bool = True,
                          include_name: bool = True,
                          typename_override: Optional[str] = None,
                          is_arg: bool = False,
                          format_name_fn: Optional[Callable[[str], str]] = None
                          ) -> str:
        spec: Spec = spec

        self.resolve_typename(spec)

        qualifiers = []
        postfix = ""
        typename = self.data_type if typename_override is None else typename_override

        if pointer and reference:
            raise ValueError(
                "pointer=true and reference=true is not currently supported")

        if pointer:
            # typename = spec.config.code_generation_config.variable_declaration_pointer_template.format(typename = typename)
            postfix += spec.config.code_generation_config.variable_postfix_pointer_template

        if reference:
            # typename = spec.config.code_generation_config.variable_declaration_reference_template.format(typename = typename)
            postfix += spec.config.code_generation_config.variable_postfix_reference_template

        if inline:
            qualifiers.append(
                spec.config.code_generation_config.qualifier_inline
            )

        if static:
            qualifiers.append(
                spec.config.code_generation_config.qualifier_static
            )

        if const:
            qualifiers.append(
                spec.config.code_generation_config.qualifier_const)

        if is_arg and (not spec.config.code_generation_config.mark_as_optional_with_default_value_in_args) and self.default_value != None:
            declaration_template = spec.config.code_generation_config.variable_declaration_template
        else:
            declaration_template = spec.config.code_generation_config.variable_declaration_template if self.required else spec.config.code_generation_config.optional_variable_declaration_template

        body = declaration_template.format(
            qualifiers=' '.join(qualifiers),
            typename=typename,
            name=(self.name if format_name_fn == None else format_name_fn(
                self.name)) if include_name else '',
            postfix=postfix
        )

        if self.default_value != None and include_assignment:
            body = spec.config.code_generation_config.variable_declaration_default_value_template.format(
                variable_declaration=body,
                value=self.default_value #if not self.json_data_type == DataType.STRING else f'"{self.default_value}"'
            )

        if close_declaration:
            body += spec.config.code_generation_config.variable_declaration_close

        self.signature = body.strip()
        return self.signature

    def resolve_assignment(self, spec, value: str):
        spec: Spec = spec

        return spec.config.code_generation_config.variable_assignment_template.format(name=self.name, value=value) + spec.config.code_generation_config.variable_assignment_close

    def resolve_description(self, spec):
        spec: Spec = spec
        return textwrap.indent('\n'.join(textwrap.wrap(self.description, 50)), f"{spec.config.code_generation_config.comment_character} ")

    def resolve_constructor(self, spec, args):
        spec: Spec = spec
        args: str = args

        return spec.config.code_generation_config.construct_object_template.format(typename=self.data_type, args=args)

    def resolve_default_value(self):
        if self.default_value != None:
            if self.json_data_type == DataType.STRING:
                self.default_value = f'"{self.default_value}"'

class AnyOf(BaseModel):
    typename: str
    possible_values: List[Variable]
    reference_variable: Variable

    def resolve(self, spec):
        spec: Spec = spec

        body = spec.config.code_generation_config.any_of_declaration_template.format(
            typename=self.typename)
        body += spec.config.code_generation_config.object_scope_character_open

        [v.resolve_default_value() for v in self.possible_values]

        values = '\n'.join([
            v.resolve_signature(spec, True, False, False, True, True, True, True) for v in self.possible_values
        ])
        body += spec.indent(values, 1)

        body += "\n" + spec.config.code_generation_config.object_scope_character_close

        self.reference_variable.default_value = spec.config.code_generation_config.static_accessor.format(
            typename = self.typename,
            member_name = self.possible_values[0].name
        )

        return body
    
    def resolve_validator(self, spec):
        spec: Spec = spec

        condition = spec.config.code_generation_config.conditional_or.join([
            spec.config.code_generation_config.self_access.format(member_name = self.reference_variable.name) + spec.config.code_generation_config.conditional_equal + \
                spec.config.code_generation_config.static_accessor.format(
                    typename = self.typename,
                    member_name = v.name
                ) for v in self.possible_values
        ])

        error_message = f'Failed to validate field {self.reference_variable.name}!'

        return condition, error_message

class Spec:
    def __init__(self, spec: dict, context_directory: str, config: Config = Config()):
        self.spec = spec
        self.context_directory = context_directory
        self.body = ""

        self.variables: List[Variable] = []
        self.required_variable_names: List[str] = []
        self.any_of_variables: List[AnyOf] = []
        self.config = config

    def get_dependent_spec(self, ref: str):
        with open(os.path.join(self.context_directory, ref)) as f:
            data = json.load(f)
            spec = Spec(data, self.context_directory)
        return spec

    def get_dependencies(self) -> List[str]:
        props = self.spec.get('properties', {})
        deps = []
        for key in props:
            has_ref = props[key].get("$ref", None) != None
            if has_ref:
                deps.append(props[key]['$ref'])
                deps.extend(self.get_dependent_spec(
                    deps[-1]).get_dependencies())

        return deps

    def title_to_typename(self) -> str:
        return self.spec['title'].replace(' ', '')

    def indent(self, string: str, levels: int):
        indent_space = self.config.code_generation_config.scope_indent_character * \
            self.config.code_generation_config.scope_indent_count*levels
        return textwrap.indent(string, indent_space)

    @property
    def sorted_variables(self):
        return sorted(
            self.variables, key=lambda v: 2 if v.default_value != None else (1 if v.required == False else 0))

    def resolve_constructor(self, only_required: bool = True):
        sorted_variables = self.sorted_variables

        def format_name_fn(name: str) -> str:
            return f"{self.config.code_generation_config.input_argument_prefix}{name}"

        context_variables = [
            v for v in sorted_variables if v.name in self.required_variable_names or not only_required
        ]

        input_signatures = [
            v.resolve_signature(self, True, True, close_declaration=False, format_name_fn=format_name_fn, is_arg=True) for v in context_variables
        ]

        body = self.config.code_generation_config.object_constructor_template.format(
            typename=self.title_to_typename(),
            args=', '.join(input_signatures)
        )

        body += self.config.code_generation_config.scope_character_open + "\n"

        for i, variable in enumerate(context_variables):
            body += self.indent(
                self.config.code_generation_config.self_access.format(member_name=variable.resolve_assignment(
                    self, self.config.code_generation_config.input_argument_prefix+variable.name)), 1
            )
            if i < len(context_variables):
                body += "\n"

        if self.has_validator():
            body += "\n"
            body += self.indent(self.call_method(self.config.code_generation_config.validate_method_name) , 1)
            body += "\n"

        body += self.config.code_generation_config.scope_charater_close + "\n"

        return body

    def resolve_description(self):
        desc = f"{self.spec.get('description', '')}"
        return textwrap.indent('\n'.join(textwrap.wrap(desc, 50)), f"{self.config.code_generation_config.comment_character} ")

    def resolve(self):
        if self.spec.get("type") == "object":
            self_name = self.title_to_typename()

            self.required_variable_names = self.spec.get("required", [])
            properties = self.spec['properties']

            self.any_of_variables = []

            for variableName in properties:
                variable_property: dict = properties[variableName]

                def resolve_variable_type_and_possible_values() -> Tuple[List[str], List[Variable]]:
                    found_type: str = None
                    if (variable_property.get("type") == None):
                        if (variable_property.get("anyOf")):
                            possible_values: List[Variable] = []
                            for v in variable_property["anyOf"]:
                                if v.get("type") != None:
                                    found_type = v["type"]
                            for v in variable_property["anyOf"]:
                                if v.get("const") != None:
                                    variable = Variable(
                                        name=v['const'] if v.get(
                                            "name") == None else v["name"],
                                        description="",
                                        json_data_type=DataType.from_string(
                                            found_type),
                                        required=True,
                                        default_value=v['const']
                                    )
                                    possible_values.append(variable)

                            return [found_type], possible_values
                        return [None], []

                    elif (variable_property["type"] == "array"):
                        # only support root levels for now
                        types = [variable_property["type"]]

                        def collect_types(data: dict, in_types: List[str]) -> List[str]:
                            if data.get("items"):
                                if data["items"].get("type"):
                                    in_types.append(data["items"]["type"])
                                    return collect_types(data["items"], in_types)
                                else:
                                    if data["items"].get("$ref"):
                                        in_types.append(
                                            f"$ref:{data['items']['$ref']}")
                                    else:
                                        raise Exception("Invalid property!")

                        collect_types(variable_property, types)
                        return types, []
                    else:
                        return [variable_property["type"]], []

                variable_types, possible_values = resolve_variable_type_and_possible_values()

                if variable_types[0] != None and '$ref' in variable_types[0]:
                    data_type: DataType = DataType.from_reference(
                        variable_types[0], self)
                else:
                    data_type: DataType = DataType.from_string(
                        variable_types[0] if variable_types[0] != None else 'object')

                if len(variable_types) > 1:
                    root_data_type = data_type
                    for variable_type in variable_types[1:]:
                        if '$ref' in variable_type:
                            child_data_type = DataType.from_reference(
                                variable_type, self)
                        else:
                            child_data_type = DataType.from_string(
                                variable_type)
                        root_data_type.child_data_type = child_data_type
                        root_data_type = child_data_type

                

                variable = Variable(
                    name=variableName,
                    description=variable_property["description"],
                    json_data_type=data_type,
                    required=variableName in self.required_variable_names,
                    default_value=variable_property.get("default"),
                    reference_type=variable_property.get("$ref")
                )

                variable.resolve_default_value()

                variable.resolve_signature(self)

                if len(possible_values) > 0:
                    self.any_of_variables.append(
                        AnyOf(typename=variableName.upper(), possible_values=possible_values, reference_variable = variable))

                self.variables.append(variable)

            self.body += f"{self.config.code_generation_config.object_declaration_template.format(typename = self_name)}{self.config.code_generation_config.object_scope_character_open}{self.indent(self.resolve_description(), 1)}\n"

            # self.body += self.indent(self.resolve_constructor(True), 1)+'\n\n'

            if not self.config.code_generation_config.declare_anyof_outside_self:
                for var in self.any_of_variables:
                    self.body += self.indent(var.resolve(self), 1)+"\n"
            else:
                b = ""
                for var in self.any_of_variables:
                    b += self.indent(var.resolve(self), 0)+"\n\n"
                self.body = b + self.body

            self.body += "\n"

            for var in self.variables:
                self.body += self.indent(var.resolve_description(self), 1) + \
                    "\n" + self.indent(var.resolve_signature(self), 1)+"\n\n"

            self.body += self.indent(self.resolve_constructor(False), 1)+'\n'

            if self.config.include_serializers_and_deserializers:
                self.body += self.indent(self.config.code_generation_config.comment_character +
                                         " JSON Encoders/Decoders" + "\n", 1)
                self.body += self.indent(self.create_json_encoder(), 1)
                self.body += "\n\n"
                self.body += self.indent(self.create_json_decoder(), 1)
                self.body += "\n"
                if self.has_validator():
                    self.body += "\n"
                    self.body += self.indent(self.create_validator(), 1)
                    self.body += "\n"

            self.body += self.config.code_generation_config.object_scope_character_close + "\n\n"

            return self.body

    def call_method(self, method_name: str, args: List[Variable] = [], is_static: bool = False):
        if not is_static:
            return self.config.code_generation_config.self_access.format(
                member_name = method_name
            ) + f"({', '.join([self.config.code_generation_config.self_access.format(member_name = v.name) for v in args])})" \
                + self.config.code_generation_config.statement_close
        
        return self.config.code_generation_config.static_accessor.format(
            typename = self.title_to_typename(),
            member_name = method_name
        ) + f"({', '.join([self.config.code_generation_config.self_access.format(member_name = v.name) for v in args])})" \
            + self.config.code_generation_config.statement_close
            

    def has_validator(self):
        return len(self.any_of_variables) > 0 and self.config.include_serializers_and_deserializers

    def create_validator(self):
        body = """"""

        body += self.config.code_generation_config.method_declaration_template.format(
            typename = self.config.data_type_config.void_typename,
            name = self.config.code_generation_config.validate_method_name,
            qualifiers = "",
            args = ""
        ).strip()

        body += self.config.code_generation_config.scope_character_open + "\n"
        
        for any_of in self.any_of_variables:
            assert_statement = ""
            condition, error_message = any_of.resolve_validator(self)
            assert_statement += self.config.code_generation_config.conditional_if_template\
                .format(condition = f'{self.config.code_generation_config.conditional_not}({condition})')
            assert_statement += self.config.code_generation_config.scope_character_open + "\n"
            assert_statement += self.indent(
                self.config.code_generation_config.throw_error_template.format(message = error_message), 1
            ) + self.config.code_generation_config.statement_close + "\n"
            assert_statement += self.config.code_generation_config.scope_charater_close + "\n"

            body += self.indent(assert_statement, 1)

        body += self.config.code_generation_config.scope_charater_close

        return body

    def create_json_encoder(self):
        self_typename = self.title_to_typename()

        self_as_variable = Variable(
            name=f"In{self_typename}",
            description="",
            json_data_type=DataType(DataType.OBJECT),
            data_type=self_typename,
            required=False
        )

        json_object_variable = Variable(
            name=f"Out{self_typename}JSON",
            description="",
            json_data_type=DataType(DataType.OBJECT),
            data_type=self.config.encoder_decoder_config.json_object_typename,
            required=True,
            default_value=self.config.encoder_decoder_config.json_object_assign_value
        )

        _optional_json_object_variable = Variable(
            name=f"Out{self_typename}JSON",
            description="",
            json_data_type=DataType(DataType.OBJECT),
            data_type=self.config.encoder_decoder_config.json_object_typename,
            required=False,
            default_value=self.config.encoder_decoder_config.json_object_assign_value
        )

        body = self.config.code_generation_config.static_method_declaration_template.format(
            qualifiers="",
            typename=_optional_json_object_variable.resolve_signature(
                self, include_assignment=False, include_name=False, close_declaration=False
            ),
            name=self.config.encoder_decoder_config.json_encode_method_name,
            args=self_as_variable.resolve_signature(
                self, True, True, close_declaration=False, include_assignment=False, typename_override=None if self.config.code_generation_config.allow_self_type_in_args else self.config.code_generation_config.any_type
            )
        ).strip()

        body = self.config.code_generation_config.static_method_template.format(
            method_declaration=body)

        body += self.config.code_generation_config.scope_character_open + "\n"

        body += self.indent(self.config.encoder_decoder_config.return_null_object_if_not_exist.format(
            name=self_as_variable.name), 1) + "\n"

        body += self.indent(json_object_variable.resolve_signature(self,
                            True, False, close_declaration=True), 1)

        body += "\n\n"

        json_set_mappings = {
            DataType.STRING: self.config.encoder_decoder_config.json_object_set_string_field,
            DataType.NUMBER: self.config.encoder_decoder_config.json_object_set_number_field,
            DataType.INTEGER: self.config.encoder_decoder_config.json_object_set_integer_field,
            DataType.OBJECT: self.config.encoder_decoder_config.json_object_set_object_field,
            DataType.BOOLEAN: self.config.encoder_decoder_config.json_object_set_boolean_field,
            DataType.ARRAY: self.config.encoder_decoder_config.json_object_set_array_field
        }

        assignments = [
            json_set_mappings[v.json_data_type.value].format(
                name=json_object_variable.name,
                variable_name=v.name,
                value=self.config.code_generation_config.access_optional_member.format(
                    object_name=self_as_variable.name, member_name=v.name),
                value_typename=v.data_type,
                json_encode_method_name=self.config.encoder_decoder_config.json_encode_method_name
            ) + self.config.code_generation_config.variable_assignment_close for v in self.variables
        ]

        assignments = self.indent('\n'.join(assignments), 1)

        body += assignments
        body += "\n"
        body += self.indent(self.config.code_generation_config.method_return_template.format(name=json_object_variable.name) +
                            self.config.code_generation_config.statement_close, 1)
        body += "\n"
        body += self.config.code_generation_config.scope_charater_close

        return body

    def create_json_decoder(self):
        self_typename = self.title_to_typename()

        sorted_variables = self.sorted_variables

        self_as_variable = Variable(
            name=f"Out{self_typename}",
            description="",
            json_data_type=DataType(DataType.OBJECT),
            data_type=self_typename,
            required=False
        )

        json_object_variable = Variable(
            name=f"In{self_typename}JSON",
            description="",
            json_data_type=DataType(DataType.OBJECT),
            data_type=self.config.encoder_decoder_config.json_object_typename,
            required=False,
            default_value=self.config.encoder_decoder_config.json_object_assign_value
        )

        body = self.config.code_generation_config.static_method_declaration_template.format(
            qualifiers="",
            typename=self_as_variable.resolve_signature(
                self, close_declaration=False, include_assignment=False, include_name=False),
            name=self.config.encoder_decoder_config.json_decode_method_name,
            args=json_object_variable.resolve_signature(
                self, True, True, close_declaration=False, include_assignment=False
            )
        ).strip()

        body = self.config.code_generation_config.static_method_template.format(
            method_declaration=body)

        body += self.config.code_generation_config.scope_character_open + "\n"

        body += self.indent(self.config.encoder_decoder_config.return_null_object_if_not_exist.format(
            name=json_object_variable.name), 1) + "\n"
        body += "\n"

        json_get_mappings = {
            DataType.STRING: self.config.encoder_decoder_config.json_object_get_string_field,
            DataType.NUMBER: self.config.encoder_decoder_config.json_object_get_number_field,
            DataType.INTEGER: self.config.encoder_decoder_config.json_object_get_integer_field,
            DataType.OBJECT: self.config.encoder_decoder_config.json_object_get_object_field,
            DataType.BOOLEAN: self.config.encoder_decoder_config.json_object_get_boolean_field,
            DataType.ARRAY: self.config.encoder_decoder_config.json_object_get_array_field
        }

        json_get_opt_mappings = {
            DataType.STRING: self.config.encoder_decoder_config.json_object_get_opt_string_field,
            DataType.NUMBER: self.config.encoder_decoder_config.json_object_get_opt_number_field,
            DataType.INTEGER: self.config.encoder_decoder_config.json_object_get_opt_integer_field,
            DataType.OBJECT: self.config.encoder_decoder_config.json_object_get_opt_object_field,
            DataType.BOOLEAN: self.config.encoder_decoder_config.json_object_get_opt_boolean_field,
            DataType.ARRAY: self.config.encoder_decoder_config.json_object_get_opt_array_field
        }

        construction_args = ', '.join([
            (json_get_mappings[v.json_data_type.value]
             if v.required else json_get_opt_mappings[v.json_data_type.value])
            .format(
                name=json_object_variable.name,
                variable_name=v.name,
                value_typename=v.data_type,
                json_decode_method_name=self.config.encoder_decoder_config.json_decode_method_name,
            ) for v in sorted_variables])

        return_value = f'\n{self.config.code_generation_config.scope_indent_character}'.join(
            textwrap.wrap(self_as_variable.resolve_constructor(self, construction_args), 75, subsequent_indent=self.config.code_generation_config.scope_indent_character*4, fix_sentence_endings=True, break_long_words=False))
        return_value += self.config.code_generation_config.statement_close
        return_value = self.indent(
            self.config.code_generation_config.method_return_template.format(name=return_value), 1)
        body += return_value

        body += "\n"
        body += self.config.code_generation_config.scope_charater_close

        return body


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file",
                        action="store", required=True, type=str)
    parser.add_argument("-c", "--config-file",
                        action="store", required=True, type=str)
    parser.add_argument("-o", "--output-file",
                        action="store", required=True, type=str)

    args = parser.parse_args()

    spec_fp = args.input_file
    spec_dir = os.path.dirname(spec_fp)

    with open(spec_fp, 'r') as f:
        data = json.load(f)

    source = ""

    config = Config.parse_file(args.config_file)

    # with open("./src/json_schema/ue_cpp_config.json", 'w') as f:
    #     json.dump(config.dict(), f)

    source += config.code_generation_config.file_start

    for module in config.code_generation_config.module_imports:
        source += config.code_generation_config.import_module_template.format(
            module_name=module) + "\n"

    source += "\n\n"

    spec = Spec(data, spec_dir, config=config)

    for dependent_spec in spec.get_dependencies():
        with open(os.path.join(spec_dir, dependent_spec), 'r') as f:
            dependent_spec_data = json.load(f)
        source += Spec(dependent_spec_data, spec_dir, config).resolve()

    source += spec.resolve()

    # print(source)

    with open(args.output_file, 'w') as f:
        f.write(source)
