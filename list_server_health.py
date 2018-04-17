#!/usr/bin/python
#### Accenture ESB Team ####

# Import Required Libraries
import sys
import os
import socket
import thread

def monitor_thread():
 print "Imported Python Libraries"

 # Connect to WebLogic
# Connect to WebLogic
print "Connecting to WebLogic Server url='t3://N1BTFL-ESB025:7001'"
connect(username='admin', password='admin#123', url='t3://10.14.114.46:7001')


 # cmo is set to DomainRuntimeMBean as the root
 domainRuntime()

 print 'Test'

 # Deployement Status & Target

 RuntimeServers=domainRuntimeService.getServerRuntimes()
 for server in RuntimeServers:
     serverName=server.getName()
     cd('ServerRuntimes/' + serverName)
     OpenSocketsCurrentCount = cmo.getOpenSocketsCurrentCount()
     cd('ServerRuntimes/' + serverName + '/ThreadPoolRuntime/ThreadPoolRuntime')
     StandbyThreadCount = cmo.getStandbyThreadCount()
     Throughput = cmo.getThroughput()
     HoggingThreadCount = cmo.getHoggingThreadCount()
     ExecuteThreadTotalCount = cmo.getExecuteThreadTotalCount()
     ExecuteThreadIdleCount = cmo.getExecuteThreadIdleCount()
#     print 'ServerName,'+  serverName
#     print 'OpenSocketsCurrentCount,'+  str(OpenSocketsCurrentCount)
#     print 'StandbyThreadCount,'+  str(StandbyThreadCount)
#     print 'Throughput,'+  str(Throughput)
#     print 'HoggingThreadCount,'+  str(HoggingThreadCount)
#     print 'ExecuteThreadTotalCount,'+  str(ExecuteThreadTotalCount)
#     print 'ExecuteThreadIdleCount,'+  str(ExecuteThreadIdleCount)
     print 'Online Domain,'+ serverName +','+ str(OpenSocketsCurrentCount) +','+ str(StandbyThreadCount) +','+ str(Throughput) +','+ str(HoggingThreadCount) +','+ str(ExecuteThreadTotalCount) +','+ str(ExecuteThreadIdleCount)
     print '\n'
     #print serverName
     #print '\n'

if __name__== "main":
     monitor_thread()
     disconnect()
