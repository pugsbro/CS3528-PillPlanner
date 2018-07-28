config={'user':'sam','password':'password','host':'127.0.0.1','database':'medicine','raise_on_warnings':True}

class MedInfoRetriever: 
	def getmed(self, name): 
		print ("Name entered: %s" % name)
		name = name.lower()
		temparray = name.split()
		for i in range(len(temparray)):
			temparray[i] = temparray[i][0].upper() + temparray[i][1:]
		name = " ".join(temparray)
		print ("Modified name: %s" % name)
		print ("Searching for medication with name: %s." % name)
		self.result = self.getall(name)
		self.med = Medication()
		if self.result == "False":
			return self.med
		else:
			self.med.medsetup(self.result)
			return self.med

	def getall(self, nameid):
		try:
			import mysql.connector
		except ImportError:
			print ("Could not find MySQLConnector Package. Reverting to backup...")
			med = self.usebackupfile(nameid)
			return med
		else:
			print ("Attempting connection to Database. Please wait...")
			try:
				cnx = mysql.connector.connect(**config) 
			except:
				print ("Could not establish connection to Database. Reverting to backup...")
				med = self.usebackupfile(nameid)
				return med
			else:
				med = "False"
				cursor = cnx.cursor()
				query = ("SELECT * FROM Medicine WHERE Name= '%s'") % nameid
				cursor.execute(query)
				for i in cursor:
					med = i
				self.updatebackupfile(cnx)
				cursor.close()
				cnx.close()
				return med


	def usebackupfile(self, nameid):
		try:
			with open('testdb.txt','r') as f:
				contents = f.readlines()
		except:
			print ("Could not locate backup file.")
			return False
		else:
			db = []
			for line in contents:
				dbline = line.split("#")
				if dbline[0] == '':
					del dbline[0]
				dbline[-1] = dbline[-1][:-1]
				db.append(dbline)
			#print (db)
			for i in range(len(db)-1):
				if db[i][1] == nameid:
					return db[i]
			return "False"
	
	def updatebackupfile(self, connection):
		try:
			from time import time
		except ImportError:
			print ("Could not import time module. Please update Python libraries and try again.")
		else:
			try:
				with open('testdb.txt', 'r+') as f:
					contents = f.readlines()
			except:
				print ("Could not locate file. Creating backup file...")
				with open('testdb.txt', 'w') as f:
					f.write('0')
					contents = ['0']
					print ("Backup file created.")
			#print (time())
			currenttime = time()
			if (currenttime - float(contents[-1].split()[0])) >= 60:
				print("Backup file outdated. Updating...")
				cursor = connection.cursor()
				query = ("SELECT * FROM Medicine")
				cursor.execute(query)
				with open('testdb.txt', 'r+') as f:
					for i in cursor:
						for j in range(len(i)):
							f.write("#" +str(i[j]))
						f.write('\n')
					f.write(str(time()))
				print ("Backup file updated successfully.")
				return True
			else:
				print ("Backup file is up to date.")
				return True
		
class Medication: 
	
	def __init__(self):
		self.name = "default"

	def medsetup(self,medication):
		self.name = medication[1]
		self.desc = medication[2]
		self.timegap = medication[3].split('/')
		for i in range(len(self.timegap)):
			self.timegap[i] = float(self.timegap[i])
		self.multiplicity = medication[4].split('/')
		for i in range(len(self.multiplicity)):
			self.multiplicity[i] = int(self.multiplicity[i])	
		self.maxmultiplicity = medication[5].split('/')
		for i in range(len(self.maxmultiplicity)):
			self.maxmultiplicity[i] = int(self.maxmultiplicity[i])	
		self.dosage = medication[6].split('/')
		for i in range(len(self.dosage)):
			self.dosage[i] = float(self.dosage[i])	
		self.conflicts = medication[7].split('/')


medinfo = MedInfoRetriever() 
med = medinfo.getmed('DIFFlam SpRaY ') 
print ("Medicine object name: %s." % med.name)
print ('\n'"Name:",med.name,'\n'"Description:",med.desc,'\n'"Timegap:",med.timegap,'\n'"Multiplicity:", med.multiplicity,'\n'"Max Multiplicity:",med.maxmultiplicity,'\n'"Dosage:",med.dosage,'\n'"Conflicts:",med.conflicts,'\n')
