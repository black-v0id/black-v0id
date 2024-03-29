# Botium Toys Audit Report
Prepared by: Karen G

Date: June 14, 2023

## Introduction
### About Company
Ficticious company. Small U.S. business that develops and sells toys. 

### Scope
Preform an audit of companys cybersecurity prorgam. The audit must align to current business practices with industry standards and best practices. The audit is meant to provide mitigation recommendations for vulnerabilities found that are classified as "high risk" and present and overall strategy for improving the security posture of the organization. 

- Assess IAM permissions, evaluate existing implemented controls, and assess present procedures and protocol sets for the following systems:
    - accounting
    - endpoint detection
    - firewalls
    - intrustion detection
    - SIEM tool
- Evaluate existing user permissions, controls, procedures, and protocols in place allign with industry standards and best practices

### Deliverables
- Adhere to NIST CSF
- Establish better process for systems to ensure they are compliant
- Fortify system controls
- Implement principle of least permissions for user credential management
- Establish policies and procedures, including playbooks
- Ensure company is meeting compliance requirements

### Security Assessment Methodology
All information was directly provided by the G00gle Certified Course. Some notes have been expanded upon due to lack of information. 

### Prioritization of Issues
- 🔴 HIGH: puts the company at risk and should be rectified as soon as possible
- 🟠 MEDIUM: chance of putting the company at risk but can be addressed in the future
- 🟡 LOW: issues should be addressed down the road in the future pending the resolution of both high and medium issues
- BLANK: no data indicating that this is a threat vector within the assessment scope

## Risk Assesment 
‼️ The following risk assessment was provided to me to assist in my evaluation of controls assessment and formal report. 
<details>
    
### Description 
Currently, there is inadequate management of assets. Additionally, the company does not have the proper controls in place and may not be complaint with U.S. and international regulations and standards. 

### Controls Best Practices
The company will need to dedicate resources to managing assets. Additionally, they will need to determine the impact of the loss of existing assets, including systems, on business continuity. 

### Risk Score
On a scale on 1 to 10, the risk score is 8, which is fairly high. This is due to a lack of controls and adherence to necessary compliance regulations and standards. 

### Additional Comments
The potential impact from the loss of an asset is rated as MEDIUM, IT is unaware which assets would be lost. The likelihood of a lost asset causing damage or recieving fines from a governing body is HIGH due to company not implementing all necessary conrols in addition to not adhering to required regulations and standards in keeping customer data private. 
</details>

## Controls Assessment
    
### Administrative Controls   
| Control Name  | Control type and detail | Needs to be implemented (X) | Priority |
| ------------- | ----------------------- | --------------------------- | -------- |
| Least Privilege  | Preventative; reduces risk by making sure vendors and non-authorized staff only have access to the assets/data within their job scope | X  | MEDIUM |
| Disaster recovery  | Corrective; business continuity  | X | LOW |
| Password policy | Preventative; establish password strength rules | | |
| Access control policies | Preventative; increase confidentiality and integrity of data | X | HIGH |
| Account management policies | Preventative; reduce attack surface | X | MEDIUM |
| Seperation of duties | Preventative; ensure access is appropriately mapped to employees | X | HIGH |


### Technical Controls    
| Control Name  | Control type and detail | Needs to be implemented (X) | Priority |
| ------------- | ----------------------- | --------------------------- | -------- |
| Firewall | Preventative; (already in place) |  |  |
| IDS | Detective; identify intrusions quickly | X | LOW |
| Encryptions | Deterrent; secure confidential information | X | HIGH |
| Backups | Corrective; aligns to DR plan | X | MEDIUM* |
| Password management system | Corrective; password recovery/lockout |  |  |
| AV software | Corrective; detect and quarentine known threats | X | HIGH |
| Manual monitoring, maintenance, intervention | Preventative/Corrective; for legacy systems | X | HIGH* |

* Backups = ensure current controls match DR plan or are improved upon based on NIST CSF standards
* Manual monitoring = situation I was given to evaluate did not have details on the legacy system besides "they're there"; in this case I would be sure to evaluate if the systems could be replaced/upgraded and if there are devices that are accepted risk are they seperated from the network and what effort of monitoring do they require


### Physical Controls
| Control Name  | Control type and detail | Needs to be implemented (X) | Priority |
| ------------- | ----------------------- | --------------------------- | -------- |
| Time-controlled safe | Deterrent; reduce attack surface of physical threats |  |   |
| Adequate lighting | Deterrent; deters threats |  |  |
| CCTV Surveillance | Preventative; reduce risk of certain events | X | LOW |
| Locking cabinets (network gear) | Preventative; prevent unauthorized access | X | HIGH |
| Signage indicating alarm service provider | Deterrent |  |  |
| Locks | Preventative; physical and digital assets more secure | X | MEDIUM |
| Fire detection and prevention | Detective/Preventative; prevents damage to inventory |  |  |

