from fastapi import HTTPException
from schemas.patient import patients, Patients, PatientsCreateEdit

class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data = []
        for pat in patient_data:
            data.append(patients[pat])
        return data
        
    @staticmethod
    def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found', status_code=404)
        return patient
    
    @staticmethod
    def create_patient(patient_data: PatientsCreateEdit):
        id= len(patients)
        patient= Patients(
            id=id,
            **patient_data.model_dump()
        )
        patients[id] = patient
        return patient
    
    @staticmethod
    def edit_patient(payload: PatientsCreateEdit):
        id = len(patients)
        patient = patients(
            id=id,
            **payload.model_dump()
        )
        patients[id]= patient
        return patient
    
    @staticmethod
    def delete_patient(patient_id:int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException (detail= 'Patient not found', status_code=404)
        del patients[patient_id]
        