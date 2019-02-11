#! /usr/bin/env sh

now=`date +"%Y%m%d %H:%M:%S"`

if [ `whoami` != 'root' ]; then
	echo 'Please run this script with root'
	exit 1
fi

currdir=`pwd`

cd ${currdir}/Install-pkg && \
echo 'start collect hardware info ... ' && \
python2.7 ${currdir}/Install-pkg/salt_get_hwinfo.py

[ $? == 0 ] && echo "[+] ${now} hw info collect success!" || echo "[!] ${now} hw info collect faile ):"
