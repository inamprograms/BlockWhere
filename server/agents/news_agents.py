from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, tool
import os
from dotenv import load_dotenv
import pandas as pd
from IPython.display import Markdown

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
llm = ChatGroq(temperature=0, model_name="llama3-70b-8192", api_key=GROQ_API_KEY)
search_tool = SerperDevTool(api_key=SERPER_API_KEY)

def create_agent(role, goal, backstory):
    return Agent(
        llm=llm,
        role=role,
        goal=goal,
        backstory=backstory,
        tools=[search_tool],
        allow_delegation=False,
        verbose=True
    )
    
news_planner = create_agent(
    role="News Content Planner",
    goal="Plan and prioritize engaging news content on {topic} for social media posts (LinkedIn, Instagram, Twitter).",
    backstory="You are planning news posts for {topic}, collecting trending information, prioritizing sources, and adjusting tone/formats based on the platform (LinkedIn, Instagram, Twitter). You suggest popular hashtags and formats, and help refine content iteratively based on feedback.",
)
news_writer = create_agent(
    role="News Content Writer",
    goal="Draft a well-structured and engaging news post on {topic} for {platform}, ensuring it aligns with user preferences (LinkedIn, Instagram, or Twitter).",
    backstory="You are writing a news post on {topic} based on the planner's outline. You adjust the tone and format according to the platform's audience and include relevant data and trends. You incorporate platform-specific best practices for engagement.",
)

news_editor = create_agent(
    role="News Content Editor",
    goal="Edit and refine the news post to align with platform-specific requirements and user preferences.",
    backstory="You review the news post, ensuring it follows the platform's best practices, aligns with the brand's voice, and corrects any grammatical errors. You suggest engaging formats and trending hashtags.",
)


def create_task(description, expected_output, agent):
    return Task(description=description, expected_output=expected_output, agent=agent)


plan_news = create_task(
    description=(
        "1. Research the latest news and trends on {topic} from prioritized sources.\n"
        "2. Identify target audiences for the post and analyze their preferences and platform usage.\n"
        "3. Create a detailed outline for a post, including key points, SEO keywords, and suggested hashtags.\n"
        "4. Adjust the tone and format for the selected platform {platform}.\n"
        "5. Suggest popular trends, hashtags, and formats for higher engagement."
    ),
    expected_output="A comprehensive news content plan tailored for the chosen platform {platform} with an outline, trending topics, SEO keywords, suggested hashtags, and sources related to {topic}.",
    agent=news_planner,
)

write_news = create_task(
    description=(
        "1. Use the content plan to draft an engaging news post on {topic} for {platform}.\n"
        "2. Adapt the tone and format based on the platform's specific requirements (LinkedIn, Instagram, Twitter).\n"
        "3. Include relevant data and ensure a strong opening, informative body, and impactful conclusion.\n"
        "4. Integrate trending hashtags and follow best practices for {platform} platform-specific  engagement.\n"
        "5. Make suggestions for iterative refinement based on user feedback (e.g., tone adjustments, focus areas)."
    ),
    expected_output="A well-crafted news post in the format suited for the {platform} platform, including sections with 2-3 paragraphs each and relevant hashtags.",
    agent=news_writer,
)

edit_news = create_task(
    description="Proofread and edit the news post for grammatical accuracy, platform alignment, and optimal brand voice. Suggest trending hashtags or content format enhancements.",
    expected_output="A polished news post formatted for the {platform} platform, ready for publishing, with each section having 2-3 paragraphs and including suggested hashtags.",
    agent=news_editor,
)

crew = Crew(
    agents=[news_planner, news_writer, news_editor], 
    tasks=[plan_news, write_news, edit_news], 
    verbose=True,
    process=Process.sequential
    )

# result = crew.kickoff(inputs={"topic": "What is trading", "platform": "linkedIn"})
# print(result)