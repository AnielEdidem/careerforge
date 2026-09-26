import json
import os
from openai import OpenAI

def generate_cv_content(profile):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {
            "summary": profile.bio or f"Motivated {profile.target_role} with a strong interest in building useful solutions.",
            "experience": profile.experience or "Experience details will appear here."
        }

    client = OpenAI(api_key=api_key)
    prompt = f"""
Create professional CV content from the following candidate information.
Do not invent employers, dates, degrees, achievements, or skills.
Return ONLY valid JSON with keys: summary, experience.
The experience value should be concise bullet-style text.

Name: {profile.full_name}
Target role: {profile.target_role}
Bio: {profile.bio}
Education: {profile.education}
Experience: {profile.experience}
Skills: {profile.skills}
Projects: {profile.projects}
Certifications: {profile.certifications}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a professional CV writer."},
            {"role": "user", "content": prompt},
        ],
    )
    return json.loads(response.choices[0].message.content)
