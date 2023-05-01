"""
# The project takes the youtube transcript and returns the summarized version (abstractive summarization) using HuggingFace's transformer library
# HuggingFace's Transformers was chosen because it provides us with thousands of pre-trained models not just for text summarization but for a wide
# variety of NLP tasks, such as text classification, text paraphrasing, question answering machine translation, text generation, chatbot, and more.
# The T5 transformer model is going to be used in our abstractive summary
"""

# Importing libraries
from flask import Flask, make_response, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer
from pytube import extract
import json

# GLOBAL VARIABLES
# initialize the model architecture and weights
model = T5ForConditionalGeneration.from_pretrained("t5-large")
# initialize the model tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-large")

# define a variable to hold the app
app = Flask(__name__)

# define the resource endpoints
@app.route('/')
def index_page():
    return render_template('index.html')

# Helper method: return transcript list as string
def transcript_to_text(transcript_list):
    text = ""
    for i in transcript_list:
        text+=" "+i['text']
    return text

# Helper method: Function to summarize text
def summarize_transcript(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors = "pt", max_length = 512, truncation =True )
    outputs = model.generate(inputs, max_length=150, min_length =30,length_penalty = 2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0]) # print summary

# Helper method: Function to extract video id from youtube url
def extract_id_from_url(youtube_url):
    id = extract.video_id(youtube_url)
    return id


"""
# accept youtube url as an input parameter and return transcript as output
# Extracts the video id from the url and uses it to generate the transcript
"""
def transcript_summary(youtube_url):
    try:
        vid_id = extract_id_from_url(youtube_url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id=vid_id)
        summary = summarize_transcript(transcript_to_text(transcript_list=transcript_list))
        return summary
    except Exception:
        msg = "Sorry, the youtube video cannot be transcribed or the url provided cannot be recognised"
        return msg

@app.route('/api/summarize', methods=['GET'])
def summarizer_api():
    if len(request.args) > 0 and 'youtube_url' in request.args:
        url = request.args['youtube_url']
        return render_template('summarize.html', message = transcript_summary(url))
    return render_template('summarize.html', message = "Kindly specify api request as /api/summarize?youtube_url=<<url>>")


# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True, port=5000)