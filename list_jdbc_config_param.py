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

allJDBCResources = cmo.getJDBCSystemResources()

print 'Test'

print 'DomainName,Datsource Name,JDBC_URL,Driver Name,Connection Reserve Timeout Seconds,Initial Capacity,Max Capacity,Min Capacity,Statement Cache Size,Shrink Frequency Seconds,Seconds To Trust An IdlePoolConnection,Connection Creation RetryFrequencySecs,Global Transactions Protocol,Test Frequency Seconds'

# JDBC Part
for jdbcResource in allJDBCResources:
    cd('/')
    dsname = jdbcResource.getName()
    datasource = False
    try:
        cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDriverParams/' + dsname + '/Properties/' + dsname )
        datasource = True 
    except:
        datasource = False
    if datasource:
        cd('/JDBCSystemResources/' + dsname )
        cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDriverParams/' + dsname + '/Properties/' + dsname)
        cd('/')
        dsurl = jdbcResource.getJDBCResource().getJDBCDriverParams().getUrl()
        drivername = jdbcResource.getJDBCResource().getJDBCDriverParams().getDriverName()
        conntimesec = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getConnectionReserveTimeoutSeconds()
        initialcapacity = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getInitialCapacity()
        maxcapacity = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getMaxCapacity()
        mincapacity = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getMinCapacity()
        shrinkfrequsec = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getShrinkFrequencySeconds()
        statementcachesize = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getStatementCacheSize()
        connretryfreq = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getConnectionCreationRetryFrequencySeconds()
        testfreqsec = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getTestFrequencySeconds()
        trustidlepoolconn = jdbcResource.getJDBCResource().getJDBCConnectionPoolParams().getSecondsToTrustAnIdlePoolConnection()
        protocol = jdbcResource.getJDBCResource().getJDBCDataSourceParams().getGlobalTransactionsProtocol()
        print 'Online Domain,'+ dsname + ',' + str(dsurl) + ',' + str(drivername) + ',' + str(conntimesec) + ',' + str(initialcapacity) + ',' + str(maxcapacity) + ',' + str(mincapacity) + ',' + str(statementcachesize) + ',' + str(shrinkfrequsec) + ',' + str(trustidlepoolconn) + ',' + str(connretryfreq) + ',' + str(protocol) + ',' + str(testfreqsec)
