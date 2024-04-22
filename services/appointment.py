from fastapi import HTTPException
from schemas.appointment import appointments, Appointments, AppointmentsCreateEdit
from schemas.doctor import doctors, DoctorCreateEdit, Doctors
from schemas.patient import patients, Patients, PatientsCreateEdit

class AppointmentService:

    @staticmethod
    def parse_appointments(appointment_data):
        data = []
        for appoint in appointment_data:
            data.append(appointments[appoint])
        return data
        
    @staticmethod
    def create_appointment (appointment_data: AppointmentsCreateEdit):
        id = len(appointments)
        appointment= Appointments(
            id=id,
            **appointment_data.model_dump()
        )
        appointments[id] = appointment
        return appointment
    
    @staticmethod
    def check_availability(payload: AppointmentsCreateEdit):
        doctors_id = payload.appointments
        for doctor_id in doctors_id:
            doctor: Doctors = doctors.get(int, (doctors_id))
            if doctor.is_available(False):
                raise HTTPException(status_code=400, detail='Doctor not available')
            doctor.is_available(True)
        return payload