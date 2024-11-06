target = int(input("enter distance: "))
clubs = int(input("enter number of clubs: "))
club_data = []

for i in range(clubs):
    value = int(input(f"Enter club{i} travel distance: "))
    club_data.append(value)
