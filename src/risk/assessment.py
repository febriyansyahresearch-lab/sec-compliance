from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Asset:
    name: str
    value: float
    criticality: str


@dataclass
class Threat:
    name: str
    likelihood: int
    impact: int


@dataclass
class Risk:
    asset: Asset
    threat: Threat
    inherent_score: float
    residual_score: float
    inherent_level: str = ""
    residual_level: str = ""

    def __post_init__(self):
        self.inherent_level = risk_level(self.inherent_score)
        self.residual_level = risk_level(self.residual_score)


def calculate_score(likelihood: int, impact: int) -> Tuple[float, float]:
    inherent = float(likelihood * impact)
    residual = inherent * 0.6
    return (inherent, residual)


def risk_level(score: float) -> str:
    if score >= 20:
        return "Critical"
    elif score >= 10:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"


def assess(assets: List[Asset], threats: List[Threat]) -> List[Risk]:
    results = []
    for asset in assets:
        for threat in threats:
            inherent, residual = calculate_score(threat.likelihood, threat.impact)
            results.append(
                Risk(
                    asset=asset,
                    threat=threat,
                    inherent_score=inherent,
                    residual_score=residual,
                )
            )
    return results
