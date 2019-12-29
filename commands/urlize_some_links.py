import re
from glob import glob

import frontmatter

URL_NOT_ALREADY_URLIZED = re.compile(r'(?<!\"|\>)(https?:\/\/[^\s\\\"\<]+)(?!\"|\<)')

def main():
    for filename in sorted(glob("comments/*.md"), reverse=True):
        with open(filename, "r") as f:
            comment_post = frontmatter.load(f)

        comments = comment_post.metadata["comments"]
        new_comments = []
        for comment in comments:
            content = comment["comment_content"]
            if re.search(URL_NOT_ALREADY_URLIZED, content):
                comment["comment_content"] = re.sub(
                    URL_NOT_ALREADY_URLIZED,
                    '<a href="\\1" rel="nofollow">\\1</a>',
                    content
                )

            new_comments.append(comment)

        with open(filename, "wb") as f:
            comment_post.metadata["comments"] = new_comments
            frontmatter.dump(comment_post, f)


if __name__ == '__main__':
    main()
