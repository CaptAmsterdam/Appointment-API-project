from pydantic import BaseModel

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: int
    is_available: str

class DoctorCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: int
    is_available: str
  


doctors: dict[int, Doctors] = {
   0: Doctors(id=0, name= "Williams", specialization= "Surgery", phone= 7638, is_available= "True"),
   1: Doctors(id=1, name= "Shimi", specialization= "Internal medicine", phone= 6738, is_available= "True")
}