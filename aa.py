import sys

for c,line in enumerate(sys.stdin):
	print(c,line)

#tail -f log | python aa.py