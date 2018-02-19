####################################Script made by Rochak Agrawal#################################################
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("weblogic.properties")
var1=config.get("properties","username")
var2=config.get("properties","password")
var3=config.get("properties","ip")
var4=config.get("properties","port")
url="t3://"+var3+":"+var4
connect(var1,var2,url)

var1 = cmo.getName()
apps=cmo.getAppDeployments()
for a in apps:
	name = a.getName()
	print "Application Name :",name
	path = a.getAbsoluteSourcePath()
	print "Application Path :",path
	print "                           "
	target = a.getTargets()
	for tgt in target:
		target_name = tgt.getName()
		target_type = tgt.getType()
		print "Application Target Name :",target_name 
		print "Application Target Type :",target_type
		print "                           "
	
print "                                                  "
print "                                                  "
	
cd ('SelfTuning')
cd (var1)
cd ('WorkManagers')

wm=cmo.getWorkManagers()	
for i in wm:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\Capacities')
cp=cmo.getCapacities()
for i in cp:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\ContextRequestClasses')
crc=cmo.getContextRequestClasses()
for i in crc:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\FairShareRequestClasses')
frc=cmo.getFairShareRequestClasses()
for i in frc:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\MaxThreadsConstraints')
maxtc=cmo.getMaxThreadsConstraints()
for i in maxtc:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\MinThreadsConstraints')
mintc=cmo.getMinThreadsConstraints()
for i in mintc:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\ResponseTimeRequestClasses')
rtrc=cmo.getResponseTimeRequestClasses()
for i in rtrc:
	print i.getName()
	
print "                                                  "
print "                                                  "
	
cd ('..\ResponseTimeRequestClasses')
rtrc=cmo.getResponseTimeRequestClasses()
for i in rtrc:
	print i.getName()

print "                                                  "
print "                                                  "
