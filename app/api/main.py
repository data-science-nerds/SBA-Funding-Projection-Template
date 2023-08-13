from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from textsplitter import split_into_sentences

app = FastAPI()

class Data(BaseModel):
    text: str
    number: float

@app.post("/process_data")
async def process_data(data: Data):
    # Split text using textsplitter
    sentences = split_into_sentences(data.text)

    # Pseudo langchain and pinecone integrations
    # For example, let's assume langchain translates and pinecone processes numbers
    translated_sentences = [f"Translated: {sentence}" for sentence in sentences]
    processed_number = data.number * 2  # Placeholder for pinecone's numeric processing
    
    return {
        "original_text": data.text,
        "translated_sentences": translated_sentences,
        "original_number": data.number,
        "processed_number": processed_number
    }
