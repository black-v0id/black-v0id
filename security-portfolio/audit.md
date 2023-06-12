# Botium Toys Audit Report
Prepared by: Karen G

Date: June 12, 2023

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
- Evaluate existing user permissions, controls, procedures, and protocols in place allign with NIST CSF and GDPR copliance requirements

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
- HIGH: puts the company at risk and should be rectified as soon as possible
- MEDIUM: chance of putting the company at risk but can be addressed in the future
- LOW: issues should be addressed down the road in the future pending the resolution of both high and medium issues
- BLANK: no data indicating that this is a threat vector within the assessment scope

## Risk Assesment 
all of the following information was provided to me to assist in my evaluation of controls assessment and recomendations. 
### Description 
Currently, there is inadequate management of assets. Additionally, the compnay does not have the proper controls in place and may not be complaint with U.S. and international regulations and standards. 

### Controls Best Practices
The compnay will need to dedicate resources to managing assets. Additionally, they will need to determine the impact of the loss of existing assets, including systems, on business continuity. 

### Risk Score
On a scale on 1 to 10, the risk score is 8, which is fairly high. This is due to a lack of controls and adherence to necessary compliance regulations and standards. 

### Additional Comments
The potential impact from the loss of an asset is rated as MEDIUM, IT is unaware which assets would be lost. The likelihood of a lost asset causing damage or recieving fines from a governing body is HIGH due to company not implementing all necessary conrols in addition to not adhering to required regulations and standards in keeping customer data private. 


## Controls Assessment
|     Administrative Controls   |
| Control Name  | Control type and detail | Needs to be implemented (X) | Priority |
| ------------- | ----------------------- | --------------------------- | -------- |
| Least Privilege  | Preventative; reduces risk by making sure vendors and non-authorized staff only have access to the assets/data within their job scope | X  | MEDIUM |
| Disaster recovery  | Corrective; business continuity  | X | HIGH |
| Password policy | Preventative; establish password strength rules | | |
| Access control policies | Preventative; increase confidentiality and integrity of data | X | HIGH |
| Account management policies | Preventative; reduce attack surface | X | MEDIUM |
| Seperation of duties | Preventative; ensure access is appropriately mapped to employees | X | HIGH |


|    Technical Controls    |
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



|    Physical Controls    |
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
| HIGH | 7 |
| MEDIUM | 4 |
| LOW | 2 |
| NA | 7 | 

## Report
HIGH

MEDIUM

LOW



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

:questionmark: what are the biggest risks to the organization?
    - Legacy system management - that takes time and manpower which takes away from other tasks
    - Business continuity outages via lack of controls & procedures - bringing in new team members is challenging and so is communicating with other departments due to a lack of policies, procedures and unified controls
    - Security misconfiguration - if they aren't sure what the controls are/where the assets are then they have a major hole in the system for visibility 
    - Compliance risk - if they are expanding into EU they must comply with GDPR before conducting business

:questionmark: which controls are most essential to implement immediately vs in the future?
    immediate: implement controls on firewall that are alligned to NIST followed by accounting system then ED then ID them SIEM tools; IAM controls via principle of least privilege; creating proesses and procedures with subsequent training/re-education of staff
    future: establish process for ensuring system is compliant; 

:questionmark: which compliance regulations does the company need to adhere to, to ensure the company keeps customer and vendor data safe, avoids fines, etc.?
    The compliance regulation to adhere to is the GDPR. The framework that is going to aid them in getting there is the NIST CSF which is mapped in further deatil by resourcrs such as NIST 800, ISO 2700 etc.




</deatils>