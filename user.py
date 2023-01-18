import pickle
class UserAPI:

    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, name):
        self.users[name] = {}

    def set_current_user(self, name):
        if name in self.users:
            self.current_user = name
        else:
            print(f"User {name} does not exist.")

    def get_all_users(self):
        return list(self.users.keys())

    def add_event(self, date, event):
        if self.current_user:
            if date not in self.users[self.current_user]:
                self.users[self.current_user][date] = []
            self.users[self.current_user][date].append(event)
        else:
            print("No user selected.")

    def get_events(self, date):
        if self.current_user:
            if date in self.users[self.current_user]:
                return self.users[self.current_user][date]
            else:
                return []
        else:
            print("No user selected.")

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    def load(self):
        with open('user_data.pickle', 'rb') as f:
            user = pickle.load(f)
            return user