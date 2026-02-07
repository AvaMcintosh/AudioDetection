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
    with open(file_1, "rb") as f1, open(file_2, "rb") as f2:
        audio1_data = f1.read()
        audio2_data = f2.read()
    audio1 = Part.from_data(data=audio1_data, mime_type="audio/wav")
    audio2 = Part.from_data(data=audio2_data, mime_type="audio/wav")
    chat = model.start_chat(history=history)
    # img1 = Part.from_image(Image.load_from_file(file_1))
    # img2 = Part.from_image(Image.load_from_file(file_2))
    # prompt = [
    #     "Please compare these two images of sound waves (spectrograms/waveforms). "
    #     "Analyze their patterns, frequency distribution, and amplitude. "
    #     "Please output a similarity score based on how similar the two look based off frequency and magnitude. and only the similarity score",
      
    # ]

    prompt = """
        Task: Audio Similarity Analysis for Notification Trigger.

        Input A: Template sound (target).
        Input B: Real-time recorded environment sound.

        Instructions:
        1. Extract the spectral envelope and fundamental frequency of Input A.
        2. Search for a matching signature within Input B.
        3. Ignore static background noise (hiss, hum) and normalize for volume differences.
        4. Focus on the 'Attack, Decay, Sustain, and Release' (ADSR) profile of the sounds.
        5. Prioritize Frequency in your comparisions

        Output Requirement:
        If the core sound in Input B is a 90% match or higher to Input A, output 'MATCH: [score]'. 
        Otherwise, output 'NO_MATCH: [score]'.
        
        """
    # response = await chat.send_message_async(prompt)
    response = await model.generate_content_async([prompt, audio1, audio2])
    cleaned_response= response.text.strip()
    print (cleaned_response)


async def main():
    akp = ".env/gen-lang-client-0827930295-96dccb33fbb4.json"
    image1 = 'src/CarHonk.png'
    image2 = 'src/recordedHonk.png'
    audio1 = 'src/CarHonk1.wav'
    audio2 = "src/HELLO.wav"
    await aiApproval(akp, audio1, audio2)


if __name__ == "__main__":
    asyncio.run(main())