# iba-code-guard

**Verify intent before code merges. Prevent hidden actors from owning your protocol.**

North Korean developers have been quietly contributing to major DeFi protocols for years — building the very infrastructure millions of users trust.

This tool adds real cryptographic governance to open-source contributions.

Wrap any code change, PR, or diff with a signed **IBA Intent Certificate** so only approved human intent can be merged.

## Features
- Requires IBA-signed intent before any code merge
- Prevents stealthy long-term infiltration
- Optional safe hollowing / flagging of suspicious contributions
- Works with GitHub PRs, diffs, or raw code files

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-code-guard.git
cd iba-code-guard
pip install -r requirements.txt
python guard.py path/to/your-diff.patch
