from employee import administrator, cafeManager, chef, doctor, hospitalEmployee, janitor, nurse, receptionist, surgeon, waiter
import os

answering = []
cafeType = []
category = []
customer = []
department = []
firstName = []
foodPrepared = []
ID = []
lastName = []
operating = []
patient = []
specialty = []
sweeping = []
xans = []
xcft = []
xcat = []
xcst = []
xdep = []
xfdp = []
xfst = []
xid = []
xlst = []
xops = []
xpat = []
xspe = []
xswp = []  

def loadFile():
    if (os.path.exists("Employee List.txt") == False):
        ofstream = open("Employee List.txt", "w")
        ofstream.close()
    ifstream = open("Employee List.txt", "r")
    if (os.stat("Employee List.txt").st_size == 0):
        print()
    else:
        print()
        lines = ifstream.readlines()
        for line in lines:
            if (line[:3] == "ADM"):
                CATG, IDEN, LSTN, FSTN, DEPT = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append(DEPT)
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append('')
            elif (line[:3] == "CFM"):
                CATG, IDEN, LSTN, FSTN, CFET = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append(CFET)
                category.append(CATG)
                customer.append(0)
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append('')
            elif (line[:3] == "CHF"):
                CATG, IDEN, LSTN, FSTN, CFET, FOOD = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append(CFET)
                category.append(CATG)
                customer.append(0)
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(int(FOOD))
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append('')
            elif (line[:3] == "DOC"):
                CATG, IDEN, LSTN, FSTN, SPEC = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append(SPEC)
                sweeping.append('')
            elif (line[:3] == "HOS"):
                CATG, IDEN, LSTN, FSTN = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append('')
            elif (line[:3] == "JAN"):
                CATG, IDEN, LSTN, FSTN, DEPT, SWEP = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append(DEPT)
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append(SWEP)
            elif (line[:3] == "NRS"):
                CATG, IDEN, LSTN, FSTN, PATI = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(int(PATI))
                specialty.append('')
                sweeping.append('')
            elif (line[:3] == "REC"):
                CATG, IDEN, LSTN, FSTN, DEPT, ANSW = line.strip("\n").split(" ")
                answering.append(ANSW)
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append(DEPT)
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append('')
            elif (line[:3] == "SGT"):
                CATG, IDEN, LSTN, FSTN, SPEC, OPER = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append('')
                category.append(CATG)
                customer.append(0)
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append(OPER)
                patient.append(0)
                specialty.append(SPEC)
                sweeping.append('')
            elif (line[:3] == "WTR"):
                CATG, IDEN, LSTN, FSTN, CFET, CUST = line.strip("\n").split(" ")
                answering.append('')
                cafeType.append(CFET)
                category.append(CATG)
                customer.append(int(CUST))
                department.append('')
                firstName.append(FSTN)
                foodPrepared.append(0)
                ID.append(int(IDEN))
                lastName.append(LSTN)
                operating.append('')
                patient.append(0)
                specialty.append('')
                sweeping.append('')
    ifstream.close()
def mainMenu():
    b0 = False
    while (b0 == False):
         b0 = True
         for x in range(1, len(ID), 1):
              if (ID[x - 1] > ID[x]):
                   b0 = False
                   ANSW = answering[x]
                   CFET = cafeType[x]
                   CATG = category[x]
                   CUST = customer[x]
                   DEPT = department[x]
                   FSTN = firstName[x]
                   FOOD = foodPrepared[x]
                   IDEN = ID[x]
                   LSTN = lastName[x]
                   OPER = operating[x]
                   PATI = patient[x]
                   SPEC = specialty[x]
                   SWEP = sweeping[x]
                   answering[x] = answering[x - 1]
                   cafeType[x] = cafeType[x - 1]
                   category[x] = category[x - 1]
                   customer[x] = customer[x - 1]
                   department[x] = department[x - 1]
                   firstName[x] = firstName[x - 1]
                   foodPrepared[x] = foodPrepared[x - 1]
                   ID[x] = ID[x - 1]
                   lastName[x] = lastName[x - 1]
                   operating[x] = operating[x - 1]
                   patient[x] = patient[x - 1]
                   specialty[x] = specialty[x - 1]
                   sweeping[x] = sweeping[x - 1]
                   answering[x - 1] = ANSW
                   cafeType[x - 1] = CFET
                   category[x - 1] = CATG
                   customer[x - 1] = CUST
                   department[x - 1] = DEPT
                   firstName[x - 1] = FSTN
                   foodPrepared[x - 1] = FOOD
                   ID[x - 1] = IDEN
                   lastName[x - 1] = LSTN
                   operating[x - 1] = OPER
                   patient[x - 1] = PATI
                   specialty[x - 1] = SPEC
                   sweeping[x - 1] = SWEP
    b0 = False
    while (b0 == False):
        print("Please choose the following ")
        print("1 - Add Employee")
        print("2 - Drop Employee")
        print("3 - Modify Employee")
        print("4 - Save Employees")
        print("5 - View Employees")
        print("0 - EXIT")
        select0 = int(input(": "))
        if (select0 > -1 and select0 < 6):
            b0 = True
        else:
            print("ERROR: Please enter a valid integer")
    if (select0 == 1):
        addEmployee()
    elif (select0 == 2):
        dropEmployee()
    elif (select0 == 3):
        modifyEmployee()
    elif (select0 == 4):
        saveEmployee()
    elif (select0 == 5):
        viewEmployee()
