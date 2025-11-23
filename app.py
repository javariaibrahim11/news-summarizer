# -*- coding: utf-8 -*-


import gradio as gr
from transformers import pipeline

# Load summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function
def summarize_text(text):
    if len(text.strip()) == 0:
        return "Please enter some text to summarize."

    result = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return result[0]["summary_text"]

# Gradio UI
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=8, label="Enter News Article"),
    outputs=gr.Textbox(label="Summary"),
    title="📰 AI News Summarizer",
    description="Paste any news article or long text — AI will summarize it!"
)

interface.launch()
