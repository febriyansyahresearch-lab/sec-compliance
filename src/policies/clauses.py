from dataclasses import dataclass
from typing import List


@dataclass
class Clause:
    id: str
    text: str
    category: str


def get_standard_clauses() -> List[Clause]:
    return [
        Clause("CLA-001", "This policy applies to all employees, contractors, consultants, and third parties accessing organizational information assets.", "scope"),
        Clause("CLA-002", "All personnel must acknowledge and comply with this policy as a condition of access to organizational systems.", "scope"),
        Clause("CLA-003", "The purpose of this policy is to protect the confidentiality, integrity, and availability of organizational information assets.", "purpose"),
        Clause("CLA-004", "This policy establishes the minimum security requirements for protecting organizational data and systems.", "purpose"),
        Clause("CLA-005", "Compliance with this policy is mandatory and non-negotiable for all personnel.", "compliance"),
        Clause("CLA-006", "Violations of this policy may result in disciplinary action, including termination of employment and legal prosecution.", "enforcement"),
        Clause("CLA-007", "All security incidents must be reported immediately to the Information Security team.", "enforcement"),
        Clause("CLA-008", "Management is responsible for ensuring that personnel under their supervision understand and comply with this policy.", "enforcement"),
        Clause("CLA-009", "This policy shall be reviewed at least annually or upon significant organizational change.", "review"),
        Clause("CLA-010", "Exceptions to this policy must be formally documented, risk-assessed, and approved by the Chief Information Security Officer.", "review"),
        Clause("CLA-011", "All organizational data must be classified according to its sensitivity and criticality.", "scope"),
        Clause("CLA-012", "Access to information systems must be granted on a need-to-know and least-privilege basis.", "purpose"),
        Clause("CLA-013", "Personnel must not share passwords, tokens, or any authentication credentials with others.", "compliance"),
        Clause("CLA-014", "Organizational assets must be protected against unauthorized access, modification, disclosure, or destruction.", "purpose"),
        Clause("CLA-015", "All systems must be configured in accordance with approved security hardening standards.", "compliance"),
        Clause("CLA-016", "Security awareness training must be completed by all personnel upon hire and annually thereafter.", "compliance"),
        Clause("CLA-017", "Third parties with access to organizational systems must comply with equivalent security requirements.", "scope"),
        Clause("CLA-018", "Data breaches must be reported to relevant regulatory authorities within the required notification timeline.", "compliance"),
        Clause("CLA-019", "Business continuity plans must be tested at least annually to ensure their effectiveness.", "review"),
        Clause("CLA-020", "All changes to production systems must follow the approved change management process.", "compliance"),
        Clause("CLA-021", "Personal devices used for work purposes must meet minimum security requirements as defined by the organization.", "scope"),
        Clause("CLA-022", "Encryption must be used to protect sensitive data at rest and in transit.", "compliance"),
    ]


def get_banking_clauses() -> List[Clause]:
    return [
        Clause("BANK-001", "This policy complies with POJK No. 11/POJK.03/2022 regarding IT Implementation for Commercial Banks.", "compliance"),
        Clause("BANK-002", "IT risk management must follow the framework defined in POJK No. 38/POJK.03/2016 as amended.", "compliance"),
        Clause("BANK-003", "Technology innovation initiatives must comply with POJK No. 12/POJK.03/2021.", "compliance"),
        Clause("BANK-004", "Customer data protection must comply with POJK consumer protection regulations and applicable privacy laws.", "compliance"),
        Clause("BANK-005", "Anti-fraud strategies must be implemented in accordance with POJK No. 18/POJK.03/2020.", "compliance"),
        Clause("BANK-006", "Business continuity and disaster recovery plans must comply with POJK No. 12/POJK.03/2018.", "compliance"),
        Clause("BANK-007", "Outsourcing of banking IT services must comply with POJK outsourcing regulations.", "compliance"),
        Clause("BANK-008", "IT audit must be conducted at least annually in accordance with Indonesian banking regulations.", "compliance"),
        Clause("BANK-009", "Incident reporting to Bank Indonesia and OJK must follow prescribed timelines and procedures.", "compliance"),
        Clause("BANK-010", "This policy is subject to examination by Bank Indonesia and the Financial Services Authority (OJK).", "enforcement"),
    ]
