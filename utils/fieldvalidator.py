from pydantic import BaseModel , Field ,AnyUrl ,EmailStr , field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
        valid_domains = ['hdfc.com' , 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains :
            raise ValueError ('not a valid domain')
        

        return value 
    
def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

Patient_info = {'name':'abhishek','age' : 29,'weight': 80 ,'married':True ,'allergies':['pollen','dust'],'contact_details':{'email':'abc@hdfc.com','phone':'1231432'}}


patient1 = Patient(**Patient_info)



insert_patient_data(patient1)