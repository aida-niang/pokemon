# Pokémon Game in Python

![preview main](preview.png)

## Project Description

This project is an implementation of a **Pokémon game** using the **Pygame** library. It allows players to capture and battle with Pokémon in an interactive environment. The game includes several features inspired by the famous Pokémon franchise, such as turn-based battles, Pokémon capture mechanics, and a navigable world.

## Demo

Play the game: [Live Demo](https://www.youtube.com/watch?v=qHljZ4D597c&feature=youtu.be)

## 🎮 Features

- **Sound Effects**: Enjoy immersive in-game sound effects.
- **Battle Mechanics**: Engage in turn-based battles with wild Pokémon.
- **Pokémon Capture System**: Catch Pokémon after battles.
- **Health Points Management**: Keep track of your Pokémon’s health during battles.
- **Pokémon Storage**: Manage your Pokémon team and store them in your Pokédex.

## Technologies Used

- **Python**: Main programming language.
- **Pygame**: Library for game development.
- **POKEAPI**: API to collect Pokémon information.
- **JSON**: Used to save Pokémon details like name, health points, level, attack, defense, and type.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- The following Python libraries:
  - `pygame`
  - `requests`
  - `os`
  - `json`
  - `random`

## Installation Steps

1. Clone this repository:
   ```bash
2. Install dependencies:
   ```bash
   pip install pygame requests os json random
   ```

## Usage

Run the game with:
```bash
python3 main.py
```

## Project Structure

```
📂 pokemon-game  
├── 📁 assets/            # Graphics and sound resources  
│   ├── 📁 fonts/         # Fonts used in the game (e.g., for text rendering)  
│   ├── 📁 images/        # Graphics and images for the Pokémon and game world  
│   ├── 📁 sounds/        # Sound effects for different game events (battles, music)  
├── 📁 data/              
│   ├── 📁 sprite/        # Contains sprite files for Pokémon  
│   ├── 📁 .json/         # JSON files storing Pokémon information and game state  
├── battle.py             # Manages the battle logic, including turn-based mechanics  
├── game.py               # Main game logic, handling player movements and interactions  
├── main.py               # Entry point for the game, starts the game loop  
├── menu.py               # Handles menu screens (e.g., start screen, options, etc.)  
├── players.py            # Defines the player class and player-related actions  
├── pokedex.py            # Manages the Pokédex, storing caught Pokémon data  
├── pokemon.py            # Defines the Pokémon class with attributes (name, health, type, etc.)  
├── save_data.json        # JSON file used to save game progress (e.g., captured Pokémon)  
├── settings.py           # Stores game settings (e.g., screen size, game speed, etc.)  
├── utils.py              # Utility functions for sprite loading, data management, etc.  
├── .gitignore            # Files to exclude from version control (e.g., saved game data)  
└── README.md             # Project documentation  

```

## Detailed File Descriptions
- battle.py: Contains the logic for the turn-based battle system, including Pokémon health, move selection, and attack mechanics.
- game.py: The main file managing the game flow, such as player movement, environment interaction, and transitioning between game states.
- main.py: The entry point for the game. This script initializes and starts the game loop.
- menu.py: Manages different menus, such as the start screen, pause menu, and settings screen.
- players.py: Defines the Player class, which tracks player information and actions in the game.
- pokedex.py: Manages the player's Pokédex, which stores information about the Pokémon caught throughout the game.
- pokemon.py: Contains the Pokemon class, defining properties like name, health, level, type, and battle mechanics.
- save_data.json: Stores the player's progress, including captured Pokémon, health stats, and other game-related data.
- settings.py: Includes settings for game configurations such as screen resolution, sound settings, and other customizable options.
- utils.py: Contains helper functions for loading assets, managing Pokémon data, and other utility tasks.
- assets/: Stores all game assets, including fonts, images, and sound effects.
- data/: Contains JSON files used for storing information about the Pokémon, sprites, and game data.

## Contributing

This project was developed by:
- [Aida NIANG](https://github.com/aida-niang/)
- Amina TALEB
- Margaux TROUDE

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to everyone who contributed to the development of this game!

## Built With

- Python 3.8
- Pygame

## Contact

**Aida NIANG** - [LinkedIn](https://linkedin.com/in/aidabenhamathniang) - aidam.niang@gmail.com  
Project Link: [Portfolio](https://aida-niang.students-laplateforme.io)

