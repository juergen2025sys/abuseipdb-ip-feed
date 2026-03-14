
# 🛡️ NETSHIELD

**Automatisiertes IP-Threat-Intelligence-System mit dynamischer Blacklist-Verwaltung**

NETSHIELD aggregiert, bewertet und bereinigt täglich IP-Bedrohungsdaten aus über 130 öffentlichen Feeds. Das System unterscheidet zwischen aktiven Bedrohungen und veralteten statischen Listen – und stellt daraus qualitativ hochwertige Blocklisten für Firewalls (OPNsense, pfSense, iptables) bereit.

---

## 📋 Inhalt

- [Architektur](#architektur)
- [Blocklisten](#blocklisten)
- [Wie funktioniert die Bewertung](#wie-funktioniert-die-bewertung)
- [Workflows](#workflows)
- [Für OPNsense / Firewall](#für-opnsense--firewall)
- [Community Reports](#community-reports)
- [Dateistruktur](#dateistruktur)

---

## Architektur

<svg width="100%" viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <!-- HQ-Feeds -->
  <rect x="40" y="30" width="180" height="52" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="14" font-weight="500" fill="#085041" x="130" y="52" text-anchor="middle" dominant-baseline="central">HQ-Feeds</text>
  <text font-family="sans-serif" font-size="12" fill="#0F6E56" x="130" y="70" text-anchor="middle" dominant-baseline="central">Feodo · Talos · AbuseIPDB · Spamhaus</text>

  <!-- Non-HQ-Feeds -->
  <rect x="460" y="30" width="180" height="52" rx="8" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="14" font-weight="500" fill="#2C2C2A" x="550" y="52" text-anchor="middle" dominant-baseline="central">Non-HQ-Feeds</text>
  <text font-family="sans-serif" font-size="12" fill="#5F5E5A" x="550" y="70" text-anchor="middle" dominant-baseline="central">romainmarcoux · ipsum · littlejake</text>

  <!-- Arrows from feeds into engine -->
  <line x1="200" y1="82" x2="290" y2="148" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
  <line x1="460" y1="82" x2="390" y2="148" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>

  <!-- Arrow labels -->
  <text font-family="sans-serif" font-size="12" fill="#444441" x="226" y="108" text-anchor="middle">setzt last_seen</text>
  <text font-family="sans-serif" font-size="12" fill="#444441" x="444" y="108" text-anchor="middle">erhöht feed_count</text>

  <!-- Main engine box -->
  <rect x="210" y="150" width="260" height="80" rx="10" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="14" font-weight="500" fill="#26215C" x="340" y="180" text-anchor="middle" dominant-baseline="central">Update Combined Blacklist</text>
  <text font-family="sans-serif" font-size="12" fill="#534AB7" x="340" y="200" text-anchor="middle" dominant-baseline="central">8× täglich · seen_db · IP-Lebenszeit 180 Tage</text>

  <!-- Arrow down center -->
  <line x1="340" y1="230" x2="340" y2="280" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>

  <!-- Splitter lines -->
  <line x1="150" y1="280" x2="150" y2="305" stroke="#B4B2A9" stroke-width="0.5" fill="none"/>
  <line x1="530" y1="280" x2="530" y2="305" stroke="#B4B2A9" stroke-width="0.5" fill="none"/>
  <line x1="150" y1="305" x2="530" y2="305" stroke="#B4B2A9" stroke-width="0.5" fill="none"/>
  <line x1="150" y1="305" x2="150" y2="340" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
  <line x1="340" y1="305" x2="340" y2="340" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
  <line x1="530" y1="305" x2="530" y2="340" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>

  <!-- active_blacklist -->
  <rect x="50" y="340" width="200" height="70" rx="8" fill="#FAECE7" stroke="#993C1D" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="14" font-weight="500" fill="#4A1B0C" x="150" y="362" text-anchor="middle" dominant-baseline="central">active_blacklist</text>
  <text font-family="sans-serif" font-size="12" fill="#993C1D" x="150" y="379" text-anchor="middle" dominant-baseline="central">30T + Score ≥ 50</text>
  <text font-family="sans-serif" font-size="12" fill="#993C1D" x="150" y="395" text-anchor="middle" dominant-baseline="central">→ OPNsense / Firewall</text>

  <!-- combined_blacklist -->
  <rect x="240" y="340" width="200" height="70" rx="8" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="14" font-weight="500" fill="#2C2C2A" x="340" y="362" text-anchor="middle" dominant-baseline="central">combined_blacklist</text>
  <text font-family="sans-serif" font-size="12" fill="#5F5E5A" x="340" y="379" text-anchor="middle" dominant-baseline="central">180 Tage · alle IPs</text>
  <text font-family="sans-serif" font-size="12" fill="#5F5E5A" x="340" y="395" text-anchor="middle" dominant-baseline="central">→ Audit / SIEM</text>

  <!-- confidence40 -->
  <rect x="430" y="340" width="200" height="70" rx="8" fill="#FAEEDA" stroke="#854F0B" stroke-width="0.5"/>
  <text font-family="sans-serif" font-size="14" font-weight="500" fill="#412402" x="530" y="362" text-anchor="middle" dominant-baseline="central">confidence40</text>
  <text font-family="sans-serif" font-size="12" fill="#854F0B" x="530" y="379" text-anchor="middle" dominant-baseline="central">Score ≥ 50 · watchlist</text>
  <text font-family="sans-serif" font-size="12" fill="#854F0B" x="530" y="395" text-anchor="middle" dominant-baseline="central">→ Analyse</text>

  <!-- Bottom note -->
  <text font-family="sans-serif" font-size="12" fill="#888780" x="340" y="450" text-anchor="middle">IP ohne HQ-Bestätigung → altert aus nach 180 Tagen · kehrt zurück wenn wieder aktiv</text>
</svg>

**Kernprinzip:** Nur HQ-Feeds (Feodo, Talos, AbuseIPDB, Spamhaus etc.) bestimmen die Lebenszeit einer IP. Statische Mega-Listen erhöhen den Confidence-Score, können eine IP aber nicht am Leben halten. Das System bereinigt automatisch was die Feeds selbst nicht können.

---

## Blocklisten

| Datei | Beschreibung | Einträge | Update | Empfohlen für |
|---|---|---:|---|---|
| [`active_blacklist_ipv4.txt`](active_blacklist_ipv4.txt) | Aktive Bedrohungen (30T + Conf≥50) | **2,503,595** | 8x täglich | **OPNsense / Firewall** |
| [`combined_threat_blacklist_ipv4.txt`](combined_threat_blacklist_ipv4.txt) | Alle IPs (180 Tage) | **3,256,706** | 8x täglich | Audit / SIEM |
| [`blacklist_confidence40_ipv4.txt`](blacklist_confidence40_ipv4.txt) | Hohe Konfidenz (Score ≥50) | **2,331,037** | 8x täglich | Strenge Umgebungen |
| [`watchlist_confidence20to39_ipv4.txt`](watchlist_confidence20to39_ipv4.txt) | Watchlist (Score 25–49) | **528,091** | 8x täglich | Monitoring |
| [`tor_exit_nodes.txt`](tor_exit_nodes.txt) | Tor Exit Nodes | **7,768** | täglich 23:30 | Anonymisierung blockieren |
| [`cve_exploit_ips.txt`](cve_exploit_ips.txt) | CVE-Exploit & C2-Server | **227,111** | täglich 04:00 | IDS/IPS |
| [`vpn_proxy_ranges.txt`](vpn_proxy_ranges.txt) | VPN/Proxy/Datacenter | **57,781** | wöchentlich Mo | Proxy-Erkennung |
| [`honeypot_ips.txt`](honeypot_ips.txt) | Honeypot-bestätigte IPs | **14,159** | täglich 23:00 | Ergänzung |
| [`bot_detector_blacklist_ipv4.txt`](bot_detector_blacklist_ipv4.txt) | Bot-Detector | **17,954** | täglich 23:45 | Web-Schutz |
| [`asn_blocklist_firewall.txt`](asn_blocklist_firewall.txt) | Hochrisiko-ASNs (Score≥50) | **19** | täglich 02:00 | ASN-Blocking |

### Geo-Listen

| Verzeichnis | Beschreibung |
|---|---|
| [`continents/`](continents/) | IPv4-Ranges pro Kontinent (africa, asia, europe, north_america, oceania, south_america) |
| [`countries/`](countries/) | IPv4-Ranges pro Land, organisiert nach Kontinent |
| [`all_countries_ipv4.txt`](all_countries_ipv4.txt) | Alle Länder zusammengeführt |

---

## Für OPNsense / Firewall

**Alias URL (aktive Blockliste):**
```
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt
```

**Tor Exit Nodes:**
```
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt
```

**Hohe Konfidenz:**
```
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt
```

---

## Wie funktioniert die Bewertung

Jede IP erhält einen **Confidence-Score von 0–100** aus vier Dimensionen:

```
Score = A (Quellen-Qualität) + B (Aktualität) + C (Persistenz) + D (Bekannt seit)
```

| Dimension | Max | Beschreibung |
|---|---|---|
| **A – Quellen-Qualität** | 40 | HQ-Feed = 40 Pkt, mehrere Feeds = 20–35 Pkt |
| **B – Aktualität** | 30 | Letzte HQ-Bestätigung: heute = 30, vor 7T = 20, vor 30T = 6 |
| **C – Persistenz** | 20 | Über mehrere Tage bestätigt: 14+ Tage = 20 Pkt |
| **D – Bekannt seit** | 10 | Länger im System = stabiler Score |

**Schwellwerte:**
- Score ≥ 50 → `active_blacklist` + `blacklist_confidence40`
- Score 25–49 → `watchlist`
- Score < 25 → nur in `combined` (Audit)

### HQ-Feeds (bestimmen Lebenszeit)

Feodo C2, Talos Intelligence, AbuseIPDB (API + Score100), Spamhaus DROP/EDROP, Emerging Threats, FireHOL Level 1/2/3, blocklist.de, CINS Score, C2-Tracker, Cobalt Strike Tracker, ThreatFox IOC, URLhaus, Binary Defense, Turris Greylist, GreenSnow, ThreatView High Confidence, DShield u.v.m.

---

## Workflows

| Workflow | Zeitplan | Aufgabe |
|---|---|---|
| **Update Combined Blacklist** | 8x täglich (alle 3h) | Haupt-Engine: Feeds laden, seen_db aktualisieren, Stufe 1+2 schreiben |
| **Confidence Blacklist** | 8x täglich (15min nach Combined) | confidence40 + watchlist aus seen_db berechnen |
| **False Positive Checker** | 3x täglich (05:30/13:30/21:30) | Whitelist-CIDRs prüfen, FP aus combined entfernen |
| **Tor Exit Node Monitor** | täglich 23:30 | 6 Tor-Quellen aggregieren → tor_exit_nodes.txt |
| **Honeypot Monitor** | täglich 23:00 | Honeypot-Feeds aggregieren → honeypot_ips.txt |
| **Bot-Detector Blacklist** | täglich 23:45 | bot_detector_blacklist_ipv4.txt aktualisieren |
| **CVE-to-IP Mapper** | täglich 04:00 | C2/Exploit-IPs → cve_exploit_ips.txt |
| **Duplicate Cleaner** | täglich 04:30 | Duplikate in Sub-Listen bereinigen |
| **VPN & Proxy Detector** | wöchentlich Mo 03:30 | vpn_proxy_ranges.txt aktualisieren |
| **Update All Countries IPv4** | Mo + Mi 02:30 | Länder/Kontinente/all_countries synchron erzeugen |
| **Auto Feed Discovery** | wöchentlich So 04:30 | GitHub nach neuen IP-Feeds durchsuchen + bewerten |
| **Geo-Tagger** | wöchentlich So 06:30 | Blacklist-IPs mit Länder-Geo-Daten anreichern |
| **ASN Reputation Scorer** | täglich 02:00 | ASN-Reputationsscoring → asn_reputation_db.json |
| **Score Decay Monitor** | wöchentlich So 07:00 | Alterungs-Report (read-only, löscht nichts) |
| **Feed Health Monitor** | täglich 01:00 | Alle Feed-URLs auf Erreichbarkeit prüfen |
| **Workflow Health Checker** | täglich 01:05 | YAML-Workflows auf Fehler/Warnungen analysieren |
| **NETSHIELD Report Generator** | alle 30 Minuten | NETSHIELD_REPORT.md + README IP-Zahlen aktualisieren |
| **Community IP Report** | bei Issue-Erstellung | Community-gemeldete IPs verarbeiten und in seen_db eintragen |

---

## Community Reports

Verdächtige IPs können über das **Issue-System** gemeldet werden. Das System:

1. Validiert die IP (nur öffentliche IPv4, keine DNS-Whitelist)
2. Trägt sie mit `hq=False` in seen_db ein (Watchlist)
3. Schließt das Issue automatisch mit Feedback
4. Promoted die IP zur aktiven Blacklist sobald **3 unabhängige Meldungen** vorliegen

**Limit:** 5 Reports pro User pro Tag.

Verwende das Label `community-report` beim Erstellen des Issues.

---

## Dateistruktur

```
NETSHIELD/
├── .github/workflows/          # 17 GitHub Actions Workflows
├── continents/                 # IPv4-Ranges pro Kontinent
├── countries/                  # IPv4-Ranges pro Land
│   ├── africa/
│   ├── asia/
│   ├── europe/
│   ├── north_america/
│   ├── oceania/
│   └── south_america/
├── active_blacklist_ipv4.txt           # → OPNsense
├── combined_threat_blacklist_ipv4.txt  # → Audit
├── blacklist_confidence40_ipv4.txt     # → Hohe Konfidenz
├── watchlist_confidence20to39_ipv4.txt # → Monitoring
├── tor_exit_nodes.txt
├── cve_exploit_ips.txt
├── honeypot_ips.txt
├── vpn_proxy_ranges.txt
├── bot_detector_blacklist_ipv4.txt
├── all_countries_ipv4.txt
├── asn_blocklist_firewall.txt
├── asn_reputation_db.json
├── blacklist_geo_enriched.json
├── auto_discovered_feeds.json
├── seen_db_meta.json
├── NETSHIELD_REPORT.md                 # Automatisch generiert
└── README.md
```

---

## Reports & Monitoring

| Datei | Beschreibung |
|---|---|
| [`NETSHIELD_REPORT.md`](NETSHIELD_REPORT.md) | Übersicht aller Listen + Feed Health (alle 30min) |
| [`feed_health_report.md`](feed_health_report.md) | Status aller Feed-URLs |
| [`workflow_health_report.md`](workflow_health_report.md) | Workflow-Analyse (Fehler/Warnungen) |
| [`geo_tagger_report.md`](geo_tagger_report.md) | Geo-Verteilung der Blacklist-IPs |
| [`asn_reputation_report.md`](asn_reputation_report.md) | ASN-Scoring-Report |
| [`score_decay_report.md`](score_decay_report.md) | Alterungs-Analyse der seen_db |
| [`auto_feed_discovery_report.md`](auto_feed_discovery_report.md) | Neu entdeckte Feeds |

---

*Automatisch aktualisiert durch NETSHIELD · [NETSHIELD_REPORT.md](NETSHIELD_REPORT.md)*
