**Note:** These are all fictitious scenarios 

## Template: [Date] - [Entry]
| Event Details    |              |
| ---------------- | -------------|
| Description      |              |
| Tool(s) used     |              | 
| 5 W's            | **Who** caused incident: <br> **What** happened: <br> **Where** the incident happened: <br> **When** the incident happend: <br> **Why** the incident happend: <br> |
| Additional Notes |              | 

## New Tool Template
### [Tool Name]
_Description:_ 

_Notes:_

----

---
## July 28th, 2023 - #4.5
### Alert ticket
(official ticket from below incident)
| Ticket ID        | Alert Message |  Severity    | Details    | Ticket Status    |
| ---------------- | --------------| -------------| -----------| -----------------|
| A-2703           | SERVER-MAIL <br> Phishing attempt, potential malware download | Medium  |  User potentially opened malicious email as well as attached file or clicked on link   | Escalated |

_Ticket Comments:_ Around 1:00pm we recieved an alert that detected a download and open of a malicious file. Upon locating the email in question it can be observed that the sender email (76tguy6hh6tgfrt7tg.su), the name within the email body (Clyde West) and the senders name (Def communications) are all inconsistent; further more the subject and body of the email contain several grammatical errors. The file in question "bfsvc.exe" was attached to the email and opened by the recipient onto the now affected machine. In a previous investigation of the file hash it is confirmed that the exe is a known malicious file. This ticket as been escalted to the SOCII team for further action. 

### Additional Information
**File Hash:** 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b 

**Email:** 
```
From: Def Communications <76tguy6hh6tgfrt7tg.su> <114.114.114.114>
Sent: Wednesday, July 20 2022 9:30:14 AM
To: <hr@inergy.com> <176.157.125.93>
Subject: Re: Infrastructure Egnieer Role

...
```



---
## July 28th, 2023 - #4
| Event Details    |              |
| ---------------- | -------------|
| Description      |      As a SOC1 analyst I have recieved an alert about a suspicious file being downloaded on an employee's computer. The file in question is a password-protected spreadsheet, I have run a <sha256sum> on the file to retrieve the file hash:  54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b       |
| Tool(s) used     |      VirusTotal        | 
| 5 W's            | **Who**: end user <br> **What**: opened file attachment in an email that installed an executable <br> **Where**: end user company laptop <br> **When**: 1:00 pm <br> **Why**: user suspected email to be legitimate <br> |
| Additional Notes |     Majority of vendors flag the file as malicious, upon investigation the file can be pin pointed as the trojan Flagpro utilized by the threat actor group BlackTech. Remediation steps have been taken. <br> ![image](https://github.com/black-v0id/black-v0id/assets/16123062/40766782-9443-46dd-af63-e50b14555082) | 


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
