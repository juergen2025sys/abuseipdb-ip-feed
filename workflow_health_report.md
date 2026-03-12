# Workflow Health Checker – Report
**Aktualisiert:** 2026-03-12 19:17 UTC

**Workflows:** 17 | ✅ 15 OK | ⚠️ 0 Warnung | ❌ 2 Fehler

---
## Übersicht

| Workflow | Status | Fehler | Warnungen | Cron |
|---|---|---|---|---|
| `asn_reputation_scorer.yml` | ✅ OK | 0 | 0 | `0 2 * * *` |
| `auto_feed_discovery.yml` | ❌ FEHLER | 1 | 0 | `30 4 * * 0` |
| `community_ip_report.yml` | ✅ OK | 0 | 0 | – |
| `cve_to_ip_mapper.yml` | ✅ OK | 0 | 0 | `0 4 * * *` |
| `duplicate_cleaner.yml` | ✅ OK | 0 | 0 | `30 4 * * *` |
| `false_positive_checker.yml` | ✅ OK | 0 | 0 | `30 5 * * *`, `30 13 * * *`, `30 21 * * *` |
| `feed_health_monitor.yml` | ✅ OK | 0 | 0 | `0 1 * * *` |
| `geo_tagger.yml` | ✅ OK | 0 | 0 | `30 6 * * 0` |
| `netshield_report_generator.yml` | ✅ OK | 0 | 0 | `50 0 * * *` |
| `score_decay_monitor.yml` | ✅ OK | 0 | 0 | `0 7 * * 0` |
| `tor_exit_monitor.yml` | ✅ OK | 0 | 0 | `30 23 * * *` |
| `update-blocklist.yml` | ✅ OK | 0 | 0 | `30 2 * * 1`, `30 2 * * 3` |
| `update_bot_detector.yml` | ✅ OK | 0 | 0 | `45 23 * * *` |
| `update_combined_blacklist.yml` | ❌ FEHLER | 1 | 0 | `0 */3 * * *` |
| `update_confidence_blacklist.yml` | ✅ OK | 0 | 0 | `15 0 * * *`, `15 3 * * *`, `15 6 * * *`, `15 9 * * *`, `15 12 * * *`, `15 15 * * *`, `15 18 * * *`, `15 21 * * *` |
| `vpn_proxy_detector.yml` | ✅ OK | 0 | 0 | `30 3 * * 1` |
| `workflow_health_checker.yml` | ✅ OK | 0 | 0 | `5 1 * * *` |

---
## ❌ Fehler im Detail

### `auto_feed_discovery.yml`

- 🔴 [AUDIT-BUG-2] seen_db.json wird per json.dump() geschrieben, aber fehlt im `git add`-Befehl. Fällt der GitHub-Cache nach 7 Tagen weg, gehen alle Änderungen (z.B. Community-Reports) dauerhaft verloren. Fix: `git add ... seen_db.json` ergänzen.

### `update_combined_blacklist.yml`

- 🔴 [AUDIT-BUG-2] seen_db.json wird per json.dump() geschrieben, aber fehlt im `git add`-Befehl. Fällt der GitHub-Cache nach 7 Tagen weg, gehen alle Änderungen (z.B. Community-Reports) dauerhaft verloren. Fix: `git add ... seen_db.json` ergänzen.


---
*Generiert: 2026-03-12 19:17 UTC | 17 Workflow-Dateien geprüft*