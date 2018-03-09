##### Hospital

class Patient(object):
    def __init__(self, id_number, name, allergies):
        self.id = id_number
        self.name = name
        self.allergies = allergies
        self.bed = None
    def info(self):
        print 'Bed number: {}'.format(self.bed)

class Hospital(object):
    
    def __init__(self, hospital_name, capacity, patients=[]):
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.patients = patients
        # self.inpatients = len(self.patients)
        self.beds = range(1,capacity +1)

    def admit(self, pat):
        # self.inpatients += 1
        if len(self.patients) < self.capacity:
            print 'You are admitted into hospital {}'.format(pat.name)
            self.bed = self.beds.pop()
            pat.bed = self.bed
            self.patients.append(pat)
            print 'Your bed number is {}'.format(self.bed)
        else:
            print "Hospital Full. Go Home"
    
    
    def list_pat(self):
        for info in self.patients:
            print 'Name: {}'.format(info.name)

    def discharge(self, pat):
        self.patients.pop(pat)
        self.beds.append(pat.bed)
        print self.beds
 



pat1 = Patient( 1, 'victor', 'peanuts')
pat2 = Patient( 2, 'sultan', 'almonds')
pat3 = Patient( 3, 'mish', 'chicken')
pat4 = Patient( 4, 'sam', 'beef')
pat5 = Patient( 5, 'ashley', 'shrimp')

# all_pats = [pat1, pat2, pat3, pat4, pat5]

hospital1 = Hospital('seton', 4, [])

hospital1.admit(pat1)
hospital1.admit(pat2)
hospital1.admit(pat3)
hospital1.admit(pat4)
hospital1.admit(pat5)

hospital1.list_pat()

hospital1.discharge(pat4)

hospital1.admit(pat5)



        