## Summary of Findings
| Severity | # of Findings |
| -------- | ------------- |
| HIGH | 6 |
| MEDIUM | 4 |
| LOW | 3 |
| NA | 7 | 

## Report
<details>
    
### 🔴 HIGH 🔴
#### 1. Access control policies 
Preform full assesment of existing permissions across sytems and implement RBAC controls. Further more, ensure system has MFA enabled as well as policies that restrict devices and locations that are not used within the company.  
Will satisfy GDPR requirement for compliance. 

#### 2. Seperation of duties 
Reassess current job descriptions and duties held by existing staff. Based on review take necessary action such as expanding access, taking away access, creating new procedures, hiring in new staff, etc. 

#### 3. Encryption 
Ensure all critical assets and data are encrypted, particularly customer databases that include indentifying informaiton. This is a requirement for PCI DSS compliance. 

#### 4. Anti Virus Software
While taking inventory of assets, install anti-virus to protect devices from malicious intent. 

#### 5. Manual monitoring, maintenance, intervention 
Take necessary steps to upgrade/destroy assets which are considered legacy and add unnecessary strain to the IT team for management. 
Any legacy system that is an accepted risk should take all other cautions available such as segrgating it from the network, ensuring proper access and passwords, frequent audits of system. 

#### 6. Locking cabinets (network gear)
Ensure networking gear is accounted for an accessible only by IT and necessary C suite members.


### 🟠 MEDIUM 🟠
#### 1. Account management policies 
Establish policies and procedures so that there is a clear understanding amoung key stakeholders and IT deptment on what to expect from account creation, to account management, to account termination. 

#### 2. Least Privilege 
Implement this core security principle to reduce attack surface and secure assets. 

#### 3. Backups
To protect data implement strategy to preform backups of critical assets. 

#### 4. Locks
Create secure area for IT team to house un-used physical assets to aid in keeping track of such assets.

### 🟡 LOW 🟡
#### 1. Disaster recovery  
Develop a disaster recovery plan, while not explicity required by the GDPR it is empasized that there should be a appropriate security measures and ability to restore data in timely manner following incident. 
Disaster recovery is considered best practice for ensuring business continuity, minimizing down time and protecting critical data/systems. 

#### 2. Intrusion Detection System
Implement IDS to assit IT team in having a way to detect threats, respond to incidents, get visibility on the network, and meet the requirement of the GDPR to implement technical measures to ensure the security of personal data.

#### 3. CCTV
Implement at headquarters to assist in identifying any security incident on site. 
</details>

## Compliance Checklist
The following section is an anlysis to critically identify which compliance regulations this ficticious company must comply to. 

<details>
### ❌ FREC-NERC
This regulation is not required to be met by the company because it does not work with electricty or is involved with the US power grid. 

### ✅ GDPR
This is a regulation that the company will need to comply with. As they expand the business to operate in Europe they will have to comply with this regulation. 

### ✅  PCI DSS
This is a requirement that the compnay will need to comply with. Because it is noted that the IT Dept manages an ecommerce system we can assume there is credit card information involved (or EIN numbers) which falls under the payment card industry. 

### ❌ HIPAA
This regulation is not required to be met by the company because it does not work with health care data. 

### ❌ SOC type 1, SOC type 2
This regulation is not required, however it is strongly encouraged to look to this documentation for guidance. Being that the company is a toy company it is not imperative that they seek out SOC I and SOC II certification. Additionally, this can be a costly certificate to obtain. 
</details>

## Stakeholder Memorandum
The following fictional email was drafted after viewing the exemplar and taking note from suggested critical rankings + my learned false assumptions. I also went rogue from the provided template. I believe a good audit will include a summary of why the control is necessary and therefore does not need to be listed in an email, the report would be attached. Also the activity made suggestions for the length of the email and in my opinion would have been far to long for anyone to read all the way through, I have shortened and condensed. 
<details>
<summary>Internal IT Audit Findings and Recommendations</summary> 
    
> TO: IT Manager, Stakeholders
> 
> FROM: Karen G
> 
> DATE: June 14 2023
> 
> SUBJECT: Internal IT Audit Findings and Recommendations


Hey everyone, 

We recently conducted an internal audit of Botium Toys, I have included my condensed thoughts and attached the audit report for more details and context. 

**;TLDR/Summary**

We have quite the list of high priority items to address. I believe the department can tackle several items, including password policies, but not all this quarter. 
The IT department will begin project scoping and request funds for the following systems: antivirus, IDS, password management system, CCTV. 
I believe that with these efforts and given the current projects in the pipeline IT can accomplish most of our goals by end of year but will need support from you all. 

🔍 **Audit Scope**

