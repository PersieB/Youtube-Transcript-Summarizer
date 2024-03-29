## Objective

In this project, I created a simple web page which will make a request to a backend REST API where it will perform NLP and respond with a summarized version of a YouTube transcript.

## Overview

Enormous number of video recordings are being created and shared on the Internet through out the day. It has become really difficult to spend time in watching such videos which may have a longer duration than expected and sometimes our efforts may become futile if we couldn't find relevant information out of it. Summarizing transcripts of such videos automatically allows us to quickly look out for the important patterns in the video and helps us to save time and efforts to go through the whole content of the video. This project gives me an opportunity to have hands on experience with state of the art NLP technique for abstractive text summarization.

## High-Level Approach

1. Extracting youtube video id from youtube url.
2. Getting transcripts/subtitles for a given YouTube video Id using a Python API.
3. Performing text summarization on obtained transcripts using HuggingFace transformers.
4. Building a Flask backend REST API endpoint to expose the summarization service to the client and testing with Postman.
5. Building a user interface for the api response.
7. Displaying summarized transcript.


## Applications

Meetings and video-conferencing on youtube - A system that could turn voice to text and generate summaries from your team meetings.
Any suggestions? - Feel free to reach out - persiebrown285@gmail.com
