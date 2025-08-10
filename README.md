

A hands-on template to validate **home mesh Wi‑Fi** (gateway + satellite nodes): onboarding, backhaul health, client roaming, and channel/band steering.

> All device names, MACs, SSIDs are **dummy**. This repo demonstrates process & automation only.

## Highlights
- Topology file (gateway + satellites) with link roles (wired/wireless backhaul)
- Backhaul latency probe (ping hop-by-hop) + KPI summary
- Client roaming smoke (simulated logs → analysis plot)
- Test plan and matrix for mesh features (DFS, band steering, 802.11k/v/r)

## Quick start
```bash
pip install -r requirements.txt
python scripts/backhaul_probe.py --topology docs/topology.json
python scripts/analyze_roam.py
pytest -q
```