Evaluate existing user permissions, controls, procedures, and protocols across IT systems. Validate that we are alligned with industry best practices as well as the required regulations GDPR (EU law on data protection and privacy) and PCI DSS (information security standard used to handle credit card data). 

🏆 **IT Goals**
- Adhere to NIST CSF
- Establish better process for systems to ensure they are compliant
- Fortify system controls
- Establish policies and procedures, including playbooks
- Ensure meeting compliance requirements

‼️ **Critical Findings (must be addressed immediately)**

The attached report will have the full list of HIGH priority items including details on the importance of each item. I have analyzyed the list and parsed it down to the top 7 items that we can for sure address this quarter that will significantly improve our security posture. 
- password polices
- encryption
- backups
- locks
- seperation of duties
- draft of disaster recovery plan
- access control polices

⚠️ **Findings Requiring Additional Processes**

The following list is items that I strongly believe we should implement this year but will require a project definition and addition funding approval.
- antivirus
- IDS
- password managment system
- CCTV

All the best, 
K
</details>


## 🤔💡 Thought Process 
<details>
<summary>Here lies my thought process while formalizing the final documentation.</summary> 

### Info I Have
**Scope/Goals/Deliverables (provided by situation)**
- Assess IAM permissions, evaluate existing implemented controls, and assess present procedures and protocol sets for the following systems:
    - accounting
    - endpoint detection
    - firewalls
    - intrustion detection
    - SIEM tool
- Evaluate existing user permissions, controls, procedures, and protocols in place allign with NIST CSF and GDPR compliance requirements
- Ensure current technology is accounted for both physical and logical
- Adhere to NIST CSF
- Establish better process for systems to ensure they are compliant
- Fortify system controls
- Implement principle of least permissions for user credential management
- Establish policies and procedures, including playbooks
- Ensure meeting compliance requirements

**Risk Assessment (provided by situation)**
- Inadequate management of assets
- Proper controls are not in place
- May not be compliant with U.S. and international regulations and guidelines
- Current risk score is 8/10 (high), due to a lack of controls and adherence to compliance regulations and standards

**Asset List**
Managed by IT Dept:
- on-prem equipment for in-office business needs
- employee equipment: end-user devices, remote workstations, headsets, keyboards, docking stations, surveillance cameras
- management of systems, software, and services: accounting, telecommunicaiton, database, security, ecommerce, inventory management
- internet access
- vendor access management
- data center hosting services
- data retention and storage
- badge readers
- legacy system maintance: EOL systems needing human monitoring

I find myself doing a lot of "... but what if" scenarios like "what if the network password is admin/admin" "what if there is 1 IT person running all of this" "what if there are some controls in place but not up to date with the growth and change of positions within the company" so I catch myself trying to refocus on the scope given and the explicit details I have. 

❓ what are the biggest risks to the organization?

    - Legacy system management - that takes time and manpower which takes away from other tasks 
    - Business continuity outages via lack of controls & procedures - bringing in new team members is challenging and so is communicating with other departments due to a lack of policies, procedures and unified controls 
    - Security misconfiguration - if they aren't sure what the controls are/where the assets are then they have a major hole in the system for visibility 
    - Compliance risk - if they are expanding into EU they must comply with GDPR before conducting business and PCI DSS can be a heafty regulation to implement if they have not started/designed around the requirements within

❓ which controls are most essential to implement immediately vs in the future?

    immediate: implement controls on firewall that are alligned to NIST followed by accounting system then ED then ID them SIEM tools; IAM controls via principle of least privilege; creating proesses and procedures with subsequent training/re-education of staff
    future: establish process for ensuring system is compliant; 

❓ which compliance regulations does the company need to adhere to, to ensure the company keeps customer and vendor data safe, avoids fines, etc.?

    The compliance regulation to adhere to is the GDPR and PCI DSS. The framework that is going to aid them in getting there is the NIST CSF which is mapped in further deatil by resources such as NIST 800, ISO 2700 etc.

</details>


## 👀 Spoilers and Personal Review

<details>
<summary>Exemplars of Activity</summary> 
After reviewing the "correct answers" provided (not going to provide them here in case anyone finds this that is enrolled and wants to skip ahead) I have a few take aways. 


1. I scored things a lot more cautiously, to me having 6 HIGH items for a toy company felt like a lot. I made the report with empathy for the company and getting them a list they could tackle vs what is required by compliance regulations. I should have approached this from an auditors perspective vs an internal leader putting emphasis on what is most important. 
2. I commpletely overlooked the wording "Proper controls are not in place", I was so focused on regluations that I assumed that that is what was being referred. So I assumed basic technical controls were in place and regulation controls were not. I would change several rankings after this realization. 
3. I disagree on SOC, it is not a US requirement by law. It does make business easier since a lot of companies ask for the report to vet a company but a TOY COMPANY?!?! They have bigger fish to fry than obtaining that. 


</details>
