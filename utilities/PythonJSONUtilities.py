# Copyright 2022 Aiden Soedjarwo

import json
from typing import *

class JsonUtilities:
    def __init__(self, data: Optional[dict] = {}):
        self.data = data
    
    def validate_type(self, variable: Any, type: Type):
        assert isinstance(variable, type), f"Variable must be of type {variable}"
    
    def get_string_field(self, field_name: str) -> Optional[str]:
        if self.data.get(field_name):
            self.validate_type(self.data[field_name], str)
            return self.data[field_name]
        
    def get_number_field(self, field_name: str) -> Optional[float]:
        if self.data.get(field_name):
            self.validate_type(self.data[field_name], float)
            return self.data[field_name]
    
    def get_integer_field(self, field_name: str) -> Optional[int]:
        if self.data.get(field_name):
            self.validate_type(self.data[field_name], int)
            return self.data[field_name]
    
    def get_boolean_field(self, field_name: str) -> Optional[bool]:
        if self.data.get(field_name):
            self.validate_type(self.data[field_name], bool)
            return self.data[field_name]
    
    def get_array_field(self, field_name: str) -> Optional[List[Any]]:
        if self.data.get(field_name):
            self.validate_type(self.data[field_name], list)
            return self.data[field_name]
    
    def set_string_field(self, field_name: str, value: Optional[str]):
        if value != None:
            self.validate_type(value, str)
            self.data[field_name] = value
    
    def set_number_field(self, field_name: str, value: Optional[float]):
        if value != None:
            self.validate_type(value, float)
            self.data[field_name] = value
    
    def set_integer_field(self, field_name: str, value: Optional[int]):
        if value != None:
            self.validate_type(value, int)
            self.data[field_name] = value
    
    def set_boolean_field(self, field_name: str, value: Optional[bool]):
        if value != None:
            self.validate_type(value, bool)
            self.data[field_name] = value
    
    def set_array_field(self, field_name: str, value: List[Any]):
        if value != None:
            self.validate_type(value, list)
            self.data[field_name] = value