from glob import glob

import frontmatter

def main():
    for filename in sorted(glob("posts/*.md"), reverse=True):
        with open(filename, "r") as f:
            post = frontmatter.load(f)

        new_metadata = post.metadata.copy()
        new_guid = "http://friendlybit.com" + post.metadata["permalink"]
        if new_guid != new_metadata["guid"]:
            new_metadata["guid"] = new_guid

            with open(filename, "wb") as f:
                new_post = frontmatter.Post(post.content, **new_metadata)
                frontmatter.dump(new_post, f)
                f.write(b"\n")


if __name__ == '__main__':
    main()
