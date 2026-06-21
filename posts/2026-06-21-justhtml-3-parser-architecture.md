---
author: Emil Stenström
categories:
- Python
date: 2026-06-21 12:00:00
guid: http://friendlybit.com/python/justhtml-3-parser-architecture/
id: 1094
permalink: /python/justhtml-3-parser-architecture/
title: 'JustHTML 3.0.0: A new HTML5 parser architecture'
---

JustHTML 3.0.0 is out, and the biggest change is not a new API. It's a new parser core.

Up until now, JustHTML looked like most HTML5 parsers. First tokenize the input, then feed those tokens into a tree builder, and only after that apply the default-safe cleanup that makes untrusted HTML usable in applications.

That's the normal structure. The HTML5 spec itself is written that way. The tokenizer is one state machine, the tree builder is another, and the boundary between them is a stream of tokens: start tags, end tags, text, comments, doctypes, parse errors.

`html5lib`, browser engines, and `html5ever` all broadly follow that shape, even if the details differ a lot.

## What changed in 3.0.0

JustHTML 3.0.0 collapses that split into one plan-driven parser engine.

So instead of scanning characters into token objects, handing those tokens to a second subsystem, and then applying sanitizer decisions as a later pass, the new engine does that work in one loop.

It still implements the same HTML5 concepts: insertion modes, the open-element stack, active formatting elements, foster parenting, fragment parsing, RAWTEXT/RCDATA handling, foreign content rules, and all the other painful details that make browser parsing browser parsing.

But the control flow is different now. The parser scans the source string directly, decides what the current tag means in context, mutates the DOM immediately, and can apply default-safe policy decisions while it is still in the hot path.

This is a real architecture change, not just another round of optimization.

## How it works

The key idea is the word "plan".

Before parsing starts, JustHTML compiles the requested behavior into an `EnginePlan`. There are different plans for the common cases:

- the default safe path
- custom sanitization policies that can be compiled into parser actions
- the raw path used by `sanitize=False` and transform-heavy cases

That plan contains the parser-time decisions that used to be scattered across later steps: tag actions, allowed tags, attribute handling, URL policy hooks, void-element knowledge, formatting-element behavior, and other mode-specific tables.

So the hot path is no longer asking "what should I do with this node later?" It already knows.

In practice the engine now looks more like this:

```python
plan = compile_default_engine_plan(fragment=False)
engine = ParseEngine(html, fragment=False, plan=plan)
root = engine.parse()
```

Inside `parse()`, the engine sets up either a document shell or fragment root, then walks the input with a single range parser. On the fast path it uses specialized start-tag and end-tag parsers for compiled-safe mode, so it avoids building generic token objects and skips the tokenizer-to-treebuilder handoff completely.

Attributes are handled differently too. In the old shape, a tokenizer typically parses all attributes into token payloads, and then the tree builder or sanitizer revisits them. In the new JustHTML engine, attribute scanning can be projected directly through the current plan: preserve what is needed, drop what is not, and keep only the state required for correct tree construction.

That last part matters. HTML parsing is not just "keep the allowed attrs". Some information is needed for parser state even if it will never survive serialization.

## Why this is faster

The 3.0.0 changelog reports about a **2x speedup**, and the reason is not very mysterious.

Traditional parser structure pays several overhead costs:

- token objects have to be allocated
- token payloads have to be normalized and handed off
- the tree builder has to re-interpret information the tokenizer already discovered
- default-safe behavior often becomes a separate tree walk or transform stage

The fused engine removes a lot of that machinery from the common path.

When JustHTML is used in its default mode, the parser can scan characters, recognize a tag, decide whether that tag is allowed, project the interesting attributes, and mutate the DOM immediately. Less indirection, fewer temporary objects, fewer full-tree passes.

This is the kind of optimization that sounds boring until you remember it's happening in Python, where object churn and extra passes cost real time.

## The comparison to other parsers

I still think the standard architecture is the safest place to start.

If you are implementing HTML5 from scratch, tokenizer and tree builder as separate layers is easier to reason about, easier to debug, and closer to the specification. It is also friendlier to test harnesses that want to inspect intermediate token streams.

So I don't think this proves everyone else wrong. `html5ever` and browser parsers are structured the classic way because that structure maps well to the spec and to large codebases with many contributors.

What JustHTML 3.0.0 changes is the tradeoff. It keeps the browser-style recovery model, but stops treating token emission as a required architectural boundary.

That makes JustHTML a bit unusual among HTML parsers. It is still pure Python, still targets exact HTML5 behavior, and still does safe-by-default parsing for application use. But the parser core is now closer to a fused execution engine than a textbook tokenizer plus tree builder pipeline.

I also think this is a better fit for what JustHTML actually is. Most users are not consuming a token stream. They want a correct DOM tree, and often they want it sanitized. If that is the real product, it makes more sense to optimize around that end-to-end job than around intermediate artifacts.

## What did not change

From the outside, this release is pleasantly boring.

`JustHTML(html)` still gives you a DOM. Fragment parsing still works. Streaming, source-location tracking, strict mode, and safe-by-default behavior are still there.

The main breaking change is diagnostics. Since the old tokenizer/tree-builder internals are gone, `collect_errors=True` and `strict=True` now report a smaller, more intentional built-in error set. If you depended on exact error codes, counts, or ordering, you will need to adjust.

Everyone else should mostly experience 3.0.0 as "the same parser, only faster".

That's exactly what I wanted.