## Objective

In this project, I will be a creating a Chrome Extension which will make a request to a backend REST API where it will perform NLP and respond with a summarized version of a YouTube transcript.

## Overview

Enormous number of video recordings are being created and shared on the Internet through out the day. It has become really difficult to spend time in watching such videos which may have a longer duration than expected and sometimes our efforts may become futile if we couldn't find relevant information out of it. Summarizing transcripts of such videos automatically allows us to quickly look out for the important patterns in the video and helps us to save time and efforts to go through the whole content of the video. This project will give us an opportunity to have hands on experience with state of the art NLP technique for abstractive text summarization and implement an interesting idea suitable for intermediates and a refreshing hobby project for professionals.

## High-Level Approach

1. Get transcripts/subtitles for a given YouTube video Id using a Python API.
2. Perform text summarization on obtained transcripts using HuggingFace transformers.
3. Build a Flask backend REST API to expose the summarization service to the client.
4. Develop a chrome extension which will utilize the backend API to display summarized text to the user.

## Project Stages

1. Open a Youtube Video and Click on Summarize in Chrome Extension to create a HTTP request to the back-end.
2. Request Transcript for a given youtube video id
3. Return Transcript for a video id as a HTTP response
4. Perform Transcript Summarization and return it as a HTTP response
5. Display summarized transcript on the extension

## Applications

Meetings and video-conferencing - A system that could turn voice to text and generate summaries from your team meetings.
Patent research - A summarizer to extract the most salient claims across patents.