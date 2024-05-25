import requests

# Read the API key from the API_KEY.txt file
with open('API_KEY.txt', 'r') as file:
    API_KEY = file.read().strip()

def get_last_event_for_team(team_number):
    headers = {'User-Agent': 'Mozilla/5.0', 'X-TBA-Auth-Key': API_KEY}
    url = f"https://www.thebluealliance.com/api/v3/team/frc{team_number}/events/2024"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json()
        for event in reversed(events):
            if event['event_type'] == 3:  # Only consider Championship Division events
                return event
    return None

def get_event_division(event_key):
    headers = {'User-Agent': 'Mozilla/5.0', 'X-TBA-Auth-Key': API_KEY}
    url = f"https://www.thebluealliance.com/api/v3/event/{event_key}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        event_data = response.json()
        division = event_data.get('short_name', 'Unknown Division')
        return division
    return 'Unknown Division'

def get_matches_for_event(event_key):
    headers = {'User-Agent': 'Mozilla/5.0', 'X-TBA-Auth-Key': API_KEY}
    url = f"https://www.thebluealliance.com/api/v3/event/{event_key}/matches"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def get_matches_with_team(team_numbers, starting_match):
    matches_with_team = {}
    for team_number in team_numbers:
        last_event = get_last_event_for_team(team_number)
        if last_event:
            event_key = last_event['key']
            division = get_event_division(event_key)
            matches = get_matches_for_event(event_key)
            if matches:
                for match in matches:
                    match_number = match['match_number']
                    if match_number >= starting_match:
                        blue_teams = [team.split('frc')[1] for team in match['alliances']['blue']['team_keys']]
                        red_teams = [team.split('frc')[1] for team in match['alliances']['red']['team_keys']]
                        if str(team_number) in blue_teams or str(team_number) in red_teams:
                            if match_number not in matches_with_team:
                                matches_with_team[match_number] = {'teams': [], 'division': division}
                            matches_with_team[match_number]['teams'].append((team_number, division))
    return matches_with_team

def print_matches_with_team(matches_with_team):
    for match_number, data in sorted(matches_with_team.items()):
        team_division_pairs = data['teams']
        division = data['division']
        team_str_list = []
        for team_number, team_division in team_division_pairs:
            team_str_list.append(f"{team_number} ({team_division})")
        teams_str = ", ".join(team_str_list)
        print(f"Match {match_number}: {teams_str}")

# List of team numbers
team_numbers = [3339, 1690, 4414, 1678, 254, 1323, 2056, 118]
starting_match = 40

matches_with_team = get_matches_with_team(team_numbers, starting_match)
print_matches_with_team(matches_with_team)
