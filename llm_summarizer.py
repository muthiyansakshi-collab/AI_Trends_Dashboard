import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary():

    prompt = """
    Give a short summary of current trends in Artificial Intelligence.
    Include OpenAI, Gemini, NVIDIA and Generative AI.
    """

    response = model.generate_content(prompt)

    return response.text