# Cybersecurity Incident Report: Network Traffic Analysis
## Background
Review the scenario below. Then complete the step-by-step instructions.

You are a cybersecurity analyst working at a company that specializes in providing IT consultant services. Several customers contacted your company to report that they were not able to access the company website www.yummyrecipesforme.com, and saw the error “destination port unreachable” after waiting for the page to load. 

You are tasked with analyzing the situation and determining which network protocol was affected during this incident. To start, you visit the website and you also receive the error “destination port unreachable.” Next, you load your network analyzer tool, tcpdump, and load the webpage again. This time, you receive a lot of packets in your network analyzer. The analyzer shows that when you send UDP packets and receive an ICMP response returned to your host, the results contain an error message: “udp port 53 unreachable.” 

In the DNS and ICMP log, you find the following information:

In the first two lines of the log file, you see the initial outgoing request from your computer to the DNS server requesting the IP address of yummyrecipesforme.com. This request is sent in a UDP packet.

Next you find timestamps that indicate when the event happened. In the log, this is the first sequence of numbers displayed. For example: 13:24:32.192571. This displays the time 1:24 p.m., 32.192571 seconds.

The source and destination IP address is next. In the error log, this information is displayed as: 192.51.100.15.52444 > 203.0.113.2.domain. The IP address to the left of the greater than (>) symbol is the source address. In this example, the source is your computer’s IP address. The IP address to the right of the greater than (>) symbol is the destination IP address. In this case, it is the IP address for the DNS server: 203.0.113.2.domain

The second and third lines of the log show the response to your initial ICMP request packet. In this case, the ICMP 203.0.113.2 line is the start of the error message indicating that the ICMP packet was undeliverable to the port of the DNS server.

Next are the protocol and port number, which displays which protocol was used to handle communications and which port it was delivered to. In the error log, this appears as: udp port 53 unreachable. This means that the UDP protocol was used to request a domain name resolution using the address of the DNS server over port 53. Port 53, which aligns to the .domain extension in 203.0.113.2.domain, is a well-known port for DNS service. The word “unreachable” in the message indicates the message did not go through to the DNS server. Your browser was not able to obtain the IP address for yummyrecipesforme.com, which it needs to access the website because no service was listening on the receiving DNS port as indicated by the ICMP error message “udp port 53 unreachable.”

The remaining lines in the log indicate that ICMP packets were sent two more times, but the same delivery error was received both times. 

Now that you have captured data packets using a network analyzer tool, it is your job to identify which network protocol and service were impacted by this incident. Then, you will need to write a follow-up report. 

As an analyst, you can inspect network traffic and network data to determine what is causing network-related issues during cybersecurity incidents. Later in this course, you will demonstrate how to manage and resolve incidents. For now, you only need to analyze the situation. 

This incident, in the meantime, is being handled by security engineers after you and other analysts have reported the issue to your direct supervisor. 

## Supporting Documents
<img width="454" alt="image" src="https://github.com/black-v0id/black-v0id/assets/16123062/38eba332-f507-4c1c-b710-c9e3c8326805">

## Report
Part 1: Provide a summary of the problem found in the DNS and ICMP traffic log

Log data collected by the packet analyzer indicate that port 53 is unreachable when attempting to access the company website. Port 53 is assigned by IANA and widely standardized as DNS service. This may indicate a problem with the domain server. It is likely that the receiving DNS port on the server does not have a service listening for requests.

Part 2: Explain your analysis of the data and provide one solution to implement

The incident occurred mid-day when we received several reports from customers about a website outage. The network security team launched an investigation at 1:24pm and utilized the packet analyzer tool tcpdump to retrieve logs. The logs reported that UDP port 53, which is used for DNS traffic, is not reachable. 

We are continuing our investigation of the root cause to determine how to fully restore the main website. Next steps include investigating our DNS server for active errors or outages, inspecting anti-virus logs for alerts, and validating firewall configurations for port 53.

# Cybersecurity Incident Report: Analyze Network Attack
## Background
Review the following scenario. Then complete the step-by-step instructions.

You work as a security analyst for a travel agency that advertises sales and promotions on the company’s website. The employees of the company regularly access the company’s sales webpage to search for vacation packages their customers might like.

One afternoon, you receive an automated alert from your monitoring system indicating a problem with the web server. You attempt to visit the company’s website, but you receive a connection timeout error message in your browser.

You use a packet sniffer to capture data packets in transit to and from the web server. You notice a large number of TCP SYN requests coming from an unfamiliar IP address. The web server appears to be overwhelmed by the volume of incoming traffic and is losing its ability to respond to the abnormally large number of SYN requests. You suspect the server is under attack by a malicious actor.

You take the server offline temporarily so that the machine can recover and return to a normal operating status. You also configure the company’s firewall to block the IP address that was sending the abnormal number of SYN requests. You know that your IP blocking solution won’t last long, as an attacker can spoof other IP addresses to get around this block. You need to alert your manager about this problem quickly and discuss the next steps to stop this attacker and prevent this problem from happening again. You will need to be prepared to tell your boss about the type of attack you discovered and how it was affecting the web server and employees.


