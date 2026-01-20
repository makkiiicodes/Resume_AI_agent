from pydantic import BaseModel, Field
from typing import List

class ResumeFeedback(BaseModel):
    clarity_score: int = Field(description="Score from 1-10 on readability", ge=1, le=10)
    ats_score: int = Field(description="Score from 1-10 on ATS optimization", ge=1, le=10)
    missing_skills: List[str] = Field(description="Key technical skills missing for CS roles")
    weak_points: List[str] = Field(description="Areas where the resume lacks impact")
    improved_bullet: str = Field(description="A rewritten, high-impact version of a weak bullet point")