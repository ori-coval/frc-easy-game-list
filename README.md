# FRC Easy Game List

<strong>Notice:</strong> The project is currently hard-coded with specific team numbers and a starting match number due to time constraints. Future updates will aim to make the script more flexible and broad to accommodate different inputs and use cases.


This Python script is designed to retrieve and list matches for specific FRC (FIRST Robotics Competition) teams from their most recent Championship Division event, starting from a specified match number. The script utilizes The Blue Alliance API to gather event and match data.

## Features

- **Retrieve the latest Championship Division event** for specified FRC teams.
- **Fetch and display matches** for these teams starting from a given match number.
- **Show team participation** in matches along with their divisions.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/frc-easy-game-list.git
    cd frc-easy-game-list
    ```

2. **Install the required packages**:
    The script uses the `requests` library. You can install it using pip:
    ```sh
    pip install requests
    ```

3. **Set up your API key**:
    Create a file named `API_KEY.txt` in the root directory of the project and paste your API key from The Blue Alliance into this file.

## Usage

1. **List of team numbers**:
    Update the list `team_numbers` with the FRC team numbers you are interested in.

2. **Starting match number**:
    Set the `starting_match` variable to the match number from which you want to start listing matches.

3. **Run the script**:
    ```sh
    python frc_easy_game_list.py
    ```

The script will output matches in the format:
