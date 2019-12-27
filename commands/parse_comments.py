import csv
from glob import glob
import frontmatter
from collections import defaultdict

def main():
    post_id_to_filename = {}
    filename_to_comments = defaultdict(lambda: [])

    for filename in sorted(glob("posts/*.md"), reverse=True):
        with open(filename, "r") as f:
            post = frontmatter.load(f)
            post_id_to_filename[post.metadata["id"]] = filename.split(".")[0].replace("posts/", "comments/")

    with open('commands/comments.csv') as csvfile:
        commentreader = csv.DictReader(csvfile, delimiter='\t')

        for comment in commentreader:
            post_id = int(comment["comment_post_ID"])
            if post_id in post_id_to_filename.keys():
                filename = f"{post_id_to_filename[post_id]}_comments.md"
                filename_to_comments[filename] += [comment]

    for filename, comments in filename_to_comments.items():
        comments = frontmatter.Post("", comments=comments)
        with open(filename, "wb") as f:
            frontmatter.dump(comments, f)


if __name__ == '__main__':
    main()
