import re


def main(text: str) -> dict:
    pattern = re.compile(r'@"(.*?)"\s*:=\s*#(-?\d+)')
    return {match[0]: int(match[1]) for match in pattern.findall(text)}
