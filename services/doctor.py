from fastapi import HTTPException
from schemas.doctor import doctors, Doctors, DoctorCreateEdit

class DoctorsService:

    @staticmethod
    def parse_doctors(doctor_data):
        data = []
        for doc in doctor_data:
            data.append(doctors[doc])
        return data
    
    @staticmethod
    def get_doctors_by_id(doctors_id):
        doctor = doctors.get(doctors_id)
        if not doctor:
            raise HTTPException(detail="Doctor not found", status_code=404)
        return doctor
    
    @staticmethod
    def create_doctor(doctor_data: DoctorCreateEdit):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **doctor_data.model_dump()
        )
        doctors[id] = doctor
        return doctor
    
    @staticmethod
    def edit_doctor(payload: DoctorCreateEdit):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **payload.model_dump()
        )
        doctors[id] = doctor
        return doctor

    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            return HTTPException(detail='Doctor not found', status_code=404)
        del doctors[doctor_id]