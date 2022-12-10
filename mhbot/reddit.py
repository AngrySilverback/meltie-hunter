import praw

class MeltieHunter(praw.Reddit):

    def __init__(self):

        super().__init__('MeltieHunterBot')
        self.stream_superstonk()

    def get_meltie_comments(self, username):

        comments = []

        user = self.redditor(str(username))
        for comment in user.comments.new(limit=1000):
            if str(comment.subreddit) == 'gme_meltdown':
                comments.append(comment)

        return comments

    def handle_common(self, obj, kind):

        if obj is None:
            return

        meltie_comments = self.get_meltie_comments(obj.author)
        if len(meltie_comments) > 0:
            print('\n=========================================================\n')

            if kind == 'comment':
                print('Superstonk comment by:', obj.author, '(MELTIE USER)')
            if kind == 'submission':
                print('Superstonk submission by:', obj.author, '(MELTIE USER)')

            for meltie_comment in meltie_comments:
                print('\nMELTDOWN COMMENT:')
                print(meltie_comment.body)

    def stream_superstonk(self):

        subreddit   = self.subreddit('Superstonk')
        comments    = subreddit.stream.comments(pause_after=-1)
        submissions = subreddit.stream.submissions(pause_after=-1)

        while True:
            for comment in comments:
                self.handle_common(comment, 'comment')
            for submission in submissions:
                self.handle_common(submission, 'submission')
