from google.adk import Agent
from summarizer_agent.tools import summarize_text_tool

summarizer_agent = Agent(
    name="SummarizerAgent",
    model='gemini-2.0-flash',
    description="You are an AI assistant that summarizes text or pdf's uploaded by users into clear and concise summaries. Use the summarize_text_tool to generate summaries."
    "Only return the summary and nothing else.",
    tools=[summarize_text_tool],
)