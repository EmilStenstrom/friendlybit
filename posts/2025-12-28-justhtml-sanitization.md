---
author: Emil Stenström
categories:
- Python
- Security
date: 2025-12-28 12:00:00
guid: http://friendlybit.com/python/justhtml-sanitization/
id: 1093
permalink: /python/justhtml-sanitization/
title: "JustHTML is now safe-by-default"
---

If you accept HTML from users (comments, profiles, CMS fields), you eventually hit the same problem:

- You want to keep *some* markup.
- You really don’t want to ship an [XSS](https://learn.snyk.io/lesson/xss/?ecosystem=javascript).

That’s why JustHTML now includes a built-in, policy-driven HTML sanitizer, and why serialization is **safe-by-default**.

## Safe-by-default serialization

JustHTML sanitizes when you serialize to HTML or Markdown:

```python
from justhtml import JustHTML

user_html = (
    '<p>Hello <b>world</b> <script>alert(1)</script> '
    '<a href="javascript:alert(1)">bad</a> '
    '<a href="https://example.com/?a=1&b=2">ok</a></p>'
)

doc = JustHTML(user_html, fragment=True)

print(doc.to_html())
print()
print(doc.to_markdown())
```

This drops `<script>` and strips dangerous URLs:

```html
<p>Hello <b>world</b>  <a>bad</a> <a href="https://example.com/?a=1&amp;b=2">ok</a></p>
```

```markdown
Hello **world** [bad] [ok](https://example.com/?a=1&b=2)
```

## Turning it off (trusted input only)

If the input is trusted and you want raw output, you can opt out:

```python
print(doc.to_html(safe=False))
print(doc.to_markdown(safe=False))
```

## Custom allowlist policies

The default policy is intentionally conservative, but you can provide your own `SanitizationPolicy`.
Here’s a small example that only allows `p`, `b`, and `a[href]`, and only allows `https` links:

```python
from justhtml import JustHTML, SanitizationPolicy, UrlRule

policy = SanitizationPolicy(
    allowed_tags=["p", "b", "a"],
    allowed_attributes={"*": [], "a": ["href"]},
    url_rules={
        ("a", "href"): UrlRule(allowed_schemes=["https"]),
    },
)

doc = JustHTML(user_html, fragment=True)
print(doc.to_html(policy=policy))
```

If you’re sanitizing a full document, safe serialization keeps `<html>`, `<head>`, and `<body>` wrappers.
For snippets, pass `fragment=True` to avoid implicit document wrappers.

There are also a couple of knobs that tend to show up in real systems:

- URL proxying (for example, rewriting `https://example.com/…` to `/proxy?url=…`)
- Optional inline styles, with an allowlist of CSS properties and conservative value checks

## Why I built `justhtml-xss-bench`

If you’ve worked on sanitizers before, you know the hard part isn’t writing a policy — it’s knowing what the browser will actually do with the result.

So I built a tiny benchmark harness: `[justhtml-xss-bench](https://github.com/EmilStenstrom/justhtml-xss-bench/)`.

What it does:

- Takes a payload vector and a sanitizer.
- Sanitizes the payload.
- Embeds the sanitized output into the initial HTML page ("server-side" style).
- Loads it in a real Playwright browser engine.
- Fails the case if JavaScript executes (including signals like dialogs or attempted external script fetches).

It ships with **7,000+ real-world XSS vectors** and can be used to compare JustHTML’s output with other sanitizers.

If you want to explore it locally, the CLI looks like this:

```bash
# Run all vector files in ./vectors against the default sanitizer set
xssbench

# Limit to one engine
xssbench --browser chromium

# List available sanitizers
xssbench --list-sanitizers

# Run a subset
xssbench --vectors vectors/bleach.json --sanitizers noop
```

## Threat model (what “safe” means)

JustHTML’s sanitizer aims to prevent script execution when you sanitize untrusted HTML and embed the result into an HTML document as markup.

It does *not* make it safe to drop the output into JavaScript string contexts, CSS contexts, URL contexts, or other non-HTML contexts — those need their own escaping/handling.

If you want the details, see the JustHTML sanitization documentation:

- https://github.com/EmilStenstrom/justhtml/blob/master/docs/sanitization.md

And the benchmark harness repo:

- https://github.com/EmilStenstrom/justhtml-xss-bench
