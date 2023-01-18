from typing import Union
from pydantic import BaseModel

class Student(BaseModel):
    stdNo: str
    name: Union[str, None] = None

