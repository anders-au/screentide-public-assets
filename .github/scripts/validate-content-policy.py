"""Validate a moderation policy before publishing it to public assets."""
import json
import re
import sys

policy = json.load(open(sys.argv[1], encoding="utf-8"))
assert policy["schema_version"] == 1
assert isinstance(policy["revision"], str) and policy["revision"]
providers = {"icanhazdadjoke", "zenquotes", "uselessfacts"}
assert set(policy["disabled_providers"]) <= providers
assert set(policy["providers"]) <= providers
for values in policy["providers"].values():
    assert all(isinstance(value, str) and value for value in values["blocked_ids"])
    assert all(re.fullmatch("[a-f0-9]{64}", value) for value in values["blocked_hashes"])
print("Content policy valid")
