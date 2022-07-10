class Student():

    def __init__(self, list_points) -> None:
        self.list_points = list_points

    def find_winners(self, positions: int):
        print(self.list_points[0:positions])

    def find_users_by_percent(self, percent: int):
        pass
