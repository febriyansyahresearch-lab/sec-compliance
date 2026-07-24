from dataclasses import dataclass, field
from typing import List
from src.controls.framework import ControlFramework


@dataclass
class AuditItem:
    id: str
    control_ref: str
    question: str
    evidence_required: str
    status: str = "pending"


def generate_checklist(framework: ControlFramework) -> List[AuditItem]:
    items = []
    for i, c in enumerate(framework.controls, 1):
        items.append(
            AuditItem(
                id=f"AUD-{framework.name[:3].upper()}-{i:03d}",
                control_ref=c.id,
                question=f"Is the control '{c.name}' implemented and operating effectively?",
                evidence_required=f"Evidence for: {c.description}",
            )
        )
    return items


def get_nist_audit_checklist() -> List[AuditItem]:
    return [
        AuditItem("AUD-NST-001", "GV.OC-01",
                  "Is the organizational context documented and understood?",
                  "Organizational context documentation"),
        AuditItem("AUD-NST-002", "GV.RM-01",
                  "Is the risk management strategy formally established?",
                  "Risk management strategy document"),
        AuditItem("AUD-NST-003", "GV.PO-01",
                  "Are cybersecurity policies established and maintained?",
                  "Policy documents and review records"),
        AuditItem("AUD-NST-004", "ID.AM-01",
                  "Is there a complete inventory of physical devices?",
                  "Asset inventory report"),
        AuditItem("AUD-NST-005", "ID.RA-01",
                  "Are cybersecurity risk assessments conducted regularly?",
                  "Recent risk assessment reports"),
        AuditItem("AUD-NST-006", "PR.AC-01",
                  "Is identity and access management implemented?",
                  "IAM policy and access review logs"),
        AuditItem("AUD-NST-007", "PR.DS-01",
                  "Is data at rest protected with encryption?",
                  "Encryption implementation evidence"),
        AuditItem("AUD-NST-008", "PR.AT-01",
                  "Are cybersecurity awareness programs conducted?",
                  "Training records and completion reports"),
        AuditItem("AUD-NST-009", "DE.CM-01",
                  "Is continuous monitoring in place for networks and systems?",
                  "Monitoring configuration and alerts"),
        AuditItem("AUD-NST-010", "DE.CM-02",
                  "Are logs collected from diverse sources?",
                  "Log collection and SIEM configuration"),
        AuditItem("AUD-NST-011", "RS.MA-01",
                  "Is an incident response plan in place and tested?",
                  "Incident response plan and test results"),
        AuditItem("AUD-NST-012", "RC.RP-01",
                  "Is a recovery plan documented and tested?",
                  "Recovery plan and exercise reports"),
    ]


def get_iso27001_audit_checklist() -> List[AuditItem]:
    return [
        AuditItem("AUD-ISO-001", "A.5.1",
                  "Is the information security policy defined and approved?",
                  "Approved information security policy"),
        AuditItem("AUD-ISO-002", "A.5.9",
                  "Is an inventory of information assets maintained?",
                  "Asset inventory list"),
        AuditItem("AUD-ISO-003", "A.5.10",
                  "Are acceptable use rules defined for information assets?",
                  "Acceptable use policy"),
        AuditItem("AUD-ISO-004", "A.6.3",
                  "Is security awareness training provided to personnel?",
                  "Training records and materials"),
        AuditItem("AUD-ISO-005", "A.7.1",
                  "Is a physical security perimeter implemented?",
                  "Physical security controls evidence"),
        AuditItem("AUD-ISO-006", "A.7.2",
                  "Are physical entry controls in place?",
                  "Access control system logs"),
        AuditItem("AUD-ISO-007", "A.8.1",
                  "Are user endpoint devices properly secured?",
                  "Endpoint security configuration"),
        AuditItem("AUD-ISO-008", "A.8.2",
                  "Are privileged access rights controlled?",
                  "Privileged access management records"),
        AuditItem("AUD-ISO-009", "A.8.3",
                  "Is information access restricted on need-to-know basis?",
                  "Access control lists and reviews"),
        AuditItem("AUD-ISO-010", "A.8.5",
                  "Is secure authentication implemented?",
                  "Authentication mechanisms documentation"),
        AuditItem("AUD-ISO-011", "A.5.3",
                  "Is segregation of duties implemented?",
                  "Segregation of duties matrix"),
        AuditItem("AUD-ISO-012", "A.5.7",
                  "Is threat intelligence collected and analyzed?",
                  "Threat intelligence reports"),
    ]


def get_pci_audit_checklist() -> List[AuditItem]:
    return [
        AuditItem("AUD-PCI-001", "1.1",
                  "Is a firewall configuration standard documented and implemented?",
                  "Firewall configuration standards"),
        AuditItem("AUD-PCI-002", "1.2",
                  "Is network segmentation implemented for cardholder data?",
                  "Network diagram and segmentation evidence"),
        AuditItem("AUD-PCI-003", "2.1",
                  "Are vendor default passwords changed?",
                  "Change documentation"),
        AuditItem("AUD-PCI-004", "3.2",
                  "Is stored cardholder data encrypted?",
                  "Encryption implementation evidence"),
        AuditItem("AUD-PCI-005", "4.1",
                  "Is cardholder data encrypted during transmission?",
                  "TLS/SSL configuration evidence"),
        AuditItem("AUD-PCI-006", "5.1",
                  "Is anti-malware software deployed on all systems?",
                  "Anti-malware deployment records"),
        AuditItem("AUD-PCI-007", "6.2",
                  "Are vulnerability scans performed regularly?",
                  "Vulnerability scan reports"),
        AuditItem("AUD-PCI-008", "7.1",
                  "Is access to cardholder data restricted by need-to-know?",
                  "Access control documentation"),
        AuditItem("AUD-PCI-009", "8.2",
                  "Is multi-factor authentication implemented for remote access?",
                  "MFA configuration evidence"),
        AuditItem("AUD-PCI-010", "10.1",
                  "Are audit logs implemented to track access to cardholder data?",
                  "Audit log configuration and samples"),
        AuditItem("AUD-PCI-011", "11.1",
                  "Are internal and external vulnerability scans performed?",
                  "Scan reports and remediation evidence"),
        AuditItem("AUD-PCI-012", "12.1",
                  "Is a comprehensive information security policy maintained?",
                  "Information security policy document"),
    ]
