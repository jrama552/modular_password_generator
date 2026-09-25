class Profile:
    def __init__(self, account, username, password, tags):
        self.acc = account
        self.user = username
        self.password = password
        self.tags = tags

    def printo(self):
        if self.password == '':
            print(f'{self.acc}\nUsername: {self.user}\nPassword: None\nTags: ', end='')
            for x in self.tags:
                print(x, end='; ')
            print('\n')
        else:
            print(f'{self.acc}\nUsername: {self.user}\nPassword: {self.password}\nTags: ', end='')
            for x in self.tags:
                print(x, end='; ')
            print('\n')


