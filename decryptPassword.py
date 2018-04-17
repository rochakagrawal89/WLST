#=======================================================================================
# This Script decrypt WebLogic passwords
#
# Usage: 
#      wlst decryptPassword.py <DOMAIN_HOME> <ENCRYPTED_PASSWORD>
#
# Author: Rochak Agrawal
#
#=======================================================================================
import os
import weblogic.security.internal.SerializedSystemIni
import weblogic.security.internal.encryption.ClearOrEncryptedService

def decrypt(domainHomeName, encryptedPwd):
    domainHomeAbsolutePath = os.path.abspath(domainHomeName)
    encryptionService = weblogic.security.internal.SerializedSystemIni.getEncryptionService(domainHomeAbsolutePath)
    ces = weblogic.security.internal.encryption.ClearOrEncryptedService(encryptionService)
    clear = ces.decrypt(encryptedPwd)
    print "RESULT:" + clear

try:
    if len(sys.argv) == 3:
        decrypt(sys.argv[1], sys.argv[2])
    else:
		print "INVALID ARGUMENTS"
		print " Usage: java weblogic.WLST decryptPassword.py <DOMAIN_HOME> "<ENCRYPTED_PASSWORD>"
		print " Example:"
		print "	java weblogic.WLST decryptPassword.py D:/Oracle/Middleware/user_projects/domains/base_domain "{AES}819R5h3JUS9fAcPmF58p9Wb3syTJxFl0t8NInD/ykkE="
except:
    print "Unexpected error: ", sys.exc_info()[0]
    dumpStack()
    raise
