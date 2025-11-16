import os
import httpx
from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from typing import List
# from langchain.document_loaders import DirectoryLoader
# from langchain.schema import Document

# DATA_PATH = "data"

# # Load environment variables from .env file
# load_dotenv()

# def load_documents() -> List[Document]:
#     loader = DirectoryLoader(DATA_PATH, glob="*.pdf")
#     documents = loader.load()
#     return documents


app = FastAPI()


@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}


@app.get("/chat")
async def chat() -> Dict[str, str]:
    return {"res": "working api connection"}


class EmbedRequest(BaseModel):
    msg: str


class EmbedResponse(BaseModel):
    vector: List[float]


@app.post("/vecter")
async def vecter(request: EmbedRequest) -> EmbedResponse:
    # Load environment variables
    load_dotenv()

    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        # Create embedding using OpenAI API
        response = client.embeddings.create(
            model="text-embedding-ada-002", input=request.msg
        )

        # Extract the vector from the response
        vector = response.data[0].embedding

        return EmbedResponse(vector=vector)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error creating embedding: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003)
