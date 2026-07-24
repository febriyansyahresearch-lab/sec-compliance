from typing import List, Dict


def get_inherent_risk_matrix() -> List[List[int]]:
    matrix = []
    for i in range(1, 6):
        row = []
        for j in range(1, 6):
            row.append(i * j)
        matrix.append(row)
    return matrix


def get_residual_risk_matrix() -> List[List[int]]:
    inherent = get_inherent_risk_matrix()
    matrix = []
    for row in inherent:
        residual_row = [max(1, int(v * 0.6)) for v in row]
        matrix.append(residual_row)
    return matrix


def get_banking_asset_types() -> List[Dict]:
    return [
        {"name": "Customer Data", "category": "Data", "criticality": "Critical"},
        {"name": "Transaction Systems", "category": "Application", "criticality": "Critical"},
        {"name": "Core Banking System", "category": "Infrastructure", "criticality": "Critical"},
        {"name": "ATM Network", "category": "Infrastructure", "criticality": "High"},
        {"name": "Mobile Banking", "category": "Application", "criticality": "Critical"},
        {"name": "Internet Banking", "category": "Application", "criticality": "Critical"},
        {"name": "Payment Gateway", "category": "Application", "criticality": "Critical"},
        {"name": "SWIFT / Messaging", "category": "Infrastructure", "criticality": "Critical"},
        {"name": "HR Database", "category": "Data", "criticality": "Medium"},
        {"name": "Email System", "category": "Infrastructure", "criticality": "Medium"},
        {"name": "Branch Network", "category": "Infrastructure", "criticality": "High"},
        {"name": "Card Management", "category": "Application", "criticality": "High"},
        {"name": "Anti-Fraud System", "category": "Application", "criticality": "High"},
        {"name": "Data Warehouse", "category": "Data", "criticality": "Medium"},
        {"name": "Regulatory Reporting", "category": "Application", "criticality": "High"},
    ]


def get_common_banking_threats() -> List[Dict]:
    return [
        {"name": "Unauthorized Access", "likelihood": 4, "impact": 5},
        {"name": "Data Breach", "likelihood": 3, "impact": 5},
        {"name": "Ransomware Attack", "likelihood": 3, "impact": 5},
        {"name": "Insider Threat", "likelihood": 3, "impact": 4},
        {"name": "DDoS Attack", "likelihood": 4, "impact": 3},
        {"name": "Phishing / Social Engineering", "likelihood": 5, "impact": 3},
        {"name": "System Outage", "likelihood": 3, "impact": 4},
        {"name": "Data Leakage", "likelihood": 3, "impact": 4},
        {"name": "Physical Security Breach", "likelihood": 2, "impact": 4},
        {"name": "Third Party Vendor Risk", "likelihood": 3, "impact": 3},
        {"name": "Compliance Violation", "likelihood": 2, "impact": 5},
        {"name": "Fraud / Transaction Manipulation", "likelihood": 2, "impact": 5},
    ]
