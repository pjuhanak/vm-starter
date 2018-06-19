#!/usr/bin/python
"""
VM starter - start your virtual hosts based on config file
--------------------------------------------------------------------------------
@author  Petr Juhanak,  http://www.hackerlab.cz
@release 1.0, 20130808
@licence GPLv3          http:://www.gnu.org/licenses/gpl-3.0.html
--------------------------------------------------------------------------------
"""
import re
import sys
import os.path
import subprocess
import time
import operator

START_SYMBOL = [ 'x', 'X', '1','i','I','s','S']
VBOX_MANAGE  = 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'

if os.name == 'nt':
    vbox_manage  = os.path.normpath('"'+VBOX_MANAGE+'"')

# functions
def show_banner():
    print "VM starter 1.0 - Author Petr Juhanak | http://www.hackerlab.cz (GPLv3)"
    print ""

def report_error(message):
    print "Usage: vm.py <lab.config> [START|stop|reset]"
    print ""
    print "   [!]", message
    
def print_vmtable():
    file = open(LAB_CONFIG)
    for line in file:
        print line.strip()
        
def vmtable(filename):
    vmt  = []
    file = open(filename)

    for i,line in enumerate(file):
        if not line.startswith(";"):
            
            match = re.search('(.*)\|(.*)\|(.*)\|(.*)', line)
            if match:
                name    = match.group(1).strip()
                execute = match.group(2).strip()
                delay   = match.group(3).strip()
                comment = match.group(4).strip()
                
                try:
                    int(delay)
                except ValueError:
                    delay = '0'
                    
                vmt.append([name, execute, delay, comment])
    return vmt

# start
show_banner()

if len(sys.argv) > 1:   
    CONFIG_FILE   = sys.argv[1]
else:
    report_error("Error: missing config file")
    sys.exit(1)
    
if len(sys.argv) > 2:
    ACTION = sys.argv[2].upper().strip()
else:
    ACTION = "start".upper().strip()



# start VMs according lab.config          
vmt = vmtable(CONFIG_FILE)
vmt.sort(key=lambda x: int(x[2]))

for vm in vmt:

    name  = vm[0] 
    execute = vm[1] 
    delay = vm[2]
    comment = vm[3]
    
    if execute in START_SYMBOL:
    
        if ACTION == "START":
            cmd = vbox_manage + ' startvm ' + '"' + name + '"'
        
        if ACTION == "RESET":
            cmd = vbox_manage + ' controlvm ' + '"' + name + '"' + ' reset'
            
        if ACTION == "STOP":
            cmd = vbox_manage + ' controlvm ' + '"' + name + '"' + ' poweroff'
        
        print ""
        if (delay > 0) and ACTION in ["START", "RESET"]:
            print '[*] ' + ACTION + ' VM ' +  name + ' after ' + str(delay) + ' sec.'
            time.sleep(float(delay))
        else: 
            print '[*] ' + ACTION + ' VM ' +  name
        
        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

        while True:
            out = p.stderr.read(1)
            if out == '' and p.poll() != None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()
                
"""
Example LAB.CONFIG:
===================
;
;
;           Start VM when start symbol is found [S, X, 1, I]
;           with a  delay: integer [sec] - default zero
;           VM name has to match with your VirtualBOX VM name
;-------------------------------------------------------------------------------
; VM name       |S| Delay | Comment
;---------------+---------+-----------------------------------------------------
PFSense VLAN1   |S|   0   | DHCP server/FW - has to start first
WinXP.SP3       |S|   25  | HTTP Apache 1.3 (started with 25sec delay)
bt5 VLAN1       |S|   24  | Backtrack       (started with 24sec delay)
VM007           |-|       | This VM will not start due to missing start symbol
"""
