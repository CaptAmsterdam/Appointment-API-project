from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: int

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: int

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name="Mathew", age= 20, sex= 'Male', weight= 76.5, height= 90.0, phone= 6743
        ),
    1: Patients(
        id=1, name="Sarah", age= 25, sex='Female', weight= 96.5, height= 80.5, phone= 6756
        ),
    2: Patients(
        id=2, name="Wale", age= 29, sex= 'Male', weight= 76, height= 98, phone= 6745
    )
}