## Supporting Documents 
[Wireshark-TCP-HTTP-log.xlsx](https://github.com/black-v0id/black-v0id/files/11826695/UrDIBLUFSlWI3TPdmpE1vw_022112c002f24475a6e2c9e7ebe6f5f1_Wireshark-TCP-HTTP-log.xlsx)

## Report
Section 1: Identify the type of attack that may have caused this network interruption

Log data collected by by the packet analyzer tool wireshark indicate a large influx of SYN requests from an unknown IP address resulting in a network level denial of service (DoS) SYN flood attack. 

Section 2:  Explain how the attack is causing the website to malfunction

Due to an influx of requests to the webserver, the server is getting flooded with SYN packet requests which exhausts the resources (ports) available. This specifically targets our network bandwidth which slows down traffic and even results in legitimate requests to be dropped.


# Cybersecurity Incident Report: OS Security Report
## Background 
Review the scenario below. Then complete the step-by-step instructions.

You are a cybersecurity analyst for yummyrecipesforme.com, a website that sells recipes and cookbooks. A disgruntled baker has decided to publish the website’s best-selling recipes for the public to access for free. 

The baker executed a brute force attack to gain access to the web host. They repeatedly entered several known default passwords for the administrative account until they correctly guessed the right one. After they obtained the login credentials, they were able to access the admin panel and change the website’s source code. They embedded a javascript function in the source code that prompted visitors to download and run a file upon visiting the website. After running the downloaded file, the customers are redirected to a fake version of the website where the seller’s recipes are now available for free.

Several hours after the attack, multiple customers emailed yummyrecipesforme’s helpdesk. They complained that the company’s website had prompted them to download a file to update their browsers. The customers claimed that, after running the file, the address of the website changed and their personal computers began running more slowly. 

In response to this incident, the website owner tries to log in to the admin panel but is unable to, so they reach out to the website hosting provider. You and other cybersecurity analysts are tasked with investigating this security event.

To address the incident, you create a sandbox environment to observe the suspicious website behavior. You run the network protocol analyzer tcpdump, then type in the URL for the website, yummyrecipesforme.com. As soon as the website loads, you are prompted to download an executable file to update your browser. You accept the download and allow the file to run. You then observe that your browser redirects you to a different URL, greatrecipesforme.com, which is designed to look like the original site. However, the recipes your company sells are now posted for free on the new website.  

The logs show the following process:

The browser requests a DNS resolution of the yummyrecipesforme.com URL.

The DNS replies with the correct IP address. 

The browser initiates an HTTP request for the webpage.

The browser initiates the download of the malware.

The browser requests another DNS resolution for greatrecipesforme.com.

The DNS server responds with the new IP address.

The browser initiates an HTTP request to the new IP address.

A senior analyst confirms that the website was compromised. The analyst checks the source code for the website. They notice that javascript code had been added to prompt website visitors to download an executable file. Analysis of the downloaded file found a script that redirects the visitors’ browsers from yummyrecipesforme.com to greatrecipesforme.com. 

The cybersecurity team reports that the web server was impacted by a brute force attack. The disgruntled baker was able to guess the password easily because the admin password was still set to the default password. Additionally, there were no controls in place to prevent a brute force attack. 

Your job is to document the incident in detail, including identifying the network protocols used to establish the connection between the user and the website.  You should also recommend a security action to take to prevent brute force attacks in the future.

## Supporting Documents
<img width="443" alt="image" src="https://github.com/black-v0id/black-v0id/assets/16123062/93a23b31-688a-471a-a5c1-37e0b94c4590">
<img width="464" alt="image" src="https://github.com/black-v0id/black-v0id/assets/16123062/40b0b300-16b9-45fd-96f7-dde8c0760494">

## Report
Section 1: Identify the network protocol involved in the incident

Incident was investigated at 14:18 within an isolated sandbox environment segrated from business operations. Our packet sniffer, tcpdump, indicated that the system was compromised using communication protocols within the application TCP/IP layer. The specifc protocol in question is HTTP, port 80. 

Section 2: Document the incident

Roughly around the time of 14:10 on Friday June 23 the company recieved 3rd party reports that upon visiting our company website individuals were prompted to download a file as well as received prompts to update their browser. Preforming these actions resulted in visitors personal devices exhibiting degraded preformance.

Concurrent immediate actions were taken by the following teams:
- The website owner investigated the website portal and discovered a lockout on the account. They have reached out to our web hosting provider to regain access. 
- The network security analysts took action to investigate the reported incident by creating a sandbox environment, an environment segregated from normal business operation systems, and preforming the actions reported. At 14:18 the team ran a network analyzer and confirmed the reported behavior to be accurate. Upon investigating the log data it has been uncovered that after connecting to yummyrecipiesforme.com a HTTP (port 80) GET request is sent out which then completes 2 minuted later at 14:20. This indicates the background download occuring. After the download completes, network traffic is being redirected to the domain greatrecipiesforme.com which is a domain we do not own or manage.
- A senior security analyst preformed a source code investigation of our website and identified javascript code that has been added which prompts website visitors to download an executable file. Analysis of the downloaded file found a script that redirects the visitors’ browsers from yummyrecipesforme.com to greatrecipesforme.com. These modifications we implemented "a few hours earlier than 14:10". 
- The cybersecurity team investigated the web server and discovered a brute force attack on our webserver that occured "a few hours earlier than 14:10". They have reported that the admin password was set as a default and no controls were in place to prevent brute force attacks. 

Upon collecting the above information the security team has investigated the domain greatrecipiesforme.com and found it linked to a former baker who registered the domain.

In summary; an incident occured at "a few hours earlier than 14:10" on Friday June 23 in which malicious action was taken by one former baker whom brute forced our webservers utilizing a default admin password. Upon gaining access to our web server they modified our website code base and added a javascript code which downloads an executable. The executable redirects our website visitors to the domain registered to the former baker in which our recipies are listed as free resources. 


Section 3: Recommend one remediation for brute force attacks

The security team is recommending a full audit of admin accounts on critical infrastructure and ensuring the username and password are:
- not default
- meet password requirements of 14 in length, minimum 1 symbol, minimum 1 capital, minimum 1 number
- not easily gussable i.e. "password4webserver"

Additional actions to be taken include: upgrading protocols to HTTPS, implemneting 2FA, auditing who has access to admin accounts, limiting number of login attempts and monitoring login attempts. 


