from typing import List, Dict
from src.controls.framework import ControlFramework, Control


def get_bi_regulations() -> List[Dict]:
    return [
        {
            "id": "POJK.11.2022",
            "name": "POJK No. 11/POJK.03/2022",
            "title": "Penyelenggaraan Teknologi Informasi oleh Bank Umum",
            "description": "IT implementation and risk management requirements for commercial banks",
            "year": 2022,
        },
        {
            "id": "POJK.12.2021",
            "name": "POJK No. 12/POJK.03/2021",
            "title": "Inovasi Teknologi di Sektor Perbankan",
            "description": "Technology innovation governance in the banking sector",
            "year": 2021,
        },
        {
            "id": "POJK.38.2016",
            "name": "POJK No. 38/POJK.03/2016",
            "title": "Manajemen Risiko Teknologi Informasi Bank Umum",
            "description": "IT risk management framework for commercial banks",
            "year": 2016,
        },
        {
            "id": "PBI.9.2007",
            "name": "PBI No. 9/15/PBI/2007",
            "title": "Manajemen Risiko Teknologi Informasi",
            "description": "IT risk management requirements for Bank Indonesia regulated entities",
            "year": 2007,
        },
        {
            "id": "POJK.13.2021",
            "name": "POJK No. 13/POJK.03/2021",
            "title": "Perlindungan Konsumen",
            "description": "Consumer protection requirements including data privacy in banking",
            "year": 2021,
        },
        {
            "id": "POJK.18.2020",
            "name": "POJK No. 18/POJK.03/2020",
            "title": "Anti-Fraud Strategy",
            "description": "Anti-fraud strategy requirements for banks",
            "year": 2020,
        },
        {
            "id": "POJK.12.2018",
            "name": "POJK No. 12/POJK.03/2018",
            "title": "Business Continuity Management",
            "description": "Business continuity management requirements for banks",
            "year": 2018,
        },
    ]


def get_bi_controls() -> ControlFramework:
    controls = [
        Control("BI-01", "IT Strategic Alignment", "Governance",
                "Align IT strategy with business strategy and regulatory requirements"),
        Control("BI-02", "IT Risk Management Framework", "Risk Management",
                "Implement comprehensive IT risk management framework per POJK 11/2022"),
        Control("BI-03", "Data Protection", "Security",
                "Protect customer data and banking information per POJK consumer protection"),
        Control("BI-04", "Business Continuity Planning", "Resilience",
                "Maintain business continuity and disaster recovery plans per POJK 12/2018"),
        Control("BI-05", "IT Change Management", "Operations",
                "Implement structured change management for IT systems"),
        Control("BI-06", "Vendor Risk Management", "Governance",
                "Manage risks from third party IT vendors and outsourcing"),
        Control("BI-07", "Fraud Detection and Prevention", "Security",
                "Implement anti-fraud strategy and monitoring per POJK 18/2020"),
        Control("BI-08", "IT Audit and Compliance", "Governance",
                "Conduct regular IT audits to ensure regulatory compliance"),
        Control("BI-09", "Incident Management", "Operations",
                "Establish IT incident management and reporting procedures"),
        Control("BI-10", "Technology Innovation Governance", "Governance",
                "Govern technology innovation initiatives per POJK 12/2021"),
        Control("BI-11", "System Access Control", "Security",
                "Control access to banking systems based on least privilege"),
        Control("BI-12", "Security Operations Center", "Security",
                "Establish SOC for continuous monitoring of banking systems"),
    ]
    return ControlFramework("BI/POJK Regulations", "Various", controls)
