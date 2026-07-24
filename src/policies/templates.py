from dataclasses import dataclass, field
from typing import List


@dataclass
class PolicyTemplate:
    id: str
    name: str
    category: str
    sections: List[str] = field(default_factory=list)


def get_policy_templates() -> List[PolicyTemplate]:
    return [
        PolicyTemplate(
            "POL-IT-001",
            "IT Security Policy",
            "Security",
            [
                "Purpose", "Scope", "Policy Statements", "Roles and Responsibilities",
                "Asset Management", "Access Control", "Cryptography", "Physical Security",
                "Operations Security", "Communications Security", "System Acquisition & Development",
                "Supplier Relationships", "Incident Management", "Business Continuity",
                "Compliance", "Policy Review", "Exceptions", "Enforcement",
                "Definitions", "References", "Document History",
            ],
        ),
        PolicyTemplate(
            "POL-AC-001",
            "Access Control Policy",
            "Security",
            [
                "Purpose", "Scope", "Policy Statements", "Access Control Principles",
                "User Access Management", "User Responsibilities", "Network Access Control",
                "Operating System Access", "Application Access", "Privileged Access Management",
                "Remote Access", "Authentication Methods", "Password Requirements",
                "Session Management", "Access Review", "Separation of Duties",
                "Compliance and Audit", "Enforcement",
            ],
        ),
        PolicyTemplate(
            "POL-IS-001",
            "Information Security Policy",
            "Security",
            [
                "Purpose", "Scope", "Information Security Objectives", "Leadership Commitment",
                "Risk Management Approach", "Asset Classification", "Information Handling",
                "Access Control", "Encryption and Key Management", "Physical Security",
                "Network Security", "Application Security", "Incident Response",
                "Business Continuity", "Third Party Security", "Compliance Obligations",
                "Training and Awareness", "Monitoring and Review", "Non-Compliance",
                "Definitions", "References", "Document Control",
            ],
        ),
        PolicyTemplate(
            "POL-BC-001",
            "Business Continuity & Disaster Recovery Plan",
            "Resilience",
            [
                "Purpose", "Scope", "BCM Policy", "BCM Governance Structure",
                "Business Impact Analysis", "Risk Assessment", "Recovery Objectives",
                "Continuity Strategies", "Incident Response Structure", "Emergency Procedures",
                "Crisis Management", "Communication Plan", "IT Disaster Recovery",
                "Data Backup and Restoration", "Alternate Site Procedures", "Critical System Recovery",
                "Vendor Continuity", "Testing and Exercises", "Plan Maintenance",
                "Training and Awareness", "Roles and Responsibilities", "Appendices",
                "Compliance References", "Document Control", "Review Schedule",
            ],
        ),
        PolicyTemplate(
            "POL-IR-001",
            "Incident Response Policy",
            "Security",
            [
                "Purpose", "Scope", "Incident Classification", "Incident Response Team",
                "Roles and Responsibilities", "Detection and Reporting", "Triage and Assessment",
                "Containment Strategies", "Eradication and Recovery", "Forensic Investigation",
                "Communication Procedures", "Regulatory Reporting", "Post-Incident Review",
                "Plan Testing", "Training Requirements", "Enforcement",
            ],
        ),
        PolicyTemplate(
            "POL-DP-001",
            "Data Protection & Privacy Policy",
            "Privacy",
            [
                "Purpose", "Scope", "Privacy Principles", "Data Classification",
                "Data Collection", "Data Processing", "Data Storage", "Data Retention",
                "Data Disposal", "Data Subject Rights", "Consent Management",
                "Cross-Border Data Transfer", "Data Breach Notification", "Third Party Data Sharing",
                "Privacy Impact Assessment", "Compliance and Audit",
            ],
        ),
        PolicyTemplate(
            "POL-TP-001",
            "Third Party Security Policy",
            "Security",
            [
                "Purpose", "Scope", "Third Party Classification", "Risk Assessment",
                "Due Diligence", "Contractual Security Requirements", "Data Protection Clauses",
                "Access Control", "Monitoring and Review", "Incident Reporting",
                "Termination Procedures", "Compliance",
            ],
        ),
        PolicyTemplate(
            "POL-SA-001",
            "Security Awareness Policy",
            "Security",
            [
                "Purpose", "Scope", "Program Objectives", "Training Requirements",
                "Training Content", "Delivery Methods", "Target Audiences",
                "Frequency and Schedule", "Assessment and Testing", "Reporting",
                "Continuous Improvement", "Enforcement",
            ],
        ),
        PolicyTemplate(
            "POL-NS-001",
            "Network Security Policy",
            "Security",
            [
                "Purpose", "Scope", "Network Architecture", "Segmentation and Zoning",
                "Firewall Management", "Remote Access Security", "Wireless Security",
                "Network Monitoring", "Intrusion Detection/Prevention", "VPN Security",
                "DNS Security", "DHCP Security", "Network Device Hardening",
                "Change Management", "Audit Logging", "Compliance",
            ],
        ),
        PolicyTemplate(
            "POL-AU-001",
            "Acceptable Use Policy",
            "Security",
            [
                "Purpose", "Scope", "General Principles", "Email Usage",
                "Internet Usage", "Social Media", "Personal Devices",
                "Software Installation", "Data Handling", "Prohibited Activities",
                "Monitoring and Enforcement", "Compliance",
            ],
        ),
    ]
