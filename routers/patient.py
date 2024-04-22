from fastapi import APIRouter,HTTPException, Response

from schemas.patient import patients, Patients, PatientsCreateEdit
from services.patient import PatientService

patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patients():
    if not patients:
        raise HTTPException(status_code=404, detail="No patients found")
    
    # Assuming PatientService.parse_patients() is defined to parse patient data
    data = PatientService.parse_patients(patient_data=patients)
    
    return {'message': 'Successful', 'data': data}

@patient_router.get('/{patient_id}', status_code=200)
def get_pattient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'Successful', 'data':data}

@patient_router.post('/', status_code=200)
def create_patient(payload:PatientsCreateEdit):
    data = PatientService.create_patient(payload)
    return {'message': 'Patient created Successfully', 'data': data}

#@patient_router.put('/{patient_id}', status_code=200)
#def edit_patient(patient_id: int, payload: PatientsCreateEdit):
#    curr_patient = None
#    for patient in patients:
#        if patient.id == patient_id:
#           curr_patient = patient
#           break
#    if not curr_patient:
#        raise HTTPException(status_code=404, detail="Patient not found")
#    curr_patient.name = payload.name
#    curr_patient.age = payload.age
#    curr_patient.sex = payload.sex
#    curr_patient.weight = payload.weight
#    curr_patient.height = payload.height

#    data = PatientService.edit_patient(payload)
#    return {'message': 'Edit Successful', 'data':data

@patient_router.put('/{patient_id}', status_code=200)
def edit_patient(patient_id: int, payload: PatientsCreateEdit):
    curr_patient = None
    for patient in patients:
        if patient.id == patient_id:
            curr_patient = patient
            break

    if not curr_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Update patient details
    curr_patient.name = payload.name
    curr_patient.age = payload.age
    curr_patient.sex = payload.sex
    curr_patient.weight = payload.weight
    curr_patient.height = payload.height
    
    return {'message': 'Edit Successful', 'data':curr_patient}


@patient_router.delete('/{patient_id}', status_code=200)
def delete_patient(patient_id:int):
    PatientService.delete_patient(patient_id)
    return {'message': 'Delete Successful'}
