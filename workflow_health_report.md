# Workflow Health Checker – Report
**Aktualisiert:** 2026-03-09 16:25 UTC

**Workflows:** 17 | ✅ 9 OK | ⚠️ 1 Warnung | ❌ 7 Fehler

---
## Übersicht

| Workflow | Status | Fehler | Warnungen | Cron |
|---|---|---|---|---|
| `active_filter.yml` | ✅ OK | 0 | 0 | `15 0 * * *` |
| `asn_reputation_scorer.yml` | ❌ FEHLER | 1 | 1 | `0 2 * * *` |
| `cve_to_ip_mapper.yml` | ❌ FEHLER | 1 | 1 | `0 4 * * *` |
| `duplicate_cleaner.yml` | ❌ FEHLER | 1 | 1 | `30 4 * * *` |
| `false_positive_checker.yml` | ❌ FEHLER | 1 | 1 | `0 5 * * 0` |
| `feed_health_monitor.yml` | ✅ OK | 0 | 0 | `0 1 * * *` |
| `firewall_format_exporter.yml` | ✅ OK | 0 | 0 | `30 0 * * *` |
| `geo_tagger.yml` | ❌ FEHLER | 1 | 1 | `0 6 * * 0` |
| `netshield_report_generator.yml` | ✅ OK | 0 | 0 | `50 0 * * *` |
| `score_decay_monitor.yml` | ✅ OK | 0 | 0 | `0 7 * * 0` |
| `tor_exit_monitor.yml` | ✅ OK | 0 | 0 | `30 23 * * *` |
| `update-blocklist.yml` | ❌ FEHLER | 1 | 2 | `0 3 * * 1`, `0 3 * * 3` |
| `update_bot_detector.yml` | ✅ OK | 0 | 0 | `45 23 * * *` |
| `update_combined_blacklist.yml` | ✅ OK | 0 | 0 | `0 0 * * *` |
| `update_confidence_blacklist.yml` | ✅ OK | 0 | 0 | `15 0 * * *` |
| `vpn_proxy_detector.yml` | ❌ FEHLER | 1 | 1 | `30 3 * * 1` |
| `workflow_health_checker.yml` | ⚠️ WARNUNG | 0 | 1 | `0 1 * * *` |

---
## ❌ Fehler im Detail

### `asn_reputation_scorer.yml`

- 🔴 Zeile 196: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs

### `cve_to_ip_mapper.yml`

- 🔴 Zeile 188: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs

### `duplicate_cleaner.yml`

- 🔴 Zeile 201: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs

### `false_positive_checker.yml`

- 🔴 Zeile 212: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs

### `geo_tagger.yml`

- 🔴 Zeile 188: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs

### `update-blocklist.yml`

- 🔴 Zeile 79: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs

### `vpn_proxy_detector.yml`

- 🔴 Zeile 179: Nacktes `git push` ohne rebase – Konflikt-Risiko bei parallelen Runs


---
## ⚠️ Warnungen im Detail

### `asn_reputation_scorer.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen

### `cve_to_ip_mapper.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen

### `duplicate_cleaner.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen

### `false_positive_checker.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen

### `geo_tagger.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen

### `update-blocklist.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen
- 🟡 Commit-Message ohne UTC-Zeitstempel: `Auto-update all_countries_ipv4.txt - $(date +'%Y-%m-%d')`

### `vpn_proxy_detector.yml`

- 🟡 Kein `timeout-minutes:` – Job könnte bis zu 6h hängen

### `workflow_health_checker.yml`

- 🟡 Commit-Message ohne UTC-Zeitstempel: `([^`


---
*Generiert: 2026-03-09 16:25 UTC | 17 Workflow-Dateien geprüft*