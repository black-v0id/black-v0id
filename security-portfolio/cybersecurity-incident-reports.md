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
