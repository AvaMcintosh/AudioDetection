import asyncio
import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account

@staticmethod
async def aiApproval(ai_key_path, file_1, file_2):
    credentials = service_account.from_service_account_file(ai_key_path)
    vertexai.init(projects="AudioDetectionProject", location="us-central1",credentials=credentials)
    history=[]
    chat=model.start_chat(history=history)
