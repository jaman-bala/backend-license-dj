from asgiref.sync import sync_to_async
from ninja import Router
from typing import List

from backend.apps.license.models import Region
# from backend.apps.license.models import FormAdd
from backend.apps.license.models import CodeLicense
from backend.apps.license.models import IssuingAuthority
from backend.apps.license.models import DBLicense

from backend.apps.license.schemas import RegionCreate
from backend.apps.license.schemas import RegionUpdate
from backend.apps.license.schemas import RegionOUT
# from backend.apps.license.schemas import FormAddOUT
# from backend.apps.license.schemas import FormAddCreate
# from backend.apps.license.schemas import FormAddUpdate
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
# @router.post("/quantities", response=FormAddOUT)
# async def create_quantity(request, data: FormAddCreate):
#     quantity = await sync_to_async(FormAdd.objects.create)(**data.dict())
#     return quantity
#
#
# @router.get("/quantities", response=List[FormAddOUT])
# async def get_quantity_all(request):
#     quantity = await sync_to_async(list)(FormAdd.objects.all())
#     return quantity
#
#
# @router.get("/quantities/{quantity_id}", response=FormAddOUT)
# async def get_quantity_pk(request, quantity_id: int):
#     quantity = await sync_to_async(FormAdd.objects.get)(id=quantity_id)
#     return quantity
#
#
# @router.put("/quantities/{quantity_id}", response=FormAddOUT)
# async def update_quantity(request, quantity_id: int, data: FormAddUpdate):
#     quantity = await sync_to_async(FormAdd.objects.get)(id=quantity_id)
#     for attr, value in data.dict().items():
#         setattr(quantity, attr, value)
#     await sync_to_async(quantity.save)()
#     return quantity
#
#
# @router.delete("/quantities/{quantity_id}")
# async def delete_quantity(request, quantity_id: int):
#     quantity = await sync_to_async(FormAdd.objects.get)(id=quantity_id)
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
async def post_license(request, data: DBLicenseCreate):
    license = await sync_to_async(DBLicense.objects.create)(**data.dict())
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
