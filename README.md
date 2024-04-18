# EpicBot-Discord-Bot
Epic Bot is a Discord bot developed in Python to provide users with real-time updates on the weekly free game offerings on the Epic Games Store. This repository contains the source code for the bot, along with documentation and resources for setting up and configuring the bot on Discord servers.


## Setup

1. Clone the repository to your local machine.

2. Install the required dependencies listed in the `requirements.txt` file.

3. Locate the `apikeys.py` file in the root directory of the project.

4. Open the `apikeys.py` file for editing.

5. Modify the placeholders in the `apikeys.py` file with your actual API keys and IDs as follows:

   ```python
   # apikeys.py

   # Discord Bot Token
   BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"

   # Epic Games API Key
   EPIC_GAMES_KEY = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions/'

   # Discord Channel IDs
   BOT_CHANNEL_ID = "YOUR_BOT_CHANNEL_ID_HERE"
   FREE_GAME_CHANNEL_ID = "YOUR_FREE_GAME_CHANNEL_ID_HERE"
   ADMIN_ROLE_ID = "YOUR_ADMIN_ROLE_ID_HERE"
   GATEWAY_LOGS_CHANNEL_ID = "YOUR_GATEWAY_LOGS_CHANNEL_ID_HERE"


## Contributing
Contributions to Epic Bot are welcome! Please follow the contribution guidelines outlined in the repository's CONTRIBUTING.md file.
