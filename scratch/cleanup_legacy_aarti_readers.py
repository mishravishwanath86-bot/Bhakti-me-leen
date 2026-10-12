import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check line 18946 (0-indexed: 18945)
print("Line 18946:", repr(lines[18945]))
# Replace function readAartiItemDirect(deityKey, idx) { ... } at lines 18945-18959
old_18946 = lines[18945:18960]
print("Lines 18946-18960 length:", len(old_18946))

# Let's inspect line 19917
print("Line 19918:", repr(lines[19917]))

# Let's inspect line 21602
print("Line 21603:", repr(lines[21602]))
