#!/usr/bin/python
#### Accenture ESB Team ####

# Import Required Libraries
import sys
import os
import socket

print "Imported Python Libraries"

## Prevent printing output to the screen
redirect('/dev/null','false')
 
# Connect to WebLogic
# Connect to WebLogic
print "Connecting to WebLogic Server url='t3://N1BTFL-ESB025:7001'"
connect(username='admin', password='admin#123', url='t3://10.14.114.46:7001')

domainRuntime()
servers = ls('/ServerRuntimes','true','c')
 
# We'll store all results in here, using the server name for a key
result=dict()
for server in servers:
    deployments = ls('/ServerRuntimes/' + server + '/ApplicationRuntimes','true','c')
    result[server] = 0;
    for deployment in deployments:
        ## If you are only interested in a single deployment, run that check here, like
        ## if(deployment.getName() == "MyApplication"):
 
        ## Could be that there are multiple workmanagers, I'm not sure, so let's iterate over them
        wms = ls('/ServerRuntimes/'  + server + '/ApplicationRuntimes/' + deployment + '/WorkManagerRuntimes','true','c')
        for wm in wms:
            cd('/ServerRuntimes/' + server + '/ApplicationRuntimes/' + deployment + '/WorkManagerRuntimes/' + wm) 
            result[server] = result[server] + get('StuckThreadCount')
 
## Reenable printing output
redirect('/dev/null','true')
 
## Print all server names and the number of stuck threads we counted per server
for key in result:
  print(key +','  + str(result[key]) )
