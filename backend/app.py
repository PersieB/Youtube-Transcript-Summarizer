"""
# The project takes the youtube transcript and returns the summarized version (abstractive summarization) using HuggingFace's transformer library
# HuggingFace's Transformers was chosen because it provides us with thousands of pre-trained models not just for text summarization but for a wide
# variety of NLP tasks, such as text classification, text paraphrasing, question answering machine translation, text generation, chatbot, and more.
# The T5 transformer model is going to be used in our abstractive summary
"""

# Importing libraries
from flask import Flask, make_response, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer
from pytube import extract
import json


# define a variable to hold the app
app = Flask(__name__)

# define the resource endpoints
@app.route('/')
def index_page():
    return "Hello world"

# return transcript list as string
def transcript_to_text(transcript_list):
    text = ""
    for i in transcript_list:
        text+=" "+i['text']
    return text



# GLOBAL VARIABLES
# initialize the model architecture and weights
model = T5ForConditionalGeneration.from_pretrained("t5-large")
# initialize the model tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-large")

# Function to summarize text
def summarize_transcript(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors = "pt", max_length = 512, truncation =True )
    outputs = model.generate(inputs, max_length=150, min_length =30,length_penalty = 2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0]) # print summary

# Function to extract video id from youtube url
def extract_id_from_url(youtube_url):
    id = extract.video_id(youtube_url)
    return id


"""
# accept youtube url as an input parameter and return transcript as output
# Extracts the video id from the url and uses it to generate the transcript
"""
@app.route('/api/summarize', methods=['GET'])
def transcript_summary():
    args = request.args
    youtube_url = args.get("youtube_url")  
    try:
        vid_id = extract_id_from_url(youtube_url=youtube_url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id=vid_id)
        summary = summarize_transcript(transcript_to_text(transcript_list=transcript_list))
        return make_response(summary, 200)
    except Exception:
        msg = "Sorry, the youtube url provided cannot be recognised"
        return make_response(msg, 404)


# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True, port=5000)