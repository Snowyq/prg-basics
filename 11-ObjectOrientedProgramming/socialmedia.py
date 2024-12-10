class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
         print(f"{self.username}")
         for i, post in enumerate(self.posts):
             print(f'{i + 1}. {post}')


profile = SocialMediaProfile('kuba')

profile.add_post('shf;sa')
profile.add_post('sajdfhsvb')

profile.display_timeline()