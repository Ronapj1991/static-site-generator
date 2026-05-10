def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    res = []

    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line.strip())
        res.append("\n".join(new_lines))
    return res