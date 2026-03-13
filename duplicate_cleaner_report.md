# Duplicate Cleaner – Report
**Aktualisiert:** 2026-03-13 16:17 UTC

---
## Dateigrößen

| Datei | IPs |
|---|---|
| ✅ `combined_threat_blacklist_ipv4.txt` | 3,244,530 |
| ✅ `tor_exit_nodes.txt` | 7,875 |
| ✅ `cve_exploit_ips.txt` | 225,067 |
| ✅ `vpn_proxy_ranges.txt` | 57,781 |
| ✅ `bot_detector_blacklist_ipv4.txt` | 15,471 |

---
## Überschneidungen mit combined_threat_blacklist

| Sub-Liste | Gemeinsame IPs | Anteil | Aktion |
|---|---|---|---|
| `tor_exit_nodes.txt` | 7,875 | 100.0% | 🔒 behalten (HQ-Feed) |
| `cve_exploit_ips.txt` | 225,067 | 100.0% | 🔒 behalten (HQ-Feed) |
| `vpn_proxy_ranges.txt` | 17 | 0.0% | 🗑️ 17 entfernt |
| `bot_detector_blacklist_ipv4.txt` | 747 | 4.8% | 🗑️ 747 entfernt |

---
## Sub-Listen Überschneidungen (nur Info)

| Paar | Gemeinsame IPs |
|---|---|
| `tor∩cve` | 728 |
| `cve∩botdet` | 9 |

*Sub-Listen-Duplikate werden nicht entfernt – combined dedupliziert automatisch.*

---
## Zusammenfassung

| Metrik | Wert |
|---|---|
| Duplikate entfernt (vpn + botdet) | **764** |
| Tor/CVE behalten (HQ-Markierung) | **232,942** |
| Combined Blacklist (unverändert) | **3,244,530** |

---
*Generiert: 2026-03-13 16:17 UTC*