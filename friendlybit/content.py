from copy import deepcopy
from datetime import datetime
from pathlib import Path

import frontmatter
import pytz

from friendlybit.settings import site
from friendlybit.utils import slugify


def _read_frontmatter(path):
    return frontmatter.loads(path.read_text())


def _load_content():
    timezone = pytz.timezone(site["timezone"])
    posts = []
    posts_by_slug = {}
    posts_by_id = {}
    posts_by_category = {}
    comments_by_slug = {}

    for path in sorted(Path("posts").glob("*.md"), reverse=True):
        post = _read_frontmatter(path)
        post.metadata["date"] = timezone.localize(post.metadata["date"])
        slug = post.metadata["permalink"].rstrip("/").rsplit("/", 1)[-1]

        posts.append(post)
        posts_by_slug[slug] = post
        posts_by_id[post.metadata["id"]] = post
        for category in post.metadata["categories"]:
            posts_by_category.setdefault(slugify(category), []).append(post)

        comments_path = Path("comments") / f"{path.stem}_comments.md"
        if comments_path.exists():
            comment_post = _read_frontmatter(comments_path)
            comments = comment_post.metadata.get("comments", [])
            for comment in comments:
                comment["comment_date"] = datetime.strptime(
                    comment["comment_date"],
                    "%Y-%m-%d %H:%M:%S",
                )
            comments_by_slug[slug] = comments

    contact = _read_frontmatter(Path("pages/contact.md"))
    return {
        "posts": posts,
        "posts_by_slug": posts_by_slug,
        "posts_by_id": posts_by_id,
        "posts_by_category": posts_by_category,
        "comments_by_slug": comments_by_slug,
        "contact": contact,
    }


_CONTENT = _load_content()


def all_posts():
    return deepcopy(_CONTENT["posts"])


def category_posts(category):
    return deepcopy(_CONTENT["posts_by_category"].get(category, []))


def post_by_slug(slug):
    post = _CONTENT["posts_by_slug"].get(slug)
    return deepcopy(post) if post else None


def post_by_id(post_id):
    post = _CONTENT["posts_by_id"].get(post_id)
    return deepcopy(post) if post else None


def comments_for_slug(slug):
    return deepcopy(_CONTENT["comments_by_slug"].get(slug, []))


def contact_page():
    return deepcopy(_CONTENT["contact"])
