from typing import Dict
from datetime import datetime
from src.policies.templates import PolicyTemplate


def generate_policy(template: PolicyTemplate, org_name: str, date: str = "") -> str:
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    lines = []
    lines.append(f"# {template.name}")
    lines.append("")
    lines.append(f"**Organization:** {org_name}")
    lines.append(f"**Date:** {date}")
    lines.append(f"**Policy ID:** {template.id}")
    lines.append(f"**Category:** {template.category}")
    lines.append("")
    lines.append("---")
    lines.append("")
    for section in template.sections:
        lines.append(f"## {section}")
        lines.append("")
        lines.append(f"[Content for {section} to be completed by the organization.]")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*This policy was auto-generated on {date}. Review and customize before adoption.*")
    return "\n".join(lines)


def generate_policy_document(template: PolicyTemplate, fields: Dict[str, str]) -> str:
    lines = []
    lines.append(f"# {template.name}")
    lines.append("")
    lines.append(f"**Policy ID:** {template.id}")
    lines.append("")
    for k, v in fields.items():
        lines.append(f"**{k}:** {v}")
    lines.append("")
    lines.append("---")
    lines.append("")
    for section in template.sections:
        key = section.lower().replace(" ", "_")
        content = fields.get(key, f"[Content for {section}]")
        lines.append(f"## {section}")
        lines.append("")
        lines.append(content)
        lines.append("")
    return "\n".join(lines)


def export_to_markdown(policy_text: str) -> str:
    return policy_text


def export_to_html(policy_text: str) -> str:
    lines = []
    lines.append("<!DOCTYPE html>")
    lines.append("<html><head><meta charset='UTF-8'>")
    lines.append("<title>Policy Document</title>")
    lines.append("<style>body{font-family:Arial,sans-serif;margin:40px;line-height:1.6}")
    lines.append("h1{color:#1a237e}h2{color:#283593;border-bottom:1px solid #ccc}")
    lines.append("strong{color:#333}</style></head><body>")
    in_list = False
    for line in policy_text.split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("**") and line.endswith("**"):
            lines.append(f"<p>{line}</p>")
        elif line.startswith("- "):
            if not in_list:
                lines.append("<ul>")
                in_list = True
            lines.append(f"<li>{line[2:]}</li>")
        elif line.strip() == "":
            if in_list:
                lines.append("</ul>")
                in_list = False
        else:
            lines.append(f"<p>{line}</p>")
    if in_list:
        lines.append("</ul>")
    lines.append("</body></html>")
    return "\n".join(lines)
