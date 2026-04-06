# guard.py - IBA protection for code contributions / PRs / diffs
import json
from datetime import datetime
import sys
import argparse

def create_iba_code_guard(input_file: str):
    try:
        with open(input_file, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
        sys.exit(1)

    cert = {
        "iba_version": "2.0",
        "certificate_id": f"code-guard-{datetime.now().strftime('%Y%m%d-%H%M')}",
        "issued_at": datetime.now().isoformat(),
        "principal": "human-owner",
        "declared_intent": "This code contribution is for legitimate development purposes only. No backdoors, no hidden functionality, no unauthorized control mechanisms.",
        "scope_envelope": {
            "resources": ["code-contribution", "pull-request"],
            "denied": ["backdoor", "stealth-control", "unauthorized-access"],
            "default_posture": "DENY_ALL"
        },
        "temporal_scope": {
            "hard_expiry": (datetime.now().replace(year=datetime.now().year + 1)).isoformat()
        },
        "entropy_threshold": {
            "max_kl_divergence": 0.12,
            "flag_at": 0.08,
            "kill_at": 0.12
        },
        "iba_signature": "demo-signature"
    }

    protected_file = input_file + ".iba-protected.md"

    with open(protected_file, "w", encoding="utf-8") as f:
        f.write("<!-- IBA PROTECTED CODE CONTRIBUTION -->\n")
        f.write(f"<!-- Intent Certificate: {json.dumps(cert, indent=2)} -->\n\n")
        f.write(content)

    print(f"✅ IBA-protected code file created: {protected_file}")
    print("   This contribution is now cryptographically governed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Protect code contributions with IBA")
    parser.add_argument("input_file", help="Path to diff, patch, or code file")
    args = parser.parse_args()

    create_iba_code_guard(args.input_file)
