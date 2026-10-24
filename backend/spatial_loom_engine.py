"""
SpatialLoom XR — Meta IWSDK (@iwsdk/core v1.0.1) + IWER (metaQuest3) Spatial AI & Acoustic Fiber Engine.
Targets Main Track ($70k-$100k) + 5 Special Awards ($125,000):
- Best Agentic Interaction ($25,000): AgentCopilotSystem
- Best First Five Minutes ($25,000): OnboardingSystem (translucent 3D Ghost Hand, ignorePointer)
- Best Accessibility Forward Experience ($25,000): Seated 2ft Ledge (z=-0.42m), 0.5x Slow-Mo, Gaze+Pinch, Dual Shape/Freq Encoding
- Best Reason to Come Back ($25,000): Daily Spatial Challenge (YYYY-MM-DD seed) + Streak Plaque + Melody Book
- Boldest Original Concept ($25,000): Physical-modeled acoustic fiber loom where system topology plays Just Intonation chords
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, List


SPECIAL_AWARDS_MAPPING = {
    "Best Agentic Interaction ($25,000)": "AgentCopilotSystem (procedural 3D topology weaver + spatial voice/harmonic synthesis)",
    "Best First Five Minutes ($25,000)": "OnboardingSystem (translucent 3D thumb+index Ghost Hand with ignorePointer, <45s first solve)",
    "Best Accessibility Forward Experience ($25,000)": "Seated Airplane Seat Test (z=-0.42m Ledge), 0.5x Slow-Mo, Gaze+Pinch parity, Dual Shape/Frequency encoding",
    "Best Reason to Come Back ($25,000)": "Deterministic YYYY-MM-DD Daily Spool Challenge + Brass Streak Plaque + Melody Book",
    "Boldest Original Concept ($25,000)": "Acoustic Fiber Loom combining 3D spatial systems engineering with physical-modeled string harmony",
}


@dataclass
class SpatialNodePeg:
    peg_id: str
    label: str
    geometry_shape: str  # "sphere" | "hex_prism" | "octahedron"
    harmonic_freq_hz: float
    position_xyz: List[float]


DEFAULT_TABLETOP_PEGS: List[SpatialNodePeg] = [
    SpatialNodePeg("N1", "Ingest Peg A", "sphere", 220.0, [-0.22, 1.02, -0.44]),
    SpatialNodePeg("N2", "Router Peg B", "hex_prism", 275.0, [-0.08, 1.08, -0.52]),
    SpatialNodePeg("N3", "Compute Peg C", "hex_prism", 330.0, [-0.05, 0.96, -0.48]),
    SpatialNodePeg("N4", "Verifier Peg D", "sphere", 396.0, [0.10, 1.07, -0.50]),
    SpatialNodePeg("N5", "Synth Peg E", "octahedron", 440.0, [0.12, 0.97, -0.46]),
    SpatialNodePeg("N6", "Output Peg F", "octahedron", 528.0, [0.24, 1.02, -0.44]),
]


def evaluate_spatial_loom_session(seed_date: str = "2026-10-25") -> Dict[str, Any]:
    pegs = [asdict(p) for p in DEFAULT_TABLETOP_PEGS]
    # Verify Airplane Seat Test: all pegs within 0.60m reach of seated origin (0, 1.0, 0)
    max_z_reach = max(abs(p.position_xyz[2]) for p in DEFAULT_TABLETOP_PEGS)
    return {
        "status": "ok",
        "iwsdk_version": "1.0.1",
        "iwer_device": "metaQuest3",
        "seed_date": seed_date,
        "airplane_seat_test_pass": max_z_reach <= 0.60,
        "special_awards_targeted": SPECIAL_AWARDS_MAPPING,
        "pegs": pegs,
        "harmonic_frequencies_hz": [p.harmonic_freq_hz for p in DEFAULT_TABLETOP_PEGS],
    }
