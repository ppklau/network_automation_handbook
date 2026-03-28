# ACME Investments — Intent Model

The intent verification and branch generation scripts from the three-part intent-based networking series.

## What This Demonstrates

- `tests/verify_intents.py` — SoT structural verification; runs in under one second; outputs JUnit XML for GitLab CI
- `scripts/generate_branch.py` — one-touch branch site generator; derives all design decisions from `design_intents.yml`; includes guardrails

The YAML source files (`requirements.yml`, `design_intents.yml`, `nodes.yml`) live in the main demo at [`../acme-investments-demo/`](../acme-investments-demo/).

## Directory Structure

```
acme-intent-model/
├── tests/
│   └── verify_intents.py     # Intent verification suite (JUnit XML output)
└── scripts/
    └── generate_branch.py    # One-touch branch site generator
```

## Usage

```bash
# Run full intent verification
python tests/verify_intents.py \
  --nodes ../acme-investments-demo/inventory/nodes.yml \
  --intents ../acme-investments-demo/design_intents.yml

# Generate a new branch site (dry run)
python scripts/generate_branch.py \
  --site-id    nyc-branch1 \
  --location   "New York, US" \
  --prefix     10.2.0.0/16 \
  --router-ip  10.2.0.1/24 \
  --router-lo  10.2.254.1/32 \
  --switch-ip  10.2.0.11/24 \
  --switch-lo  10.2.254.11/32 \
  --nodes      ../acme-investments-demo/inventory/nodes.yml \
  --intents    ../acme-investments-demo/design_intents.yml \
  --dry-run

# Generate and write to nodes.yml (with intent verification)
python scripts/generate_branch.py \
  --site-id    nyc-branch1 \
  --location   "New York, US" \
  --prefix     10.2.0.0/16 \
  --router-ip  10.2.0.1/24 \
  --router-lo  10.2.254.1/32 \
  --switch-ip  10.2.0.11/24 \
  --switch-lo  10.2.254.11/32 \
  --nodes      ../acme-investments-demo/inventory/nodes.yml \
  --intents    ../acme-investments-demo/design_intents.yml \
  --verify
```

## Handbook References

| This file | Handbook section |
|---|---|
| `tests/verify_intents.py` | Ch 7.3 — Testing Strategies (Layer 3: Verify Intents) |
| `scripts/generate_branch.py` | Ch 7.5 — One-Touch Deployment |
| Both | Ch 11.1 — Intent-Based Networking |
