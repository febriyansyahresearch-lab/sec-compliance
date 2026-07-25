# Sec-Compliance — GRC Toolkit for Banking

[![CI](https://github.com/febriyansyahresearch-lab/sec-compliance/actions/workflows/test.yml/badge.svg)](https://github.com/febriyansyahresearch-lab/sec-compliance/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-48%20passing-brightgreen)](tests/)

**Febriyansyah** — IT Cybersecurity & Infrastructure Leader (15+ yrs, Banking) | MTI Candidate

## Problem Statement

Banking institutions face complex regulatory requirements across multiple frameworks (ISO 27001, NIST CSF, PCI DSS, COBIT, BI/POJK). Maintaining compliance, assessing risk, and generating audit evidence requires significant manual effort. This toolkit automates GRC workflows for banking environments.

## Methodology

### Architecture

1. **Risk Assessment** — Asset-based risk analysis with 5x5 inherent/residual scoring matrices tailored for banking assets and threats.
2. **Control Frameworks** — Programmatic representations of NIST CSF 2.0, ISO 27001:2022, PCI DSS v4.0, COBIT 2019, and Indonesian BI/POJK regulations with cross-framework mapping.
3. **Policy Generation** — Dynamic policy document generation from structured templates with standard clauses and regulatory references.
4. **Audit Automation** — Framework-specific audit checklist generation and evidence collection tracking.

### Frameworks Covered

| Framework | Version | Controls |
|---|---|---|
| NIST Cybersecurity Framework | 2.0 | 25+ controls (GV, ID, PR, DE, RS, RC) |
| ISO/IEC 27001 | 2022 | 20+ controls (A.5–A.8) |
| PCI DSS | v4.0 | 15+ controls (6 goals) |
| COBIT | 2019 | 15+ controls (EDM, POB, APO, BAI, DSS, MEA) |
| BI/POJK | Various | 10+ banking IT regulations |

## Key Concepts

| Concept | Description |
|---|---|
| Inherent Risk | Risk before controls (Impact × Likelihood) |
| Residual Risk | Risk after controls (Inherent × Control Effectiveness) |
| Control Mapping | Cross-reference controls across frameworks |
| Policy Templates | Structured document templates with standard clauses |
| Audit Trail | Evidence collection and completeness tracking |

## Quick Demo

```bash
pip install -r requirements.txt
python -m pytest tests/ -q
```

Example output:

```text
48 passed
```

Typical workflow:

| Step | Output |
|---|---|
| Define banking assets and threats | Inherent risk score and risk level |
| Map controls across frameworks | NIST, ISO 27001, PCI DSS, COBIT, BI/POJK coverage |
| Generate audit checklist | Evidence tracking and completeness report |

## References

- NIST CSF 2.0 — https://www.nist.gov/cyberframework
- ISO/IEC 27001:2022 — Information Security Management
- PCI DSS v4.0 — https://www.pcisecuritystandards.org/
- COBIT 2019 — ISACA Framework
- POJK No. 11/POJK.03/2022 — IT Risk Management for Indonesian Banks