def addEmployee():
    b1 = False
    while (b1 == False):
        print()
        print("Add which Employee?")
        print("1 - Administrator")
        print("2 - Cafe Manager")
        print("3 - Chef")
        print("4 - Doctor")
        print("5 - Hospital Employee")
        print("6 - Janitor")
        print("7 - Nurse")
        print("8 - Receptionist")
        print("9 - Surgeon")
        print("10 - Waiter")
        print("0 - RETURN TO MAIN MENU")
        select1 = int(input(": "))
        if (select1 > -1 and select1 < 11):
            b1 = True
        else:
            print("ERROR: Please enter a valid integer")
    if (select1 > 0):
        ANS = ''
        CFT = ''
        CST = 0
        CTG = ''
        DPT = ''
        FSN = ''
        FDP = 0
        IDN = 0
        LSN = ''
        OPS = ''
        PAT = 0
        SPC = ''
        SWP = ''
        b1 = False
        while (b1 == False):
            b1 = True
            for x in range(0, len(ID), 1):
                if (IDN == ID[x]):
                    b1 = False
            if (b1 == False):
                IDN += 1
        LSN = input("Please enter the Employee's Last Name: ")
        FSN = input("Please enter the Employee's First Name: ")
        if (select1 == 1 or select1 == 6 or select1 == 8):
            DPT = input("Please enter the Department: ")
            if (select1 == 6):
                b2 = False
                while (b2 == False):
                    SWP = input("(Y/N) Is the Employee Sweeping? ")
                    if (SWP == "Y" or SWP == "y" or SWP == "N" or SWP == "n"):
                        b2 = True
                        if (SWP == "y"):
                            SWP = "Y"
                        elif (SWP == "n"):
                            SWP = "N"
                    else:
                        print("ERROR: Please enter Y or N")
            elif (select1 == 8):
                b2 = False
                while (b2 == False):
                    ANS = input("(Y/N) Is the Employee Answering Calls? ")
                    if (ANS == "Y" or ANS == "y" or ANS == "N" or ANS == "n"):
                        b2 = True
                        if (ANS == "y"):
                            ANS = "Y"
                        elif (ANS == "n"):
                            ANS = "N"
                    else:
                        print("ERROR: Please enter Y or N")
        elif (select1 == 2 or select1 == 3 or select1 == 10):
            CFT = input("Please enter the Cafe Type: ")
            if (select1 == 3):
                b2 = False
                while (b2 == False):
                    FDP = int(input("Please enter the amount of Food(s) prepared: "))
                    if (FDP > -1):
                        b2 = True
                    else:
                        print("ERROR: Please enter a number equal to or greater than 0")
            elif (select1 == 10):
                b2 = False
                while (b2 == False):
                    CST = int(input("Please enter the amount of Customer(s): "))
                    if (CST > -1):
                        b2 = True
                    else:
                        print("ERROR: Please enter a number equal to or greater than 0")
        elif (select1 == 4 or select1 == 9):
            SPC = input("Please enter the Employee's Specialty: ")
            if (select1 == 9):
                b2 = False
                while (b2 == False):
                    OPS = input("(Y/N) Does this Employee Operate? ")
                    if (OPS == "Y" or OPS == "y" or OPS == "N" or OPS == "n"):
                        b2 = True
                        if (OPS == "y"):
                            OPS = "Y"
                        elif (OPS == "n"):
                            OPS = "N"
                    else:
                        print("ERROR: Please enter Y or N")
        elif (select1 == 7):
            b2 = False
            while (b2 == False):
                PAT = int(input("Please enter the number of Patient(s): "))
                if (PAT > -1):
                    b2 = True
                else:
                    print("ERROR: Please enter a number equal to or greater than 0")
        if (select1 == 1):
            CTG = "ADM"
        elif (select1 == 2):
            CTG = "CFM"
        elif (select1 == 3):
            CTG = "CHF"
        elif (select1 == 4):
            CTG = "DOC"
        elif (select1 == 5):
            CTG = "HOS"
        elif (select1 == 6):
            CTG = "JAN"
        elif (select1 == 7):
            CTG = "NRS"
        elif (select1 == 8):
            CTG = "REC"
        elif (select1 == 9):
            CTG = "SGT"
        elif (select1 == 10):
            CTG = "WTR"
        b1 = False
        while (b1 == False):
            print("Are these correct? ")
            print("Position = ", getPosition(CTG))
            print("Name =", FSN, LSN, sep = ' ')
            if (select1 == 1 or select1 == 6 or select1 == 8):
                print("Department :", DPT, sep = ' ')
                if (select1 == 6):
                    print("Sweeping :", SWP, sep = ' ')
                elif (select1 == 8):
                    print("Answering :", ANS, sep = ' ')
            elif (select1 == 2 or select1 == 3 or select1 == 10):
                print("Café Type :", CFT, sep = ' ')
                if (select1 == 3):
                    if (FDP > 1):
                        print("Foods Prepared:", FDP, sep = ' ')
                    else:
                        print("Food Prepared:", FDP, sep = ' ')
                elif (select1 == 10):
                    if (CST > 1):
                        print("Customers:", CST, sep = ' ')
                    else:
                        print("Customer:", CST, sep = ' ')
            elif (select1 == 4 or select1 == 9):
                print("Specialty :", SPC, sep = ' ')
                if (select1 == 9):
                    print("Operating :", OPS, sep = ' ')
            elif (select1 == 7):
                if (PAT > 1):
                    print("Patients :", PAT, sep = ' ')
                else:
                    print("Patient :", PAT, sep = ' ')
            select2 = input("(Y/N) : ")
            if (select2 == "Y" or select2 == "y" or select2 == "N" or select2 == "n"):
                b1 = True
                if (select2 == "y"):
                     select2 = "Y"
                elif (select2 == "n"):
                     select2 = "N"
            else:
                print("ERROR: Please enter Y or N")
        if (select2 == "Y"):
            answering.append(ANS)
            cafeType.append(CFT)
            customer.append(CST)
            category.append(CTG)
            department.append(DPT)
            firstName.append(FSN)
            foodPrepared.append(FDP)
            ID.append(IDN)
            lastName.append(LSN)
            operating.append(OPS)
            patient.append(PAT)
            specialty.append(SPC)
            sweeping.append(SWP)
        b1 = False
        while (b1 == False):
            print("What would you like to do?")
            print("1 - CREATE ANOTHER EMPLOYEE")
            print("2 - RETURN TO MAIN MENU")
            select3 = int(input(": "))
            if (select3 == 1 or select3 == 2):
                b1 = True
            else:
                print("ERROR: Please enter the correct integer")
        if (select3 == 1):
            addEmployee()
        else:
            mainMenu()
    elif (select1 == 0):
        mainMenu()
