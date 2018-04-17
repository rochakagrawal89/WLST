####################################Script made by Abhishek Choudhury##################################################
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("weblogic.properties")
var1=config.get("properties","username")
var2=config.get("properties","password")
var3=config.get("properties","ip")
var4=config.get("properties","port")
url="t3://"+var3+":"+var4
connect(var1,var2,url)
		
ldap = cmo.getEmbeddedLDAP()
type = ldap.getType()
print "Type is :", type
print "                                                  "
print "                                                  "

var = cmo.getDomainVersion()
print "Weblogic Version is :",var
print "                                                  "
print "                                                  "

var1 = cmo.getName()
print "Domain name is :",var1
print "                                                  "
print "                                                  "

var2 = cmo.getRootDirectory()
print "Weblogic Root Directory is :",var2
print "                                                  "
print "                                                  "


clust = cmo.getClusters()
for num in clust:
	name = num.getName()
	algo = num.getDefaultLoadAlgorithm()
	mode = num.getClusterMessagingMode()
	servers = num.getServers()
	print "Cluster Name is :",name
	print "Cluster Algorithm is :",algo
	print "Cluster Mesaging Mode is :",mode
	for srv in servers:
		print "Cluster Members are :",srv.getName()
		if (srv.getAutoRestart() == 1):
			print "Auto restart is : TRUE"
		else:
			print "Auto restart is : FALSE"
		print "Default keystore is :",srv.getKeyStores()
		print "Member address is :",srv.getListenAddress()

print "                                                  "
print "                                                  "
