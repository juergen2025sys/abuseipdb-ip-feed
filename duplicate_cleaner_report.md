# Duplicate Cleaner – Report
**Aktualisiert:** 2026-03-14 19:57 UTC

---
## Dateigrößen

| Datei | IPs |
|---|---|
| ✅ `combined_threat_blacklist_ipv4.txt` | 3,461,396 |
| ✅ `tor_exit_nodes.txt` | 0 |
| ✅ `cve_exploit_ips.txt` | 0 |
| ✅ `honeypot_ips.txt` | 6 |
| ✅ `honeydb_ips.txt` | 0 |
| ✅ `vpn_proxy_ranges.txt` | 55,443 |
| ✅ `bot_detector_blacklist_ipv4.txt` | 15,490 |

---
## Überschneidungen mit combined_threat_blacklist

| Sub-Liste | Gemeinsame IPs | Anteil | Aktion |
|---|---|---|---|
| `tor_exit_nodes.txt` | 7,768 | 776800.0% | 🗑️ 7768 entfernt |
| `cve_exploit_ips.txt` | 227,427 | 22742700.0% | 🗑️ 227427 entfernt |
| `honeypot_ips.txt` | 14,153 | 235883.3% | 🗑️ 14153 entfernt |
| `honeydb_ips.txt` | 11,200 | 1120000.0% | 🗑️ 11200 entfernt |
| `vpn_proxy_ranges.txt` | 2,335 | 4.2% | 🗑️ 2335 entfernt |
| `bot_detector_blacklist_ipv4.txt` | 30 | 0.2% | 🗑️ 30 entfernt |

---
## Sub-Listen Überschneidungen (nur Info)

| Paar | Gemeinsame IPs |
|---|---|
| `cve∩honeypot` | 9,514 |
| `cve∩honeydb` | 6,073 |
| `honeypot∩honeydb` | 2,898 |
| `tor∩cve` | 726 |
| `tor∩honeydb` | 43 |
| `tor∩honeypot` | 18 |
| `cve∩botdet` | 2 |
| `honeydb∩vpn` | 1 |
| `honeydb∩botdet` | 1 |

*Sub-Listen-Duplikate werden nicht entfernt – combined dedupliziert automatisch.*

---
## Zusammenfassung

| Metrik | Wert |
|---|---|
| Duplikate entfernt (alle Sub-Listen) | **262,913** |
| Combined Blacklist (unverändert) | **3,461,396** |

---
*Generiert: 2026-03-14 19:57 UTC*