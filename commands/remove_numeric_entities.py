import re
from glob import glob

import frontmatter

NUMERIC_ENTITY_RE = re.compile(r"&#(\d+);")

def main():
    for filename in sorted(glob("comments/*.md"), reverse=True):
        with open(filename, "r") as f:
            comment_post = frontmatter.load(f)

        comments = comment_post.metadata["comments"]
        new_comments = []
        for comment in comments:
            new_comment = {}
            for field, data in comment.items():
                if data and (match := re.search(NUMERIC_ENTITY_RE, data)):
                    data = re.sub(NUMERIC_ENTITY_RE, lambda m: chr(int(m.group(1))), data)

                new_comment[field] = data

            new_comments.append(new_comment)

        with open(filename, "wb") as f:
            comment_post.metadata["comments"] = new_comments
            frontmatter.dump(comment_post, f)


if __name__ == '__main__':
    main()
