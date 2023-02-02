# Importing libraries
from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer


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

"""
# accept youtube id as an input parameter and return transcript as output
# @app.route('/transcript/<id>/')
"""

def video_transcript(id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(id)
    transcript = trans_in_string(transcript_list=transcript_list)
    return transcript

"""
# takes the youtube transcript and returns the summarized version (abstractive summarization) using HuggingFace's transformer library
# HuggingFace's Transformers was chosen because it provides us with thousands of pre-trained models not just for text summarization but for a wide
# variety of NLP tasks, such as text classification, text paraphrasing, question answering machine translation, text generation, chatbot, and more.
# The T5 transformer model is going to be used in our abstractive summary
"""

def summarise_transcript(youtube_transcript):
    # initialize the model architecture and weights
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    # initialize the model tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base")


# server the app when this file is run
if __name__ == '__main__':
    app.run()