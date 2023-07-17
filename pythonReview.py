def create_youtube_video():
    title = input("Enter the title: ")
    description = input("Enter the description: ")
    youtubevideo = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return youtubevideo

def like(youtubevideo):
    if "likes" in youtubevideo:
        youtubevideo["likes"] += 1
    return youtubevideo

def dislike(youtubevideo):
    if "dislikes" in youtubevideo:
        youtubevideo["dislikes"] += 1
    return youtubevideo

def add_comment(youtubevideo, username, comment_text):
    youtubevideo["comments"][username] = comment_text
    return youtubevideo
youtubevideo = create_youtube_video()
like(youtubevideo)
dislike(youtubevideo)
username = input("Enter your username: ")
comment_text = input("Enter your comment: ")
add_comment(youtubevideo, username, comment_text) 
print(youtubevideo)