def dropEmployee():
    print()
    b0 = False
    while (b0 == False):
        print("Which of the employees you wish to drop?")
        for x in range(0, len(ID), 1):
            print(x, firstName[x], lastName[x], sep = " ")
        print("-1 - RETURN TO MAIN MENU")
        select0 = int(input(": "))
        if (select0 > -1 and select0 < len(ID)):
            print("Are you sure you want to delete this employee?")
            print("NAME: ", firstName[select0], " ", lastName[select0])
            if (category[select0] == "ADM" or category[select0] == "JAN" or category[select0] == "REC"):
                print("DEPARTMENT:", department[select0], sep = " ")
                if (category[select0] == "JAN"):
                    print("SWEEPING:", sweeping[select0], sep = " ")
                elif (category[select0] == "REC"):
                    print("ANSWERING:", answering[select0], sep = " ")
            elif (category[select0] == "CFM" or category[select0] == "CHF" or category[select0] == "WTR"):
                print("CAFE TYPE:", cafeType[select0], sep = " ")
                if (category[select0] == "CHF" and foodPrepared[select0] <= 1):
                    print("FOOD PREPARED:", foodPrepared[select0], sep = " ")
                elif (category[select0] == "CHF" and foodPrepared[select0] > 1):
                    print("FOODS PREPARED:", foodPrepared[select0], sep = " ")
                elif (category[select0] == "WTR" and customer[select0] <= 1):
                    print("CUSTOMER:", customer[select0], sep = " ")
                elif (category[select0] == "WTR" and customer[select0] > 1):
                    print("CUSTOMERS:", customer[select0], sep = " ")
            elif (category[select0] == "DOC" or category[select0] == "SGT"):
                print("SPECIALTY:", specialty[select0], sep = " ")
                if (category[select0] == "SGT"):
                    print("OPERATING:", operating[select0], sep = " ")
            elif (category[select0] == "NRS" and patient[select0] <= 1):
                print("PATIENT:", patient[select0], sep = " ")
            elif (category[select0] == "NRS" and patient[select0] > 1):
                print("PATIENTS:", patient[select0], sep = " ")
            select1 = input("(Y/N): ")
            if (select1 == "Y" or select1 == "y" or select1 == "N" or select1 == "n"):
                b0 = True
            else:
                print("ERROR: Please enter Y or N")
        elif (select0 == -1):
             b0 = True
        else:
            print("ERROR: Please enter the correct integer")
    if (select0 == -1):
        mainMenu()
    else:
        answering.remove(answering[select0])
        cafeType.remove(cafeType[select0])
        category.remove(category[select0])
        customer.remove(customer[select0])
        department.remove(department[select0])
        firstName.remove(firstName[select0])
        foodPrepared.remove(foodPrepared[select0])
        ID.remove(ID[select0])
        lastName.remove(lastName[select0])
        operating.remove(operating[select0])
        patient.remove(patient[select0])
        specialty.remove(specialty[select0])
        sweeping.remove(sweeping[select0])
        b0 = False
        while (b0 == False):
            select2 = input("Drop another Employee? (Y/N) : ")
            if (select2 == "Y" or select2 == "y" or select2 == "N" or select2 == "n"):
                b0 = True
            else:
                print("ERROR: Please enter Y or N")
        if (select2 == "Y" or select2 == "y"):
            dropEmployee()
        else:
            mainMenu()
