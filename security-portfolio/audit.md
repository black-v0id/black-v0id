# Botium Toys Audit Report
Prepared by: Karen G
Date: June 12, 2023

## Introduction
### About Company
Ficticious company. Small U.S. business that develops and sells toys. 

### Scope
- Assess IAM permissions, evaluate existing implemented controls, and assess present procedures and protocol sets for the following systems:
    - accounting
    - endpoint detection
    - firewalls
    - intrustion detection
    - SIEM tool
- Evaluate existing user permissions, controls, procedures, and protocols in place allign with NIST CSF and GDPR copliance requirements
- Ensure current technology is accounted for both physical and logical. 

### Deliverables
- Adhere to NIST CSF
- Establish better process for systems to ensure they are compliant
- Fortify system controls
- Implement principle of least permissions for user credential management
- Establish policies and procedures, including playbooks
- Ensure meeting compliance requirements

## Controls Assesment
|     Administrative Controls   |
| Control Name  | Control type and detail | Needs to be implemented (X) | Priority |
| ------------- | ----------------------- | --------------------------- | -------- |
| Least Privilege  | Preventative; reduces risk by making sure vendors and non-authorized staff only have access to the assets/data within their job scope | X  | MEDIUM |
| Disaster recovery  | Corrective; business continuity  | X | HIGH |
| Password policy | Preventative; establish password strength rules | | |
| Access control policies | Preventative; increase confidentiality and integrity of data | X | HIGH |
| Account management policies | Preventative; reduce attack surface | X | HIGH |
| Seperation of duties | Preventative; ensure access is appropriately mapped to employees | X | MEDIUM |


|    Technical Controls    |
| Control Name  | Control type and detail | Needs to be implemented (X) | Priority |
| ------------- | ----------------------- | --------------------------- | -------- |
| Firewall | Preventative; (already in place) |  |  |
| IDS | Detective; identify intrusions quickly | X | LOW |
| Encryptions | Deterrent; secure confidential information |  |  |
| Backups | Corrective; aligns to DR plan | X | MEDIUM* |
| Password management system | Corrective; password recovery/lockout |  |  |
| AV software | Corrective; detect and quarentine known threats |  |  |
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
| Locks | Preventative; physical and digital assets more secure | X | LOW |
| Fire detection and prevention | Detective/Preventative; prevents damage to inventory |  |  |

## Findings Severity Breakdown

## Report

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

:questionmark: what are the biggest risks to the organization?
    - Legacy system management - that takes time and manpower which takes away from other tasks
    - Business continuity outages via lack of controls & procedures - bringing in new team members is challenging and so is communicating with other departments due to a lack of policies, procedures and unified controls
    - Security misconfiguration - if they aren't sure what the controls are/where the assets are then they have a major hole in the system for visibility 
    - Compliance risk - if they are expanding into EU they must comply with GDPR before conducting business

:questionmark: which controls are most essential to implement immediately vs in the future?
    immediate: implement controls on firewall that are alligned to NIST followed by accounting system then ED then ID them SIEM tools; IAM controls via principle of least privilege 
    future: establish process for ensuring system is compliant; 

:questionmark: which compliance regulations does the company need to adhere to, to ensure the company keeps customer and vendor data safe, avoids fines, etc.?
    The compliance regulation to adhere to is the GDPR. The Frameworks that is going to aid them in getting there is the NIST CSF. 




</deatils>