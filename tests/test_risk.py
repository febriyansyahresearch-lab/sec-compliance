import pytest
from src.risk.assessment import Asset, Threat, Risk, assess, calculate_score, risk_level
from src.risk.ra_templates import (
    get_inherent_risk_matrix,
    get_residual_risk_matrix,
    get_banking_asset_types,
    get_common_banking_threats,
)
from src.risk.scoring import (
    calculate_inherent,
    calculate_residual,
    calculate_control_effectiveness,
    format_report,
)


class TestRiskAssessment:
    def test_asset_creation(self):
        asset = Asset(name="Core Banking", value=1000000.0, criticality="Critical")
        assert asset.name == "Core Banking"
        assert asset.value == 1000000.0
        assert asset.criticality == "Critical"

    def test_threat_creation(self):
        threat = Threat(name="Data Breach", likelihood=3, impact=5)
        assert threat.name == "Data Breach"
        assert threat.likelihood == 3
        assert threat.impact == 5

    def test_calculate_score(self):
        inherent, residual = calculate_score(4, 5)
        assert inherent == 20.0
        assert residual == 12.0

    def test_risk_levels(self):
        assert risk_level(25) == "Critical"
        assert risk_level(15) == "High"
        assert risk_level(7) == "Medium"
        assert risk_level(3) == "Low"

    def test_assess_returns_risks(self):
        assets = [Asset(name="DB Server", value=500000.0, criticality="Critical")]
        threats = [Threat(name="Ransomware", likelihood=4, impact=5)]
        results = assess(assets, threats)
        assert len(results) == 1
        assert results[0].asset.name == "DB Server"
        assert results[0].threat.name == "Ransomware"
        assert results[0].inherent_score == 20.0


class TestRATemplates:
    def test_inherent_risk_matrix(self):
        matrix = get_inherent_risk_matrix()
        assert len(matrix) == 5
        assert len(matrix[0]) == 5
        assert matrix[0][0] == 1
        assert matrix[4][4] == 25

    def test_residual_risk_matrix(self):
        matrix = get_residual_risk_matrix()
        assert len(matrix) == 5
        assert matrix[0][0] == 1
        assert matrix[4][4] == 15

    def test_banking_asset_types(self):
        assets = get_banking_asset_types()
        assert len(assets) >= 10
        names = [a["name"] for a in assets]
        assert "Customer Data" in names
        assert "Core Banking System" in names
        assert "ATM Network" in names

    def test_common_banking_threats(self):
        threats = get_common_banking_threats()
        assert len(threats) >= 10
        names = [t["name"] for t in threats]
        assert "Unauthorized Access" in names
        assert "Data Breach" in names
        assert "Ransomware Attack" in names


class TestScoring:
    def test_calculate_inherent(self):
        score = calculate_inherent(5, 4)
        assert score == 20.0

    def test_calculate_residual(self):
        residual = calculate_residual(20.0, 0.6)
        assert residual == 8.0

    def test_control_effectiveness(self):
        controls = [True, True, False, True]
        eff = calculate_control_effectiveness(controls)
        assert eff == 0.75

    def test_control_effectiveness_empty(self):
        assert calculate_control_effectiveness([]) == 0.0

    def test_format_report(self):
        asset = Asset(name="Test", value=100.0, criticality="Low")
        threat = Threat(name="Test Threat", likelihood=2, impact=2)
        risks = [Risk(asset, threat, 4.0, 2.4)]
        report = format_report(risks)
        assert "RISK ASSESSMENT REPORT" in report
        assert "Test" in report
        assert "Test Threat" in report
