import pytest
from src.audit.checklist import AuditItem, generate_checklist, get_nist_audit_checklist, get_iso27001_audit_checklist, get_pci_audit_checklist
from src.audit.evidence import EvidenceItem, EvidenceCollector
from src.controls.framework import ControlFramework, Control


class TestChecklist:
    def test_audit_item_creation(self):
        item = AuditItem("AUD-001", "CTRL-01", "Is control implemented?", "Evidence docs")
        assert item.id == "AUD-001"
        assert item.control_ref == "CTRL-01"
        assert item.status == "pending"

    def test_generate_checklist(self):
        controls = [Control("C1", "Test Control", "Cat", "Desc")]
        fw = ControlFramework("Test", "1.0", controls)
        items = generate_checklist(fw)
        assert len(items) == 1
        assert items[0].control_ref == "C1"

    def test_nist_audit_checklist(self):
        items = get_nist_audit_checklist()
        assert len(items) >= 10
        ids = [i.id for i in items]
        assert "AUD-NST-001" in ids

    def test_iso27001_audit_checklist(self):
        items = get_iso27001_audit_checklist()
        assert len(items) >= 10
        ids = [i.id for i in items]
        assert "AUD-ISO-001" in ids

    def test_pci_audit_checklist(self):
        items = get_pci_audit_checklist()
        assert len(items) >= 10
        ids = [i.id for i in items]
        assert "AUD-PCI-001" in ids


class TestEvidence:
    def test_evidence_item_creation(self):
        ev = EvidenceItem("AUD-001", "evidence/report.pdf", "Audit evidence collected")
        assert ev.audit_item_id == "AUD-001"
        assert ev.file_path == "evidence/report.pdf"
        assert ev.timestamp != ""

    def test_evidence_collector_add(self):
        collector = EvidenceCollector()
        item = AuditItem("AUD-001", "CTRL-01", "Question?", "Evidence")
        collector.add_evidence(item, "path/to/file.pdf", "Notes here")
        assert len(collector.evidence) == 1
        assert collector.evidence[0].audit_item_id == "AUD-001"

    def test_evidence_report(self):
        collector = EvidenceCollector()
        report = collector.generate_evidence_report()
        assert "EVIDENCE COLLECTION REPORT" in report

    def test_evidence_completeness_full(self):
        collector = EvidenceCollector()
        items = [
            AuditItem("AUD-001", "C1", "Q1?", "E1"),
            AuditItem("AUD-002", "C2", "Q2?", "E2"),
        ]
        collector.add_evidence(items[0], "f1.pdf")
        collector.add_evidence(items[1], "f2.pdf")
        pct = collector.check_evidence_completeness(items)
        assert pct == 100.0

    def test_evidence_completeness_partial(self):
        collector = EvidenceCollector()
        items = [
            AuditItem("AUD-001", "C1", "Q1?", "E1"),
            AuditItem("AUD-002", "C2", "Q2?", "E2"),
            AuditItem("AUD-003", "C3", "Q3?", "E3"),
        ]
        collector.add_evidence(items[0], "f1.pdf")
        pct = collector.check_evidence_completeness(items)
        assert pct == pytest.approx(33.33, rel=0.1)
