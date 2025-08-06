OG Plex StarSync

A simple script that syncs star ratings from your Plex media server to local metadata or external tools.
🎯 Purpose

This utility allows you to automatically or manually export star ratings from live music content in Plex. Useful for music organization workflows involving tools like MusicBrainz Picard or Beets.
🛠 Files

  * plex_rate_live_music.py
    
The main Python script for syncing star ratings from Plex.

  * plex_rate_live_music.bat
    
Optional Windows batch script for launching the sync script easily.

1. Setup
    ```
    Clone the repository:

    git clone https://github.com/DeadThread/og-starsync.git
    ```
2. (Optional) Create a virtual environment:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Install dependencies (if any):
    ```
    pip install -r requirements.txt
    ```
4. Configure the script with your Plex token and library settings (if needed).

▶️ Usage

Double-click the batch file or run the Python script:

python plex_rate_live_music.py

Or:

./plex_rate_live_music.bat

🧠 Notes

You may need to generate a Plex token. See this guide if you're unsure how to get it.

Designed specifically for live music tagging workflows.

📄 License

MIT License. Use freely.