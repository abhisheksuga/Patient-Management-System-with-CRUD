#To export pydantic models as json object 


from pydantic import BaseModel 



class Address(BaseModel):

    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address


address_dict = {'city' : 'gurugaon','state' :' haryana' , 'pin' : '560503'}

address1 = Address(**address_dict)

patient_dict = {'name':'abhi','gender':'male','age':29,'address': address1}

patient1 = Patient(**patient_dict)


temp = patient1.model_dump()

print(temp)
print(temp['address']['city'])