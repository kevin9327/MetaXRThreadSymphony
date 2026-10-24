from backend.spatial_loom_engine import SPECIAL_AWARDS_MAPPING, evaluate_spatial_loom_session


def test_five_special_awards_mapped():
    assert len(SPECIAL_AWARDS_MAPPING) == 5
    assert "Best Agentic Interaction ($25,000)" in SPECIAL_AWARDS_MAPPING
    assert "Best First Five Minutes ($25,000)" in SPECIAL_AWARDS_MAPPING


def test_airplane_seat_reach_and_harmonic_pegs():
    res = evaluate_spatial_loom_session("2026-10-25")
    assert res["status"] == "ok"
    assert res["airplane_seat_test_pass"] is True
    assert len(res["pegs"]) == 6
    assert res["harmonic_frequencies_hz"] == [220.0, 275.0, 330.0, 396.0, 440.0, 528.0]
