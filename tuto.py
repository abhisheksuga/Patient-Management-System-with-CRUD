
from pydantic import BaseModel , Field ,AnyUrl ,EmailStr
from typing import List , Dict ,Optional 

class Patient(BaseModel) :
    name : str = Field(max_length=50)
    email = EmailStr
    linkdin = AnyUrl
    age : int = Field(lt= 100,gt=0) #age range validation
    weight : float = Field(gt=0)    #cant be negative 
    married : bool = False  #settinig a default value
    allergies : Optional[List[str]] = None  # optional field with a default value 
    contact_details : Dict[str,str]

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

Patient_info = {'name':'abhishek','age' : 29,'weight': 80 ,'married':True ,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1231432'}}


patient1 = Patient(**Patient_info)



insert_patient_data(patient1)