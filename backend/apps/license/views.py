from datetime import datetime
from http.client import HTTPException

from asgiref.sync import sync_to_async
from ninja import Router, Form, File
from ninja.files import UploadedFile
from typing import List

from backend.apps.license.models import Region
# from backend.apps.license.models import QuantitySchool
from backend.apps.license.models import CodeLicense
from backend.apps.license.models import IssuingAuthority
from backend.apps.license.models import DBLicense

from backend.apps.license.schemas import RegionCreate
from backend.apps.license.schemas import RegionUpdate
from backend.apps.license.schemas import RegionOUT
# from backend.apps.license.schemas import QuantityOUT
# from backend.apps.license.schemas import QuantityCreate
# from backend.apps.license.schemas import QuantityUpdate
from backend.apps.license.schemas import StatusLicenseOUT
from backend.apps.license.schemas import StatusLicenseCreate
from backend.apps.license.schemas import StatusLicenseUpdate
from backend.apps.license.schemas import IssuingAuthorityOUT
from backend.apps.license.schemas import IssuingAuthorityCreate
from backend.apps.license.schemas import IssuingAuthorityUpdate
from backend.apps.license.schemas import DBLicenseOUT
from backend.apps.license.schemas import DBLicenseCreate
from backend.apps.license.schemas import DBLicenseUpdate



router = Router()

#######################
# REGION ROUTER
#######################


@router.post("/regions", response=RegionOUT)
async def create_region(request, data: RegionCreate):
    region = await sync_to_async(Region.objects.create)(**data.dict())
    return region


@router.get("/regions", response=List[RegionOUT])
async def get_region_all(request):
    regions = await sync_to_async(list)(Region.objects.all())
    return regions


@router.get("/regions/{region_id}", response=RegionOUT)
async def get_region_pk(request, region_id: int):
    region = await sync_to_async(Region.objects.get)(id=region_id)
    return region


@router.put("/regions/{region_id}", response=RegionOUT)
async def update_region(request, region_id: int, data: RegionUpdate):
    region = await sync_to_async(Region.objects.get)(id=region_id)
    for attr, value in data.dict().items():
        setattr(region, attr, value)
    await sync_to_async(region.save)()
    return region


@router.delete("/regions/{region_id}")
async def delete_region(request, region_id: int):
    region = await sync_to_async(Region.objects.get)(id=region_id)
    await sync_to_async(region.delete)()
    return {"success": True}


#######################
# ISSUING ROUTER
#######################


@router.post("/issuing", response=IssuingAuthorityOUT)
async def create_issuing(request, data: IssuingAuthorityCreate):
    issuing = await sync_to_async(IssuingAuthority.objects.create)(**data.dict())
    return issuing


@router.get("/issuing", response=List[IssuingAuthorityOUT])
async def get_issuing_all(request):
    issuing = await sync_to_async(list)(IssuingAuthority.objects.all())
    return issuing


@router.get("/issuing/{issuing_id}", response=IssuingAuthorityOUT)
async def get_issuing_pk(request, issuing_id: int):
    issuing = await sync_to_async(IssuingAuthority.objects.get)(id=issuing_id)
    return issuing


@router.put("/issuing/{issuing_id}", response=IssuingAuthorityOUT)
async def update_issuing(request, issuing_id: int, data: IssuingAuthorityUpdate):
    issuing = await sync_to_async(IssuingAuthority.objects.get)(id=issuing_id)
    for attr, value in data.dict().items():
        setattr(issuing, attr, value)
    await sync_to_async(issuing.save)()
    return issuing


@router.delete("/issuing/{issuing_id}")
async def delete_issuing(request, issuing_id: int):
    issuing = await sync_to_async(IssuingAuthority.objects.get)(id=issuing_id)
    await sync_to_async(issuing.delete)()
    return {"success": True}

# #######################
# # QUANTITIES ROUTER
# #######################
#
#
# @router.post("/quantities", response=QuantityOUT)
# async def create_quantity(request, data: QuantityCreate):
#     quantity = await sync_to_async(QuantitySchool.objects.create)(**data.dict())
#     return quantity
#
#
# @router.get("/quantities", response=List[QuantityOUT])
# async def get_quantity_all(request):
#     quantity = await sync_to_async(list)(QuantitySchool.objects.all())
#     return quantity
#
#
# @router.get("/quantities/{quantity_id}", response=QuantityOUT)
# async def get_quantity_pk(request, quantity_id: int):
#     quantity = await sync_to_async(QuantitySchool.objects.get)(id=quantity_id)
#     return quantity
#
#
# @router.put("/quantities/{quantity_id}", response=QuantityOUT)
# async def update_quantity(request, quantity_id: int, data: QuantityUpdate):
#     quantity = await sync_to_async(QuantitySchool.objects.get)(id=quantity_id)
#     for attr, value in data.dict().items():
#         setattr(quantity, attr, value)
#     await sync_to_async(quantity.save)()
#     return quantity
#
#
# @router.delete("/quantities/{quantity_id}")
# async def delete_quantity(request, quantity_id: int):
#     quantity = await sync_to_async(QuantitySchool.objects.get)(id=quantity_id)
#     await sync_to_async(quantity.delete)()
#     return {"success": True}


