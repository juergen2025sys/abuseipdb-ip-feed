

<div align="center">

# 🛡️ NETSHIELD

**Die IPv4 Blocklist Suite für Firewall, Threat Intelligence und Geo Blocking**

[![IPv4 Threat Feeds](https://img.shields.io/badge/IPv4-Threat%20Feeds-blue?style=for-the-badge)](https://github.com/juergen2025sys/NETSHIELD)
[![GeoIP 249 Länder](https://img.shields.io/badge/GeoIP-249%20L%C3%A4nder-success?style=for-the-badge)](https://github.com/juergen2025sys/NETSHIELD/tree/main/countries)
[![6 Kontinente](https://img.shields.io/badge/Kontinente-6-orange?style=for-the-badge)](https://github.com/juergen2025sys/NETSHIELD/tree/main/continents)
[![Automatische Updates](https://img.shields.io/badge/Updates-Automatisch-brightgreen?style=for-the-badge)](https://github.com/juergen2025sys/NETSHIELD/tree/main/.github/workflows)

[![OPNsense](https://img.shields.io/badge/OPNsense-Ready-7b3fe4?style=flat-square)](#opnsense--pfsense)
[![pfSense](https://img.shields.io/badge/pfSense-Ready-0099cc?style=flat-square)](#opnsense--pfsense)
[![FortiGate](https://img.shields.io/badge/FortiGate-Compatible-e95420?style=flat-square)](#einsatzszenarien)
[![Linux](https://img.shields.io/badge/Linux-Firewall%20Friendly-333333?style=flat-square)](#einsatzszenarien)

Fertige Raw-Listen für OPNsense, pfSense, FortiGate, iptables, nftables und jede Firewall mit URL-Feed-Unterstützung.

</div>

---

## ✨ Was ist NETSHIELD?

NETSHIELD bündelt **automatisch gepflegte IPv4-Blocklisten** für zwei zentrale Einsatzzwecke:

- **Threat Blocking** – gegen bekannte Angreifer, Scanner, Tor-, Proxy- und Exploit-IPs
- **Geo Blocking** – nach Ländern und Kontinenten für Firewall-Policies und Netzwerksegmentierung

Die Nutzung ist bewusst einfach gehalten:

1. Raw-Link kopieren
2. In der Firewall als URL Table / Alias eintragen
3. Automatische Updates laufen über GitHub Actions

---

## 🚀 Quick Start

### Welche Liste für welchen Zweck?

| Einsatz | Feed | Empfehlung |
|---|---|---|
| Allgemeines Threat Blocking | [active_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt) | Beste Default-Liste, frische Bedrohungen | **3,099,113** | Qualitativ beste Liste | [blacklist_confidence40_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) | Nur mehrfach bestätigte IPs, wenig False Positives | **2,331,037** | Maximale Abdeckung | [combined_threat_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt) | Für Analyse, SOC, Feed-Fusion | **3,099,113** | Geo Blocking (alle Länder) | [all_countries_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt) | Alle Länder in einer Datei |
| Geo Blocking nach Kontinent | [continents/](https://github.com/juergen2025sys/NETSHIELD/tree/main/continents) | 6 Kontinent-Dateien einzeln |
| Spezialschutz | [tor_exit_nodes.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt) · [vpn_proxy_ranges.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/vpn_proxy_ranges.txt) · [cve_exploit_ips.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/cve_exploit_ips.txt) | Ergänzende Speziallisten |

> **Empfehlung für Einsteiger:** Starte mit [`active_blacklist_ipv4.txt`](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt) für frische Bedrohungen. Wer weniger IPs, aber höhere Treffsicherheit möchte, wechselt zu [`blacklist_confidence40_ipv4.txt`](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt). Geo Blocking und Speziallisten danach ergänzen.

---

## 📦 Enthaltene Listen

### 🧠 Threat Intelligence

| Datei | Zweck | Update-Intervall |
|---|---|---|
| [combined_threat_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt) | Aggregierte Threat-IPs aus ~80 Quellen (Vollarchiv 365 Tage) | **3,099,113** |
| [active_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt) | Frische Bedrohungen: zuletzt bestätigt ≤ 30 Tage | **3,099,113** |
| [blacklist_confidence40_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) | Qualitätsgefilterter Feed: mehrfach bestätigt, HQ-Quellen, persistent | **2,331,037** |
| [watchlist_confidence20to39_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/watchlist_confidence20to39_ipv4.txt) | Beobachtungsliste: schwächere Signale, noch nicht ausreichend bestätigt | **528,091** |
| [bot_detector_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/bot_detector_blacklist_ipv4.txt) | Bots, Scraper, Scanner, Abuse-Quellen | **15,530** |
| [tor_exit_nodes.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt) | Tor Exit Nodes aus 6 Quellen | **7,891** |
| [cve_exploit_ips.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/cve_exploit_ips.txt) | IPs mit Bezug zu aktiver Exploit-Aktivität (C2, Feodo, ThreatFox) | **224,275** |
| [vpn_proxy_ranges.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/vpn_proxy_ranges.txt) | VPN-, Proxy- und Anonymisierungs-Ranges | **57,798** |
| [abuseipdb_api_blacklist.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/abuseipdb_api_blacklist.txt) | AbuseIPDB Live-API – Community-gemeldete IPs (Score ≥ 50, bis zu 10.000 IPs) | **9,985** |
| [asn_blocklist_firewall.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/asn_blocklist_firewall.txt) | Netzwerke mit schlechter Reputation (ASN-Ebene) | täglich |

### 🌍 Geo Blocking

| Datei | Inhalt |
|---|---|
| [all_countries_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt) | Alle Länder zusammengefasst |
| [continents/](https://github.com/juergen2025sys/NETSHIELD/tree/main/continents) | 6 Kontinent-Dateien |
| [countries/](https://github.com/juergen2025sys/NETSHIELD/tree/main/countries) | Einzeldateien nach Kontinent sortiert |

---

## 📊 Listengröße (aktueller Snapshot)

| Liste | Einträge |
|---|---:|
| [combined_threat_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt) | **2.344.956** | **3,099,113** | [active_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt) | **0** | **3,099,113** | [blacklist_confidence40_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) | **0** | **2,331,037** | [watchlist_confidence20to39_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/watchlist_confidence20to39_ipv4.txt) | **0** | **528,091** | [cve_exploit_ips.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/cve_exploit_ips.txt) | **220.881** | **224,275** | [vpn_proxy_ranges.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/vpn_proxy_ranges.txt) | **111.974** | **57,798** | [tor_exit_nodes.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt) | **20.120** | **7,891** | [bot_detector_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/bot_detector_blacklist_ipv4.txt) | **17.954** | **15,530** | [abuseipdb_api_blacklist.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/abuseipdb_api_blacklist.txt) | **0** | **9,985** | [all_countries_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt) | **~254.556 CIDR-Ranges** |

---

## 🧠 Das Confidence-Modell erklärt

`blacklist_confidence40_ipv4.txt` ist die qualitativ hochwertigste Liste in NETSHIELD — aber sie funktioniert anders als eine normale Blacklist und es lohnt sich, das Prinzip zu verstehen.

### Warum nicht einfach alle IPs blocken?

NETSHIELD aggregiert ~80 Feeds gleichzeitig. Darunter befinden sich hochwertige Echtzeit-Feeds (Feodo Tracker, Spamhaus DROP, AbuseIPDB Score 100) genauso wie große statische Listen mit Hunderttausenden IPs die sich monatelang kaum ändern. Würde man alles gleichgewichtig behandeln, könnte eine IP die einmalig in einer veralteten Megalist stand, auf ewig als "aktive Bedrohung" gelten — genau das will `confidence40` verhindern.

### Wie wird ein Score berechnet?

Jede IP bekommt einen Score aus vier unabhängigen Dimensionen (max. 100 Punkte):

| Dimension | Max. | Was gemessen wird |
|---|---|---|
| **Quellen-Qualität** | 40 Pkt | HQ-Feed? Wie viele Feeds melden die IP heute? Akkumulierte Feed-Anzahl? |
| **Aktualität** | 30 Pkt | Wann wurde die IP zuletzt in ≥2 Feeds oder einem HQ-Feed gesehen? |
| **Persistenz** | 20 Pkt | An wie vielen verschiedenen Tagen wurde die IP unabhängig bestätigt? |
| **Bekannt seit** | 10 Pkt | Wie lange ist die IP schon im System? |

**Schwellwert: Score ≥ 50 → `blacklist_confidence40`**  
**Score 25–49 → `watchlist_confidence20to39`**

Eine IP die nur einmal in einer Low-Quality-Liste auftauchte und seitdem nie wieder gesehen wurde, erreicht maximal ~20 Punkte und kommt nie in die Confidence-Liste. Eine IP die täglich in mehreren HQ-Feeds auftaucht und das seit Wochen, kommt auf 70–100 Punkte.

### Was macht die Aktualitäts-Messung besonders?

Das System unterscheidet zwischen "wurde heute irgendwo erwähnt" und "wurde heute wirklich aktiv bestätigt". Das `last_seen`-Datum einer IP wird **nur dann aktualisiert**, wenn:

- die IP heute in **mindestens 2 verschiedenen Feeds** auftauchte, **oder**
- die IP heute in **mindestens einem HQ-Feed** (Feodo, Spamhaus, AbuseIPDB Score 100 usw.) gemeldet wurde

Eine IP die nur in einem einzigen statischen Feed steht — egal wie groß dieser Feed ist — gilt nicht als "heute aktiv bestätigt" und verliert schrittweise ihre Aktualitätspunkte.

### ⏳ Warum braucht die Confidence-Liste Zeit zum Aufbauen?

Der Persistenz-Score (`days_seen`) misst auf wie vielen verschiedenen **Tagen** eine IP unabhängig bestätigt wurde. Dieser Wert kann nicht rückwirkend berechnet werden — er wächst organisch mit jedem Tag an dem das System läuft.

**Zeitplan der Filterqualität:**

```
Tag 1–3   Frischer Start
          Quellen-Qualität und Aktualität dominieren das Scoring.
          Liste enthält bereits alle HQ-Feed-IPs korrekt.
          Persistenz-Bonus noch minimal.

Tag 4–7   Erste Selektionswirkung
          IPs die nur in statischen Feeds standen und seitdem
          nicht mehr bestätigt wurden, verlieren Aktualitätspunkte.
          Liste beginnt sich spürbar von "combined" zu unterscheiden.

Tag 8–14  Stabile Grundqualität
          Persistenz-Score greift für regelmäßig bestätigte IPs.
          Gut bestätigte Dauerbedrohungen haben jetzt hohe Scores.
          Einmalige Treffer fallen zunehmend aus der Liste.

Tag 15+   Volle Filterqualität
          Die Liste zeigt ihr eigentliches Profil:
          kompakt, treffsicher, wenig False Positives.
          Neue echte Bedrohungen landen sofort durch HQ-Feeds.
          Alte unbestätigte IPs fallen kontinuierlich heraus.
```

> **Kurzfassung:** In den ersten Tagen nach einem Reset ist `confidence40` noch ähnlich groß wie `combined`. Das ist normal. Nach 1–2 Wochen entwickelt sich der Unterschied deutlich — die Liste wird kleiner und gleichzeitig treffsicherer.

### Die drei Listen im Vergleich

| | `combined` | `active` | `confidence40` |
|---|---|---|---|
| **Zweck** | Vollarchiv, maximale Abdeckung | Frische Bedrohungen ≤ 30 Tage | Qualitätsgefiltert, wenig FP |
| **Größe** | Sehr groß | Mittel | Kleiner, aber präziser |
| **False Positives** | Höher | Mittel | Niedrig |
| **Neue Bedrohungen** | Sofort | Sofort | Sofort (via HQ-Feeds) |
| **Empfehlung** | SOC / Analyse | Allgemeines Blocking | Produktion, sensible Umgebungen |

---

## 🏗️ Projektstruktur

```
NETSHIELD/
├── .github/workflows/                  # Automatische Build-, Prüf- und Export-Workflows
├── active_blacklist_ipv4.txt           # Frische Bedrohungen (≤30 Tage bestätigt)
├── combined_threat_blacklist_ipv4.txt  # Großes Vollarchiv (365 Tage)
├── blacklist_confidence40_ipv4.txt     # Qualitätsgefiltert: mehrfach & HQ-bestätigt
├── watchlist_confidence20to39_ipv4.txt # Beobachtungsliste: schwächere Signale
├── bot_detector_blacklist_ipv4.txt     # Bot-, Scraper- und Scanner-Erkennung
├── tor_exit_nodes.txt                  # Tor Exit Nodes
├── cve_exploit_ips.txt                 # Exploit-nahe IPs (C2, Feodo, ThreatFox)
├── vpn_proxy_ranges.txt                # VPN- und Proxy-Ranges
├── asn_blocklist_firewall.txt          # ASN-Reputationsliste
├── all_countries_ipv4.txt              # Alle Länder in einer Datei
├── continents/                         # Kontinent-Dateien
├── countries/                          # Länderdateien nach Region sortiert
└── NETSHIELD_REPORT.md                 # Automatisch generierter Projektstatus
```

---

## ⚙️ Automatisierung via GitHub Actions

NETSHIELD ist kein statisches IP-Archiv, sondern ein **automatisiertes Blocklist-Framework**. Workflows pflegen Listen kontinuierlich:

| Workflow | Aufgabe | Intervall |
|---|---|---|
| `update_combined_blacklist.yml` | ~80 Feeds abrufen, seen_db aufbauen, combined + active + confidence schreiben | alle 3h |
| `update_confidence_blacklist.yml` | Confidence-Score neu berechnen, confidence40 + watchlist schreiben | alle 3h |
| `false_positive_checker.yml` | Whitelisted CDN/Cloud-IPs aus combined entfernen | 3x täglich |
| `score_decay_monitor.yml` | IPs nach 60 Tagen Inaktivität aus DB entfernen | wöchentlich |
| `tor_exit_monitor.yml` | Tor Exit Nodes aus 6 Quellen aktualisieren | täglich |
| `vpn_proxy_detector.yml` | VPN/Proxy-Ranges aktualisieren | wöchentlich |
| `cve_to_ip_mapper.yml` | Exploit-IPs aus C2-Trackern und ThreatFox | täglich |
| `firewall_format_exporter.yml` | iptables, nftables, pfSense XML, Cisco ACL usw. generieren | täglich |
| `asn_reputation_scorer.yml` | ASN-Reputationsbewertung und Blockliste | täglich |
| `feed_health_monitor.yml` | Feed-Erreichbarkeit und Qualität überwachen | täglich |

---

## 🎯 Einsatzszenarien

### OPNsense / pfSense

URL Table Alias anlegen (Typ `URL Table (IPs)`):

```
# Frische Bedrohungen (empfohlen als Einstieg)
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt

# Qualitätsgefiltert (für sensible Umgebungen)
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt

# Ergänzend
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/vpn_proxy_ranges.txt
```

Geo Blocking über [continents/](https://github.com/juergen2025sys/NETSHIELD/tree/main/continents) oder einzelne Länderdateien aus [countries/](https://github.com/juergen2025sys/NETSHIELD/tree/main/countries).

### Webserver / Reverse Proxies

```
# Bot- und Scanner-Schutz
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/bot_detector_blacklist_ipv4.txt
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt
```

### Linux (iptables / nftables)

Fertige Skripte im [firewall_exports/](https://github.com/juergen2025sys/NETSHIELD/tree/main/firewall_exports) Ordner:

```bash
# iptables
bash firewall_exports/blacklist_iptables.sh

# nftables
nft -f firewall_exports/blacklist_nftables.conf
```

### SOC / Lab / Forschung

```
combined_threat_blacklist_ipv4.txt   # Vollständiger aggregierter Feed
blacklist_geo_enriched.json          # IPs angereichert mit Geo/ASN-Daten
asn_reputation_report.md             # Top-Abuse-ASNs mit Score
NETSHIELD_REPORT.md                  # Aktueller Projektstatus
```

---

## 🌐 Geo Blocking – Kontinente & Länder

### Kontinente

| Datei | Region |
|---|---|
| [africa_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/africa_ipv4.txt) | Afrika |
| [asia_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/asia_ipv4.txt) | Asien |
| [europe_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/europe_ipv4.txt) | Europa |
| [north_america_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/north_america_ipv4.txt) | Nordamerika |
| [south_america_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/south_america_ipv4.txt) | Südamerika |
| [oceania_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/oceania_ipv4.txt) | Ozeanien |

### Einzelne Länder

Länderdateien unter `countries/{kontinent}/{land}_ipv4.txt`, z. B.:

- [countries/europe/germany_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/europe/germany_ipv4.txt)
- [countries/europe/russia_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/europe/russia_ipv4.txt)
- [countries/asia/china_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/asia/china_ipv4.txt)
- [countries/north_america/united_states_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/north_america/united_states_ipv4.txt)

Alle 249 Länder sind im [countries/](https://github.com/juergen2025sys/NETSHIELD/tree/main/countries) Verzeichnis verfügbar.

---

## ⚠️ Hinweise

**GeoIP ist eine Näherung.** Country- und Kontinentlisten basieren auf administrativer IP-Zuordnung. Bei CDN-Infrastruktur, Cloud-Providern, Anycast-Netzen und VPN-/Hosting-Plattformen kann es zu False Positives kommen.

**`combined` vor dem Produktiveinsatz testen.** Die Liste ist sehr groß und enthält bewusst auch ältere und schwach bestätigte IPs. Für direktes Firewall-Blocking ist `active` oder `confidence40` die bessere Wahl.

**`confidence40` braucht Anlaufzeit.** Nach einem Neustart des Systems arbeitet sich die Filterqualität in den ersten 7–14 Tagen auf ihr eigentliches Niveau ein. Mehr dazu im Abschnitt [Das Confidence-Modell](#-das-confidence-modell-erklärt).

---

## 📄 Lizenz

Im Repository ist aktuell keine Lizenz dokumentiert. Für produktive oder kommerzielle Nutzung sollte die Lizenzlage beim Projektinhaber erfragt werden.

---

<div align="center">

## 🔥 NETSHIELD ist nicht nur eine Liste.
### Es ist ein automatisiertes Blocklist-Framework für echte Firewall-Workflows.

[→ Zum Repository](https://github.com/juergen2025sys/NETSHIELD) · [→ Direkter Feed-Einstieg](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt) · [→ Projektstatus](https://github.com/juergen2025sys/NETSHIELD/blob/main/NETSHIELD_REPORT.md)

</div>
