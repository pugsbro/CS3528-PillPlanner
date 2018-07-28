
from core import *
from UI_main import*

print ("starting PillPlanner")
master = core()
print ("-------------------------------------------------------")
UI= UI_main(master) # this should have its own infinite loop to prevent garbage collection
print ("-------------------------------------------------------")
print ("closing PillPlanner")