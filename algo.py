# se medication scheduling algorith
# written by bradley scott
# b.scott.16@aberdeen.ac.uk
# V 1.6
# NOTES
# timejumps and conflicts work correctly

# implemented way to convert pos to time

# return schedule method added
# must find way to sort queue by number of conflicts
# medicine,day and timeslot must be made public class
# scheduleCreate must be called by core/controller to create schedule(pass it med list)
# added schedulability check

from operator import itemgetter







class Medicine:
    def __init__(self, name, multiplicity, jumps):
        self.name = name
        self.multiplicity = multiplicity
        self.jumps = jumps
        self.count = multiplicity
        self.conflictingMedicines = []

    def printName(self):
        print("name of med: %s" % self.name)

    def printConflicts(self):
        for med in self.conflictingMedicines:
            print(self.med.name)

    def addConflict(self, med):
        self.conflictingMedicines.append(self.med)


class MedSet:
    def __init__(self, name):
        self.scheduleSet = []
        #self.outputMedset = []
        #self.listSize = 0
        self.name = name

    def printMedset(self):
        for med in self.scheduleSet:
            print(med.name)

    def addMedicines(self, Meds):
        for each in Meds:
            self.scheduleSet.append(each)


class Timeslot:
    def __init__(self):
        self.available = True
        self.medicines = []


class Day:
    def __init__(self, name):
        # default day set here with sleeping, lunch and dinner times
        self.slots = [Timeslot() for x in range(48)]
        self.name = name


    def postoTime(self,pos):
      #times = pos * 48
       # return times

        if pos % 2 == 1:
            pos = pos - 1
            if pos == 0:
                return "00:30"
            else:
                pos = pos / 2
                if pos < 10:
                    return "0" + str(int(pos)) + ":30"
                else:
                    return str(int(pos)) + ":30"
        else:
            if pos == 0:
                return "00:00"
            else:
                pos = pos / 2
                if pos < 10:
                    return "0" + str(int(pos)) + ":00"
                else:
                    return str(int(pos)) + ":00"

    def printDay(self):
        i = 0
        for slot in self.slots:

            print("%s : i am free %s" % (self.postoTime(i), slot.available))
            for med in slot.medicines:

                print("%s : scheduled %s" % (self.postoTime(i), med.name))
            i += 1

    def countAvailable(self):
        i = 0
        for slot in self.slots:
            if (slot.available):
                i += 1

        return i

    def getSchedule(self):
        return self.slots

    def addTime(self, start, end):

        for i in range(start, end+1):
            self.slots[i].available = False

    def removeTime(self, start, end):

        for i in range(start, end+1):
            self.slots[i].available = True


    def enoughTime(self, schedule1, today):
        # method to check if there is enough available time to schedule
        part2 = True

        print("/////////////schedule information///////////")
        print("number of slots free self.today is: %s" % today.countAvailable())
        for med in schedule1.scheduleSet:
            print("SLOTS!!!! " ,(today.countAvailable()))
            print((med.multiplicity-1)*med.jumps)
            if ((med.multiplicity -1) * med.jumps) >= today.countAvailable()/2:
                print("%s cannot be scheduled " % med.name)
                part2 = False

        print("there is enough time to schedule your set: %s" % part2)

        return part2


# part 3 --- skip sort for now ----


# part4
class Scheduler:

    def __init__(self):
        self.today = Day("today")
        # set up schedule

        self.schedule1 = MedSet("Bradley's schedule")

    def checkConflicts(self, med, slotmeds):
        # this method checks for conflicts when inserting a medication into
        # timeslot
        conflict = False
        for each in slotmeds:
            #print("med name is %s" %med.name)
            #print("conflict set name is %s" %each.name )
            for every in each.conflictingMedicines:
                if med.name == every:
                    conflict = True

        return conflict


    # main bulk of the algorithm
    def algo(self):
        print("algorithm code debug")
        self.schedule1.printMedset()
        self.schedule1.scheduleSet.sort(key=lambda x: len(x.conflictingMedicines))
        self.schedule1.printMedset()

        for med in self.schedule1.scheduleSet:
            print ("schedulign medicine with name:" + med.name)
            while (med.count > 0):
                jumpcount = 0
                for slot in self.today.slots:
                    #print("check conflict result is: %s" %checkConflicts(med,slot.medicines))
                    if slot.available == True and med.count > 0 and jumpcount == 0 and self.checkConflicts(
                            med, slot.medicines) == False:
                        #print(" %s schedulde here "%med.name)
                        slot.medicines.append(med)
                        jumpcount = (med.jumps * 2) - 1
                        med.count = med.count - 1
                    elif jumpcount != 0:
                        jumpcount -= 1

        print(self.schedule1.scheduleSet)




    def addTime(self, routines):
        for start,end,activity in routines:
            self.today.addTime(start, end)


    def removeTime(self,start, end):
        self.today.removeTime(start, end)


    def scheduleCreate(self,meds):
        for each in meds:
            each.count= each.multiplicity
        self.schedule1.addMedicines(meds)
        for each in meds:
            print("///////the meds the algo gets is " + str(each.name))

        if (self.today.enoughTime(self.schedule1, self.today)):
            self.algo()
            print("we made a schedule maybe.....")
            self.today.printDay()
            return self.today  # day object
        else:
            return False
