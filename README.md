
# 🛡️ NETSHIELD — IPv4 Blocklist Suite

Complete IPv4 threat intelligence feed for firewalls, OPNsense, pfSense, and FortiGate.  
Automatically updated — free to use, no attribution required.

---

## 📁 Files

### 🌍 `all_countries_ipv4.txt`
- **Content:** All IPv4 ranges from all 249 countries worldwide
- **Entries:** ~254,556 CIDR ranges
- **Format:** CIDR (e.g. `1.0.0.0/24`)
- **Update:** Automatic
- **Raw:** `https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/all_countries_ipv4.txt`
- **Use Case:** Block all incoming WAN traffic from every country in the world with a single list. Perfect for firewalls where no inbound connections are needed — completely eliminates the attack surface from foreign IPs.

---

### 🌐 Continent Files (`continents/`)

For more granular control — block only specific regions instead of the entire world.

| Continent | File | Raw Link |
|---|---|---|
| 🇪🇺 Europe | `continents/europe_ipv4.txt` | [Raw](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/europe_ipv4.txt) |
| 🌏 Asia | `continents/asia_ipv4.txt` | [Raw](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/asia_ipv4.txt) |
| 🌍 Africa | `continents/africa_ipv4.txt` | [Raw](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/africa_ipv4.txt) |
| 🌎 North America | `continents/north_america_ipv4.txt` | [Raw](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/north_america_ipv4.txt) |
| 🌎 South America | `continents/south_america_ipv4.txt` | [Raw](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/south_america_ipv4.txt) |
| 🌊 Oceania | `continents/oceania_ipv4.txt` | [Raw](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/continents/oceania_ipv4.txt) |

---

### 🚫 `blacklist_confidence40_ipv4.txt`
- **Content:** Confirmed malicious IPs with confidence score **≥ 40%**
- **Format:** One IP per line

- **Update:** Automatic (daily)
- **Raw:** `https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt` — known attackers, scanners, brute-force bots, and malicious actors.

---

### ⚠️ `watchlist_confidence20to39_ipv4.txt`
- **Content:** Suspicious IPs with confidence score **20–39%**
- **Format:** One IP per line
- **Update:** Automatic (daily)
- **Raw:** `https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/watchlist_confidence20to39_ipv4.txt`
- **Use Case:** Monitor or soft-block low-confidence suspicious IPs — useful for rate limiting, logging, or stricter inspection rules.
- **⚠️ Warning:** This list has a **high false positive rate**. Many IPs in this range may be legitimate users, shared hosting, or dynamic IPs that were temporarily flagged. Use with caution — recommended for logging/monitoring only, not for hard blocking.

---

## ✅ Tested & Verified

IP ranges verified to be present in `all_countries_ipv4.txt`:

| Country | IP | Status |
|---|---|---|
| Russia | 5.8.18.100 | ✅ BLOCKED in 5.8.16.0/21 |
| China | 113.195.145.80 | ✅ BLOCKED in 113.194.0.0/15 |
| Brazil | 177.75.40.100 | ✅ BLOCKED in 177.75.40.0/21 |
| India | 103.10.197.50 | ✅ BLOCKED in 103.10.197.0/24 |
| Bulgaria | 31.170.100.50 | ✅ BLOCKED in 31.170.100.0/22 |
| Vietnam | 45.125.65.50 | ✅ BLOCKED in 45.125.64.0/22 |
| Romania | 82.80.100.200 | ✅ BLOCKED in 82.80.0.0/15 |
| Pakistan | 203.78.120.30 | ✅ BLOCKED in 203.78.112.0/20 |

---

## 🔧 Works great in combination with

- 🖥️ Datacenter IP lists (AWS, Azure, Hetzner, etc.)
- 🔒 VPN provider lists (NordVPN, ProtonVPN, etc.)
- 🧅 TOR exit node lists
- 🕵️ Threat intelligence feeds
- 🛑 Known malicious IP lists

---

## 📋 Tags

`security` `firewall` `blocklist` `ipv4` `opnsense` `geoip` `fortigate` `threat-intelligence` `ip-blocklist`

---

## 📜 License

Free to use for any purpose. No attribution required.

---

## 🗺️ Notes on Continent Assignment

Most countries are assigned to their geographical continent. However, a few transcontinental or politically special cases are assigned as follows:

| Country | Assigned to | Note |
|---|---|---|
| 🇹🇷 Turkey (TR) | Asia | Transcontinental — majority of land mass is in Asia |
| 🇷🇺 Russia (RU) | Europe | Politically European, but spans all of Asia too |
| 🇬🇱 Greenland (GL) | Europe | Danish territory — geographically North America |
| 🇨🇾 Cyprus (CY) | Europe | Politically European (EU member), geographically closer to Asia |

> **Note:** For firewall purposes this does not matter — every IP is present in at least one continent list and always in `all_countries_ipv4.txt`.
