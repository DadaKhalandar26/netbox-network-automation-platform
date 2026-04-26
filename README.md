# NetBox Network Automation Platform

## 🚀 Overview

This project is an enterprise-grade network automation platform built using **Python**, **NetBox**, and **multi-vendor automation frameworks**.

It demonstrates how to design and implement a scalable, production-ready automation system using NetBox as the **Source of Truth (SoT)**.

---

## 🧠 Key Features

* 🔹 NetBox-driven automation (single source of truth)
* 🔹 Multi-vendor support (Cisco, Arista, Juniper)
* 🔹 Modular and scalable architecture
* 🔹 Service-based automation (VLAN, BGP, Interfaces)
* 🔹 Jinja2 templating for configuration generation
* 🔹 Workflow-based execution (real-world use cases)
* 🔹 Logging and error handling
* 🔹 Ready for CI/CD integration

---

## 🏗️ Architecture

NetBox → Data Source
↓
Python Automation Layer
↓
Jinja2 Templates
↓
Network Devices (via Netmiko / Paramiko)

---

## 📂 Project Structure

```
automation/
  ├── vendors/        # Vendor-specific logic
  ├── services/       # Network services (VLAN, BGP, etc.)
  ├── workflows/      # End-to-end automation use cases

netbox/
  ├── client.py       # NetBox API integration

templates/
  ├── cisco/          # Jinja2 templates
```

---

## ⚙️ Technologies Used

* Python 3.14.4
* NetBox (Source of Truth) NetBox Community v4.5.8
* Netmiko / Paramiko
* Jinja2
* REST APIs
* YAML / JSON

---

## 🔄 Example Workflows

### 1. VLAN Deployment

* Fetch VLAN details from NetBox
* Generate configuration using Jinja2
* Push config to devices

### 2. Device Onboarding

* Pull device info from NetBox
* Apply base configuration
* Validate deployment

### 3. Configuration Backup

* Connect to devices
* Fetch running config
* Store locally

---

## 🔐 Environment Setup

1. Clone the repository:

```
git clone https://github.com/DadaKhalandar26/netbox-network-automation-platform.git
cd netbox-network-automation-platform
```

2. Create virtual environment:

```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Configure environment variables:

```
cp .env.example .env
```

---

## 📌 Future Enhancements

* Integration with Ansible / AWX
* CI/CD pipeline (GitHub Actions)
* Web UI for triggering automation
* Role-based access control
* Network validation and compliance checks

---

## 👨‍💻 Author

Network Engineer | Network Automation Enthusiast | B S Dada Khalandar
