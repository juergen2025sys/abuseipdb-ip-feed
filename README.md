
<div align="center">

# 🛡️ NETSHIELD

### Complete IPv4 Blocklist Suite for Firewalls & Network Security

![IPv4](https://img.shields.io/badge/IPv4-254%2C556%20Ranges-blue?style=flat-square)
![Countries](https://img.shields.io/badge/Countries-249-green?style=flat-square)
![Continents](https://img.shields.io/badge/Continents-6-orange?style=flat-square)
![Update](https://img.shields.io/badge/Update-Automatic-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-Free-lightgrey?style=flat-square)

*Designed for OPNsense · pfSense · FortiGate · and any firewall supporting IP blocklists*

</div>

---

## 📌 Overview

NETSHIELD provides ready-to-use IPv4 blocklists organized by country, continent, and threat confidence level. All lists are automatically updated and available as raw links — simply paste into your firewall and forget.

---

## 🌍 All Countries

| Property | Value |
|---|---|
| **Entries** | ~254,556 CIDR ranges |
| **Format** | CIDR (e.g. `1.0.0.0/24`) |
| **Update** | Automatic |
| **Raw Link** | [all_countries_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt) |

**Use Case:** Block all incoming WAN traffic from every country in the world with a single list. Perfect for firewalls where no inbound connections are needed — completely eliminates the attack surface from foreign IPs.

---

## 🌐 Continent Blocklists

Block entire regions with a single link.

| Continent | Raw Link |
|---|---|
| 🇪🇺 Europe | [europe_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/europe_ipv4.txt) |
| 🌏 Asia | [asia_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/asia_ipv4.txt) |
| 🌍 Africa | [africa_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/africa_ipv4.txt) |
| 🌎 North America | [north_america_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/north_america_ipv4.txt) |
| 🌎 South America | [south_america_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/south_america_ipv4.txt) |
| 🌊 Oceania | [oceania_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/oceania_ipv4.txt) |

---

## 🗺️ Country Blocklists

Block individual countries — organized by continent. Use the raw link directly in your firewall.

**Raw link pattern:**
```
https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/{continent}/{country}_ipv4.txt
```

**Examples:**
| Country | Raw Link |
|---|---|
| 🇮🇷 Iran | [iran_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/asia/iran_ipv4.txt) |
| 🇨🇳 China | [china_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/asia/china_ipv4.txt) |
| 🇷🇺 Russia | [russia_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/europe/russia_ipv4.txt) |
| 🇺🇸 United States | [united_states_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/north_america/united_states_ipv4.txt) |
| 🇧🇷 Brazil | [brazil_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/south_america/brazil_ipv4.txt) |
| 🇳🇬 Nigeria | [nigeria_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/countries/africa/nigeria_ipv4.txt) |

> Browse all 249 country files in the [`countries/`](https://github.com/juergen2025sys/NETSHIELD/tree/main/countries) folder.

---

## 🚫 Threat Intelligence Lists

### Blacklist — High Confidence (≥ 40%)

| Property | Value |
|---|---|
| **Content** | Confirmed malicious IPs with confidence score ≥ 40% |
| **Format** | One IP per line |
| **Update** | Automatic · Daily |
| **Raw Link** | [blacklist_confidence40_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) |

**Use Case:** Block high-confidence threat IPs — known attackers, scanners, brute-force bots, and malicious actors. Recommended for **hard blocking**.

---

### Watchlist — Low Confidence (20–39%)

| Property | Value |
|---|---|
| **Content** | Suspicious IPs with confidence score 20–39% |
| **Format** | One IP per line |
| **Update** | Automatic · Daily |
| **Raw Link** | [watchlist_confidence20to39_ipv4.txt](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/watchlist_confidence20to39_ipv4.txt) |

**Use Case:** Monitor or soft-block low-confidence suspicious IPs — useful for rate limiting, logging, or stricter inspection rules.

> ⚠️ **Warning:** This list has a **high false positive rate**. Many IPs may be legitimate users, shared hosting, or dynamic IPs that were temporarily flagged. Recommended for **logging and monitoring only** — not for hard blocking.

---

## ✅ Tested & Verified

All IP ranges have been verified to be present in `all_countries_ipv4.txt`:

| Country | Sample IP | Verified CIDR |
|---|---|---|
| 🇷🇺 Russia | 5.8.18.100 | ✅ 5.8.16.0/21 |
| 🇨🇳 China | 113.195.145.80 | ✅ 113.194.0.0/15 |
| 🇧🇷 Brazil | 177.75.40.100 | ✅ 177.75.40.0/21 |
| 🇮🇳 India | 103.10.197.50 | ✅ 103.10.197.0/24 |
| 🇧🇬 Bulgaria | 31.170.100.50 | ✅ 31.170.100.0/22 |
| 🇻🇳 Vietnam | 45.125.65.50 | ✅ 45.125.64.0/22 |
| 🇷🇴 Romania | 82.80.100.200 | ✅ 82.80.0.0/15 |
| 🇵🇰 Pakistan | 203.78.120.30 | ✅ 203.78.112.0/20 |

---

## 🗺️ Notes on Continent Assignment

| Country | Assigned to | Note |
|---|---|---|
| 🇹🇷 Turkey (TR) | Asia | Transcontinental — majority of land mass is in Asia |
| 🇷🇺 Russia (RU) | Europe | Politically European, but spans all of Asia too |
| 🇬🇱 Greenland (GL) | Europe | Danish territory — geographically North America |
| 🇨🇾 Cyprus (CY) | Europe | Politically European (EU member), geographically closer to Asia |

> For firewall purposes this does not matter — every IP is always present in `all_countries_ipv4.txt`.

---

## 🔧 Works Great In Combination With

- 🖥️ Datacenter IP lists — AWS, Azure, Hetzner, etc.
- 🔒 VPN provider lists — NordVPN, ProtonVPN, etc.
- 🧅 TOR exit node lists
- 🕵️ Threat intelligence feeds
- 🛑 Known malicious IP lists

---

## 📜 License

Free to use for any purpose. No attribution required.
