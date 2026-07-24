import pytest
from src.controls.framework import Control, ControlFramework, map_controls, get_gap_analysis
from src.controls.nist_csf import get_nist_csf_framework
from src.controls.iso27001 import get_iso27001_framework
from src.controls.pci_dss import get_pci_dss_framework
from src.controls.cobit import get_cobit_framework
from src.controls.bi_regs import get_bi_regulations, get_bi_controls


class TestFramework:
    def test_control_creation(self):
        c = Control("TEST-01", "Test Control", "Test", "A test control")
        assert c.id == "TEST-01"
        assert c.name == "Test Control"

    def test_framework_creation(self):
        controls = [Control("C1", "Control 1", "Cat", "Desc")]
        fw = ControlFramework("Test", "1.0", controls)
        assert fw.name == "Test"
        assert len(fw.controls) == 1

    def test_map_controls(self):
        c1 = Control("C1", "Control 1", "Cat", "Desc", mapping={"FW2": "C2"})
        c2 = Control("C2", "Control 2", "Cat", "Desc", mapping={"FW1": "C1"})
        fw1 = ControlFramework("FW1", "1", [c1])
        fw2 = ControlFramework("FW2", "1", [c2])
        mappings = map_controls(fw1, fw2)
        assert isinstance(mappings, list)

    def test_gap_analysis(self):
        implemented = [Control("C1", "Impl", "Cat", "Desc")]
        required = [
            Control("C1", "Req1", "Cat", "Desc"),
            Control("C2", "Req2", "Cat", "Desc"),
        ]
        gaps = get_gap_analysis(implemented, required)
        assert len(gaps) == 1
        assert gaps[0]["control_id"] == "C2"


class TestNIST:
    def test_nist_framework(self):
        fw = get_nist_csf_framework()
        assert fw.name == "NIST Cybersecurity Framework"
        assert fw.version == "2.0"
        assert len(fw.controls) >= 20

    def test_nist_has_all_functions(self):
        fw = get_nist_csf_framework()
        categories = {c.category for c in fw.controls}
        for cat in ["GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER"]:
            assert cat in categories


class TestISO27001:
    def test_iso_framework(self):
        fw = get_iso27001_framework()
        assert fw.name == "ISO/IEC 27001"
        assert fw.version == "2022"
        assert len(fw.controls) >= 20

    def test_iso_has_all_domains(self):
        fw = get_iso27001_framework()
        categories = {c.category for c in fw.controls}
        for cat in ["Organizational", "People", "Physical", "Technological"]:
            assert cat in categories


class TestPCIDSS:
    def test_pci_framework(self):
        fw = get_pci_dss_framework()
        assert fw.name == "PCI DSS"
        assert fw.version == "v4.0"
        assert len(fw.controls) >= 15


class TestCOBIT:
    def test_cobit_framework(self):
        fw = get_cobit_framework()
        assert fw.name == "COBIT"
        assert fw.version == "2019"
        assert len(fw.controls) >= 15
        categories = {c.category for c in fw.controls}
        assert "Governance" in categories
        assert "Management" in categories


class TestBIRegs:
    def test_bi_regulations(self):
        regs = get_bi_regulations()
        assert len(regs) >= 5
        ids = [r["id"] for r in regs]
        assert "POJK.11.2022" in ids

    def test_bi_controls(self):
        fw = get_bi_controls()
        assert fw.name == "BI/POJK Regulations"
        assert len(fw.controls) >= 10
