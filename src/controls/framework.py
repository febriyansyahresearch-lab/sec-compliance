from dataclasses import dataclass, field
from typing import List, Dict, Tuple


@dataclass
class Control:
    id: str
    name: str
    category: str
    description: str
    mapping: Dict[str, str] = field(default_factory=dict)


@dataclass
class ControlFramework:
    name: str
    version: str
    controls: List[Control] = field(default_factory=list)


def map_controls(
    source_framework: ControlFramework, target_framework: ControlFramework
) -> List[Tuple[str, str, str]]:
    mappings = []
    for sc in source_framework.controls:
        for tc in target_framework.controls:
            if sc.id in tc.mapping.get(source_framework.name, ""):
                mappings.append((sc.id, tc.id, sc.name))
            if tc.id in sc.mapping.get(target_framework.name, ""):
                mappings.append((sc.id, tc.id, sc.name))
    return mappings


def get_gap_analysis(
    implemented_controls: List[Control], required_controls: List[Control]
) -> List[Dict]:
    implemented_ids = {c.id for c in implemented_controls}
    gaps = []
    for req in required_controls:
        if req.id not in implemented_ids:
            gaps.append(
                {
                    "control_id": req.id,
                    "control_name": req.name,
                    "category": req.category,
                    "status": "missing",
                }
            )
    return gaps
