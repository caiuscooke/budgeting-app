list_of_players = [
    {
        "name": "John",
        "position": "cornerback",
        "jersey_number": 44,
        "yards_gained": 200,
        "touchdowns": 4,
    }, {
        "name": "Mike",
        "position": "runnerback",
        "jersey_number": 23,
        "yards_gained": 150,
        "touchdowns": 2,
    }, {
        "name": "Paul",
        "position": "quarterback",
        "jersey_number": 44,
        "yards_gained": 6,
        "touchdowns": 0,
    }
]

list_of_players[0]["yards_gained"] += 20
print(list_of_players[0]["yards_gained"])

player_positions_list = []
sum_of_yards = 0
sum_of_touchdowns = 0

for player in list_of_players:
    for stat, stat_value in player.items():
        if stat == "yards_gained":
            sum_of_yards += stat_value
        if stat == "touchdowns":
            sum_of_touchdowns += stat_value
        if stat == "position":
            player_positions_list.append(stat_value)

print(f"Player Positions: {player_positions_list}")

num_of_players = len(list_of_players)

average_yards_gained = sum_of_yards / num_of_players
average_touchdowns = sum_of_touchdowns / num_of_players

print(f"Yards Gained Avg: {average_yards_gained}")
print(f"Touchdowns Avg: {average_touchdowns}")
