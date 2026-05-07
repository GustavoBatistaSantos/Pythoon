import requests

API_KEY = "AIzaSyAH6Xd00TqT_39URhhOX_rz-Uoq-FvFKMI"
CHANNEL_ID = "UCZKMjUokeTAY1hX_BHCwOlg"

# -----------------------------
# PEGAR PLAYLIST DE UPLOADS
# -----------------------------

url = "https://www.googleapis.com/youtube/v3/channels"

params = {
    "part": "contentDetails",
    "id": CHANNEL_ID,
    "key": API_KEY
}

response = requests.get(url, params=params).json()

uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

print("Playlist de uploads:", uploads_playlist_id)

# -----------------------------
# LISTAR TODOS OS VÍDEOS
# -----------------------------

videos = []
next_page_token = None

while True:

    url = "https://www.googleapis.com/youtube/v3/playlistItems"

    params = {
        "part": "snippet",
        "playlistId": uploads_playlist_id,
        "maxResults": 50,
        "pageToken": next_page_token,
        "key": API_KEY
    }

    response = requests.get(url, params=params).json()

    for item in response["items"]:
        titulo = item["snippet"]["title"]
        videos.append(titulo)

    next_page_token = response.get("nextPageToken")

    if not next_page_token:
        break

# -----------------------------
# MOSTRAR RESULTADO
# -----------------------------

with open("videos.txt", "w", encoding="utf-8") as f:

    for i, titulo in enumerate(videos, start=1):
        f.write(f"{i}. {titulo}\n")

print(f"\nTotal de vídeos: {len(videos)}")
print("Arquivo videos.txt criado com sucesso.")