#######################
# STATUS ROUTER
#######################

@router.post("/status", response=StatusLicenseOUT)
async def create_status(request, data: StatusLicenseCreate):
    status = await sync_to_async(CodeLicense.objects.create)(**data.dict())
    return status

@router.get("/status", response=List[StatusLicenseOUT])
async def get_status_all(request):
    status = await sync_to_async(list)(CodeLicense.objects.all())
    return status

@router.get("/status/{status_id}", response=StatusLicenseOUT)
async def get_status_pk(request, status_id: int):
    status = await sync_to_async(CodeLicense.objects.get)(id=status_id)
    return status


@router.put("/status/{status_id}", response=StatusLicenseOUT)
async def update_status(request, status_id: int, data: StatusLicenseUpdate):
    status = await sync_to_async(CodeLicense.objects.get)(id=status_id)
    for attr, value in data.dict().items():
        setattr(status, attr, value)
    await sync_to_async(status.save)()
    return status


#######################
# LICENSE ROUTER
#######################


@router.post("/licenses", response=DBLicenseOUT)
async def create_license(
        request,
        number_register: str = Form(..., max_length=999),
        name_entity: str = Form(..., max_length=599),
        tax_name: str = Form(..., max_length=599),
        entity_address: str = Form(..., max_length=599),
        address_program: str = Form(..., max_length=599),
        cipher: str = Form(..., max_length=599),

        title_school: List[str] = Form(...),
        quantity_school: List[str] = Form(...),
        quantities: List[str] = Form(...),

        issuing_license: str = Form(..., max_length=1099),
        data_license: datetime = Form(...),
        form_number: str = Form(..., max_length=599),
        form_number_suspended: str = Form(..., max_length=2099),
        form_number_start: str = Form(..., max_length=2099),
        form_number_stop: str = Form(..., max_length=2099),
        data_address: str = Form(..., max_length=1099),
        form_number_data: str = Form(..., max_length=599),
        term: str = Form(..., max_length=599),

        file: UploadedFile = File(...),

        issuing_authorities_id: int = Form(...),
        regions_id: int = Form(...),
        code_status_id: int = Form(...),
):

    data = DBLicenseCreate(
        number_register=number_register,
        name_entity=name_entity,
        tax_name=tax_name,
        entity_address=entity_address,
        address_program=address_program,
        cipher=cipher,

        title_school=title_school,
        quantity_school=quantity_school,
        quantities=quantities,

        issuing_license=issuing_license,
        data_license=data_license,
        form_number=form_number,
        form_number_suspended=form_number_suspended,
        form_number_start=form_number_start,
        form_number_stop=form_number_stop,
        data_address=data_address,
        form_number_data=form_number_data,
        term=term,

        issuing_authorities_id=issuing_authorities_id,
        regions_id=regions_id,
        code_status_id=code_status_id,
    )

    # Получаем связанные объекты по их ID
    code_status = await sync_to_async(CodeLicense.objects.get)(id=data.code_status_id)
    issuing_authorities = await sync_to_async(IssuingAuthority.objects.get)(id=data.issuing_authorities_id)
    regions = await sync_to_async(Region.objects.get)(id=data.regions_id)

    # Создаем новый объект DBLicense с полученными объектами
    license = await sync_to_async(DBLicense.objects.create)(
        number_register=data.number_register,
        name_entity=data.name_entity,
        tax_name=data.tax_name,
        entity_address=data.entity_address,
        address_program=data.address_program,
        cipher=data.cipher,

        title_school=data.title_school,
        quantity_school=data.quantity_school,
        quantities=data.quantities,

        issuing_license=data.issuing_license,
        data_license=data.data_license,
        form_number=data.form_number,
        form_number_suspended=data.form_number_suspended,
        form_number_start=data.form_number_start,
        form_number_stop=data.form_number_stop,
        data_address=data.data_address,
        form_number_data=data.form_number_data,
        term=data.term,

        file=file,

        code_status=code_status,
        issuing_authorities=issuing_authorities,
        regions=regions,
        is_active=True,
    )
    return license


@router.get("/licenses", response=List[DBLicenseOUT])
async def get_licenses(request):
    licenses = await sync_to_async(list)(DBLicense.objects.all())
    return licenses


@router.get("/licenses/{license_id}", response=DBLicenseOUT)
async def get_license(request, license_id: int):
    license = await sync_to_async(DBLicense.objects.get)(id=license_id)
    return license


@router.put("/licenses/{license_id}", response=DBLicenseOUT)
async def update_license(request, license_id: int, data: DBLicenseUpdate):
    license = await sync_to_async(DBLicense.objects.get)(id=license_id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(license, attr, value)
    await sync_to_async(license.save)()
    return license


@router.delete("/licenses/{license_id}")
async def delete_license(request, license_id: int):
    license = await sync_to_async(DBLicense.objects.get)(id=license_id)
    await sync_to_async(license.delete)()
    return {"success": True}
