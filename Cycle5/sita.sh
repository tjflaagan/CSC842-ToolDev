#!/bin/bash 

while [[ $# -gt 1 ]]
do
	key="$1"

	case $key in
	    -f|--filename)
	    FILENAME="$2"
	    shift 
	    ;;
	    *)
	    ;;
	esac
	shift
done

function separator {
	for i in `seq 1 3`; 
	do
		perl -e 'print "#"x80; print "\n"; ' >> "${FILENAME}" 
	done
}

# User
whoami >> "${FILENAME}"
separator
# Interfaces
ifconfig >> "${FILENAME}"
separator
# Routes
netstat -rn >> "${FILENAME}" 
separator
# More Netstat
netstat -ntlp >> "${FILENAME}"
separator
netstat -nt >> "${FILENAME}"
separator
netstat -g >> "${FILENAME}"
# Arp
arp -a >> "${FILENAME}"
separator
# DNS servers
cat /etc/resolv.conf >> "${FILENAME}"
separator
# Host file
cat /etc/hosts >> "${FILENAME}"
separator
# Firewall
iptables -L -n >> "${FILENAME}"
separator
# Startup Items
initctl list >> "${FILENAME}" 
systemctl list-unit-files --type=service >> "${FILENAME}"
service --status-all >> "${FILENAME}"
separator
# Installed programs for some distros
dpkg -l >> "${FILENAME}"
rpm -qa >> "${FILENAME}"
separator
# Path
echo $PATH >> "${FILENAME}"
separator
# SSH config
cat /etc/ssh/sshd_config >> "${FILENAME}"
separator
# SSH hosts and keys
cat ~/.ssh/known_hosts >> "${FILENAME}"
ls ~/.ssh/ >> "${FILENAME}"
separator
# Command history
history 100 >> "${FILENAME}"
separator
# Network shares
smbstatus --shares >> "${FILENAME}"
separator
# Removable
df >> "${FILENAME}"
separator
# Password policy
cat /etc/login.defs >> "${FILENAME}"
separator
# Processes
ps -aux >> "${FILENAME}"
separator