def modifyEmployee():
    print()
    b0 = False
    while (b0 == False):
        print("Which of the employees you wish to change?")
        for x in range(0, len(ID), 1):
            print(x, firstName[x], lastName[x], sep = " ")
        print("-1 - RETURN TO MAIN MENU")
        select0 = int(input(": "))
        if (select0 > -2 and select0 < len(ID)):
            print("Are you sure you want to change this employee?")
            print("NAME:", firstName[select0], lastName[select0], sep = " ")
            if (category[select0] == "ADM" or category[select0] == "JAN" or category[select0] == "REC"):
                print("DEPARTMENT:", department[select0], sep = " ")
                if (category[select0] == "JAN"):
                    print("SWEEPING:", sweeping[select0], sep = " ")
                elif (category[select0] == "REC"):
                    print("ANSWERING:", answering[select0], sep = " ")
            elif (category[select0] == "CFM" or category[select0] == "CHF" or category[select0] == "WTR"):
                print("CAFE TYPE:", cafeType[select0], sep = " ")
                if (category[select0] == "CHF" and foodPrepared[select0] <= 1):
                    print("FOOD PREPARED:", foodPrepared[select0], sep = " ")
                elif (category[select0] == "CHF" and foodPrepared[select0] > 1):
                    print("FOODS PREPARED:", foodPrepared[select0], sep = " ")
                elif (category[select0] == "WTR" and customer[select0] <= 1):
                    print("CUSTOMER:", customer[select0], sep = " ")
                elif (category[select0] == "WTR" and customer[select0] > 1):
                    print("CUSTOMERS:", customer[select0], sep = " ")
            elif (category[select0] == "DOC" or category[select0] == "SGT"):
                print("SPECIALTY:", specialty[select0], sep = " ")
                if (category[select0] == "SGT"):
                    print("OPERATING:", operating[select0], sep = " ")
            elif (category[select0] == "NRS" and patient[select0] <= 1):
                print("PATIENT:", patient[select0], sep = " ")
            elif (category[select0] == "NRS" and patient[select0] > 1):
                print("PATIENTS:", patient[select0], sep = " ")
            select1 = input("(Y/N): ")
            if (select1 == "Y" or select1 == "y" or select1 == "N" or select1 == "n"):
                b0 = True
            else:
                print("ERROR: Please enter Y or N")
        else:
            print("ERROR: Please enter the correct integer")
    if (select0 == -1):
        mainMenu()
    else:
        ANS = ""
        CFT = ""
        CST = 0
        CTG = ""
        DPT = ""
        FSN = firstName[select0]
        FDP = 0
        LSN = lastName[select0]
        OPS = ""
        PAT = 0
        SPC = ""
        SWP = ""
        b0 = False
        while (b0 == False):
            print("What is the job title for ", FSN, " ", LSN, "? ")
            print("1 - Administrator")
            print("2 - Cafe Manager")
            print("3 - Chef")
            print("4 - Doctor")
            print("5 - Hospital Employee")
            print("6 - Janitor")
            print("7 - Nurse")
            print("8 - Receptionist")
            print("9 - Surgeon")
            print("10 - Waiter")
            select1 = int(input(": "))
            if (select1 > 0 and select1 < 11):
                b0 = True
            else:
                print("ERROR: Please enter the correct integer")
        if (select1 == 1):
            CTG = "ADM"
            DPT = input("Please enter the Department :")
        elif (select1 == 2):
            CTG = "CFM"
            CFT = input("Please enter the Café Type :")
        elif (select1 == 3):
            CTG = "CHF"
            CFT = input("Please enter the Café Type :")
            b1 = False
            while (b1 == False):
                FDP = int(input("Please select the number of Food(s) Prepared :"))
                if (FDP > -1):
                    b1 = True
                else:
                    print("ERROR: Please enter the correct integer")
        elif (select1 == 4):
            CTG = "DOC"
            SPC = input("Please enter the Specialty :")
        elif (select1 == 5):
            CTG = "JAN"
            DPT = input("Please enter the Department :")
            b1 == False
            while (b1 == False):
                SWP = input("Does this employee Sweep? (Y/N) : ")
                if (SWP == "Y" or SWP == "y" or SWP == "N" or SWP == "n"):
                    b1 = True
                    if (SWP == "y"):
                        SWP = "Y"
                    elif (SWP == "n"):
                        SWP = "N"
        elif (select1 == 7):
            CTG = "NRS"
            
        elif (select1 == 8):
            CTG = "REC"
            DPT = input("Please enter the Department :")
            b1 == False
            while (b1 == False):
                ANS = input("Does this employee Answer calls? (Y/N) : ")
                if (ANS == "Y" or ANS == "y" or ANS == "N" or ANS == "n"):
                    b1 = True
                    if (ANS == "y"):
                        ANS = "Y"
                    elif (ANS == "n"):
                        ANS = "N"
        elif (select1 == 9):
            CTG = "SGT"
            SPC = input("Please enter the Specialty :")
            b1 == False
            while (b1 == False):
                OPS = input("Does this employee Operate? (Y/N) : ")
                if (OPS == "Y" or OPS == "y" or OPS == "N" or OPS == "n"):
                    b1 = True
                    if (OPS == "y"):
                        OPS = "Y"
                    elif (OPS == "n"):
                        OPS = "N"
        elif (select1 == 10):
            CTG = "WTR"
            CFT = input("Please enter the Café Type :")
            while (b1 == False):
                CST = int(input("Please select the number of Customer(s) :"))
                if (CST > -1):
                    b1 = True
                else:
                    print("ERROR: Please enter the correct integer")
        b2 = False
        while (b2 == False):
            print("Is the following correct? ")
            print("NAME:", FSN, LSN, sep = ' ')
            print("ID:", ID, sep = ' ')
            if (CTG == "ADM" or CTG == "JAN" or CTG == "REC"):
                print("DEPARTMENT:", DPT, sep = ' ')
                if (CTG == "JAN"):
                    print("SWEEPING:", SWP, sep = ' ')
                elif (CTG == "REC"):
                    print("ANSWERING:", ANS, sep = ' ')
            elif (CTG == "CFM" or CTG == "CHF" or CTG == "WTR"):
                print("CAFE TYPE:", CFT, sep = ' ')
                if (CTG == "CHF"):
                    if (FDP < 2):
                        print("FOOD PREPARED:", FDP, sep = ' ')
                    else:
                        print("FOODS PREPARED:", FDP, sep = ' ')
                elif (CTG == "WTR"):
                    if (CST < 2):
                        print("CUSTOMER:", CST, sep = ' ')
                    else:
                        print("CUSTOMERS:", CST, sep = ' ')
            elif (CTG == "DOC" or CTG == "SGT"):
                print("SPECIALTY:", SPC, sep = ' ')
                if (CTG == "SGT"):
                    print("OPERATING:", OPS, sep = ' ')
            elif (CTG == "NRS"):
                if (PAT < 2):
                    print("PATIENT:", PAT, sep = ' ')
                else:
                    print("PATIENTS:", PAT, sep = ' ')
            select2 = input("(Y/N) : ")
            if (select2 == "Y" or select2 == "y" or select2 == "N" or select2 == "n"):
                b2 = True
            else:
                print("ERROR: Please select Y or N")
        if (select2 == "Y" or select2 == "y"):
            answering[select0] = ""
            cafeType[select0] = ""
            category[select0] = ""
            customer[select0] = 0
            department[select0] = ""
            foodPrepared[select0] = 0
            operating[select0] = ""
            patient[select0] = 0
            specialty[select0] = ""
            sweeping[select0] = ""
            if (CTG == "ADM"):
                department[select0] = DPT
            elif (CTG == "CFM"):
                cafeType[select0] = CFT
            elif (CTG == "CHF"):
                cafeType[select0] = CFT
                foodPrepared[select0] = FDP
            elif (CTG == "DOC"):
                specialty[select0] = SPC
            elif (CTG == "JAN"):
                department[select0] = DPT
                sweeping[select0] = SWP
            elif (CTG == "NRS"):
                patient[select0] = PAT
            elif (CTG == "REC"):
                department[select0] = DPT
                answering[select0] = ANS
            elif (CTG == "SGT"):
                specialty[select0] = SPC
                operating[select0] = OPS
            elif (CTG == "WTR"):
                cafeType[select0] = CFT
                customer[select0] = CST
        b3 = False
        while (b3 == False):
            print("What would you like to do?")
            print("1 - CHANGE ANOTHER EMPLOYEE")
            print("2 - RETURN TO MAIN MENU")
            select3 = int(input(": "))
            if (select3 == 1 or select3 == 2):
                b3 = True
            else:
                print("ERROR: Please enter the correct integer")
        if (select3 == 1):
            modifyEmployee()
        elif (select3 == 2):
            mainMenu()
