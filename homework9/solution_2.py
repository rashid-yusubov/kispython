def main(text: str) -> dict:
    result = {}
    text = text[text.find("begin") + 5:text.rfind("end")].strip()
    sections = text.split("<section>")
    for section in sections:
        if "@\"" in section and "#" in section:
            key_start = section.find("@\"") + 2
            key_end = section.find("\"", key_start)
            key = section[key_start:key_end]
            value_start = section.find("#", key_end) + 1
            value_end = section.find("</section>", value_start)
            value = int(section[value_start:value_end].strip())
            result[key] = value
    return result
