**Note:** These are all fictitious scenarios 

## Template: [Date] - [Entry]
| Event Details    |              |
| ---------------- | -------------|
| Description      |              |
| Tool(s) used     |              | 
| 5 W's            | **Who** caused incident: <br> **What** happened: <br> **Where** the incident happened: <br> **When** the incident happend: <br> **Why** the incident happend: <br> |
| Additional Notes |              | 

----

---
## July 27th, 2023 - #3
| Event Details    |              |
| ---------------- | -------------|
| Description      |  Capture network traffic and filter for analysis.  |
| Tool(s) used     |      Linux, tcpdump        | 
| 5 W's            |  N/A |
| Additional Notes |  Preformed tasks associated with utiliizing tcpdump to capture data in a p-cap file and examine the contents to focus in on specific typed of traffic.  Utilized the commands: <br> - ifconfig; to identify available interfaces <br> - tcpdump with options to capture a specified number of packets, save to a file and run as to not resolve IP addresses or ports <br> - read the output file data displayed in hexadecimal and ASCII <br> ![image](https://github.com/black-v0id/black-v0id/assets/16123062/9004e7b7-456f-4113-bc3c-0a00d69f6306) ![image](https://github.com/black-v0id/black-v0id/assets/16123062/5a200478-f2aa-4618-900c-cb458f75b809) | 


---
## July 27th, 2023 - #2
| Event Details    |              |
| ---------------- | -------------|
| Description      |  Analyzing a network packet capture file that contains traffic data related to a user connecting to an internet site. |
| Tool(s) used     |  Wireshark            | 
| 5 W's            | N/A |
| Additional Notes |   Investigated a packet capture file where I explored a single packet to examine various protocol and data layers inside a network packet; applied filters to select and inspect packets based on specific criteria; filtered and inspected UDP DNS trffic to examine protocol data; and applied filters to a TCP packet to locate specific payload text data. <br> Used filters such as: <br> - ip.src <br> - ip.dst <br> - udp.port <br> - tcp contains "curl" <br> ![image](https://github.com/black-v0id/black-v0id/assets/16123062/1eb5a288-12b9-451a-ab4d-8ed467ab095d) | 

--- 
## July 25th, 2023 - #1
| Event Details    |              |
| ---------------- | -------------|
| Description      |  Cybersecurity incident. Small US health clinic experiences security incident where employees are unable to access files and software. |
| Tool(s) used     |  - SIEM <br> - IDS | 
| 5 W's            | **Who**: External attacker<br> **What**: ransomware incident via phising email<br> **Where**: small health clinic <br> **When**: 9:00am Tuesday<br> **Why**: Social engineering tactics via targeted phishing on employees. After gaining access the attacker launched ransomware onto the system which encrypted critical files. Motivation for the attack appears to be financial based on ransom note for large sum. <br> |
| Additional Notes | What systems could be improved to prevent future events such as this? <br> How are we recovering bricked systems? <br> Is there any data loss? | 
