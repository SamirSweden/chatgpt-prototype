import os
import logging
import openai
from http.client import HTTPException



openai.api_key = os.getenv("TOKEN") # ! ur token must be in .env file , do not put token in  code 

logger = logging.getLogger(__name__)

async def ask_bot(prompt: str):
    try:
        resp = await openai.Completion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}],
            temperature=0.7,
            streaming=True,
        )

        return resp.choices[0].message.content
    except Exception as e:

        logger.error(f"Error: {e}" , exc_info=True)

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error. Обратитесь в поддержку."
        )