def saveEmployee():
    print()
    ofstream = open("Employee List.txt", "w")
    for x in range(0, len(ID), 1):
        if (category[x] == "ADM"):
            ad = administrator(ID[x], lastName[x], firstName[x], department[x])
            ofstream.write(ad.toString())
        elif (category[x] == "CFM"):
            cf = cafeManager(ID[x], lastName[x], firstName[x], cafeType[x])
            ofstream.write(cf.toString())
        elif (category[x] == "CHF"):
            ch = chef(ID[x], lastName[x], firstName[x], cafeType[x], foodPrepared[x])
            ofstream.write(ch.toString())
        elif (category[x] == "DOC"):
            dr = doctor(ID[x], lastName[x], firstName[x], specialty[x])
            ofstream.write(dr.toString())
        elif (category[x] == "HOS"):
            hs = hospitalEmployee(ID[x], lastName[x], firstName[x])
            ofstream.write(hs.toString())
        elif (category[x] == "JAN"):
            jn = janitor(ID[x], lastName[x], firstName[x], department[x], sweeping[x])
            ofstream.write(jn.toString())
        elif (category[x] == "NRS"):
            nr = nurse(ID[x], lastName[x], firstName[x], patient[x])
            ofstream.write(nr.toString())
        elif (category[x] == "REC"):
            rc = receptionist(ID[x], lastName[x], firstName[x], department[x], answering[x])
            ofstream.write(rc.toString())
        elif (category[x] == "SGT"):
            sg = surgeon(ID[x], lastName[x], firstName[x], specialty[x], operating[x])
            ofstream.write(sg.toString())
        elif (category[x] == "WTR"):
            wt = waiter(ID[x], lastName[x], firstName[x], cafeType[x], customer[x])
            ofstream.write(wt.toString())
    ofstream.close()
    mainMenu()
