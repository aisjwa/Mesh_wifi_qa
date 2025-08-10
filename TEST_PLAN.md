# Mesh Wi‑Fi Test Plan (Generic)

## Scope
- Onboarding: add satellite node to gateway
- Backhaul: link quality, latency, recovery after link drop
- Roaming: client moves between nodes (2.4/5/6 GHz)
- Band steering: prefer 5/6 GHz when RSSI adequate
- DFS behavior: channel switch resilience

## KPIs
- Satellite onboarding success ≥ 99%
- Backhaul P95 latency < 15 ms (wireless), < 5 ms (wired)
- Roam handover < 1500 ms with < 3% packet loss window
