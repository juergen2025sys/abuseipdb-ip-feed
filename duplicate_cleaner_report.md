# Duplicate Cleaner – Report
**Aktualisiert:** 2026-03-10 05:33 UTC

---
## Dateigrößen

| Datei | IPs |
|---|---|
| ✅ `combined_threat_blacklist_ipv4.txt` | 2,930,225 |
| ✅ `tor_exit_nodes.txt` | 7,924 |
| ✅ `cve_exploit_ips.txt` | 221,322 |
| ✅ `vpn_proxy_ranges.txt` | 57,802 |
| ✅ `bot_detector_blacklist_ipv4.txt` | 15,450 |

---
## Überschneidungen mit combined_threat_blacklist

| Sub-Liste | Gemeinsame IPs | Anteil | Aktion |
|---|---|---|---|
| `tor_exit_nodes.txt` | 7,924 | 100.0% | 🔒 behalten (HQ-Feed) |
| `cve_exploit_ips.txt` | 221,196 | 99.9% | 🔒 behalten (HQ-Feed) |
| `vpn_proxy_ranges.txt` | 54,157 | 93.7% | 🗑️ 54157 entfernt |
| `bot_detector_blacklist_ipv4.txt` | 2,504 | 16.2% | 🗑️ 2504 entfernt |

---
## Sub-Listen Überschneidungen (nur Info)

| Paar | Gemeinsame IPs |
|---|---|
| `tor∩cve` | 728 |
| `cve∩botdet` | 439 |
| `tor∩botdet` | 1 |

*Sub-Listen-Duplikate werden nicht entfernt – combined dedupliziert automatisch.*

---
## Zusammenfassung

| Metrik | Wert |
|---|---|
| Duplikate entfernt (vpn + botdet) | **56,661** |
| Tor/CVE behalten (HQ-Markierung) | **229,120** |
| Combined Blacklist (unverändert) | **2,930,225** |

---
*Generiert: 2026-03-10 05:33 UTC*