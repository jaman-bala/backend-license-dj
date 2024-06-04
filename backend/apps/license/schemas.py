from ninja import Schema, Field
from datetime import datetime


class RegionBase(Schema):
    title: str

    is_active: bool
    created_date: datetime
    updated: datetime


class RegionCreate(RegionBase):
    pass


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


class IssuingAuthorityCreate(IssuingAuthorityBase):
    pass


class IssuingAuthorityUpdate(Schema):
    title: str
    is_active: bool


class IssuingAuthorityOUT(Schema):
    id: int
    title: str

    class Config:
        orm_mode = True


class QuantityBase(Schema):
    title: str

    is_active: bool
    created_date: datetime
    updated: datetime


class QuantityCreate(QuantityBase):
    pass


class QuantityUpdate(Schema):
    title: str
    is_active: bool


class QuantityOUT(Schema):
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
    number_register: str = Field(None, max_length=599)
    name_entity: str = Field(None, max_length=599)
    tax_name: str = Field(None, max_length=599)
    entity_address: str = Field(None, max_length=599)
    address_program: str = Field(None, max_length=599)
    cipher: str = Field(None, max_length=599)
    title_school: str = Field(None, max_length=599)
    quantity_school: str = Field(None, max_length=599)
    issuing_license: str = Field(None, max_length=599)
    data_license: datetime
    form_number: str = Field(None, max_length=599)
    form_number_suspended: str = Field(None, max_length=599)
    form_number_start: str = Field(None, max_length=599)
    form_number_stop: str = Field(None, max_length=599)
    data_address: str = Field(None, max_length=599)
    form_number_data: str = Field(None, max_length=599)

    file: str = None
    issuing_authorities_id: int = None
    regions_id: int = None
    quantities_id: int = None
    code_status_id: int = None

    is_active: bool
    created_date: datetime
    updated: datetime


class DBLicenseCreate(Schema):
    number_register: str = Field(None, max_length=599)
    name_entity: str = Field(None, max_length=599)
    tax_name: str = Field(None, max_length=599)
    entity_address: str = Field(None, max_length=599)
    address_program: str = Field(None, max_length=599)
    cipher: str = Field(None, max_length=599)
    title_school: str = Field(None, max_length=599)
    quantity_school: str = Field(None, max_length=599)
    issuing_license: str = Field(None, max_length=599)
    data_license: datetime
    form_number: str = Field(None, max_length=599)
    form_number_suspended: str = Field(None, max_length=599)
    form_number_start: str = Field(None, max_length=599)
    form_number_stop: str = Field(None, max_length=599)
    data_address: str = Field(None, max_length=599)
    form_number_data: str = Field(None, max_length=599)

    file: str = None
    issuing_authorities_id: int = None
    regions_id: int = None
    quantities_id: int = None
    code_status_id: int = None


class DBLicenseUpdate(Schema):
    number_register: str = Field(None, max_length=599)
    name_entity: str = Field(None, max_length=599)
    tax_name: str = Field(None, max_length=599)
    entity_address: str = Field(None, max_length=599)
    address_program: str = Field(None, max_length=599)
    cipher: str = Field(None, max_length=599)
    title_school: str = Field(None, max_length=599)
    quantity_school: str = Field(None, max_length=599)
    issuing_license: str = Field(None, max_length=599)
    data_license: datetime = None
    form_number: str = Field(None, max_length=599)
    form_number_suspended: str = Field(None, max_length=599)
    form_number_start: str = Field(None, max_length=599)
    form_number_stop: str = Field(None, max_length=599)
    data_address: str = Field(None, max_length=599)
    form_number_data: str = Field(None, max_length=599)

    file: str = None
    issuing_authorities_id: int = None
    regions_id: int = None
    quantities_id: int = None
    code_status_id: int = None

    is_active: bool = None


class DBLicenseOUT(Schema):
    id: int
    number_register: str = Field(None, max_length=599)
    name_entity: str = Field(None, max_length=599)
    tax_name: str = Field(None, max_length=599)
    entity_address: str = Field(None, max_length=599)
    address_program: str = Field(None, max_length=599)
    cipher: str = Field(None, max_length=599)
    title_school: str = Field(None, max_length=599)
    quantity_school: str = Field(None, max_length=599)
    issuing_license: str = Field(None, max_length=599)
    data_license: datetime
    form_number: str = Field(None, max_length=599)
    form_number_suspended: str = Field(None, max_length=599)
    form_number_start: str = Field(None, max_length=599)
    form_number_stop: str = Field(None, max_length=599)
    data_address: str = Field(None, max_length=599)
    form_number_data: str = Field(None, max_length=599)

    file: str = None
    issuing_authorities_id: int = None
    regions_id: int = None
    quantities_id: int = None
    code_status_id: int = None

    class Config:
        orm_mode = True
