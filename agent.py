import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from schema import ResumeFeedback

load_dotenv()

model = OpenAIChatModel(
    model_name="openai/gpt-4o-mini",
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENROUTER_API_KEY'),

)

agent = Agent(
    model=model,
    output_type=ResumeFeedback,
    system_prompt=(
        "You are an expert technical recruiter. "
        "Analyze the resume provided. You MUST return a JSON object. "
        "Provide a clarity_score (1-10), ats_score (1-10), "
        "a list of missing_skills, a list of weak_points, and an improved_bullet."
    ),
)
