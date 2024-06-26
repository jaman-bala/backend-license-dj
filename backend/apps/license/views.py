import logging
from datetime import datetime
from http import HTTPStatus
from ninja.errors import HttpError
from django.http import HttpRequest
from asgiref.sync import sync_to_async
from ninja import Router, File, Form
from ninja.files import UploadedFile
from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError
from typing import List, Optional

from backend.apps.account.auth.jwt import AuthBearer

from backend.apps.license.models import Region
from backend.apps.license.models import CodeLicense
from backend.apps.license.models import IssuingAuthority
from backend.apps.license.models import DBLicense

from backend.apps.license.schemas import RegionCreate
from backend.apps.license.schemas import RegionUpdate
from backend.apps.license.schemas import RegionOUT
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
logger = logging.getLogger(__name__)
#######################
# REGION ROUTER
#######################


@router.post("/regions", response={HTTPStatus.CREATED: RegionOUT})
async def create_region(request: HttpRequest, data: RegionCreate):
    try:
        region = await sync_to_async(Region.objects.create)(**data.dict())
    except Exception as e:
        raise HttpError(HTTPStatus.BAD_REQUEST, f"Ошибка создания региона: {str(e)}")
    return region


@router.get("/regions", response={HTTPStatus.OK: List[RegionOUT]})
async def get_region_all(request: HttpRequest):
    try:
        regions = await sync_to_async(list)(Region.objects.all())
        if not regions:
            raise HttpError(HTTPStatus.NOT_FOUND, "В базе нет данных")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения регионов: {str(e)}")
    return regions


@router.get("/regions/{region_id}", response={HTTPStatus.OK: RegionOUT})
async def get_region_pk(request: HttpRequest, region_id: int):
    try:
        region = await sync_to_async(Region.objects.get)(id=region_id)
    except Region.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "С таким ID регион не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения региона: {str(e)}")
    return region


@router.put("/regions/{region_id}", response={HTTPStatus.OK: RegionOUT})
async def update_region(request: HttpRequest, region_id: int, data: RegionUpdate):
    try:
        region = await sync_to_async(Region.objects.get)(id=region_id)
    except Region.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Регион не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения региона: {str(e)}")

    try:
        for attr, value in data.dict().items():
            setattr(region, attr, value)
        await sync_to_async(region.save)()
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка обновления региона: {str(e)}")

    return region


@router.delete("/regions/{region_id}", response={HTTPStatus.OK: dict})
async def delete_region(request: HttpRequest, region_id: int):
    try:
        region = await sync_to_async(Region.objects.get)(id=region_id)
    except Region.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Регион не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения региона: {str(e)}")

    try:
        await sync_to_async(region.delete)()
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка удаления региона: {str(e)}")

    return {"message": "Регион удален"}


###########################
# ISSUING AUTHORITY ROUTER
###########################


@router.post("/issuing", response={HTTPStatus.CREATED: IssuingAuthorityOUT})
async def create_issuing(request: HttpRequest, data: IssuingAuthorityCreate):
    try:
        issuing = await sync_to_async(IssuingAuthority.objects.create)(**data.dict())
    except Exception as e:
        raise HttpError(HTTPStatus.BAD_REQUEST, f"Ошибка создания органа выдачи: {str(e)}")
    return issuing

@router.get("/issuing", response={HTTPStatus.OK: List[IssuingAuthorityOUT]})
async def get_issuing_all(request):
    try:
        issuing = await sync_to_async(list)(IssuingAuthority.objects.all())
        if not issuing:
            raise HttpError(HTTPStatus.NOT_FOUND, "В базе нет данных")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения органов выдачи: {str(e)}")
    return issuing

@router.get("/issuing/{issuing_id}", response={HTTPStatus.OK: IssuingAuthorityOUT})
async def get_issuing_pk(request: HttpRequest, issuing_id: int):
    try:
        issuing = await sync_to_async(IssuingAuthority.objects.get)(id=issuing_id)
    except IssuingAuthority.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "С таким ID орган выдачи не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения органа выдачи: {str(e)}")
    return issuing

@router.put("/issuing/{issuing_id}", response={HTTPStatus.OK: IssuingAuthorityOUT})
async def update_issuing(request: HttpRequest, issuing_id: int, data: IssuingAuthorityUpdate):
    try:
        issuing = await sync_to_async(IssuingAuthority.objects.get)(id=issuing_id)
    except IssuingAuthority.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Орган выдачи не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения органа выдачи: {str(e)}")

    try:
        for attr, value in data.dict().items():
            setattr(issuing, attr, value)
        await sync_to_async(issuing.save)()
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка обновления органа выдачи: {str(e)}")
    return issuing

@router.delete("/issuing/{issuing_id}", response={HTTPStatus.OK: dict})
async def delete_issuing(request: HttpRequest, issuing_id: int):
    try:
        issuing = await sync_to_async(IssuingAuthority.objects.get)(id=issuing_id)
    except IssuingAuthority.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Орган выдачи не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения органа выдачи: {str(e)}")

    try:
        await sync_to_async(issuing.delete)()
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка удаления органа выдачи: {str(e)}")
    return {"message": "Орган выдачи удален"}


