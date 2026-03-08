[Uploading README.md…]()
# 🛡️ NETSHIELD — IPv4 Blocklist Suite

Complete IPv4 threat intelligence feed for firewalls, OPNsense, pfSense, and FortiGate.  
Automatically updated via PowerShell — free to use, no attribution required.

---

## 📁 Files

### 🌍 `all_countries_ipv4.txt`
- **Content:** All IPv4 ranges from all 249 countries worldwide
- **Entries:** 254,556 CIDR ranges
- **Format:** CIDR (e.g. `1.0.0.0/24`)
- **Source:** [country-ip-blocks.hackinggate.com](https://country-ip-blocks.hackinggate.com)
- **Update:** Manual — run the included PowerShell script
- **Use Case:** Block all incoming WAN traffic from every country in the world with a single list. Perfect for firewalls where no inbound connections are needed — completely eliminates the attack surface from foreign IPs.

---

### 🚫 `blacklist_confidence40_ipv4.txt`
- **Content:** Confirmed malicious IPs with AbuseIPDB confidence score **≥ 40%**
- **Format:** One IP per line
- **Source:** [AbuseIPDB](https://www.abuseipdb.com)
- **Update:** Automatic (daily)
- **Use Case:** Block high-confidence threat IPs — known attackers, scanners, brute-force bots, and malicious actors.

---

### ⚠️ `watchlist_confidence20to39_ipv4.txt`
- **Content:** Suspicious IPs with AbuseIPDB confidence score **20–39%**
- **Format:** One IP per line
- **Source:** [AbuseIPDB](https://www.abuseipdb.com)
- **Update:** Automatic (daily)
- **Use Case:** Monitor or soft-block low-confidence suspicious IPs — useful for rate limiting, logging, or stricter inspection rules.

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

`security` `firewall` `blocklist` `ipv4` `opnsense` `geoip` `fortigate` `threat-intelligence` `ip-blocklist` `abuseipdb`

---

## 📜 License

Free to use for any purpose. No attribution required.
