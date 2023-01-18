from typing import List, Union

from pydantic import BaseModel


class BigDataInputBase(BaseModel):
    yy: str
    shtm: str
    std_no: str


class BigDataInputCreate(BigDataInputBase):
    pass


class BigDataInput(BigDataInputBase):
    idx: int

    class Config:
        orm_mode = True
