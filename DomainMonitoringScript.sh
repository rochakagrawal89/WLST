. /fmwshared/Oracle/Middleware/wlserver_10.3/server/bin/setWLSEnv.sh
java weblogic.WLST /home/wladmin/splunk/DomainMonitorXml/DomainMonitoringScript.py
sleep 10
sudo chmod 777 domainstats.xml
mv /home/wladmin/splunk/DomainMonitorXml/domainstats.xml /home/wladmin/splunk/DomainMonitorXml/domainstats.xml
