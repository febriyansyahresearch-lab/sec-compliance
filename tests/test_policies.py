import pytest
from src.policies.templates import PolicyTemplate, get_policy_templates
from src.policies.generator import generate_policy, generate_policy_document, export_to_markdown, export_to_html
from src.policies.clauses import get_standard_clauses, get_banking_clauses, Clause


class TestTemplates:
    def test_policy_template_creation(self):
        pt = PolicyTemplate("POL-001", "Test Policy", "Security", ["Purpose", "Scope"])
        assert pt.id == "POL-001"
        assert pt.name == "Test Policy"
        assert len(pt.sections) == 2

    def test_get_all_templates(self):
        templates = get_policy_templates()
        assert len(templates) == 10
        names = [t.name for t in templates]
        assert "IT Security Policy" in names
        assert "Access Control Policy" in names
        assert "Incident Response Policy" in names

    def test_template_sections_count(self):
        templates = get_policy_templates()
        for t in templates:
            assert len(t.sections) >= 10


class TestGenerator:
    def test_generate_policy(self):
        template = PolicyTemplate("POL-001", "Test Policy", "Security", ["Purpose", "Scope"])
        text = generate_policy(template, "Test Bank")
        assert "# Test Policy" in text
        assert "Test Bank" in text
        assert "## Purpose" in text
        assert "## Scope" in text

    def test_generate_policy_with_date(self):
        template = PolicyTemplate("POL-001", "Test Policy", "Security", ["Purpose"])
        text = generate_policy(template, "Bank", "2024-01-01")
        assert "2024-01-01" in text

    def test_generate_policy_document(self):
        template = PolicyTemplate("POL-001", "Test Policy", "Security", ["Purpose"])
        fields = {"purpose": "This is the purpose section.", "org_name": "Test Bank"}
        text = generate_policy_document(template, fields)
        assert "Test Policy" in text
        assert "POL-001" in text

    def test_export_to_markdown(self):
        text = "# Test\n## Section\nContent"
        result = export_to_markdown(text)
        assert result == text

    def test_export_to_html(self):
        text = "# Test Policy\n## Section\nSome content"
        html = export_to_html(text)
        assert "<h1>Test Policy</h1>" in html
        assert "<h2>Section</h2>" in html
        assert "</html>" in html


class TestClauses:
    def test_standard_clauses_count(self):
        clauses = get_standard_clauses()
        assert len(clauses) >= 20

    def test_standard_clauses_categories(self):
        clauses = get_standard_clauses()
        categories = {c.category for c in clauses}
        for cat in ["scope", "purpose", "compliance", "enforcement", "review"]:
            assert cat in categories

    def test_banking_clauses(self):
        clauses = get_banking_clauses()
        assert len(clauses) >= 10
        texts = [c.text for c in clauses]
        assert any("POJK" in t for t in texts)

    def test_clause_creation(self):
        c = Clause("TEST-01", "Test clause text", "compliance")
        assert c.id == "TEST-01"
        assert c.text == "Test clause text"
        assert c.category == "compliance"
