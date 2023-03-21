#!/usr/bin/python3
""" Test delete feature
"""
from models.base_model import BaseModel

dict_obj = {"name": "Taiwo Babalola", "role": "Software Engineer", "Exp": 2}
# name, new_dict = dict_obj
# print(name, new_dict)
base = BaseModel()
print(base.to_dict())
print()

base_dict = base.to_dict()
base_dict.update(**dict_obj)

base2 = BaseModel(**base_dict)

print(base2.to_dict())

new = {"name": "Teepane"}

if base2.to_dict().get("name"):
    print("yes")
    _dict = base2.to_dict()
    del _dict["name"]
    print(_dict)
    print(base2.to_dict().get("name"))
else:
    print("No")
