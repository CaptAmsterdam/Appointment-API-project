from fastapi import APIRouter, Response

from schemas.doctor import doctors, DoctorCreateEdit
from services.doctor import DoctorsService



doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctors():
    data = DoctorsService.parse_doctors(doctor_data=doctors)
    return {'message': 'Successful', 'data': data}

@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctors_by_id(doctor_id: int):
    data = DoctorsService.get_doctors_by_id(doctor_id)
    return {'message': 'successful', 'data': data}

@doctor_router.post('/', status_code=200)
def create_doctor(payload: DoctorCreateEdit):
    data = DoctorsService.create_doctor(payload)
    return {'message': 'created successfully', 'data':data}

@doctor_router.put('/{doctor_id}',status_code=200)
def edit_doctor(doctor_id: int, payload: DoctorCreateEdit):
    data = DoctorsService.edit_doctor(payload)
    return {'message': 'edit successful', 'data': data}

@doctor_router.delete('/{doctor_id}')
def delete_doctor(doctor_id:int,):
    DoctorsService.delete_doctor(doctor_id)
    return{'message': 'Deleted Successfully',}

