from mysql3 import *
from algo import *
from UI_main import *


class core:
    def __init__(self):
        # constructor class
        self.medlist = {}
        self.newmedlist = []
        self.searchmed = Medicine("new med", 0, 0)
        self.medinfo = MedInfoRetriever()
        self.routines = []

    def getmedinfo(self, name):
        # searches databse for medicine
        # TODO: if there is no matching name in the database return an error
        # i would like this error to be a medication class with med.name= "error" or "notFound",
        # this would be easier to handle in the UI, but an empty(None) object
        # is possible, just let me know
        self.searchmed = medinfo.getmed(name)
        return self.searchmed

    def addmed(self, dosage, multiplicity, timegap):
        # overwrites Medication(database) object and creates Medicine(algorithm) object
        # that is used for algorithm

        self.newmed = Medicine("test", 0, 0)

        self.newmed.name = self.searchmed.name
        self.newmed.jumps = timegap
        self.newmed.dose = dosage
        self.newmed.multiplicity = multiplicity
        self.newmed.count = multiplicity
        self.newmed.conflictingMedicines = self.searchmed.conflicts

        self.medlist[self.newmed.name] = self.newmed
        return True

    def createschedule(self):
        # calls algorithm and returns schedule
        print("medlist before convert to list")
        print(self.medlist)
        del self.newmedlist[:]
        for key, value in self.medlist.items():
            temp = value
            print(temp)
            self.newmedlist.append(temp)

        print("med list before pass")
        print(self.newmedlist)



        try:
            del self.scheduler
        except Exception as e:
            pass

        self.scheduler = Scheduler()

        self.scheduler.addTime(self.routines)

        self.schedule = self.scheduler.scheduleCreate(self.newmedlist)

        return self.schedule
    
    def testme(self):
        # test function to search and print print medication info,  can be
        # removed
        print(type(self.medlist))
        self.test = self.getmedinfo("Paracetamol")
        self.addmed(0.2, 3, 8)
        print(self.medlist)
        self.test = self.getmedinfo("Ibuprofen")
        #self.addmed(0.25, 3, 5)
        print("before schedule run")
        print(self.medlist)

        self.addRoutine(0, 12, "sleeping")
        self.addRoutine(45, 48, "sleeping")
        #self.addRoutine(13, 15, "eat")
        #self.addRoutine(30, 32, "eat")

        self.finalschedule = self.createschedule()
        print(type(self.medlist))
        print(self.medlist)
        print("end of test function")


    def removeMed(self, name):
        # int index // the index of the medication in medlist, provided that it is not asynch with that in the UI
        # this can be replaced with its name, which could work better if you
        # use dictionaries like medDict= {medName:medObject}

        # using dictionarys so passing name will delete

        del self.medlist[name]

    def addRoutine(self, start, end, activity):
        # float time // clock time in half hour steps (can be 3.0, 3.5, 4.0 etc. but not inbetween and not above 23.5)
        # String activity // the thing the patient does at that time like eat, go to bed etc
        # note that going to bed means the patient sleeps until thye get up,
        # this must be handled when creating the personal schedule
        self.routines.append([start,end,activity])
        print (self.routines)
        #addTime(start, end)
    # but also remember that routines might be removed later

    def removeRoutine(self, start):
        # float time // clock time of the routine to be removed, as in addRoutine()
        # this could be changeced if there is a better parameter, depending on
        # how a list of routines is handled in the core#
        for rout in self.routines:
            if rout[0]==start:
                self.routines.remove(rout)
        
        print(self.routines)
    
        
        



if __name__ == "__main__":
        print ("starting PillPlanner from core")
        master = core()
        print ("-------------------------------------------------------")
        UI= UI_main(master)
        print ("-------------------------------------------------------")
        print ("closing PillPlanner")
