#!/bin/sh
FILE="list_deployments_status_$(date +%Y%m%d_%H%M%S).csv"
ED=/u01/oracle/script/scripts/splunk
MW_HOME=/u01/Oracle/Middleware
ORACLE_HOME="${MW_HOME}/Oracle_OSB1"
WL_HOME="${MW_HOME}/wlserver_10.3"
 
# Setup Common Environment
WLS_NOT_BRIEF_ENV=true
. "${WL_HOME}/server/bin/setWLSEnv.sh"
 
CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${FMWLAUNCH_CLASSPATH}${CLASSPATHSEP}${DERBY_CLASSPATH}${CLASSPATHSEP}${DERBY_TOOLS}${CLASSPATHSEP}${POINTBASE_CLASSPATH}${CLASSPATHSEP}${POINTBASE_TOOLS}"
 
CLASSPATH=$CLASSPATH:$ORACLE_HOME/modules/com.bea.common.configfwk_1.7.0.0.jar:$ORACLE_HOME/lib/sb-kernel-api.jar:$ORACLE_HOME/lib/sb-kernel-impl.jar:$WL_HOME/server/lib/weblogic.jar:$ORACLE_HOME/lib/alsb.jar;
export CLASSPATH
 
if [ "${WLST_HOME}" != "" ] ; then
WLST_PROPERTIES="-Dweblogic.wlstHome='${WLST_HOME}'${WLST_PROPERTIES}"
export WLST_PROPERTIES
fi
JVM_ARGS="-Dprod.props.file='${WL_HOME}'/.product.properties ${WLST_PROPERTIES} ${JVM_D64} ${MEM_ARGS} ${CONFIG_JVM_ARGS}"
 
$ORACLE_HOME/common/bin/wlst.sh ${ED}/list_deployments_status.py > ${ED}/list_deployments_status.tmp
sed -i '0,/^Test$/d' ${ED}/list_deployments_status.tmp
sed '/^$/d' ${ED}/list_deployments_status.tmp > ${ED}/list_deployments_status1.csv
tail -n +5 < ${ED}/list_deployments_status1.csv > ${ED}/list_deployments_status2.csv
echo DomainName,TargetName,state,appName > ${ED}/list_deployments_status/$FILE
cat ${ED}/list_deployments_status2.csv >> ${ED}/list_deployments_status/$FILE
rm ${ED}/list_deployments_status.tmp ${ED}/list_deployments_status1.csv ${ED}/list_deployments_status2.csv
chmod 755 ${ED}/list_deployments_status/$FILE
find ${ED}/list_deployments_status/* -mtime +1 -delete
