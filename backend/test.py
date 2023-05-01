from pytube import extract
def extract_id_from_url(youtube_url):
    try:         
        id = extract.video_id(youtube_url)
        print(id)

    except Exception:
        print("sorry")

extract_id_from_url("kdkdk")