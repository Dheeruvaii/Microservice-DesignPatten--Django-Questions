"""
PYDANTIC:It is a Python library that provides data validation and parsing capabilities for data serialization and deserialization

1.Data Model:
            A data model in Pydantic is defined using a Python class that inherits from the pydantic.BaseModel class. The data model class represents the structure and validation rules for a particular set of data.
            It typically consists of attributes with type annotations and optional validation constraints.
            eg.py:
            from pydantic import BaseModel
            class User(BaseModel):
                name: str
                age: int
                email: str


2.Validation:
            Pydantic performs automatic data validation based on the defined data model. When you create an instance of the data model class and provide input data.
            Pydantic validates the input against the defined types and constraints.
            It checks if the input conforms to the expected structure and raises validation errors if any discrepancies are found.
            eg2.py:
            user_data = {
            "name": "John Doe",
            "age": 30,
            "email": "john@example.com"
                }
        user = User(**user_data) 
3.Parsing and Serialization:
            Pydantic also provides functionality for parsing and serializing data. 
            It can automatically convert raw input data (e.g., JSON, dictionaries) into instances of the defined data model class, and vice versa.
            This parsing and serialization capability simplifies the handling of data from different sources and formats.
            eg3.py
            Parsing JSON data into a User instance
            import json

            json_data = '{"name": "Jane Smith", "age": 25, "email": "jane@example.com"}'
            user = User.parse_raw(json_data)

            # Serializing a User instance into JSON data
            json_data = user.json()

"""