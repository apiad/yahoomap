import json
import sys

states = {}
data = {}

with open("us_state_abbr.csv") as fp:
    for line in fp:
        state, _, abbr, __ = line.strip().split(",")
        states[state] = abbr.lower()

with open(sys.argv[1]) as fp:
    for line in fp:
        key, value = line.strip().split(",")
        data[states[key]] = dict(value=int(value), name=key)

print(json.dumps(data))
