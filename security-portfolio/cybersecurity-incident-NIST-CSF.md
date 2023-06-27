
## Scenario
<details>
You are a cybersecurity analyst working for a multimedia company that offers web design services, graphic design, and social media marketing solutions to small businesses. Your organization recently experienced a DDoS attack, which compromised the internal network for two hours until it was resolved.

During the attack, your organization’s network services suddenly stopped responding due to an incoming flood of ICMP packets. Normal internal network traffic could not access any network resources. The incident management team responded by blocking incoming ICMP packets, stopping all non-critical network services offline, and restoring critical network services. 

The company’s cybersecurity team then investigated the security event. They found that a malicious actor had sent a flood of ICMP pings into the company’s network through an unconfigured firewall. This vulnerability allowed the malicious attacker to overwhelm the company’s network through a distributed denial of service (DDoS) attack. 

To address this security event, the network security team implemented: 

A new firewall rule to limit the rate of incoming ICMP packets

Source IP address verification on the firewall to check for spoofed IP addresses on incoming ICMP packets

Network monitoring software to detect abnormal traffic patterns

An IDS/IPS system to filter out some ICMP traffic based on suspicious characteristics

As a cybersecurity analyst, you are tasked with using this security event to create a plan to improve your company’s network security, following the National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF). You will use the CSF to help you navigate through the different steps of analyzing this cybersecurity incident and integrate your analysis into a general security strategy.
</details>

## Summary 
Recently the company experienced an outage on the internal network for two hours. The outage was caused by a malicous external actor launching an ICMP flood attack, commonly categorized as a DDoS attack, against the network. This attack is used to overwhlem the network with ICMP packets thus rendering it inaccessible to normal traffic. The team responded by blocking the attack then stopping all non-critical network services in order to restore the critical network services.  

## Identify
The incident management team evaluated the systems impacted by the attack and identified an incoming flood of ICMP packets which was preventing normal traffic from accessing network resources. The cybersecruity team then identified the malicious actor to have exploited the companies unconfigured firewall to send a flood of ICMP pings to the network. This is commonly refered to as a distributed denial of service (DDoS) attack.

## Protect
 Based on the findings the network security team has implemented a new firewall rule that limits the rate of incoming ICMP packets has been implemented as well as an IDS/IPS system to automatically filter out ICMP traffic detections based on suspicious characteristics.

## Detect
To detect future ICMP attacks the the network security team has added network software monitoring tools to detect abnormal traffic patterns and implemented source IP verification on the firewall which checks for spoofed IP addresses on incoming ICMP packets. 

## Respond 
As an immediate action, the incident management team responded by blocking incoming ICMP packets and stopping all non-critical network services, thus allowing us to restore critical services. Going forward, the security team will isolate effected system to stop the spread of a large network outage. As in this instance, the team will make attempts to restore critical systems and services that have been distrupted before addressing non-critical systems. Finally, utilizing the network logs the team will analyze the data to pinpoint any suspicious or abnormal activity. Any incidents with outage times defined within our disaster recovery plan will need to be communicated to the company/affected department heads through unaffected channels or alternate established channels. 

## Recover
In the event a malicious ICMP attack slips through the newly implemented systems, the team will recover from a network outage by employing industry best practices and communicating amongst key team members in order to restore the system to a normal functioning state. 


## 🤔 Reflection/Notes
Summary: I liked how they specifically referenced the team that identified the problem as well as the resolution since this scenario is working from the aftermath side of things. I have updated my section to include these modifications. i think their example should have mentioned the duration to get a scope on the impact. 

Identify: their example was shorter... but with my experience I like the details I added for context. I'm also starting to recognize some overlap, is it imperative to add "resources were secured and restored to functioning state" if that is addressed in the respond section? Or I guess I am recognizing that given the context and situation of the reports purpose each section takes on a different purpose. 

Protect: aha. I see how the scenario subtly added context while allowing students to parse out what action falls under which bucket. I shuffled where I placed certain actions in the various NIST buckets. 

Respond: mmm. I see. Again more of a response to the new system put in place and not necessarily what did happen. I different lense that I wasn't seeing at the time of writing this up. Changes have been made to reflect this. 

Recover: Thier example just restates the same things mentioned in respond, not sure I like the repitition but also I was grasping for words to add to this section and kept landing at "get the system running via discussed methods?". I can recognize why the repition is important in this case. 
