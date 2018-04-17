#!/bin/sh
FILE="list_server_health_$(date +%Y%m%d_%H%M%S).csv"
FILE1="list_server_health_stuck_threads_$(date +%Y%m%d_%H%M%S).csv"
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
 
$ORACLE_HOME/common/bin/wlst.sh ${ED}/list_server_health.py > ${ED}/list_server_health.tmp
sed -i '0,/^Test$/d' ${ED}/list_server_health.tmp
sed '/^$/d' ${ED}/list_server_health.tmp > ${ED}/list_server_health1.tmp
echo DomainName,ServerName,OpenSocketsCurrentCount,StandbyThreadCount,Throughput,HoggingThreadCount,ExecuteThreadTotalCount,ExecuteThreadIdleCount > ${ED}/list_server_health/$FILE
sed '$d' ${ED}/list_server_health1.tmp >> ${ED}/list_server_health/$FILE
chmod 755 ${ED}/list_server_health/$FILE
rm -rf ${ED}/list_server_health1.tmp ${ED}/list_server_health.tmp

#$ORACLE_HOME/common/bin/wlst.sh ${ED}/list_server_health_stuck_threads.py > ${ED}/list_server_health_stuck_threads.csv
#sed -i '0,/^Test$/d' ${ED}/list_server_health_stuck_threads.csv
find ${ED}/list_server_health/* -mtime +1 -delete
