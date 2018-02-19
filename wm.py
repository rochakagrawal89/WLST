####################################Script made by Rochak Agrawal#################################################
import sys
import os
import socket
import wlstModule
from com.bea.wli.sb.management.configuration import SessionManagementMBean
from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from com.bea.wli.sb.management.configuration import ProxyServiceConfigurationMBean
from com.bea.wli.sb.util import EnvValueTypes
from com.bea.wli.config import Ref
from com.bea.wli.sb.util import Refs

import ConfigParser
config = ConfigParser.ConfigParser()
config.read("weblogic.properties")
var1=config.get("properties","username")
var2=config.get("properties","password")
var3=config.get("properties","ip")
var4=config.get("properties","port")
url="t3://"+var3+":"+var4
connect(var1,var2,url)

domainRuntime()

sessionMBean = findService(SessionManagementMBean.NAME,SessionManagementMBean.TYPE)
sessionName="WLSTSession"+ str(System.currentTimeMillis())
sessionMBean.createSession(sessionName)
alsbSession = findService(ALSBConfigurationMBean.NAME + "." + sessionName, ALSBConfigurationMBean.TYPE)
alsbCore = findService(ALSBConfigurationMBean.NAME, ALSBConfigurationMBean.TYPE)

allRefs=alsbCore.getRefs(Ref.DOMAIN)
for ref in allRefs.iterator():
    typeId = ref.getTypeId()
    if typeId == "BusinessService" :
        name=ref.getFullName()
        uris=alsbSession.getEnvValue(ref, EnvValueTypes.WORK_MANAGER, None)
		uris1=alsbSession.getEnvValue(ref, EnvValueTypes.SERVICE_RETRY_INTERVAL, None)
		uris2=alsbSession.getEnvValue(ref, EnvValueTypes.SERVICE_RETRY_COUNT, None)
        print "============================================BUSINESS SERVICES============================================================================="
		print name
        print "WORK MANAGER: ",uris
		print "RETRY INTERVAL: ",uris1
		print "RETRY COUNT: ",uris2
	print "=========================================================================================================================================="
    if typeId == "ProxyService" :
        name=ref.getFullName()
        uris=alsbSession.getEnvValue(ref, EnvValueTypes.WORK_MANAGER, None)
		uris1=alsbSession.getEnvValue(ref, EnvValueTypes.SERVICE_RETRY_INTERVAL, None)
		uris2=alsbSession.getEnvValue(ref, EnvValueTypes.SERVICE_RETRY_COUNT, None)
        print "============================================PROXY SERVICES================================================================================"
        print name
        print name
        print "WORK MANAGER: ",uris
		print "RETRY INTERVAL: ",uris1
		print "RETRY COUNT: ",uris2
        print "=========================================================================================================================================="

