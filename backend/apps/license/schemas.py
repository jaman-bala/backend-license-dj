from typing import List, Optional
from ninja import Schema
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
    number_register: Optional[str]
    name_entity: Optional[str]
    tax_name: Optional[str]
    entity_address: Optional[str]
    address_program: Optional[str]
    cipher: Optional[str]
    issuing_license: Optional[str]
    data_license: datetime
    form_number: Optional[str]
    form_number_suspended: Optional[str]
    form_number_start: Optional[str]
    form_number_stop: Optional[str]
    data_address: Optional[str]
    form_number_data: Optional[str]
    term: Optional[str]

    title_school: List[str] = None
    quantity_school: List[str] = None
    quantities: List[str] = None

    file: Optional[str]

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None

    is_active: bool
    created_date: datetime
    updated: datetime

class DBLicenseCreate(Schema):
    number_register: Optional[str]
    name_entity: Optional[str]
    tax_name: Optional[str]
    entity_address: Optional[str]
    address_program: Optional[str]
    cipher: Optional[str]
    issuing_license: Optional[str]
    data_license: datetime
    form_number: Optional[str]
    form_number_suspended: Optional[str]
    form_number_start: Optional[str]
    form_number_stop: Optional[str]
    data_address: Optional[str]
    form_number_data: Optional[str]
    term: Optional[str]

    title_school: List[str] = None
    quantity_school: List[str] = None
    quantities: List[str] = None

    file: Optional[str]

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None

class DBLicenseUpdate(Schema):
    number_register: Optional[str]
    name_entity: Optional[str]
    tax_name: Optional[str]
    entity_address: Optional[str]
    address_program: Optional[str]
    cipher: Optional[str]
    issuing_license: Optional[str]
    data_license: datetime
    form_number: Optional[str]
    form_number_suspended: Optional[str]
    form_number_start: Optional[str]
    form_number_stop: Optional[str]
    data_address: Optional[str]
    form_number_data: Optional[str]
    term: Optional[str]

    title_school: List[str] = None
    quantity_school: List[str] = None
    quantities: List[str] = None

    file: Optional[str]

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None


class DBLicenseOUT(Schema):
    id: int
    number_register: Optional[str]
    name_entity: Optional[str]
    tax_name: Optional[str]
    entity_address: Optional[str]
    address_program: Optional[str]
    cipher: Optional[str]
    issuing_license: Optional[str]
    data_license: datetime
    form_number: Optional[str]
    form_number_suspended: Optional[str]
    form_number_start: Optional[str]
    form_number_stop: Optional[str]
    data_address: Optional[str]
    form_number_data: Optional[str]
    term: Optional[str]

    title_school: List[str] = None
    quantity_school: List[str] = None
    quantities: List[str] = None

    file: Optional[str]

    issuing_authorities_id: Optional[int] = None
    regions_id: Optional[int] = None
    code_status_id: Optional[int] = None

    class Config:
        orm_mode = True
