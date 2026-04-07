# iba-code-guard

Patent Pending: GB2603013.0 (filed 5 Feb 2026) and related PCT applications.
Commercial use or derivative works may require licensing. Contact IBA@intentbound.com

**Verify intent before code merges. Prevent hidden actors from owning your protocol.**

North Korean developers have been quietly contributing to major DeFi protocols for years — building the very infrastructure millions of users trust.

This tool adds real cryptographic governance to open-source contributions.

Wrap any code change, PR, or diff with a signed **IBA Intent Certificate** so only approved human intent can be merged.

## Live Demo
Try the governed code pipeline: [https://governinglayer.com/codeguard-html/](https://governinglayer.com/codeguard-html/)

## Features
- Requires IBA-signed intent before any code merge
- Prevents stealthy long-term infiltration and sleeper attacks
- Detects obfuscated backdoors before merge
- OFAC / sanctions identity check at merge gate
- Contribution pattern anomaly detection across commit history
- Optional safe hollowing / flagging of suspicious contributions
- Full WitnessBound immutable audit chain — who signed, what scope, when
- Works with GitHub PRs, diffs, or raw code files

## Quick Start
```bash
