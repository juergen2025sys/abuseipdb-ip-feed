# Duplicate Cleaner – Report
**Aktualisiert:** 2026-03-13 05:34 UTC

---
## Dateigrößen

| Datei | IPs |
|---|---|
| ✅ `combined_threat_blacklist_ipv4.txt` | 2,859,128 |
| ✅ `tor_exit_nodes.txt` | 7,875 |
| ✅ `cve_exploit_ips.txt` | 225,067 |
| ✅ `vpn_proxy_ranges.txt` | 57,798 |
| ✅ `bot_detector_blacklist_ipv4.txt` | 16,218 |

---
## Überschneidungen mit combined_threat_blacklist

| Sub-Liste | Gemeinsame IPs | Anteil | Aktion |
|---|---|---|---|
| `tor_exit_nodes.txt` | 7,758 | 98.5% | 🔒 behalten (HQ-Feed) |
| `cve_exploit_ips.txt` | 222,199 | 98.7% | 🔒 behalten (HQ-Feed) |
| `vpn_proxy_ranges.txt` | 0 | 0.0% | ✅ bereits sauber |
| `bot_detector_blacklist_ipv4.txt` | 1,736 | 10.7% | 🗑️ 1736 entfernt |

---
## Sub-Listen Überschneidungen (nur Info)

| Paar | Gemeinsame IPs |
|---|---|
| `tor∩cve` | 728 |
| `cve∩botdet` | 482 |
| `tor∩botdet` | 1 |

*Sub-Listen-Duplikate werden nicht entfernt – combined dedupliziert automatisch.*

---
## Zusammenfassung

| Metrik | Wert |
|---|---|
| Duplikate entfernt (vpn + botdet) | **1,736** |
| Tor/CVE behalten (HQ-Markierung) | **229,957** |
| Combined Blacklist (unverändert) | **2,859,128** |

---
*Generiert: 2026-03-13 05:34 UTC*