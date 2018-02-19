
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("weblogic.properties")
var1=config.get("properties","username")
var2=config.get("properties","password")
var3=config.get("properties","ip")
var4=config.get("properties","port")
url="t3://"+var3+":"+var4
connect(var1,var2,url)

import sys
import os
import socket
 
from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from com.bea.wli.config import Ref
from java.lang import String
from com.bea.wli.sb.util import Refs
from com.bea.wli.sb.management.configuration import CommonServiceConfigurationMBean
from com.bea.wli.sb.management.configuration import SessionManagementMBean
from com.bea.wli.sb.management.configuration import ProxyServiceConfigurationMBean
from com.bea.wli.sb.management.query import ProxyServiceQuery
from com.bea.wli.sb.management.query import BusinessServiceQuery
from com.bea.wli.monitoring import StatisticType
from com.bea.wli.monitoring import ServiceDomainMBean
from com.bea.wli.monitoring import ServiceResourceStatistic
from com.bea.wli.monitoring import StatisticValue
from com.bea.wli.monitoring import ServiceDomainMBean
from com.bea.wli.monitoring import ServiceResourceStatistic
from com.bea.wli.monitoring import StatisticValue
from com.bea.wli.monitoring import ResourceType
 
domainRuntime()
 
alsbCore = findService(ALSBConfigurationMBean.NAME, ALSBConfigurationMBean.TYPE)
 
psQuery = ProxyServiceQuery()
psQuery.setServiceEnabled(true)
allRefs= alsbCore.getRefs(psQuery)
print "List of enabled Proxy Services"
print "========================================================================="
for ref in allRefs:
  typeId = ref.getTypeId()
  if typeId == "ProxyService":
     print "Proxy Service: " + ref.getFullName()
 
psQuery = ProxyServiceQuery()
psQuery.setServiceEnabled(false)
allRefs= alsbCore.getRefs(psQuery)
print "List of disabled Proxy Services"
print "========================================================================="
for ref in allRefs:
  typeId = ref.getTypeId()
  if typeId == "ProxyService":
     print "Proxy Service: " + ref.getFullName()
 
bsQuery = BusinessServiceQuery()
bsQuery.setServiceEnabled(true)
allRefs= alsbCore.getRefs(bsQuery)
print "List of enabled Business Services"
print "========================================================================="
for ref in allRefs:
  typeId = ref.getTypeId()
  if typeId == "BusinessService":
     print "Business Service: " + ref.getFullName()
 
bsQuery = BusinessServiceQuery()
bsQuery.setServiceEnabled(false)
allRefs= alsbCore.getRefs(bsQuery)
print "List of disabled Business Services"
print "========================================================================="
for ref in allRefs:
  typeId = ref.getTypeId()
  if typeId == "BusinessService":
     print "Business Service: " + ref.getFullName()

bsQuery = BusinessServiceQuery()
bsQuery.setTransportScheme("http")
allRefs= alsbCore.getRefs(bsQuery)
print "List of HTTP enabled Business Services"
print "========================================================================="
for ref in allRefs:
   print ref
 