#######################
# STATUS ROUTER
#######################

@router.post("/status", response={HTTPStatus.CREATED: StatusLicenseOUT})
async def create_status(request: HttpRequest, data: StatusLicenseCreate):
    try:
        status = await sync_to_async(CodeLicense.objects.create)(**data.dict())
    except Exception as e:
        raise HttpError(HTTPStatus.BAD_REQUEST, f"Ошибка создания статуса: {str(e)}")
    return status

@router.get("/status", response={HTTPStatus.OK: List[StatusLicenseOUT]})
async def get_status_all(request: HttpRequest):
    try:
        status = await sync_to_async(list)(CodeLicense.objects.all())
        if not status:
            raise HttpError(HTTPStatus.NOT_FOUND, "В базе нет данных")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения статусов: {str(e)}")
    return status

@router.get("/status/{status_id}", response={HTTPStatus.OK: StatusLicenseOUT})
async def get_status_pk(request: HttpRequest, status_id: int):
    try:
        status = await sync_to_async(CodeLicense.objects.get)(id=status_id)
    except CodeLicense.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "С таким ID статус не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения статуса: {str(e)}")
    return status

@router.put("/status/{status_id}", response={HTTPStatus.OK: StatusLicenseOUT})
async def update_status(request: HttpRequest, status_id: int, data: StatusLicenseUpdate):
    try:
        status = await sync_to_async(CodeLicense.objects.get)(id=status_id)
    except CodeLicense.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Статус не найден")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения статуса: {str(e)}")

    try:
        for attr, value in data.dict().items():
            setattr(status, attr, value)
        await sync_to_async(status.save)()
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка обновления статуса: {str(e)}")
    return status


#######################
# LICENSE ROUTER
#######################


@router.post("/licenses", response={HTTPStatus.CREATED: DBLicenseOUT})
async def post_license(request: HttpRequest,
                       payload: DBLicenseCreate,
                        ):
    try:
        # Создаем объект DBLicense без сохранения
        license = DBLicense(**payload.dict())

        # Сначала сохраняем объект без файлов
        await sync_to_async(license.save)()

        # Сохранение изменений в базе данных (если необходимо)
        await sync_to_async(license.save)()

    except ValidationError as e:
        raise HttpError(HTTPStatus.BAD_REQUEST, f"Ошибка создания лицензии: {e.message_dict}")
    except Exception as e:
        # В случае ошибки откатываем создание лицензии
        await sync_to_async(license.delete)()
        raise HttpError(HTTPStatus.BAD_REQUEST, f"Ошибка создания лицензии: {str(e)}")

    return license

@router.get("/licenses", response={HTTPStatus.OK: List[DBLicenseOUT]})
async def get_licenses(request: HttpRequest):
    try:
        licenses = await sync_to_async(list)(DBLicense.objects.all())
        if not licenses:
            raise HttpError(HTTPStatus.NOT_FOUND, "В базе нет данных")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения лицензий: {str(e)}")
    return licenses


@router.get("/licenses/{license_id}", response={HTTPStatus.OK: DBLicenseOUT})
async def get_license(request: HttpRequest, license_id: int):
    try:
        license = await sync_to_async(DBLicense.objects.get)(id=license_id)
    except DBLicense.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "С таким ID лицензия не найдена")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения лицензии: {str(e)}")
    return license


@router.put("/licenses/{license_id}", response={HTTPStatus.OK: DBLicenseOUT})
async def update_license(request: HttpRequest,
                         license_id: int,
                         data: DBLicenseUpdate,
                         ):
    # user = request.auth  # Получение текущего пользователя

    try:
        license = await sync_to_async(DBLicense.objects.get)(id=license_id)
    except DBLicense.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Лицензия не найдена")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения лицензии: {str(e)}")

    try:
        for attr, value in data.dict(exclude_unset=True).items():
            setattr(license, attr, value)

        await sync_to_async(license.save)()
    except ValidationError as e:
        raise HttpError(HTTPStatus.BAD_REQUEST, f"Ошибка обновления лицензии: {e.message_dict}")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка обновления лицензии: {str(e)}")

    return license



@router.delete("/licenses/{license_id}", response={HTTPStatus.OK: dict})
async def delete_license(request: HttpRequest, license_id: int):
    try:
        license = await sync_to_async(DBLicense.objects.get)(id=license_id)
    except DBLicense.DoesNotExist:
        raise HttpError(HTTPStatus.NOT_FOUND, "Лицензия не найдена")
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка получения лицензии: {str(e)}")

    try:
        await sync_to_async(license.delete)()
    except Exception as e:
        raise HttpError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Ошибка удаления лицензии: {str(e)}")
    return {"message": "Лицензия удалена"}
