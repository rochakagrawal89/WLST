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

print 'Test'

# AppDeploymentMBean[] The collection of deployable entities in this domain.
cd ('AppDeployments')
myapps=cmo.getAppDeployments()


# Deployement Status & Target
for app in myapps:
      appName = app.getName()
      # Changing Location to domainConfig tree. This is a read-only tree with DomainMBean as the root.
      domainConfig()
      cd ('/AppDeployments/'+appName+'/Targets')
      mytargets = cmo.getTargets()
      # The domainRuntime command places WLST at the root of the domain-wide runtime management objects, DomainRuntimeMBean.
      domainRuntime()
      cd('AppRuntimeStateRuntime/AppRuntimeStateRuntime')
      for target in mytargets:
            targetName = target.getName()
            # Aggregate state for the application. This is defined as the most advanced state of the application's modules on the named target.
            state=cmo.getCurrentState(appName,targetName)
            print 'Online Domain,' + targetName + ',' + state + ','+ appName
