# Complete the function below.
from operator import attrgetter

class doctor(object):
    def __init__(self, id, name, zip, scripts, scriptValue):
        self.id = id
        self.name = name
        self.zip = zip
        self.scripts = scripts
        self.scriptValue = scriptValue

    def showDoctor(self):
        print( str(self.name) + ' ' + str(self.scriptValue) )

def sortDoc(doc):
    return doc.scriptValue


def doctor_sort(csv_string):
    doctorsArray = csv_string.split('\n')
    doctors = []
    #print(doctorsArray)
    for record in doctorsArray:
        fieldVal = record.split(',')
        #print(fieldVal)
        doc = doctor(fieldVal[0],fieldVal[1],fieldVal[2],fieldVal[3],fieldVal[4])
        doctors.append(doc)
    sortedDocs = sorted(doctors, key=sortDoc)
    for x in sortedDocs:
        x.showDoctor()
    #return ""


# creating sample doctors object list and sorted
def mySorting():
    doctors = []
    for i in range(5):
        doctors.append(doctor(i, 'name',95926+i,19+i,7-i))
    # for doc in doctors:
    #     print(doc.scriptValue)
    x = sorted(doctors, key=attrgetter('scriptValue'))
    x = sorted(doctors,key=sortDoc)
    # for doc in x:
    #     print(doc.id)


csv = """1,alex,80405,13,5
3,bob,94123,320,1.5
2,jane,94032,35,2.8
4,will,94110,31.6,6.1
5,jess,94117,48,4
6,sam,94032,31.4,9
7,jim,94036,35,19"""

#print(csv)
#doctor_sort(csv)
doctor_sort(csv)
#print(doctor_sort(csv))
#mySorting()