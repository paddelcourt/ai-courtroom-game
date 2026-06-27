from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.AI_GATEWAY_API_KEY,
    base_url="https://ai-gateway.vercel.sh/v1",
)