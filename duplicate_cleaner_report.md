# Duplicate Cleaner – Report
**Aktualisiert:** 2026-03-12 05:36 UTC

---
## Dateigrößen

| Datei | IPs |
|---|---|
| ✅ `combined_threat_blacklist_ipv4.txt` | 2,868,092 |
| ✅ `tor_exit_nodes.txt` | 7,891 |
| ✅ `cve_exploit_ips.txt` | 224,275 |
| ✅ `vpn_proxy_ranges.txt` | 57,798 |
| ✅ `bot_detector_blacklist_ipv4.txt` | 15,530 |

---
## Überschneidungen mit combined_threat_blacklist

| Sub-Liste | Gemeinsame IPs | Anteil | Aktion |
|---|---|---|---|
| `tor_exit_nodes.txt` | 7,891 | 100.0% | 🔒 behalten (HQ-Feed) |
| `cve_exploit_ips.txt` | 224,273 | 100.0% | 🔒 behalten (HQ-Feed) |
| `vpn_proxy_ranges.txt` | 2 | 0.0% | 🗑️ 2 entfernt |
| `bot_detector_blacklist_ipv4.txt` | 2,424 | 15.6% | 🗑️ 2424 entfernt |

---
## Sub-Listen Überschneidungen (nur Info)

| Paar | Gemeinsame IPs |
|---|---|
| `tor∩cve` | 731 |
| `cve∩botdet` | 468 |
| `tor∩botdet` | 1 |

*Sub-Listen-Duplikate werden nicht entfernt – combined dedupliziert automatisch.*

---
## Zusammenfassung

| Metrik | Wert |
|---|---|
| Duplikate entfernt (vpn + botdet) | **2,426** |
| Tor/CVE behalten (HQ-Markierung) | **232,164** |
| Combined Blacklist (unverändert) | **2,868,092** |

---
*Generiert: 2026-03-12 05:36 UTC*