---
author: Emil Stenström
categories:
- Python
- AI
date: 2025-12-03 12:00:00
guid: http://friendlybit.com/python/writing-justhtml-with-coding-agents/
id: 1091
permalink: /python/writing-justhtml-with-coding-agents/
title: 'How I wrote JustHTML using coding agents'
---

I recently released [JustHTML](https://github.com/EmilStenstrom/justhtml), a python-based HTML5 parser. It passes 100% of the html5lib test suite, has zero dependencies, and includes a CSS selector query API. Writing it taught me a lot about how to work with coding agents effectively.

I thought I knew HTML going into this project, but it turns out I know nothing when it comes to parsing broken HTML5 code. That's the majority of the algorithm.

[Henri Sivonen](https://hsivonen.fi/), who implemented the HTML5 parser for Firefox, called the "[adoption agency algorithm](https://html.spec.whatwg.org/multipage/parsing.html#adoption-agency-algorithm)" (which handles misnested formatting elements) "the most complicated part of the tree builder". It involves a "[Noah's Ark](https://html.spec.whatwg.org/multipage/parsing.html#list-of-active-formatting-elements)" clause (limiting identical elements to 3) and complex stack manipulation that breaks the standard stack model.

I still don't know how to solve those problem. But I still have a parser that solves those problems better than the reference implementation [html5lib](https://github.com/html5lib/html5lib-python). Power of AI! :)

## Why HTML5?

When picking a project to build with coding agents, choosing one that already has a lot of tests is a great idea. HTML5 is extremely well-specified, with a long specification and thousands of treebuilder and tokenizer tests available in the [`html5lib-tests`](https://github.com/html5lib/html5lib-tests) repository.

When using coding agents autonomously, you need a way for them to understand their own progress. A complete test suite is perfect for that. The agent can run the tests, see what failed, and iterate until they pass.

## The Journey

Writing a full HTML5 parser is not a short one-shot problem. I have been working on this project for a couple of months on off-hours.

Tooling: I used plain VS Code with Github Copilot in Agent mode. I enabled automatic approval of all commands, and then added a blacklist of commands that I always wanted to approve manually. I wrote an [agent instruction](https://github.com/EmilStenstrom/justhtml/blob/main/.github/copilot-instructions.md) that told it to keep working, and don't stop to ask questions. Worked well!

Here is the 17-step process it took to get here:

### 1. The Naive Start
I asked the agent to write a super-basic one-shot html5 parser. It didn't work very well, but it was a start.

### 2. The Reality Check
I wired up the `html5lib-tests` and saw that we had a <1% pass rate. Yes, those tests are hard. They are the gold standard for HTML5 parsing, containing thousands of edge cases like:

```html
<b><p></b></i>
```

### 3. The Slog
We started iterating, slowly climbing to about 30% pass rate. This involved a lot of refactoring and fixing small bugs.

### 4. The Architecture
I decided I liked a handler-based structure, where each tag gets its own handler. Modular structure ftw! Asked the agent to refactor and it did.

```python
class TagHandler:
    """Base class for all tag handlers."""
    def handle_start(self, context, token):
        pass

class UnifiedCommentHandler(TagHandler):
    """Handles comments in all states."""
    def handle_start(self, context, token):
        context.insert_comment(token.data)
```

### 5. The First Summit
We continued iterating to 100% test coverage. This took a long time, and the [Claude Sonnet 3.7](https://www.anthropic.com/news/claude-3-7-sonnet) release was the reason we got anywhere at all.

### 6. The Speed Bump
I set up [benchmark](https://github.com/EmilStenstrom/justhtml/blob/master/benchmarks/performance.py) to test how fast my parser was. I saw that I was 3x slower than `html5lib`, which is already considered slow.

### 7. The Rust Detour
I let an agent rewrite the tokenizer in Rust to speed things up (Note: I don't know Rust). It worked, and the speed barely passed `html5lib`. It created a whole `rust_tokenizer` crate with 690 lines of Rust code in `lib.rs` that I couldn't read, but it passed the tests.

### 8. The Discovery
I found [`html5ever`](https://github.com/servo/html5ever), [Servo](https://servo.org/)'s parsing engine. It is very correct and written from scratch in Rust to be fast.

### 9. The Existential Crisis
Why would the world need a slower version of `html5ever` in partial Python? What is the meaning of it all?! Almost just deleted the whole project.

### 10. The Pivot
I considered writing a Python interface against `html5ever`, but decided I didn't like the hassle of a library requiring installing binary files. I decided to go pure Python, but with a faster approach: What if I port the `html5ever` logic to Python? Shouldn't that be faster than the existing Python libraries? Decided to throw all previous work away.

### 11. The Restart
I started over from <1% test coverage again and iterated with the same set of tests all the way up to 100%. This time I asked it to cross reference the Rust codebase in the beginning. It was tedious work, doing the same thing over again.

### 12. The Disappointment
I ran the benchmark on the new codebase and found that it was *still* slower than `html5lib`.

### 13. The Optimization
I wrote some new tools for the agents to use: a simple profiler and a scraper that built a dataset of 100k popular webpages for real-workd benchmarking. I managed to get the speed down below the target with Python micro-optimizations, but only when using the just-released Gemini 3 Pro (which is incredible) to run the benchmark and profiler iteratively. No other model made any progress on the benchmarks.

```python
def _append_text_chunk(self, chunk, *, ends_with_cr=False):
    if not chunk:
        self.ignore_lf = ends_with_cr
        return
    if self.ignore_lf:
        if chunk[0] == "\n":
            chunk = chunk[1:]
            # ...
```

### 14. The Cleanup
On a whim I ran [`coverage`](https://coverage.readthedocs.io/) on codebase, and found that large parts of the code was "untested". But this was backwards, because I already knew that the tests were covering everything important. So lines with no test coverage could be removed! Told the agent to start removing code to reach 100% test coverage, which was an interesting reversal of roles. These removals actually sped up the code as much as the microoptimizations.

```python
# Before: 786 lines of treebuilder code
# After: 453 lines of treebuilder code
# Result: Faster and cleaner
```

### 15. The Meeting
After removing code, I got worried that I had removed too much, and missed corner cases. So I asked the agent to write a [html5 fuzzer](https://github.com/EmilStenstrom/justhtml/blob/master/benchmarks/fuzz.py) that tried really hard to generate HTML that broke the parser.

```python
def generate_fuzzed_html():
    """Generate a complete fuzzed HTML document."""
    parts = []
    if random.random() < 0.5:
        parts.append(fuzz_doctype())
    # Generate random mix of elements
    num_elements = random.randint(1, 20)
    # ...
```

It did break the parser, and for each breaking case I asked it to fix it, and write a new test for the test suite. Passed 3 million generated webpages without any crashes, and hardened the codebase again.

### 16. The Validation
I figured I should run the `html5lib` tests against the other parsers, just to understand how our 100% compares.  I found that **no other parser passes 90% coverage**, and that `lxml` one of the most popular python parsers, are at **1%**. The reference implementation, html5lib itself, is at 88%. Maybe this is a hard problem after all?

### 17. The Librarification
To make this a good library I asked the agent to set up CI, releases via github, a [query API](https://github.com/EmilStenstrom/justhtml/blob/master/src/justhtml/selector.py), write README's, and so on.

```python
from justhtml import JustHTML, query

doc = JustHTML("<div><p>Hello</p></div>")
elements = query(doc, "div > p")
```

Decided to rename the library from turbohtml to justhtml, to not fool anyone that it's the fastest library, and instead focus on the feeling of everything just working.

## The Agent's Role vs. My Role

After writing the parser, I still don't know HTML5 properly. The agent wrote it for me. I guided it when it came to API design and corrected bad decisions at the high level, but it did ALL of the gruntwork and wrote all of the code.

I handled all git commits myself, reviewing code as it went in. I didn't understand all the algorithmic choices, but I understood when it didn't do the right thing.

As models have gotten better, I've seen steady increases in test coverage. **Gemini is the smartest model from a one-shot perspective, while Claude Opus is best at iterating its way to a good solution.**

## Tips for working with coding agents

1.  **Start with a clear, measurable goal.** "Make the tests pass" is better than "improve the code."
2.  **Review the changes.** The agent writes a lot of code. Read it. You'll catch issues and learn things.
3.  **Push back.** If something feels wrong, say so. "I don't like that" is a valid response.
4.  **Use version control.** If the agent goes in the wrong direction, you can always revert.
5.  **Let it fail.** Running a command that fails teaches the agent something. Don't try to prevent all errors upfront.

## Was it worth it?

Yes. [JustHTML](https://github.com/EmilStenstrom/justhtml) is about 3,000 lines of Python with 8,500+ tests passing. I couldn't have written it this quickly without the agent.

But "quickly" doesn't mean "without thinking." I spent a lot of time reviewing code, making design decisions, and steering the agent in the right direction. The agent did the typing; I did the thinking.

That's probably the right division of labor.
