
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("weblogic.properties")
var1=config.get("properties","username")
var2=config.get("properties","password")
var3=config.get("properties","ip")
var4=config.get("properties","port")
url="t3://"+var3+":"+var4
connect(var1,var2,url)

allJMSResources = cmo.getJMSSystemResources()
for jmsResource in allJMSResources:
		module = jmsResource.getName()
		descfile = jmsResource.getDescriptorFileName()
		print "                   "
		print "Module Name", module
		FgnServ = jmsResource.getJMSResource().getForeignServers()
		for member in FgnServ:
			print "Foreign Server Name is :", member.getName()
			print member.getName()," has JNDI NAME as :", member.getInitialContextFactory()
			print "                   "
			FgnConnFact = member.getForeignConnectionFactories()
			for m in FgnConnFact:
				print "Foreign Connection factory Name is :", m.getName()
				print m.getName()," has LOCALJNDINAME as :", m.getLocalJNDIName()
				print m.getName()," has REMOTEJNDINAME as :", m.getRemoteJNDIName()
				print "                   "
			FgnDest = member.getForeignDestinations()
			for z in FgnDest:
				print "Foreign Destination Name is :", z.getName()
				print z.getName()," has LOCALJNDINAME as :", z.getLocalJNDIName()
				print z.getName()," has REMOTEJNDINAME as :", z.getRemoteJNDIName()
				print "                   "
			jndiprop = member.getJNDIProperties()
			for x in jndiprop:
				print "JNDI Value is :", x.getValue()
				print "                   "
