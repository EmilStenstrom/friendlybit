from glob import glob

import frontmatter

WHITELISTED_METADATA = [
    "id",
    "title",
    "date",
    "author",
    "guid",
    "permalink",
    "categories",
    "lang",
]

def main():
    for filename in sorted(glob("posts/*.md"), reverse=True):
        with open(filename, "r") as f:
            comment_post = frontmatter.load(f)

        new_metadata = {}
        for field, data in comment_post.metadata.items():
            if field not in WHITELISTED_METADATA:
                continue

            new_metadata[field] = data

        with open(filename, "wb") as f:
            new_comment_post = frontmatter.Post(comment_post.content, **new_metadata)
            frontmatter.dump(new_comment_post, f)


if __name__ == '__main__':
    main()
