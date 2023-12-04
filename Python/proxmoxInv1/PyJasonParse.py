#!/usr/bin/env python3
import json

with open("archivo.json", "r") as file:
    data = json.load(file)

all_hosts = data["hostvars"]
print("name,CPU,RAM,HDD,status")
for host in all_hosts.values():
    proxmox_name = host["proxmox_name"]
    proxmox_cpus = host["proxmox_cpus"]
    proxmox_maxmem = round(host["proxmox_maxmem"] / (1024 ** 3))  # Convertir bytes a gigabytes
    proxmox_maxdisk = round(host["proxmox_maxdisk"] / (1024 ** 3))  # Convertir bytes a gigabytes
    proxmox_status = host["proxmox_status"]
    
    print(f"{proxmox_name},{proxmox_cpus},{proxmox_maxmem},{proxmox_maxdisk},{proxmox_status}")