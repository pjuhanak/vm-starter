vm-starter
==========

Start your VM hosts (VirtualBox) based on lab configuration file. Start, stop or restart whole labs.

VirtualBox - https://www.virtualbox.org


Usage
=====

   d:\pentest\py\vm>vm.py

   VM starter 1.0 - Petr Juhanak | http://www.lockdown.cz/tools (GPLv3)

   Usage: vm.py <lab.config> [START|stop|reset]

      [!] Error: missing config file
   

Lab config file
===============
Lab config file defines set of VM for start. We can define a delay between VMs starts in seconds.
We can exclude a specific VM from start order.

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


Start VM LAB
============
d:\pentest\py\vm>vm.py ./lab02.conf
VM starter 1.0 - Petr Juhanak | http://www.lockdown.cz/tools (GPLv3)


[*] START VM PFSense VLAN1 after 0 sec.
Waiting for VM "PFSense VLAN1" to power on...
VM "PFSense VLAN1" has been successfully started.

[*] START VM bt5 VLAN1 after 24 sec.
Waiting for VM "bt5 VLAN1" to power on...
VM "bt5 VLAN1" has been successfully started.

[*] START VM WinXP.SP3 after 25 sec.
Waiting for VM "WinXP.SP3" to power on...
VM "WinXP.SP3" has been successfully started.



Restart running lab
===================
d:\pentest\py\vm>vm.py ./lab02.conf RESET
VM starter 1.0 - Petr Juhanak | http://www.lockdown.cz/tools (GPLv3)


[*] RESET VM PFSense VLAN1 after 0 sec.

[*] RESET VM bt5 VLAN1 after 24 sec.

[*] RESET VM WinXP.SP3 after 25 sec.



Stop VM LAB
============
d:\pentest\py\vm>vm.py ./lab02.conf STOP
VM starter 1.0 - Petr Juhanak | http://www.lockdown.cz/tools (GPLv3)


[*] STOP VM PFSense VLAN1
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

[*] STOP VM bt5 VLAN1
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

[*] STOP VM WinXP.SP3
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
