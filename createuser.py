#############################################################################
#
# @author Copyright (c) 2010 - 2011 by Middleware Magic, All Rights Reserved.
#
#############################################################################
 
from java.io import FileInputStream
 
propInputStream = FileInputStream("details1.properties")
configProps = Properties()
configProps.load(propInputStream)
 
domainName=configProps.get("domain.name")
adminURL=configProps.get("admin.url")
adminUserName=configProps.get("admin.userName")
adminPassword=configProps.get("admin.password")
realmName=configProps.get("security.realmName")
 
totalGroups_to_Create=configProps.get("total.groups")
totalUsers_to_Create=configProps.get("total.username")
 
connect(adminUserName, adminPassword, adminURL)
serverConfig()
authenticatorPath= '/SecurityConfiguration/' + domainName + '/Realms/' + realmName + '/AuthenticationProviders/DefaultAuthenticator'
print authenticatorPath
cd(authenticatorPath)
print ' '
print ' '
  
print 'Adding Group Membership of the Users:'
for y in 1,2:
    grpName = configProps.get("create.group.name."+ str(y))
    groupMembers= configProps.get("create.group.name."+ str(y) + ".members")
    usrName=''
    for member in groupMembers:
        if member == ",":
            cmo.addMemberToGroup(grpName,usrName)
            print 'USER:' , usrName , 'Added to GROUP: ' , grpName
            usrName=''
        else:
            usrName=usrName+member
print ' '
print ' '