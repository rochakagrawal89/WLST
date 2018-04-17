#!/usr/bin/python
#### Accenture ESB Team ####

# Import Required Libraries
import sys
import os
import socket

print "Imported Python Libraries"

# Connect to WebLogic
print "Connecting to WebLogic Server url='t3://N1BTFL-ESB025:7001'"
connect(username='admin', password='admin#123', url='t3://10.14.114.46:7001')


# cmo is set to DomainRuntimeMBean as the root
domainRuntime()

print 'Test'

# Deployement Status & Target

RuntimeServers=domainRuntimeService.getServerRuntimes()

print 'DomainName,Server,DataSource Name,ActiveConnectionsCurrentCount,ActiveConnectionsHighCount,ConnectionDelayTime,ConnectionsTotalCount,CurrCapacity,CurrCapacityHighCount,LeakedConnectionCount'
for server in RuntimeServers:
    runtimeJDBC = server.getJDBCServiceRuntime();
    runtimeDS = runtimeJDBC.getJDBCDataSourceRuntimeMBeans()
    serverName = server.getName()
    for dataSource in runtimeDS:
        dataSourceName = dataSource.getName()
        ActiveConnectionsCurrentCount = dataSource.getActiveConnectionsCurrentCount()
        ActiveConnectionsHighCount = dataSource.getActiveConnectionsHighCount()
        ConnectionDelayTime = dataSource.getConnectionDelayTime()
        ConnectionsTotalCount = dataSource.getConnectionsTotalCount()
        CurrCapacity = dataSource.getCurrCapacity()
        CurrCapacityHighCount = dataSource.getCurrCapacityHighCount()
        LeakedConnectionCount = dataSource.getLeakedConnectionCount()
        print 'Online4 HA Domain,'+ serverName + ',' + dataSourceName + ',' + str(ActiveConnectionsCurrentCount) + ',' + str(ActiveConnectionsHighCount) + ',' + str(ConnectionDelayTime) + ',' + str(ConnectionsTotalCount) + ',' + str(CurrCapacity) + ',' + str(CurrCapacityHighCount) + ',' + str(LeakedConnectionCount)

