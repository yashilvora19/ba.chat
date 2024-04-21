# state.py
import reflex as rx
import asyncio
import google.generativeai as gai
import base64
from email.message import EmailMessage
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class State(rx.State):
    # The current question being asked.
    question: str
    location: str
    location_2: str
    email: str
    diagnosis: str
    insurance_company: str
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]
    curr_chat_history: str

    # def gmail_create_draft(to_email, from_email, subject, content):
    #     creds, _ = google.auth.default()

    #     try:
    #         # create gmail api client
    #         service = build("gmail", "v1", credentials=creds)

    #         message = EmailMessage()

    #         message.set_content(content)

    #         message["To"] = to_email
    #         message["From"] = from_email
    #         message["Subject"] = subject

    #         # encoded message
    #         encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    #         create_message = {"message": {"raw": encoded_message}}
    #         # pylint: disable=E1101
    #         draft = (
    #             service.users()
    #             .drafts()
    #             .create(userId="me", body=create_message)
    #             .execute()
    #         )

    #         # print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    #     except HttpError as error:
    #         print(f"An error occurred: {error}")
    #         draft = None

    #     return draft


    async def answer(self, key):
        college_context_mapping = {
                "UC Los Angeles": "chatapp/ucla_ship.txt",
                "UC San Diego": "chatapp/ucsd_ship.txt",
                "UC Berkeley": "chatapp/ucb_ship.txt",
                "UC Irvine": "chatapp/uci_ship.txt",
                "UC Santa Barbara": "chatapp/ucsb_ship.txt",
                "UC Santa Cruz": "chatapp/ucsc_ship.txt",
                "UC Riverside": "chatapp/ucr_ship.txt",
                "UC Merced": "chatapp/ucm_ship.txt"
        }

        filename = college_context_mapping[self.location]

        with open(filename, "r", encoding='utf-8') as file:
            context = file.read().strip()
        # context = "you have no context-"
        gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
        # Based on this and any other knowledge that is useful, give them the best way to use their insurance. If you are given this statement 'KEYWORD: HOSPITAL' in the prompt, then simply suggest  10 hospitals based on their location that would be good to visit for diagnosis along with estimated costs. Here

        model = gai.GenerativeModel('gemini-1.5-pro-latest',
                                    system_instruction="You are a healthcare insurance advisor, please help the user with the diagnoses and maximising their insurance . You will be given their location, initial diagnosis, and insurance plan and you will give them an estimate of what their bill should cost (by giving explanations of their tests and procedures and what each will cost with a tally at the end after insurance). Here is the input  that you will get: their diagnosis, location, and details about the insurance plan.")
        if (key == 4):
            print(4)
            prompt = "Here is my location: " + str(self.location) + "Here is my insurance plan: " + str(context) + " Here is my question:" + str(self.question) + " Here is our conversation up till now: " + str(self.curr_chat_history) + " Answer my question succintly for simplicity"
        elif (key == 0):
            print(0)
            prompt = "Here is my location: " + str(self.location) + "Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) +  "Analyze my diagnosis and suggest how I can maximize my insurance to minimize my cost and save me time. Keep in mind my location and insurance plan and find niche places that I might miss out on or where I may have not read the fine print to maximize my benefit. Also give me a brief table of the tests/procedures along with their associated costs and a total estimated cost at the end. Make sure to get all of these points, write your answer to the point, and be concise. Here is our conversation up till now: " + str(self.curr_chat_history)
        elif (key == 1):
            print(1)
            prompt = "Here is my location: " + str(self.location) + "Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) + "I want you to have book a few appointments for me. Can you find availabilities for a the steps I need to take and list out a few available times for each of them. Use my location to find relevant hospitals/health centers and make a table to simplify it for me. Also make sure to keep in mind my insurance plan to maximize my benefit. Please give me the contact number of each place as well. Here is our conversation up till now: " + str(self.curr_chat_history)
        elif (key == 2):
            print(2)
            prompt = "Here is my location: " + str(self.location) + "Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) + "Draft an email using the cost that I have been given to my insurance company stating that the cost is above the market rate (after looking at market rates) and negotiate the price for me. Make sure to include points from my insurance plan and draft a short succint email stating my name (Yashil Vora) and clear state how my cost can be reduced. Here is our conversation up till now: " + str(self.curr_chat_history)
        elif (key == 3):
            print(3)
            prompt = "Here is my location: " + str(self.location) + "Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) + "You know my prescription and diagnosis. Can you please suggest me whether I need to make a second opinion? Are these the medicines typically given to patients with this issue. If you think there is something incorrect with my diagnosis or prescription, make sure to alert me about it. Please output whether or not you think a second opinion is needed, why you think so, and give me options and contact information for 2 other healthcare providers. Again, keeping in mind my location and insurance plan suggest where I can get a second opinion. Here is our conversation up till now: " + str(self.curr_chat_history)


        response = model.generate_content(prompt)
        if key == 2:
            answer = response.text + "\n **A draft of this email has been created in your email account. Please review it and send it to your insurance provider.**"
        else:
            answer = response.text
        self.chat_history.append((self.question,answer))
        self.curr_chat_history += "I asked: " + self.question + " \nYou replied: " + answer + "n"
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.001)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield
        # gmail_create_draft("yvora@ucsd.edu", "mjethwani@ucsd.edu", "Negotiation of patient charges- Yashil Vora", answer)
        