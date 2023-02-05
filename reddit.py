from snscrape.modules import Reddit

reddit = Reddit(
    {
        "resources": ["posts"],
        "posts.query": "python",
        "posts.limit": 100,
    }
)

for post in reddit.get_items():
    print(post.title)