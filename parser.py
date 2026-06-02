def parse_srt(content):
blocks = content.strip().split("\n\n")

```
subtitles = []

for block in blocks:
    lines = block.split("\n")

    if len(lines) >= 3:
        subtitles.append({
            "index": lines[0],
            "time": lines[1],
            "text": "\n".join(lines[2:])
        })

return subtitles
```

def build_srt(subtitles):
result = []

```
for item in subtitles:
    result.append(
        f"{item['index']}\n"
        f"{item['time']}\n"
        f"{item['text']}"
    )

return "\n\n".join(result)
```
