from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from src.audit.checklist import AuditItem


@dataclass
class EvidenceItem:
    audit_item_id: str
    file_path: str
    notes: str
    timestamp: str = ""
    verified: bool = False

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class EvidenceCollector:
    def __init__(self):
        self.evidence: List[EvidenceItem] = []

    def add_evidence(self, item: AuditItem, file_path: str, notes: str = "") -> None:
        ev = EvidenceItem(
            audit_item_id=item.id,
            file_path=file_path,
            notes=notes,
        )
        self.evidence.append(ev)

    def generate_evidence_report(self) -> str:
        lines = []
        lines.append("=" * 80)
        lines.append("EVIDENCE COLLECTION REPORT")
        lines.append("=" * 80)
        lines.append("")
        if not self.evidence:
            lines.append("No evidence collected.")
            return "\n".join(lines)
        lines.append(f"{'Audit Item':<20} {'File Path':<40} {'Status':<10}")
        lines.append("-" * 70)
        for ev in self.evidence:
            status = "Verified" if ev.verified else "Pending"
            lines.append(f"{ev.audit_item_id:<20} {ev.file_path:<40} {status:<10}")
        lines.append("")
        lines.append(f"Total Evidence Items: {len(self.evidence)}")
        return "\n".join(lines)

    def check_evidence_completeness(self, checklist: List[AuditItem]) -> float:
        if not checklist:
            return 100.0
        collected_ids = {ev.audit_item_id for ev in self.evidence}
        total = len(checklist)
        covered = sum(1 for item in checklist if item.id in collected_ids)
        return round((covered / total) * 100, 2)
