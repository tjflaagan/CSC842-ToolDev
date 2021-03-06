<#
.SYNOPSIS
A Powershell script to gather system information
.PARAMETER FILE
Name of output file
.EXAMPLE
.\sit1.ps1 -FILE stuff.txt
#>

[CmdletBinding()]
Param(
    [Parameter(ValueFromPipeline=$true, ValueFromPipelineByPropertyName = $true)]
    [string[]]$FILE
)

function sep {
	for($i = 1; $i -le 3; $i++){
		$outstring = '#' * 60
		Add-Content $FILE $outstring
	}
}

Import-Module activedirectory

Out-File "$FILE" 
# User info
[Environment]::UserName | Add-Content "$FILE" 
[Environment]::UserDomainName | Add-Content "$FILE" 
[Environment]::MachineName | Add-Content "$FILE" 
sep
# Domain info
Get-ADDomain | Add-Content "$FILE" 
sep
# Get user groups
Get-ADPrincipalGroupMembership [Environment]::UserName | select name  | Add-Content "$FILE" 
sep
# AD Users 
get-aduser -filter * -properties * | select-object samaccountname memberof | Add-Content "$FILE"
sep
# PSinfo
Get-Host | Add-Content "$FILE"
sep
# Comp info
Get-ComputerInfo | Add-Content "$FILE"
sep
# Interfaces
ipconfig /all | Add-Content "$FILE"
Get-Netadapter | Add-Content "$FILE"
sep
# Routes
netstat -rn | Add-Content "$FILE"
sep
# More 
netstat -ntp | Add-Content "$FILE"
sep
# ARP
arp -a | Add-Content "$FILE"
sep
# DNS
Get-DnsClientServerAddress | Select-Object –ExpandProperty ServerAddresses | Add-Content "$FILE"
sep
# Get hotfix list
Get-HotFix | Add-Content "$FILE"
sep
# Hosts file
Get-Content -Path "C:\Windows\System32\drivers\etc\hosts" | Add-Content "$FILE"
sep
# Firewall
Get-NetFirewallRule -PolicyStore ActiveStore | Add-Content "$FILE"
sep
# Startup items 
Get-CimInstance Win32_StartupCommand | Select-Object name, command, location, user | Format-List | Add-Content "$FILE"
sep 
# Installed Programs
Get-WmiObject -Class Win32_Product | Add-Content "$FILE"
sep
# Shares
Get-WmiObject -Class Win32_Share | Add-Content "$FILE"
sep 
# Drives
Get-WmiObject -Class win32_diskdrive | Add-Content "$FILE"
sep
# Processes
Get-Process | Add-Content "$FILE"
sep
# ACL
Get-Acl | Add-Content "$FILE"
sep

