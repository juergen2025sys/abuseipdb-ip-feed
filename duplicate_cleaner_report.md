# Duplicate Cleaner – Report
**Aktualisiert:** 2026-03-15 07:17 UTC

---
## Dateigrößen

| Datei | IPs |
|---|---|
| ✅ `combined_threat_blacklist_ipv4.txt` | 3,478,252 |
| ✅ `tor_exit_nodes.txt` | 194 |
| ✅ `cve_exploit_ips.txt` | 2,692 |
| ✅ `honeypot_ips.txt` | 2,930 |
| ✅ `honeydb_ips.txt` | 11,211 |
| ✅ `vpn_proxy_ranges.txt` | 55,440 |
| ✅ `bot_detector_blacklist_ipv4.txt` | 16,195 |

---
## Überschneidungen mit combined_threat_blacklist

> LOCAL_FEEDS (tor/cve/honeypot/honeydb/botdet) werden nicht bereinigt –

> combined liest sie direkt ein. Nur `vpn_proxy_ranges.txt` wird bereinigt.

| Sub-Liste | Gemeinsame IPs | Anteil | Aktion |
|---|---|---|---|
| `tor_exit_nodes.txt` | 194 | 100.0% | ⏭️ übersprungen (LOCAL_FEED) |
| `cve_exploit_ips.txt` | 2,692 | 100.0% | ⏭️ übersprungen (LOCAL_FEED) |
| `honeypot_ips.txt` | 2,930 | 100.0% | ⏭️ übersprungen (LOCAL_FEED) |
| `honeydb_ips.txt` | 10,116 | 90.2% | ⏭️ übersprungen (LOCAL_FEED) |
| `vpn_proxy_ranges.txt` | 2 | 0.0% | 🗑️ 2 entfernt |
| `bot_detector_blacklist_ipv4.txt` | 686 | 4.2% | ⏭️ übersprungen (LOCAL_FEED) |

---
## Sub-Listen Überschneidungen (nur Info)

| Paar | Gemeinsame IPs |
|---|---|
| `cve∩honeydb` | 24 |
| `honeypot∩honeydb` | 5 |
| `cve∩honeypot` | 3 |
| `honeydb∩botdet` | 3 |
| `cve∩botdet` | 2 |

*Sub-Listen-Duplikate werden nicht entfernt – combined dedupliziert automatisch.*

---
## Zusammenfassung

| Metrik | Wert |
|---|---|
| Duplikate entfernt (nur vpn_proxy_ranges) | **2** |
| Combined Blacklist (unverändert) | **3,478,252** |

---
*Generiert: 2026-03-15 07:17 UTC*