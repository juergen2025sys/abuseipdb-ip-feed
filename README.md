# AbuseWatch IP Lists

This repository provides automatically generated IPv4 reputation lists based on AbuseIPDB data and contextual scoring.

The goal of this project is **not to blindly block every reported IP**, but to create a **balanced and realistic threat intelligence feed** that reduces false positives while still identifying potentially malicious infrastructure.

## Why this project exists

Many public IP blocklists rely solely on raw abuse reports.
In practice, this leads to extremely high false positive rates.

Large parts of the internet run on shared cloud infrastructure such as:

* Google Cloud
* Microsoft Azure
* AWS
* Cloudflare
* Akamai
* CDN providers

If a single server in these networks performs scanning or malicious activity, the IP often receives multiple abuse reports.
However, the same infrastructure may also host legitimate services.

Because of this, many public feeds can contain **50–70% false positives**.

This repository attempts to reduce that problem.

## Scoring Logic

IPs are categorized based on AbuseIPDB reputation scores.

### Blocklist

`abuseipdb_blacklist_ipv4.txt`

Contains IPs with:

* Abuse Score **>= 40**

These addresses have a stronger reputation signal and are more likely to represent:

* botnet nodes
* compromised servers
* brute-force infrastructure
* malicious scanners
* command-and-control related hosts

This list is intended for **firewall blocking**.

### Watchlist

`abuseipdb_watchlist_ipv4.txt`

Contains IPs with:

* Abuse Score **20–39**

These addresses may have abuse reports but often belong to:

* cloud infrastructure
* shared hosting
* research scanners
* misconfigured services

This list is intended for:

* monitoring
* log correlation
* investigation

Blocking these addresses automatically may cause unnecessary disruptions.

## Philosophy

This project follows a **balanced security approach**:

* avoid excessive blocking
* minimize false positives
* allow legitimate cloud infrastructure
* still detect suspicious activity

Security systems that block aggressively without context often break legitimate services, including:

* software updates
* cloud APIs
* gaming platforms
* CDN traffic

AbuseWatch attempts to provide a **more realistic signal**.

## Important Note

This repository should be used as **one signal among many**, not as a single source of truth.

Always combine threat intelligence with:

* firewall logs
* behavioral analysis
* ASN / provider context
* application telemetry

## Disclaimer

This list is generated automatically from public abuse data.
No guarantee is provided regarding completeness or accuracy.

Use at your own risk.
