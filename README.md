# Custom SOC Automation & Threat Detection Pipeline

## Objective
This project demonstrates the design and deployment of a custom local Security Operations Center (SOC) environment to simulate, ingest and detect advanced adversarial tactics. The pipeline automatically parses endpoint telemetry to identify MITRE ATT&CK T1003.001 (OS Credential Dumping).

## Technologies & Tools
* **Infrastructure:** Windows 11 & Ubuntu Linux Virtual Machines
* **SIEM & Telemetry:** Splunk Enterprise, Splunk Universal Forwarder, Sysmon
* **Adversary Simulation:** Atomic Red Team
* **Automation:** Python 

## The Pipeline

### 1. Adversary Simulation
Executed a simulated credential dumping attack against the Local Security Authority Subsystem Service (LSASS) using Atomic Red Team. 

![Attack Execution](Attack%20Execution.png)

### 2. Log Ingestion & Forwarding
Configured a Splunk Universal Forwarder to capture Sysmon Event ID 1 (Process Creation) telemetry and transmit it across the network to a centralized Linux SIEM server.

![Splunk Ingestion](SIEM%20Ingestion.png)

### 3. Automated Threat Detection
Developed a custom Python automation script to parse exported SIEM data, evaluate logs against a threat intelligence database, and generate critical alerts upon detecting the `rdrleakdiag.exe` payload.

![Python Detection](Automated%20Detection.png)
