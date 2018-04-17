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

allServers=domainRuntimeService.getServerRuntimes();
if (len(allServers) > 0):
	for tempServer in allServers:
		jdbcServiceRT = tempServer.getJDBCServiceRuntime();
		dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();
		if (len(dataSources) > 0):
			for dataSource in dataSources:
				print 'Data Source Name is :',  dataSource.getName()
				print 'Data Source ActiveConnectionsHighCount is :'  ,  dataSource.getActiveConnectionsHighCount()
				print 'Data Source ConnectionsTotalCount is :'  ,  dataSource.getConnectionsTotalCount()
				print 'Data Source CurrentCapacity is :',  dataSource.getCurrCapacity()
				print 'Data Source CurrCapacityHighCount is :'  ,  dataSource.getCurrCapacityHighCount()
				print 'Data Source DeploymentState is :'  ,  dataSource.getDeploymentState()
				print 'Data Source ModuleId is :'  ,  dataSource.getModuleId()
				print 'Data Source NumAvailable is :'  ,  dataSource.getNumAvailable()
				print 'Data Source NumUnavailable is :'  ,  dataSource.getNumUnavailable()
				print 'Data Source Parent is :'  ,  dataSource.getParent()
				print 'Data Source Properties is :'  ,  dataSource.getProperties()
				print 'Data Source State is :'  ,  dataSource.getState()
				print 'Data Source Type is :'  ,  dataSource.getType()
				print 'Data Source VersionJDBCDriver is :'  ,  dataSource.getVersionJDBCDriver()
				print "                                                                         "
