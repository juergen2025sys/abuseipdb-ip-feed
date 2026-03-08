
<div align="center">

# 🛡️ NETSHIELD

### Vollständige IPv4-Blocklist-Suite für Firewalls & Netzwerksicherheit

![Combined IPs](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_report.md&label=Combined+IPs&query=$.count&color=blue&style=flat-square)
![Länder](https://img.shields.io/badge/L%C3%A4nder-249-green?style=flat-square)
![Kontinente](https://img.shields.io/badge/Kontinente-6-orange?style=flat-square)
![Quellen](https://img.shields.io/badge/Threat--Quellen-31-red?style=flat-square)
![Update](https://img.shields.io/badge/Update-Automatisch-brightgreen?style=flat-square)
![Lizenz](https://img.shields.io/badge/Lizenz-Kostenlos-lightgrey?style=flat-square)

*Entwickelt für OPNsense · pfSense · FortiGate · iptables · nftables · und jede Firewall mit IP-Blocklist-Unterstützung*

</div>

---

## 📌 Übersicht

NETSHIELD bietet fertige IPv4-Blocklisten, organisiert nach Land, Kontinent und Bedrohungsstufe. Alle Listen werden vollautomatisch über GitHub Actions aktualisiert und sind als Raw-Links verfügbar — einfach in die Firewall einfügen und vergessen.

**Was NETSHIELD bietet:**
- 🌍 **249 Länder-Blocklisten** — einzelne Länder gezielt blockieren
- 🌐 **6 Kontinenten-Blocklisten** — ganze Regionen mit einem Link
- 🚫 **Combined Threat Blacklist** — kreuzvalidierte Bedrohungs-IPs aus 31 Quellen
- 🎯 **Confidence Blacklist** — nach Konfidenz-Score gewichtete Angreifer-IPs
- 🤖 **Bot-Detector-Blacklist** — Bots, Scraper, Scanner, DDoS-Quellen
- 🧅 **Tor Exit Nodes** — alle aktiven Tor-Ausgangsknoten
- 🦠 **CVE Exploit IPs** — IPs die aktuelle Sicherheitslücken ausnutzen
- 🔒 **VPN & Proxy Ranges** — Anonymisierungs-Dienste
- 🏢 **ASN Reputation Blocklist** — missbräuchliche Netzwerke nach Score

---

## 📥 Schnellstart — Direkte Download-Links

| Liste | Raw Link | Update |
|---|---|---|
| 🌍 Alle Länder | [all_countries_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt) | Mo + Mi |
| 💀 Combined Threat | [combined_threat_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt) | Alle 6h |
| 🎯 Hohe Konfidenz ≥40% | [blacklist_confidence40_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) | Alle 6h |
| 🤖 Bot Detector | [bot_detector_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/bot_detector_blacklist_ipv4.txt) | Alle 6h |
| 🧅 Tor Exit Nodes | [tor_exit_nodes.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt) | Täglich |
| 🦠 CVE Exploit IPs | [cve_exploit_ips.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/cve_exploit_ips.txt) | Täglich |
| 🔒 VPN & Proxy | [vpn_proxy_ranges.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/vpn_proxy_ranges.txt) | Wöchentlich |
| 🏢 ASN Blocklist | [asn_blocklist_firewall.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/asn_blocklist_firewall.txt) | Täglich |
| 👁️ Watchlist 20-39% | [watchlist_confidence20to39_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/watchlist_confidence20to39_ipv4.txt) | Alle 6h |

---

## 🎯 Konfidenz-Blacklist (≥ 40%)

Die intelligenteste Liste in NETSHIELD — jede IP bekommt einen **Konfidenz-Score** basierend auf Quellenqualität, Aktualität und Persistenz.

### Konfidenz-Berechnung

**Basis-Score:**

| Bedingung | Punkte |
|---|---|
| IP aus einem **HQ-Feed** (Feodo, ThreatFox, DShield, Firehol, Binary Defense usw.) | **60%** |
| IP aus **2+ normalen Feeds** (kreuzvalidiert) | **40%** |
| IP nur in 1 normalem Feed | wird ignoriert |

**Aktualitäts-Bonus:**

| Bedingung | Punkte |
|---|---|
| Zuletzt gesehen **≤ 7 Tage** | **+20%** |
| Zuletzt gesehen **≤ 30 Tage** | **+10%** |

**Persistenz-Bonus:**

| Bedingung | Punkte |
|---|---|
| IP seit **≥ 30 Tagen** bekannt | **+10%** |
| IP seit **≥ 14 Tagen** bekannt | **+5%** |

**Maximaler Score: 100%**

**Beispiele:**
```
Feodo-IP, heute gemeldet:         60 + 20 + 0  = 80% → blacklist_confidence40
HQ-IP, 2 Monate alt, noch aktiv: 60 +  0 + 10 = 70% → blacklist_confidence40
3 Feeds, seit 3 Wochen aktiv:     40 + 10 + 5  = 55% → blacklist_confidence40
2 Feeds, letzte Woche neu:        40 + 20 + 0  = 60% → blacklist_confidence40
1 normaler Feed, neu:             nicht aufgenommen
```

**Ausgabe:**
- **≥ 40%** → `blacklist_confidence40_ipv4.txt` → **blockieren**
- **20–39%** → `watchlist_confidence20to39_ipv4.txt` → **beobachten**

| Eigenschaft | Wert |
|---|---|
| **Update** | Alle 6 Stunden (15 Min nach Combined) |
| **Raw Link** | [blacklist_confidence40_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) |

---

## 💀 Combined Threat Blacklist

Kreuzvalidierte Bedrohungs-IPs aus **31 Threat-Intelligence-Quellen** — die umfangreichste Liste in NETSHIELD.

| Eigenschaft | Wert |
|---|---|
| **Format** | Eine IP pro Zeile · sortiert |
| **Update** | Alle 6 Stunden |
| **Ablauf** | IPs die 90 Tage in keinem Feed auftauchen werden automatisch entfernt |
| **Raw Link** | [combined_threat_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt) |

**Inhalt:** Bestätigte Angreifer · Brute-Force-Quellen · SSH-Scanner · DDoS-Quellen · Botnet-IPs · Honeypot-Treffer · Malware-C2-Server

### Kreuzvalidierungs-Filter

Eine IP kommt nur in die Liste wenn sie mindestens **eine** Bedingung erfüllt:

| Bedingung | Bedeutung |
|---|---|
| **2+ Feeds** | IP taucht in mindestens 2 verschiedenen Quellen auf |
| **1 HQ-Feed** | IP steht in einer besonders zuverlässigen Quelle |

### Feed-Quellen (31 gesamt)

| Kategorie | Quellen |
|---|---|
| **C2 / Malware / IOC** | Feodo Tracker · ThreatFox · ThreatView · trcert-malware · Firehol Cybercrime |
| **Scanner / Brute-Force** | CrowdSec SSH · DShield · CINS Score · Danger Bruteforce · Greensnow · Interserver |
| **DDoS** | L7 DDoS Signatures · Binary Defense |
| **Anonymisierung** | Firehol Anonymous · Cloudzy |
| **Threat-Aggregatoren** | Data-Shield · romainmarcoux (3×) · black-mirror · 4IP Solutions · cyna · bbcan177 · kevinmarx · honeypot-blocklist · nixbear · ufukart · f3csystems · FortiGate Azure · florent banned · edanwong |

### Eingebaute Schutzfilter

Folgende IPs können **nie** in die Liste aufgenommen werden:
- **Bekannte DNS-Server:** Google (8.8.8.8), Cloudflare (1.1.1.1), OpenDNS, Quad9, AdGuard
- **Private IP-Ranges:** `10.x.x.x` · `172.16–31.x.x` · `192.168.x.x` · `127.x.x.x`
- **Reservierte Ranges:** Multicast · Broadcast · Loopback

---

## 🤖 Bot-Detector-Blacklist

| Eigenschaft | Wert |
|---|---|
| **Inhalt** | Bots, Scraper, Scanner, DDoS-Quellen, VPN/Proxy-Missbrauch, Cloud-Bots |
| **Update** | Alle 6 Stunden |
| **Raw Link** | [bot_detector_blacklist_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/bot_detector_blacklist_ipv4.txt) |

**Kategorien:** KI-Crawler · SEO-Bots · Scraper · Schwachstellen-Scanner · DDoS-Quellen · Proxy/VPN-Missbrauch · Hosting/Cloud-Bots (AWS, Azure, DigitalOcean usw.)

> ⚠️ **Hinweis:** Enthält Cloud/Hosting-IPs — empfohlen für **Webserver und APIs**, nicht für allgemeines LAN-Blocking.

---

## 🧅 Tor Exit Nodes

| Eigenschaft | Wert |
|---|---|
| **Inhalt** | Alle aktiven Tor-Ausgangsknoten aus 6 Quellen |
| **Update** | Täglich 22:30 UTC |
| **Raw Link** | [tor_exit_nodes.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/tor_exit_nodes.txt) |

**Quellen:** TorProject (offiziell) · Dan.me.uk · SecOps Institute · SNORT Tor Feed · Ultimate Hosts · Ipsum

---

## 🦠 CVE Exploit IPs

| Eigenschaft | Wert |
|---|---|
| **Inhalt** | IPs die aktiv bekannte CVE-Sicherheitslücken ausnutzen |
| **Update** | Täglich 04:00 UTC |
| **Raw Link** | [cve_exploit_ips.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/cve_exploit_ips.txt) |

---

## 🔒 VPN & Proxy Ranges

| Eigenschaft | Wert |
|---|---|
| **Inhalt** | VPN-Anbieter, offene Proxies, Hosting-Ranges die für Anonymisierung genutzt werden |
| **Update** | Wöchentlich Montag 03:30 UTC |
| **Raw Link** | [vpn_proxy_ranges.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/vpn_proxy_ranges.txt) |

---

## 🌍 Länder & Kontinent-Blocklisten

### Alle Länder (eine Liste)

| Eigenschaft | Wert |
|---|---|
| **Einträge** | ~254.556 CIDR-Ranges |
| **Format** | CIDR (z.B. `1.0.0.0/24`) |
| **Update** | Mo + Mi 03:00 UTC |
| **Raw Link** | [all_countries_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt) |

### Kontinent-Blocklisten

| Kontinent | Raw Link |
|---|---|
| 🇪🇺 Europa | [europe_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/europe_ipv4.txt) |
| 🌏 Asien | [asia_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/asia_ipv4.txt) |
| 🌍 Afrika | [africa_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/africa_ipv4.txt) |
| 🌎 Nordamerika | [north_america_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/north_america_ipv4.txt) |
| 🌎 Südamerika | [south_america_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/south_america_ipv4.txt) |
| 🌊 Ozeanien | [oceania_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/oceania_ipv4.txt) |

### Einzelne Länder

**Raw-Link-Schema:**
```
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/{kontinent}/{land}_ipv4.txt
```

**Beispiele:**

| Land | Raw Link |
|---|---|
| 🇮🇷 Iran | [iran_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/asia/iran_ipv4.txt) |
| 🇨🇳 China | [china_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/asia/china_ipv4.txt) |
| 🇷🇺 Russland | [russia_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/europe/russia_ipv4.txt) |
| 🇺🇸 USA | [united_states_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/north_america/united_states_ipv4.txt) |
| 🇧🇷 Brasilien | [brazil_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/south_america/brazil_ipv4.txt) |
| 🇳🇬 Nigeria | [nigeria_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/africa/nigeria_ipv4.txt) |

> Alle 249 Länderdateien im [`countries/`](https://github.com/juergen2025sys/NETSHIELD/tree/main/countries) Ordner.

---

## ⚙️ Update-Zeitplan (UTC)

### Täglich

| Zeit | Workflow | Ausgabe |
|---|---|---|
| 22:30 | Tor Exit Monitor | `tor_exit_nodes.txt` |
| 23:45 | Bot Detector Update | `bot_detector_blacklist_ipv4.txt` |
| 00:00 | Update Combined Blacklist | `combined_threat_blacklist_ipv4.txt` |
| 00:15 | Update Confidence Blacklist | `blacklist_confidence40_ipv4.txt` · `watchlist_confidence20to39_ipv4.txt` |
| 00:30 | Firewall Format Exporter | `firewall_exports/` (JSON, CSV, iptables, nftables usw.) |
| 00:50 | NETSHIELD Report Generator | `NETSHIELD_REPORT.md` |
| 02:00 | ASN Reputation Scorer | `asn_blocklist_firewall.txt` |
| 04:00 | CVE-to-IP Mapper | `cve_exploit_ips.txt` |
| 04:30 | Duplicate Cleaner | bereinigt alle Sub-Listen |

### Wöchentlich

| Zeit | Workflow | Ausgabe |
|---|---|---|
| Mo 03:00 + Mi 03:00 | Update Blocklist | `all_countries_ipv4.txt` + Länder/Kontinente |
| Mo 03:30 | VPN & Proxy Detector | `vpn_proxy_ranges.txt` |
| So 05:00 | False Positive Checker | bereinigt `combined_threat_blacklist_ipv4.txt` |
| So 06:00 | Geo-Tagger | `blacklist_geo_enriched.json` |
| So 07:00 | Score Decay Monitor | entfernt 60+ Tage inaktive IPs |

---

## 🔥 Firewall-Exporte

NETSHIELD generiert automatisch fertige Konfigurationsdateien für alle gängigen Firewalls im Ordner [`firewall_exports/`](https://github.com/juergen2025sys/NETSHIELD/tree/main/firewall_exports):

| Datei | Format | Verwendung |
|---|---|---|
| `blacklist.json` | JSON | APIs, Skripte, SIEM |
| `blacklist.csv` | CSV | Excel, Datenbanken |
| `blacklist_iptables.sh` | iptables | Linux (Ubuntu, Debian, CentOS) |
| `blacklist_nftables.conf` | nftables | Linux (moderner iptables-Ersatz) |
| `blacklist_pfsense_opnsense.xml` | XML Alias | pfSense / OPNsense Import |
| `blacklist_cisco_acl.txt` | Cisco ACL | Cisco IOS / IOS-XE |
| `blacklist_mikrotik.rsc` | RouterOS | Mikrotik Router |
| `blacklist_windows_firewall.ps1` | PowerShell | Windows Server / Desktop |

**Schnellstart:**

```bash
# Linux iptables
sudo bash blacklist_iptables.sh

# Linux nftables
sudo nft -f blacklist_nftables.conf

# Mikrotik
/import file=blacklist_mikrotik.rsc

# Windows (Admin PowerShell)
.\blacklist_windows_firewall.ps1
```

**OPNsense/pfSense:** Firewall → Aliases → Import → `blacklist_pfsense_opnsense.xml`

---

## 🌐 OPNsense / pfSense — URL-Integration

Listen direkt als URL-Alias einbinden — aktualisiert sich automatisch:

1. **Firewall → Aliases → Hinzufügen**
2. Typ: `URL Table (IPs)`
3. URL einfügen (z.B. Combined Threat):
```
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt
```
4. Refresh-Intervall: `6 Stunden` (passend zum Update-Rhythmus)
5. Alias in Firewall-Regel → WAN Inbound → **Block** verwenden

---

## 🐧 Linux iptables / nftables

```bash
# Direkt herunterladen und anwenden
wget https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/firewall_exports/blacklist_iptables.sh
sudo bash blacklist_iptables.sh

# Oder per ipset (effizient für große Listen)
ipset create NETSHIELD hash:ip
while IFS= read -r ip; do
  [[ "$ip" =~ ^#.*$ ]] && continue
  ipset add NETSHIELD "$ip" 2>/dev/null
done < <(curl -s https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt)
iptables -I INPUT -m set --match-set NETSHIELD src -j DROP
```

---

## 🏢 ASN Reputation Blocklist

Blockt ganze Netzwerke (ASNs) die überdurchschnittlich viele Blacklist-IPs enthalten.

| Eigenschaft | Wert |
|---|---|
| **Inhalt** | ASNs mit Score ≥ 50 (Berechnung aus Blacklist-Anteil + Spamhaus DROP + Emerging Threats) |
| **Update** | Täglich 02:00 UTC |
| **Raw Link** | [asn_blocklist_firewall.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/asn_blocklist_firewall.txt) |

> ⚠️ **Hinweis:** ASN-Blocking kann legitimen Datenverkehr von Hosting-Providern treffen. Empfohlen für Hochsicherheitsumgebungen.

---

## 🗺️ Kontinentzuordnung — Hinweise

| Land | Zugeordnet zu | Hinweis |
|---|---|---|
| 🇹🇷 Türkei (TR) | Asien | Transkontinental — Großteil der Landfläche in Asien |
| 🇷🇺 Russland (RU) | Europa | Politisch europäisch, erstreckt sich über ganz Asien |
| 🇬🇱 Grönland (GL) | Europa | Dänisches Territorium — geografisch Nordamerika |
| 🇨🇾 Zypern (CY) | Europa | EU-Mitglied, geografisch näher an Asien |

---

## ✅ Getestet & Verifiziert

| Land | Beispiel-IP | Verifiziertes CIDR |
|---|---|---|
| 🇷🇺 Russland | 5.8.18.100 | ✅ 5.8.16.0/21 |
| 🇨🇳 China | 113.195.145.80 | ✅ 113.194.0.0/15 |
| 🇧🇷 Brasilien | 177.75.40.100 | ✅ 177.75.40.0/21 |
| 🇮🇳 Indien | 103.10.197.50 | ✅ 103.10.197.0/24 |
| 🇧🇬 Bulgarien | 31.170.100.50 | ✅ 31.170.100.0/22 |
| 🇻🇳 Vietnam | 45.125.65.50 | ✅ 45.125.64.0/22 |
| 🇷🇴 Rumänien | 82.80.100.200 | ✅ 82.80.0.0/15 |
| 🇵🇰 Pakistan | 203.78.120.30 | ✅ 203.78.112.0/20 |

---

## 📜 Lizenz

Kostenlos für jeden Zweck nutzbar. Keine Namensnennung erforderlich.
