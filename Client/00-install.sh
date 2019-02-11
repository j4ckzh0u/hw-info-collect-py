#! /usr/bin/env sh

if [ `whoami` != 'root' ]; then
	echo 'Please run this script with root!'
	exit 1
fi

currdir=`pwd`

cd ${currdir}/Install-pkg && \
echo 'start install salt ....' && \
yum localinstall salt-minion* --nogpgcheck	 

[ $? == 0 ] && echo 'salt install success!' || echo 'salt install faile ):'

echo 'start config the salt ....' && \
cat ${currdir}/Install-pkg/minion > /etc/salt/minion

echo 'salt config success!'
