import asyncio
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image
from google.oauth2.service_account import Credentials 

@staticmethod
async def aiApproval(ai_key_path, file_1, file_2):
    credentials = Credentials.from_service_account_file(ai_key_path)
    vertexai.init(project="gen-lang-client-0827930295", location="us-central1",credentials=credentials)
    history=[]
    model=GenerativeModel("gemini-2.0-flash-001")
    chat = model.start_chat(history=history)
    img1 = Part.from_image(Image.load_from_file(file_1))
    img2 = Part.from_image(Image.load_from_file(file_2))
    prompt = [
        "Please compare these two images of sound waves (spectrograms/waveforms). "
        "Analyze their patterns, frequency distribution, and amplitude. "
        "Please output a similarity score based on how similar the two look based off frequency and magnitude.",
        img1, 
        img2
    ]
    response = await chat.send_message_async(prompt)
    cleaned_response= response.text.strip()
    print (cleaned_response)


async def main():
    akp = ".env/gen-lang-client-0827930295-96dccb33fbb4.json"
    image1 = 'src/CarHonk.png'
    image2 = 'src/recordedHonk.png'
    await aiApproval(akp, image1, image2)


if __name__ == "__main__":
    asyncio.run(main())