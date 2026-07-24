from typing import List, Tuple
from src.risk.assessment import Risk, risk_level as rl


def calculate_inherent(impact: int, likelihood: int) -> float:
    return float(impact * likelihood)


def calculate_residual(inherent: float, control_effectiveness: float) -> float:
    return inherent * (1.0 - control_effectiveness)


def calculate_control_effectiveness(controls: List[bool]) -> float:
    if not controls:
        return 0.0
    implemented = sum(1 for c in controls if c)
    return implemented / len(controls)


def risk_level(score: float) -> str:
    return rl(score)


def format_report(risks: List[Risk]) -> str:
    lines = []
    lines.append("=" * 80)
    lines.append("RISK ASSESSMENT REPORT")
    lines.append("=" * 80)
    lines.append("")
    for r in risks:
        lines.append(f"Asset       : {r.asset.name}")
        lines.append(f"Threat      : {r.threat.name}")
        lines.append(f"Inherent    : {r.inherent_score:.1f} ({r.inherent_level})")
        lines.append(f"Residual    : {r.residual_score:.1f} ({r.residual_level})")
        lines.append("-" * 40)
    lines.append("")
    lines.append(f"Total Risks : {len(risks)}")
    return "\n".join(lines)
