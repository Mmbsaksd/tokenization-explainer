#!/usr/bin/env python3
"""Split data/pubmed_sample.jsonl into disjoint train / held-out files.

Default: 45 000 train, 5 000 held-out  (requires data/pubmed_sample.jsonl).
Shuffle is deterministic (seed 42 on line indices) — same split every run.

Run: uv run python scripts/split_corpus.py
"""
