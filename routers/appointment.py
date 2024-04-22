from fastapi import APIRouter, Depends, HTTPException

from schemas.appointment import AppointmentStatus, appointments, Appointments, AppointmentsCreateEdit
from services.appointment import AppointmentService


appointments_router = APIRouter()


@appointments_router.get('/', status_code=200)
def list_appointmets():
    if not appointments:
        raise HTTPException(status_code=404, detail='No Appointment found')
    data = AppointmentService.parse_appointments(appointment_data=appointments)

    return  {'message': 'Successful', 'data': data}

@appointments_router.post('/', status_code=200)
def create_appointment(payload: AppointmentsCreateEdit = Depends(AppointmentService.check_availability)):
    patient_id: int =payload.patient_id
    appointment_id = len(appointments)
    new_appointment = Appointments(
        id= appointment_id,
        patient_id=patient_id,
        customers = patient_id
    )
    appointments.append(new_appointment)
    return {'message': 'Successful', 'data': appointments}

@appointments_router.post ('/process_appointment/{appointment_id}', status_code=200)
def process_appointment (appointment_id: int = Depends (AppointmentService.check_availability)):
    for appointment in appointments:
       if appointment.id == appointment_id:
            appointment.status = AppointmentStatus.completed.value
            return {'message': 'Successful', 'data': appointment}

