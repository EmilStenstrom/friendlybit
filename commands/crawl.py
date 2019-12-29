import re
import requests
import html5validate
from urllib.parse import urlparse, urljoin

QUEUE = []
VISITED = set()
WHITELISTED_DOMAINS = set([
    "localhost:8000",
])
WHITELISTED_ATTRS = set(["href"])
BLACKLISTED_URL_PATTERNS = [
    "index_mangled.html",
    "/files/",
]

FILETYPE_RE = re.compile(r"\.([a-z0-9]{2,4})(?:\?.+)?$")

def is_checkable_pre(url):
    result = urlparse(url)
    if result.netloc not in WHITELISTED_DOMAINS:
        return False, f"Domain {result.netloc} is not whitelisted"

    match = re.search(FILETYPE_RE, result.path)
    if match:
        filetype = match.groups()[0]
        if filetype not in ["html"]:
            return False, f"Filetype is {filetype}"

    return True, ""

def is_checkable_post(response):
    for ignore_pattern in BLACKLISTED_URL_PATTERNS:
        if ignore_pattern in response.url:
            return False, f"Matched blacklisted pattern {ignore_pattern}"

    content_type = response.headers['content-type']
    if not content_type.startswith("text/html") and not content_type.startswith("text/plain"):
        return False, f"Content-Type == {response.headers['content-type']}"

    return True, ""


def main():
    QUEUE.append("http://localhost:8000")

    while len(QUEUE) > 0:
        url = QUEUE.pop(0)
        while url in VISITED:
            if len(QUEUE) > 0:
                url = QUEUE.pop(0)
            else:
                return

        print(f"Checking: {url: <100} --> ", end="")

        is_ok, error = is_checkable_pre(url)
        if not is_ok:
            print(f"SKIP (PRE): {error}")
            VISITED.add(url)
            continue

        response = requests.get(url)

        is_ok, error = is_checkable_post(response)
        if not is_ok:
            print(f"SKIP (POST): {error}")
            VISITED.add(url)
            continue

        VISITED.add(url)

        if response.status_code != 200:
            raise Exception(f"STATUS_CODE == {response.status_code}")

        html = response.text
        print(("VALID" if html5validate.validate(html) is None else "INVALID"))

        links = re.findall(r'([^ ]+)="((?:https?://|/)[^"]+)"', html)
        for attr, link in links:
            link = urljoin(url, link)
            if attr in WHITELISTED_ATTRS:
                # print(f"Adding to queue: {link}")
                QUEUE.append(link)


if __name__ == '__main__':
    main()
