import os
import json
import random
import asyncio
from pathlib import Path

PORTS = [
    21,    # FTP
    22,    # SSH
    23,    # Telnet
    25,    # SMTP
    53,    # DNS
    69,    # TFTP
    80,    # HTTP
    110,   # POP3
    123,   # NTP
    135,   # MS RPC
    137, 138, 139,  # NetBIOS
    143,   # IMAP
    161, 162,  # SNMP
    443,   # HTTPS
    445,   # SMB
    514,   # Syslog
    5900,  # VNC
    6667,  # IRC
    1433,  # MS SQL
    1521,  # Oracle
    1723,  # PPTP
    1900,  # SSDP
    2049,  # NFS
    3306,  # MySQL
    3389,  # RDP
    5060,  # SIP
    5432,  # PostgreSQL
    8080,  # HTTP-alt
    10000  # Webmin
]

MAX_CONCURRENT = 200
DISCOVERED_IPS = []
dont_run = []

async def scan_ip(ip, semaphore):
    
    async with semaphore:
        if ip not in DISCOVERED_IPS or ip not in dont_run:
            for port in PORTS:
                try:
                    reader, writer = await asyncio.wait_for(
                        asyncio.open_connection(ip, port), 
                        timeout=2
                    )
                    print(ip, port)
                    DISCOVERED_IPS.append(f"{ip}:{port}\t\tState{state}")
                    writer.close()
                    await writer.wait_closed()
                    return True
                except:
                    dont_run.append(ip)
                    continue
    return False

async def main():
    global state
    
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    tasks = []
    
    with open(os.path.abspath("json.json"), "r", encoding='utf-8', errors='ignore') as f:
        json_file = f.read()

    dichnry = json.loads(json_file)

    for name, value in dichnry["continents"].items():
        for line in value["ip_ranges"]:
            ip = line.split("-")[0].split(".")[0]
            state = line.split("-")[1]
            
            for _ in range(100):
                ip = f"{ip.strip()}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                tasks.append(scan_ip(str(ip), semaphore))
        
    results = await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    
    Path("targets.txt").write_text("".join(str(x) for x in  DISCOVERED_IPS))