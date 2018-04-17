import java.lang
import os
import string
import time
from java.io import FileInputStream
from time import gmtime, strftime
import datetime


now = datetime.datetime.now()
outfile = open("/home/wladmin/splunk/DomainMonitorXml/domainstats.xml", "w")
propInputStream = FileInputStream("/home/wladmin/splunk/DomainMonitorXml/SubjectDetails.properties")
configProps = Properties()
configProps.load(propInputStream)

def connnectToAdminServer(connUri,adminUserName,password):
         connect(adminUserName,password,connUri);

def monitorServerStatus() :
   print >>outfile, "<serverInfo>"
   cd('ServerRuntimes')
   servers=domainRuntimeService.getServerRuntimes()
   for server in servers:
       print >>outfile,"<servers><Server>%s</Server><ServerState>%s</ServerState><ListenAddress>%s</ListenAddress><ListenPort>%s</ListenPort><Healthstatus>%s</Healthsta
tus></servers>"%(server.getName(),server.getState(),           server.getListenAddress(),str(server.getListenPort()),getHealthStateInformation(server.getHealthState()))
   print >>outfile, "</serverInfo>"

def serverAllstatus() :
   domainConfig()
   serverList = cmo.getServers()
   domainRuntime()
   cd('/ServerLifeCycleRuntimes/')
   print >> outfile, "<serverState>"
   for server in serverList:
    name = server.getName()
    cd(name)
    serverState = cmo.getState()
    print >> outfile, "<servers><server>" + name + "</server><state>" + serverState + "</state></servers>"
    cd('..')
   print >> outfile, "</serverState>"


def monitorThreadStatus() :
    print >>outfile, "<ThreadInfo>"
    DSlist=["null"]

    servers=domainRuntimeService.getServerRuntimes()
    for sname in servers:
     cd("/ServerLifeCycleRuntimes/" + sname.getName())
     serverState = cmo.getState()
     if serverState == "RUNNING"   :
       cd("/ServerRuntimes/" + sname.getName())
       if cmo.getThreadPoolRuntime() is not  None:
          atuning(sname.getName())

    print >>outfile, "</ThreadInfo>"

def atuning(sname):
    cd("/ServerRuntimes/" + sname)
    cd("ThreadPoolRuntime/ThreadPoolRuntime/")
    #cmd = "echo " + "Server ThreadPool Information:" +" >> Domain_Monitoring_Output_file"
    print >>outfile,"<servers><Server>%s</Server><HealthState>%s</HealthState><CompletedRequestCount>%s</CompletedRequestCount><HoggingThreadCount>%s</HoggingThreadCoun
t><PendingUserRequestCount>%s</PendingUserRequestCount><StandbyThreadCount>%s</StandbyThreadCount></servers>"%(sname,getHealthStateInformation(get("HealthState")),str(g
et("CompletedRequestCount")),str(get("HoggingThreadCount")), str(get("PendingUserRequestCount")),str(get("StandbyThreadCount")))

def getHealthStateInformation(myState):  # is of type weblogic.health.HealthState
        if(myState.getState()==weblogic.health.HealthState.HEALTH_OK):
            return "HEALTH_OK"
        elif(myState.getState()==weblogic.health.HealthState.HEALTH_WARN):
            return "HEALTH_WARN"
        elif(myState.getState()==weblogic.health.HealthState.HEALTH_CRITICAL):
            return "HEALTH_CRITICAL"
        elif(myState.getState()==weblogic.health.HealthState.HEALTH_FAILED):
            return "HEALTH_FAILED"
        elif(myState.getState()==weblogic.health.HealthState. HEALTH_OVERLOADED):
            return "HEALTH_OVERLOADED"
        else:
            return "UNKNOWN STATE"

def monitorJDBCStatus():
   print >>outfile, "<jdbcInfo>"

   allServers=domainRuntimeService.getServerRuntimes();
   for server in allServers:
       jdbcServiceRT = server.getJDBCServiceRuntime();
       dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();
       for ds in dataSources:
          print >>outfile,"<servers><server>%s</server><Datasource>%s</Datasource><ActiveConnectionsCurrentCount>%s</ActiveConnectionsCurrentCount><ActiveConnectionsHig
hCount>%s</ActiveConnectionsHighCount><LeakedConnectionCount>%s</LeakedConnectionCount><State>%s</State><TestDS>%s</TestDS></servers>"%(server.getName(),ds.getName(),st
r(ds.getActiveConnectionsCurrentCount()),str(ds.getActiveConnectionsHighCount()), str(ds.getLeakedConnectionCount()),           ds.getState(),getDSTestState(ds.testPool
()))

   print >>outfile, "</jdbcInfo>"
