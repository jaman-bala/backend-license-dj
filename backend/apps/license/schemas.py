from typing import List, Optional

from ninja import Schema, Field
from datetime import datetime


class RegionBase(Schema):
    title: str

    is_active: bool
    created_date: datetime
    updated: datetime


class RegionCreate(Schema):
    title: str


class RegionUpdate(Schema):
    title: str
    is_active: bool


class RegionOUT(Schema):
    id: int
    title: str

    class Config:
        orm_mode = True


class IssuingAuthorityBase(Schema):
    title: str

    is_active: bool
    created_date: datetime
    updated: datetime


class IssuingAuthorityCreate(Schema):
    title: str


class IssuingAuthorityUpdate(Schema):
    title: str
    is_active: bool


class IssuingAuthorityOUT(Schema):
    id: int
    title: str

    class Config:
        orm_mode = True


class StatusLicenseBase(Schema):
    title: str = None

    is_active: bool
    created_date: datetime
    updated: datetime


class StatusLicenseCreate(Schema):
    title: str = None


class StatusLicenseUpdate(Schema):
    title: str
    is_active: bool


class StatusLicenseOUT(Schema):
    id: int
    title: str

    class Config:
        orm_mode = True


class DBLicenseBase(Schema):
    number_register: Optional[str] = Field(None, max_length=999)
    name_entity: Optional[str] = Field(None, max_length=599)
    tax_name: Optional[str] = Field(None, max_length=599)
    entity_address: Optional[str] = Field(None, max_length=599)
    address_program: Optional[str] = Field(None, max_length=599)
    cipher: Optional[str] = Field(None, max_length=599)

    title_school: Optional[List[str]] = Field(None, max_length=599)
    quantity_school: Optional[List[str]] = Field(None, max_length=599)
    quantities: Optional[List[str]] = Field(None, max_length=599)

    issuing_license: Optional[str] = Field(None, max_length=1099)
    data_license: datetime
    form_number: Optional[str] = Field(None, max_length=599)
    form_number_suspended: Optional[str] = Field(None, max_length=2099)
    form_number_start: Optional[str] = Field(None, max_length=2099)
    form_number_stop: Optional[str] = Field(None, max_length=2099)
    data_address: Optional[str] = Field(None, max_length=1099)
    form_number_data: Optional[str] = Field(None, max_length=599)
    term: Optional[str] = Field(None, max_length=599)


    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None

    is_active: bool
    created_date: datetime
    updated: datetime


class DBLicenseCreate(Schema):
    number_register: Optional[str] = Field(None, max_length=999)
    name_entity: Optional[str] = Field(None, max_length=599)
    tax_name: Optional[str] = Field(None, max_length=599)
    entity_address: Optional[str] = Field(None, max_length=599)
    address_program: Optional[str] = Field(None, max_length=599)
    cipher: Optional[str] = Field(None, max_length=599)

    title_school: Optional[List[str]] = Field(None, max_length=599)
    quantity_school: Optional[List[str]] = Field(None, max_length=599)
    quantities: Optional[List[str]] = Field(None, max_length=599)

    issuing_license: Optional[str] = Field(None, max_length=1099)
    data_license: datetime
    form_number: Optional[str] = Field(None, max_length=599)
    form_number_suspended: Optional[str] = Field(None, max_length=2099)
    form_number_start: Optional[str] = Field(None, max_length=2099)
    form_number_stop: Optional[str] = Field(None, max_length=2099)
    data_address: Optional[str] = Field(None, max_length=1099)
    form_number_data: Optional[str] = Field(None, max_length=599)
    term: Optional[str] = Field(None, max_length=599)

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None


class DBLicenseUpdate(Schema):
    number_register: Optional[str] = Field(None, max_length=999)
    name_entity: Optional[str] = Field(None, max_length=599)
    tax_name: Optional[str] = Field(None, max_length=599)
    entity_address: Optional[str] = Field(None, max_length=599)
    address_program: Optional[str] = Field(None, max_length=599)
    cipher: Optional[str] = Field(None, max_length=599)

    title_school: Optional[List[str]] = Field(None, max_length=599)
    quantity_school: Optional[List[str]] = Field(None, max_length=599)
    quantities: Optional[List[str]] = Field(None, max_length=599)

    issuing_license: Optional[str] = Field(None, max_length=1099)
    data_license: datetime
    form_number: Optional[str] = Field(None, max_length=599)
    form_number_suspended: Optional[str] = Field(None, max_length=2099)
    form_number_start: Optional[str] = Field(None, max_length=2099)
    form_number_stop: Optional[str] = Field(None, max_length=2099)
    data_address: Optional[str] = Field(None, max_length=1099)
    form_number_data: Optional[str] = Field(None, max_length=599)
    term: Optional[str] = Field(None, max_length=599)

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None

    is_active: bool = None


class DBLicenseOUT(Schema):
    id: int
    number_register: Optional[str] = Field(None, max_length=999)
    name_entity: Optional[str] = Field(None, max_length=599)
    tax_name: Optional[str] = Field(None, max_length=599)
    entity_address: Optional[str] = Field(None, max_length=599)
    address_program: Optional[str] = Field(None, max_length=599)
    cipher: Optional[str] = Field(None, max_length=599)

    title_school: Optional[List[str]] = Field(None, max_length=599)
    quantity_school: Optional[List[str]] = Field(None, max_length=599)
    quantities: Optional[List[str]] = Field(None, max_length=599)

    issuing_license: Optional[str] = Field(None, max_length=1099)
    data_license: datetime
    form_number: Optional[str] = Field(None, max_length=599)
    form_number_suspended: Optional[str] = Field(None, max_length=2099)
    form_number_start: Optional[str] = Field(None, max_length=2099)
    form_number_stop: Optional[str] = Field(None, max_length=2099)
    data_address: Optional[str] = Field(None, max_length=1099)
    form_number_data: Optional[str] = Field(None, max_length=599)
    term: Optional[str] = Field(None, max_length=599)

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None

    class Config:
        orm_mode = True
