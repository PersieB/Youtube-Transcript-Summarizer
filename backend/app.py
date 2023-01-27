from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi

# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"

# return transcript list as string
def trans_in_string(transcript_list):
    text = ""
    for i in transcript_list:
        text+=" "+i['text']
    return text

# accept youtube id as an input parameter and return transcript as output
# @app.route('/transcript/<id>/')
def video_transcript(id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(id)
    transcript = trans_in_string(transcript_list=transcript_list)
    return transcript



# server the app when this file is run
if __name__ == '__main__':
    app.run()