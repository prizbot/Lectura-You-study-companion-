import json
from langchain_groq import ChatGroq

def generate_quiz_questions(input_file: str):
    # Configuration constants defined inside the function
    GROQ_API_KEY = "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"
    OUTPUT_FILE = "quiz_questions.json"
    MODEL_NAME = "llama3-70b-8192"
    TEMPERATURE = 0.4

    # Read the transcript from the input file
    with open(input_file, "r", encoding="utf-8") as f:
        transcription = f.read()

    # Create the Groq client
    chat = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME,
        temperature=TEMPERATURE
    )

    # Build a prompt with strict formatting instructions
    prompt = f"""Generate exactly 5 quiz questions based on this transcript. Follow these rules:
1. Questions only - NO ANSWERS
2. No introductory text
3. One question per line
4. Avoid markdown formatting
5. Focus on key concepts

Transcript:
{transcription[:15000]}  # Truncate if too long

Your response must be exactly 5 questions following this format:
What is...?
How does...?
Why is...?
[Continue with 5 questions]"""

    # Generate the response using the Groq model
    response = chat.invoke(prompt)

    # Process the response: split into lines and filter valid questions
    raw_lines = response.content.split("\n")
    questions = []
    for line in raw_lines:
        cleaned = line.strip()
        if (cleaned and 
            not cleaned.startswith(("Here are", "Answer:", "Q:")) and 
            not cleaned.endswith(":") and 
            len(cleaned) > 15):
            # Remove any numbering (if the line starts with a digit)
            if cleaned[0].isdigit():
                cleaned = cleaned.split(". ", 1)[-1]
            questions.append(cleaned)

    # Ensure exactly 5 questions (truncate if more; warn if less)
    final_questions = questions[:5]
    if len(final_questions) < 5:
        print(f"Warning: Only generated {len(final_questions)} valid questions")

    # Save the questions to a JSON file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"questions": final_questions}, f, indent=2)

    print(f"Successfully saved {len(final_questions)} questions to {OUTPUT_FILE}")
    return final_questions


