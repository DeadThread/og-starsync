from plexapi.server import PlexServer

# Configuration
PLEX_URL = 'http://192.168.1.109:32400'
PLEX_TOKEN = 'pi4pvw1pyYurhYsw4mTw'
LIBRARY_NAME = 'Live Music'
TARGET_RATING = 6.0  # 3 stars

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)
music_lib = plex.library.section(LIBRARY_NAME)

# Get all tracks (search with no filters = get all)
print(f"Connecting to '{LIBRARY_NAME}'...")
tracks = music_lib.searchTracks()

print(f"Found {len(tracks)} tracks.")

# Rate each track
for i, track in enumerate(tracks, 1):
    try:
        if track.userRating != TARGET_RATING:
            track.rate(TARGET_RATING)
            print(f"[{i}] Rated: {track.title} - {track.parentTitle}")
        else:
            print(f"[{i}] Skipped (already rated): {track.title}")
    except Exception as e:
        print(f"[{i}] Error rating {track.title}: {e}")

print("✅ All done!")
