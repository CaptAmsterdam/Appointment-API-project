# from pydantic import BaseModel
# from datetime import date

# from schemas.patient import Patients, patients
# from schemas.doctor import Doctors, doctors

# class Appointments(BaseModel):
#     id: int
#     patient: Patients
#     doctor: Doctors
#     date: date(2024,4,4)

# class AppointmentsCreateEdit(BaseModel):
#     patient: Patients
#     doctor: Doctors
#     date: date(2024,4,4)

# appointments: dict[ optional [int], Appointments] ={
#     0: Appointments (id=0, patient=patients[0], doctor=doctors[0],date= date(2024,4,4)),
#     1: Appointments (id=1, patient=patients[1], doctor=doctors[1],date= date(2024,6,14))
# }

from pydantic import BaseModel
from enum import Enum

from schemas.patient import Patients, patients
from schemas.doctor import Doctors, doctors

class AppointmentStatus(Enum):
    completed = "COMPLETED"
    pending = "PENDING"

class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: str


class AppointmentsCreateEdit(BaseModel):
    patient: Patients
    doctor: Doctors
    date: str

appointments: dict[int, Appointments] = {
    0: Appointments(id=0, patient=patients[0], doctor=doctors[0], date='2024-4-4'),  
    1: Appointments(id=1, patient=patients[1], doctor=doctors[1], date='2024-6-14') 
}