def viewEmployee():
    print()
    cadm = 0
    ccfm = 0
    cchf = 0
    cdoc = 0
    chos = 0
    cjan = 0
    cnrs = 0
    crec = 0
    csgt = 0
    cwtr = 0
    b0 = False
    for x in range(0, len(ID), 1):
        if (category[x] == "ADM"):
            cadm += 1
        elif (category[x] == "CFM"):
            ccfm += 1
        elif (category[x] == "CHF"):
            cchf += 1
        elif (category[x] == "DOC"):
            cdoc += 1
        elif (category[x] == "HOS"):
            chos += 1
        elif (category[x] == "JAN"):
            cjan += 1
        elif (category[x] == "NRS"):
            cnrs += 1
        elif (category[x] == "REC"):
            crec += 1
        elif (category[x] == "SGT"):
            csgt += 1
        elif (category[x] == "WTR"):
            cwtr += 1
    for x in range(0, len(ID), 1):
        xans.append(answering[x])
        xcft.append(cafeType[x])
        xcat.append(category[x])
        xcst.append(customer[x])
        xdep.append(department[x])
        xfst.append(firstName[x])
        xfdp.append(foodPrepared[x])
        xid.append(ID[x])
        xlst.append(lastName[x])
        xops.append(operating[x])
        xpat.append(patient[x])
        xspe.append(specialty[x])
        xswp.append(sweeping[x])
    b0 = False
    while (b0 == False):
        b0 = True
        for x in range(1, len(xid), 1):
            if (xlst[x - 1] > xlst[x]):
                b0 = False
                tans = xans[x]
                tcft = xcft[x]
                tcat = xcat[x]
                tcst = xcst[x]
                tdep = xdep[x]
                tfdp = xfdp[x]
                tfst = xfst[x]
                tid = xid[x]
                tlst = xlst[x]
                tops = xops[x]
                tpat = xpat[x]
                tspe = xspe[x]
                tswp = xswp[x]
                xans[x] = xans[x - 1]
                xcft[x] = xcft[x - 1]
                xcat[x] = xcat[x - 1]
                xcst[x] = xcst[x - 1]
                xdep[x] = xdep[x - 1]
                xfdp[x] = xfdp[x - 1]
                xfst[x] = xfst[x - 1]
                xid[x] = xid[x - 1]
                xlst[x] = xlst[x - 1]
                xops[x] = xops[x - 1]
                xpat[x] = xpat[x - 1]
                xspe[x] = xspe[x - 1]
                xswp[x] = xswp[x - 1]
                xans[x - 1] = tans
                xcft[x - 1] = tcft
                xcat[x - 1] = tcat
                xcst[x - 1] = tcst
                xdep[x - 1] = tdep
                xfdp[x - 1] = tfdp
                xfst[x - 1] = tfst
                xid[x - 1] = tid
                xlst[x - 1] = tlst
                xops[x - 1] = tops
                xpat[x - 1] = tpat
                xspe[x - 1] = tspe
                xswp[x - 1] = tswp
            elif ((xlst[x - 1] == xlst[x]) and (xfst[x - 1] > xfst[x])):
                b0 = False
                tans = xans[x]
                tcft = xcft[x]
                tcat = xcat[x]
                tdep = xdep[x]
                tfdp = xfdp[x]
                tfst = xfst[x]
                tid = xid[x]
                tlst = xlst[x]
                tops = xops[x]
                tpat = xpat[x]
                tspe = xspe[x]
                tswp = xswp[x]
                xans[x] = xans[x - 1]
                xcft[x] = xcft[x - 1]
                xcat[x] = xcat[x - 1]
                xdep[x] = xdep[x - 1]
                xfdp[x] = xfdp[x - 1]
                xfst[x] = xfst[x - 1]
                xid[x] = xid[x - 1]
                xlst[x] = xlst[x - 1]
                xops[x] = xops[x - 1]
                xpat[x] = xpat[x - 1]
                xspe[x] = xspe[x - 1]
                xswp[x] = xswp[x - 1]
                xans[x - 1] = tans
                xcft[x - 1] = tcft
                xcat[x - 1] = tcat
                xdep[x - 1] = tdep
                xfdp[x - 1] = tfdp
                xfst[x - 1] = tfst
                xid[x - 1] = tid
                xlst[x - 1] = tlst
                xops[x - 1] = tops
                xpat[x - 1] = tpat
                xspe[x - 1] = tspe
                xswp[x - 1] = tswp
            elif ((xlst[x - 1] == xlst[x]) and (xfst[x - 1] == xfst[x]) and (xid[x - 1] > xid[x])):
                b0 = False
                tans = xans[x]
                tcft = xcft[x]
                tcat = xcat[x]
                tdep = xdep[x]
                tfdp = xfdp[x]
                tfst = xfst[x]
                tid = xid[x]
                tlst = xlst[x]
                tops = xops[x]
                tpat = xpat[x]
                tspe = xspe[x]
                tswp = xswp[x]
                xans[x] = xans[x - 1]
                xcft[x] = xcft[x - 1]
                xcat[x] = xcat[x - 1]
                xdep[x] = xdep[x - 1]
                xfdp[x] = xfdp[x - 1]
                xfst[x] = xfst[x - 1]
                xid[x] = xid[x - 1]
                xlst[x] = xlst[x - 1]
                xops[x] = xops[x - 1]
                xpat[x] = xpat[x - 1]
                xspe[x] = xspe[x - 1]
                xswp[x] = xswp[x - 1]
                xans[x - 1] = tans
                xcft[x - 1] = tcft
                xcat[x - 1] = tcat
                xdep[x - 1] = tdep
                xfdp[x - 1] = tfdp
                xfst[x - 1] = tfst
                xid[x - 1] = tid
                xlst[x - 1] = tlst
                xops[x - 1] = tops
                xpat[x - 1] = tpat
                xspe[x - 1] = tspe
                xswp[x - 1] = tswp
    b0 = False
    if (cadm > 0):
        cot = 0
        b0 = True
        print("ADMINISTRATOR")
        print()
        if (cadm == 1):
            print("There is currently 1 Administrator")
        else:
            print("There are currently " + cadm + " Administrators")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "DEPARTMENT")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "ADM"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xdep[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (ccfm > 0):
        cot = 0
        b0 = True
        print("CAFE MANAGER")
        print()
        if (ccfm == 1):
            print("There is currently 1 Café Manager")
        else:
            print("There are currently " + ccfm + " Café Managers")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "CAFE TYPE")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "CFM"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xcft[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (cchf > 0):
        cot = 0
        b0 = True
        print("CHEF")
        print()
        if (cchf == 1):
            print("There is currently 1 Chef")
        else:
            print("There are currently " + cchf + " Chefs")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "CAFE TYPE", '%20s' % "FOOD(S) PREPARED")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "CHF"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xcft[x], '%20s' % xfdp[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (cdoc > 0):
        cot = 0
        b0 = True
        print("DOCTOR")
        print()
        if (cdoc == 1):
            print("There is currently 1 Doctor")
        else:
            print("There are currently " + cdoc + " Doctors")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "SPECIALTY")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "DOC"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xspe[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (chos > 0):
        cot = 0
        b0 = True
        print("HOSPITAL EMPLOYEE")
        print()
        if (chos == 1):
            print("There is currently 1 Hospital Employee")
        else:
            print("There are currently " + chos + " Hospital Employees")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "HOS"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (cjan > 0):
        cot = 0
        b0 = True
        print("JANITOR")
        print()
        if (cjan == 1):
            print("There is currently 1 Janitor")
        else:
            print("There are currently " + cjan + " Janitors")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "DEPARTMENT", '%20s' % "SWEEPING")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "JAN"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xdep[x], '%20s' % xswp[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (cnrs > 0):
        cot = 0
        b0 = True
        print("NURSE")
        print()
        if (cnrs == 1):
            print("There is currently 1 Nurse")
        else:
            print("There are currently " + cnrs + " Nurses")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "PATIENTS")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "NRS"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xpat[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (crec > 0):
        cot = 0
        b0 = True
        print("RECEPTIONIST")
        print()
        if (crec == 1):
            print("There is currently 1 Receptionist")
        else:
            print("There are currently " + crec + " Receptionists")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "DEPARTMENT", '%20s' % "ANSWERING")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "REC"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xdep[x], '%20s' % xans[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (csgt > 0):
        cot = 0
        b0 = True
        print("SERGEANT")
        print()
        if (csgt == 1):
            print("There is currently 1 Surgeon")
        else:
            print("There are currently " + csgt + " Surgeons")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "SPECIALTY", '%20s' % "OPERATING")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "SGT"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xspe[x], '%20s' % xops[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (cwtr > 0):
        cot = 0
        b0 = True
        print("WAITER")
        print()
        if (cwtr == 1):
            print("There is currently 1 Waiter")
        else:
            print("There are currently " + cwtr + " Waiters")
        print()
        print()
        print('%5s' % "#", '%20s' % "LAST NAME", '%20s' % "FIRST NAME", '%10s' % "ID", '%20s' % "CAFE TYPE", '%20s' % "CUSTOMER(S)")
        format("==")
        print()
        for x in range(0, len(xid), 1):
            if (xcat[x] == "WTR"):
                print('%5s' % cot, '%20s' % xlst[x], '%20s' % xfst[x], '%10s' % xid[x], '%20s' % xcft[x], '%20s' % xcst[x])
                print()
                cot += 1
        print()
        input("Press Enter to continue...")
    if (b0 == False):
        print("There are currently no employees")
    mainMenu()    
def getPosition(p):
    if (p == "ADM"):
        return "Administrator"
    elif (p == "CFM"):
        return "Café Manager"
    elif (p == "CHF"):
        return "Chef"
    elif (p == "DOC"):
        return "Doctor"
    elif (p == "HOS"):
        return "Hospital Employee"
    elif (p == "JAN"):
        return "Janitor"
    elif (p == "NRS"):
        return "Nurse"
    elif (p == "REC"):
        return "Receptionist"
    elif (p == "SGT"):
        return "Surgeon"
    elif (p == "WTR"):
        return "Waiter"
    
def format(f):
    for x in range(0, 50, 1):
        print(f, end = '', sep = '')