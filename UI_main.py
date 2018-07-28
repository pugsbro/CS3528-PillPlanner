# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 04:46:43 2018

@author: local2
"""


import sys
import UI_routines
import UI_schedule
import UI_medications
import UI_viewSched

import PyQt5
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets # important!!! this won't run unless client has PyQt5 and uses python that registers that module
# if running iwht normal python fails use Anaconda prompt to run

class UI_main:
    def __init__(self,masterIn):
    #-- initiate
        self.master=masterIn
        self.routList=[] # item format: [float start time, float end time,String actvity]
        self.medList=[] # item format: [String medName,float dose,int multiplicity, int jump]
        self.routSenseBool=False
        self.medSenseBool=False
        print("starting GUI")
        self.app= PyQt5.QtWidgets.QApplication(sys.argv)
        self.shownWindow= PyQt5.QtWidgets.QWidget()
        self.schedule()
        print("-------------")
        self.app.exec_() # keeps main thread running to prevent garbage collect
    #----

    """ setting up the windows and the navigation between them"""

    def closeWindow(self):
    #-- close the open window in order to change form without errors
        self.shownWindow.close()
        self.shownWindow.show()
        self.shownWindow= PyQt5.QtWidgets.QWidget()
    #----
    
    def viewSched(self):
        print("viewing schedule")
    #-- setup window layout
        self.viewWindow= UI_viewSched.Ui_viewSched()
        self.closeWindow()
        self.viewWindow.setupUi(self.shownWindow)
        self.shownWindow.show()
    #-- setup interactive areas
        self.viewWindow.back_to_sched.clicked.connect(self.schedule)
        self.viewWindow.createTXT.clicked.connect(self.exportSched)
    #----

    def schedule(self):
        print("entering schedule window") #------------
    #-- setup window and layout
        self.schedWindow= UI_schedule.Ui_schedule()
        self.closeWindow()
        self.schedWindow.setupUi(self.shownWindow)
        self.shownWindow.show()
    #-- setup interactive areas
        self.schedWindow.go_to_med.clicked.connect(self.medications)
        self.schedWindow.go_to_rout.clicked.connect(self.routines)
        self.schedWindow.run_sched.clicked.connect(self.run)
    #----

    def routines(self):
        print("entering routines window")
    #-- setup window and layout
        self.routWindow= UI_routines.Ui_routines()
        self.closeWindow()
        self.routWindow.setupUi(self.shownWindow)
        self.routWindow.infoText.setText("")
        self.routDisplay()
        self.shownWindow.show()
    #-- setup interactive areas /TODO/
        self.routWindow.back_to_sched.clicked.connect(self.schedule)
        self.routWindow.addRout.clicked.connect(self.addRout)
        self.routWindow.removeRout.clicked.connect(self.removeRout)
    #----

    def medications(self):
        print("entering medications window")
    #-- setup window and layout
        self.medWindow= UI_medications.Ui_medications()
        self.closeWindow()
        self.medWindow.setupUi(self.shownWindow)
        self.medWindow.instructionDisplayDose.setText("")
        self.medWindow.instructionDisplayMult.setText("")
        self.medWindow.instructionDisplayJump.setText("")
        self.medDisplay()
        self.shownWindow.show()
    #-- setup interactive areas
        self.medWindow.back_to_sched.clicked.connect(self.schedule)
        self.medWindow.addMed.clicked.connect(self.addMed)
        self.medWindow.searchMed.clicked.connect(self.searchMed)
        self.medWindow.removeMed.clicked.connect(self.removeMed)
    #----

    """actions performed based on signals from widgets"""

    def addRout(self):
    #-- retrieve start and end times for this routine and translate to half hour format used by routList
    #   this value is a float describing the number of hours after midnight. this enables half hour steps but nothing more precise is taken into account
    #   note that in the lower layers all the half hours in the day are simply numbered with integers.
        print("adding routine attempt")
        timeStart=self.routWindow.timeStart.time()
        timeStartH= float(timeStart.hour())
        if timeStart.minute() > 29:
            timeStartH+=0.5
        timeEnd=self.routWindow.timeEnd.time()
        timeEndH= float(timeEnd.hour())
        if timeEnd.minute() > 29:
            timeEndH+=0.5
    #-- get the activity for this time slot
        activity=self.routWindow.routTypeChoice.currentText()
        #-- handle routines we have not defined
        if activity=="custom routine":
            activity= self.routWindow.customRout.toPlainText()
            if activity in ['',"CustomRoutineDescription"]:
                self.routWindow.infoText.setPlainText("Please enter a custom routine description.")
                return
            if len(activity)>30:
                self.routWindow.infoText.setText("This routine description is too long, please give it a conveniently short name.")
                return
            temp=activity.replace(" ","")
            if temp=='':
                self.routWindow.infoText.setText("Please enter a custom description")
                return
        #-- handle routines that overlap
        startA=int(2*timeStartH)
        endA=int(2*timeEndH)
        for i in range(len(self.routList)):
            startB=int(2*self.routList[i][0])
            endB=int(2*self.routList[i][1])
            # if the start of A is inside B, the end is or if any part of B is inside A, they overlap
            if startA in range(startB,endB+1) or endA in range(startB,endB+1) or startB in range(startA,endA+1):
                self.routWindow.infoText.setText("This routine overlaps with the routine number '" + str(i+1) + "' that you already added.\nPlease remove in order to add this routine.")
                return
    #-- handle routines that pass over midnight and add routine(s) to lower layer
        if timeStart>timeEnd:
            if activity not in ['sleep','work']:
                if not self.routSenseBool:
                    self.routWindow.infoText.setText("This does not seem to make sense. Are you sure?\nIf so please press Add again.")
                    self.routSenseBool=True
                    return
            self.master.addRoutine(int(2*timeStartH),int(47),activity)
            self.master.addRoutine(int(0),int(2*timeEndH),activity)
        else:
            self.master.addRoutine(int(2*timeStartH),int(2*timeEndH),activity)
        self.routSenseBool=False
        self.routWindow.infoText.setText("routine added successfully.")
    #-- remember this routine and display the new and sorted list of routines
        self.routList.append([timeStartH,timeEndH,activity])
        self.routList.sort()
        self.routDisplay()
    #----            

    def routDisplay(self):
    #-- display routList on screen
        self.routWindow.customRout.setPlainText("Custom Routine Description")
        self.routList.sort()
        self.routWindow.routListDisplay.clear()
        for item in self.routList: #item= [start,end,activity]
            timeStart= item[0]
            timeEnd= item[1]
            rout= 'Between ' + str(int(timeStart))
            if int(timeStart)<timeStart:
                rout= rout + ':30 and '
            else:
                rout= rout + ':00 and '
            rout= rout + str(int(timeEnd))
            if int(timeEnd)<timeEnd:
                rout= rout + ':30 you '
            else:
                rout= rout + ':00 you '
            rout= rout + item[2]
            self.routWindow.routListDisplay.addItem(rout)
    #----


    def removeRout(self):
    # TODO removing element from an empty list
    #-- retrieve index of routine, remove it from UI list, from the lower layer and update the display
    # TODO chagne format
        print("removing routine attempted")
        index= self.routWindow.routListDisplay.currentIndex()
        if index==-1:
            return
        rout= self.routList[index] #rout= [start,end,activity]
        self.routWindow.infoText.setText("routine removed successfully.")
        del self.routList[index]
        if rout[0]>rout[1]:
            pass
            self.master.removeRoutine(int(2*rout[0]))
            self.master.removeRoutine(int(0))
        else:
            self.master.removeRoutine(int(2*rout[0]))
        self.routDisplay()
    #----


    def searchMed(self):
        #-- check if entered name makes sense i.e. if there is a name, if that med is already in the list etc
        print("search of med attempted")
        nameList=[]
        for item in self.medList:
            nameList.append(item[0])
        self.medName=self.medWindow.nameOfMed.toPlainText()
        if (self.medName=='' or self.medName=="Medication Name"):
            self.medWindow.infoText.setPlainText("Please enter a Medication name.")
            del self.medName # links to addMed test for whether searchMed has been run before
            return
        if (self.medName in nameList):
            self.medWindow.infoText.setPlainText("You are already taking this Medication. Please remove it from the list if you want to change its parameters.")
            del self.medName
            return
    #-- consult lower layers to get medication information, expected to return med.name= "error" or "notFoiund" if something is wrong
        self.med= self.master.getmedinfo(self.medName) # TODO still throws error when searching for a medication that does not exist
        med=self.med
        # TODO error returned?
        if (self.medName==med.name):
            self.medWindow.infoText.setPlainText("Medication found, please enter additional Data.")
        elif med.name=="error": # some unknown error is creating issues
            self.medWindow.infoText.setPlainText("An unknown error is causeing issues, please restart the application, your machine or contact support.")
            del self.medName
            return
        elif (med.name=="default"): # if there was no such medication in the database
            self.medWindow.infoText.setPlainText("This Medication was not found in the Database. Are you sure the spelling is correct?")
            del self.medName
            return
        else: # if the medication was not found but there was a similar name (typo etc could have created this situation)
            self.medWindow.nameOfMed.setPlainText(med.name)
            self.medWindow.infoText.setPlainText("We didn't find this name in our Database, here is what we found.")
            self.medName=med.name
    #-- enable user to choose dosage and multiplicity and let them know
        self.medWindow.instructionDisplayDose.setText("Dose of your Medication:")
        self.medWindow.instructionDisplayMult.setText("Number of Doses per Day:")
        self.medWindow.instructionDisplayJump.setText("Time between Doses:")
        self.medWindow.dosageChoice.clear()
        self.medWindow.multiplicityChoice.clear()
        self.medWindow.jumpChoice.clear()
        for dose in med.dosage:
            self.medWindow.dosageChoice.addItem(str(dose) + ' miligramms')
        for mult in range(1,med.maxmultiplicity[0]+1):
            self.medWindow.multiplicityChoice.addItem(str(mult))
        jumpMax=int(2*max(med.timegap))
        jumpMin=int(2*min(med.timegap))
        for jump in range(jumpMin,jumpMax+1):
            self.medWindow.jumpChoice.addItem(str(float(jump)/2) + ' hours')
        self.medSenseBool=False
        # ToDo: what about overwrite multiplicity?
    #----

    def medDisplay(self):
    #-- display medList on screen
        self.medWindow.medicationListDisplay.clear()
        for item in self.medList:
            med= item[0] + ' for ' + item[1] + ' microgramms, ' + item[2] + ' times a day, ' + item[3] + ' hours apart'
            self.medWindow.medicationListDisplay.addItem(med)
    #----

    def addMed(self):
        print("adding med attempt")
    #-- check if there is a medication being specified such that self.seachMed() was called previously
        try:
            self.medName
        except (NameError,AttributeError):
            self.medWindow.infoText.setPlainText("Please use the search function to find your medication in the Database first.")
            return
    #-- retrieve dosage and multiplicity, send this to the lower layer and tell the user
        dose= self.medWindow.dosageChoice.currentText()
        dose= dose.split()
        dose= (dose[0])
        mult= self.medWindow.multiplicityChoice.currentText()
        jump= self.medWindow.jumpChoice.currentText()
        jump= jump.split()
        jump= (jump[0])
        #-- check if multiplicity is above normally allowed
        if self.med.multiplicity[0]< int(mult) and not self.medSenseBool:
            self.medWindow.infoText.setText("You are taking unusually much of this Medication, \nplease make sure you have entered the correct Number of Doses per Day and press Add again." )
            self.medSenseBool=True
            return
        self.medSenseBool=False
        self.master.addmed(float(dose),int(mult),int(float(jump)))
        self.medWindow.infoText.setPlainText("Medication added successfully")
    #-- reset layout
        self.medWindow.instructionDisplayDose.setText("")
        self.medWindow.instructionDisplayMult.setText("")
        self.medWindow.instructionDisplayJump.setText("")
        self.medWindow.dosageChoice.clear()
        self.medWindow.multiplicityChoice.clear()
        self.medWindow.jumpChoice.clear()

    #-- update list of meds in the UI
        self.medList.append([self.medName,dose,mult,jump])
        self.medDisplay()
        del self.medName
    #----


    def removeMed(self):
    # TODO removing elements from an empty list
    #-- retrieve index of med to be removed, delete it from list, delete in the lower layer and update the display
        index=self.medWindow.medicationListDisplay.currentIndex()
        if index==-1:
            return
        name=self.medList[index][0]
        self.master.removeMed(name)
        del self.medList[index]
        self.medWindow.infoText.setPlainText("Medication removed successfully")
        self.medDisplay()
    #----

    def run(self): #ToDo
        print("attempting to run scheduler")
    #-- check if routines and medications are provided
        if not self.medList:
            self.schedWindow.infoText.setText("Please enter a list of Medications first.")
            return
#        if not self.routList:
#            self.schedWindow.infoText.setText("Please tell us about your routines first.")
#            return
    #-- retrieve schedule from core
        self.schedDay=self.master.createschedule()
        sched=self.schedDay
        if sched==False:
            self.schedWindow.infoText.setText("Something is wrong with this Schedule, this probably has something to do with your routines.")
            return
        self.viewSched()
    #-- output those schedule slots with medications
        for i in range(48):
            time= float(i)/2
            if int(time)<time:
                if time<10:
                    time= '0' + str(int(time))
                else:
                    time= str(int(time))
                time= time + ':30'
            else:
                if time<10:
                    time= '0' + str(int(time))
                else:
                    time= str(int(time))
                time= time + ':00'
            for med in (sched.slots[i].medicines):
                self.viewWindow.ScheduleDisplay.append('at ' + time + ' take ' + str(med.dose) + ' miligramms of ' + med.name)
    #----
    
    def exportSched(self):
    #-- export schedule on display to a txt file
        print("creating schedule file")
        self.file=open(self.schedDay.name + '.txt' , 'w')
        self.file.write("For questions or changes to your Medication please consult you Doctor or Pharmacist.")
        self.file.write("\n\n")
        for i in range(48):
            time= float(i)/2
            if int(time)<time:
                if time<10:
                    time= '0' + str(int(time))
                else:
                    time= str(int(time))
                time= time + ':30'
            else:
                if time<10:
                    time= '0' + str(int(time))
                else:
                    time= str(int(time))
                time= time + ':00'
            for med in (self.schedDay.slots[i].medicines):
                self.file.write('at ' + time + ' take ' + str(med.dose) + ' miligramms of ' + med.name + '\n')
        self.file.close()
        self.viewWindow.ScheduleDisplay.append("\n\n\nSchedule Exported successfully.")
    #----


if __name__=="__main__":
    from core import *
    master=core()
    print("starting PillPlanner from GUI")
    start=UI_main(master)
    print("----------")
    print ("closing application")