def monitorJVMStatus():
  print >>outfile, "<JVMInfo>"
  servers = domainRuntimeService.getServerRuntimes();
  #os.system("echo " + '-------JVMMonitoringInformation-------'+" >> Domain_Monitoring_Output_file")
  for server in servers:
            cd ("/ServerRuntimes/"+server.getName()+"/"+"JVMRuntime/"+server.getName())
            uptime=str(get("Uptime")/1000)+" seconds"
            print >>outfile,"<servers><server>%s</server><heapFreeCurrent>%s</heapFreeCurrent><HeapFreePercent>%s</HeapFreePercent><HeapSizeCurrent>%s</HeapSizeCurrent>
<Uptime>%s</Uptime><JavaVersion>%s</JavaVersion></servers>"%(server.getName(),str(get("HeapFreeCurrent")),str(get("HeapFreePercent")),str(get("HeapSizeCurrent")), str(u
ptime),str(get("JavaVersion")))

  print >>outfile, "</JVMInfo>"

def getDSTestState(DSState):
        if(DSState==None):
            return "TEST_OK"
        else:
            return "TEST_NOK"

def monitorJMSStatus():
   print >>outfile, "<JMSInfo>"
   servers = domainRuntimeService.getServerRuntimes();
   #os.system("echo " + '-------JMSMonitoringInformation-------'+" >> Domain_Monitoring_Output_file")
   if(len(servers) > 0):
     for server in servers:
         jmsRuntime = server.getJMSRuntime();
         jmsServers = jmsRuntime.getJMSServers();
         for jmsServer in jmsServers:
             destinations = jmsServer.getDestinations();
             for destination in destinations:
                           print >>outfile,"<servers><server>%s</server><queueName>%s</queueName><messageCurrentCount>%s</messageCurrentCount><messagePendingCount>%s</m
essagePendingCount><consumersCurrent>%s</consumersCurrent></servers>"%(server.getName(),destination.getName(),getMessagesCurrentState(destination.getMessagesCurrentCoun
t()),                                      getPendingMessagesState(destination.getMessagesPendingCount()),str(destination.getConsumersCurrentCount()))
   print >>outfile, "</JMSInfo>"
   print >>outfile, "</Domain>"

def getPendingMessagesState(pendingMessagesCount):
       if(pendingMessagesCount>0):
          return str(pendingMessagesCount)
       else :
          return str(pendingMessagesCount)

def getMessagesCurrentState(currentMessagesCount):
      if(currentMessagesCount>100):
         return str(currentMessagesCount)
      else :
          return str(currentMessagesCount)

def monitorLogLevelStatus(env_info):
    servers=domainRuntimeService.getServerRuntimes()
    print >>outfile, "<Domain>"
    print >>outfile, "<domainName>"+env_info+"</domainName>"
    print >>outfile, "<logLevel>"
    for server in servers:
       cd ("/Servers/"+server.getName()+'/Log/'+server.getName())
       LogSeverityStatus=cmo.getLogFileSeverity()
       print >>outfile,"<servers><server>%s</server><LogLevelStatus>%s</LogLevelStatus></servers>"%(server.getName(),getLogFileSeverity(cmo.getLogFileSeverity()))
    print >>outfile, "</logLevel>"

def getLogFileSeverity(LogLevelSeverity):
    if(LogLevelSeverity=='Warning'):
       return "Warning"
    else:
       return str(LogLevelSeverity)

if __name__== "main":
   print >>outfile, "<DomainMonitoring>"
   print >>outfile, "<startTime>"+now.strftime("%Y-%m-%d %H:%M:%S")+"</startTime>"
   subject= configProps.get("subject")
   print >>outfile, "<appName>"+subject+"</appName>"
   file = open('/home/wladmin/splunk/DomainMonitorXml/ConnectionDetails.csv', "r")
   for line in file.readlines():
       line = line.lstrip().rstrip()
       array = line.split(',')
       connUri=array[0]
       adminUserName=array[1]
       password=array[2]
       envDtl=array[3]
       connnectToAdminServer(connUri,adminUserName,password)
       monitorLogLevelStatus(envDtl)
       serverRuntime()
       domainRuntime()
       monitorServerStatus()
       serverAllstatus()
       monitorThreadStatus()
       monitorJDBCStatus()
       monitorJVMStatus()
       monitorJMSStatus()
   now1 = datetime.datetime.now()
   #end_time = datetime.time()
   #now2 = end_time - start_time
   print >>outfile, "<endTime>"+now1.strftime("%Y-%m-%d %H:%M:%S")+"</endTime>"
   #print >>outfile, "<ElapsedTime>"+now2+"Seconds </Elapsedtime>"
   print >>outfile, "</DomainMonitoring>"
   disconnect()
exit()
