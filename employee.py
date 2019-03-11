  
class hospitalEmployee():
    def __init__(self, ID, lastName, firstName):
        hospitalEmployee.setID(self, ID)
        hospitalEmployee.setLastName(self, lastName)
        hospitalEmployee.setFirstName(self, firstName)
    def getID(self):
        return self._ID
    def getLastName(self):
        return self._lastName
    def getFirstName(self):
        return self._firstName
    def setID(self, ID):
        self._ID = ID
    def setLastName(self, lastName):
        self._lastName = lastName
    def setFirstName(self, firstName):
        self._firstName = firstName
    def toString(self):
        return ("HOS " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + "\n")
    
class administrator(hospitalEmployee):
    def __init__(self, ID, lastName, firstName, department):
        super().__init__(ID, lastName, firstName)
        administrator.setDepartment(self, department)
    def getDepartment(self):
        return self._department
    def setDepartment(self, department):
        self._department = department
    def toString(self):
        return ("ADM " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + administrator.getDepartment(self) + "\n")
        
class cafeManager(hospitalEmployee):
    def __init__(self, ID, lastName, firstName, cafeType):
        super().__init__(ID, lastName, firstName)
        cafeManager.setCafeType(self, cafeType)
    def getCafeType(self):
        return self._cafeType
    def setCafeType(self, cafeType):
        self._cafeType = cafeType
    def toString(self):
        return ("CFM " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + cafeManager.getCafeType(self) + "\n")

class doctor(hospitalEmployee):
    def __init__(self, ID, lastName, firstName, specialty):
        super().__init__(ID, lastName, firstName)
        doctor.setSpecialty(self, specialty)
    def getSpecialty(self):
        return self._specialty
    def setSpecialty(self, specialty):
        self._specialty = specialty
    def toString(self):
        return ("DOC " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + doctor.getSpecialty(self) + "\n")
        
class nurse(hospitalEmployee):
    def __init__(self, ID, lastName, firstName, patient):
        super().__init__(ID, lastName, firstName)
        nurse.setPatient(self, patient)
    def getPatient(self):
        return self._patient
    def setPatient(self, patient):
        self._patient = patient
    def toString(self):
        return ("NRS " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + str(nurse.getPatient(self)) + "\n")

class chef(cafeManager):
    def __init__(self, ID, lastName, firstName, cafeType, foodPrepared):
        super().__init__(ID, lastName, firstName, cafeType)
        chef.setFoodPrepared(self, foodPrepared)
    def getFoodPrepared(self):
        return self._foodPrepared
    def setFoodPrepared(self, foodPrepared):
        self._foodPrepared = foodPrepared
    def toString(self):
        return ("CHF " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + cafeManager.getCafeType(self) + " " + str(chef.getFoodPrepared(self)) + "\n")
    
class janitor(administrator):
    def __init__(self, ID, lastName, firstName, department, sweeping):
        super().__init__(ID, lastName, firstName, department)
        janitor.setSweeping(self, sweeping)
    def getSweeping(self):
        return self._sweeping
    def setSweeping(self, sweeping):
        self._sweeping = sweeping
    def toString(self):
        return ("JAN " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + administrator.getDepartment(self) + " " + janitor.getSweeping(self) + "\n")
    
class receptionist(administrator):
    def __init__(self, ID, lastName, firstName, department, answering):
        super().__init__(ID, lastName, firstName, department)
        receptionist.setAnswering(self, answering)
    def getAnswering(self):
        return self._answering
    def setAnswering(self, answering):
        self._answering = answering
    def toString(self):
        return ("REC " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + administrator.getDepartment(self) + " " + receptionist.getAnswering(self) + "\n")
    
class surgeon(doctor):
    def __init__(self, ID, lastName, firstName, specialty, operating):
        super().__init__(ID, lastName, firstName, specialty)
        surgeon.setOperating(self, operating)
    def getOperating(self):
        return self._operating
    def setOperating(self, operating):
        self._operating = operating
    def toString(self):
        return ("SGT " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + doctor.getSpecialty(self) + " " + surgeon.getOperating(self) + "\n")
    
class waiter(cafeManager):
    def __init__(self, ID, lastName, firstName, cafeType, customer):
        super().__init__(ID, lastName, firstName, cafeType)
        waiter.setCustomer(self, customer)
    def getCustomer(self):
        return self._customer
    def setCustomer(self, customer):
        self._customer = customer
    def toString(self):
        return ("WTR " + str(hospitalEmployee.getID(self)) + " " + hospitalEmployee.getLastName(self) + " " + hospitalEmployee.getFirstName(self) + " " + cafeManager.getCafeType(self) + " " + str(waiter.getCustomer(self)) + "\n")