# state.py
import reflex as rx
import asyncio
import google.generativeai as gai

class State(rx.State):
    # The current question being asked.
    question: str
    location: str
    location_2: str
    calendar_link: str
    diagnosis: str
    insurance_company: str
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]
    curr_chat_history: str

    async def answer(self, key):
        college_context_mapping = {
            "UC Los Angeles": "ucla_ship.txt",
            "UC San Diego": "chatapp/ucsd_ship.txt",
            "UC Berkeley": "ucb_ship.txt",
            "UC Irvine": "uci_ship.txt",
            "UC Santa Barbara": "ucsb_ship.txt",
            "UC Santa Cruz": "ucsc_ship.txt",
            "UC Riverside": "ucr_ship.txt",
            "UC Merced": "ucm_ship.txt"
        }

        filename = college_context_mapping[self.location]

        with open(filename, "r", encoding='utf-8') as file:
            context = file.read().strip()
        # context = "you have no context-"
        gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
        # Based on this and any other knowledge that is useful, give them the best way to use their insurance. If you are given this statement 'KEYWORD: HOSPITAL' in the prompt, then simply suggest  10 hospitals based on their location that would be good to visit for diagnosis along with estimated costs. Here

        model = gai.GenerativeModel('gemini-1.5-pro-latest',
                                    system_instruction="You are an assistant that helps people with their health related information. You will be given their location, initial diagnosis, and insurance plan and you will give them an estimate of what their bill should cost (by giving explanations of their tests and procedures and what each will cost with a tally at the end after insurance). Here is the input  that you will get: their diagnosis, location, and details about the insurance plan.")
        if (key == 4):
            print(4)
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + " Here is my question:" + str(self.question) + " Here is our conversation up till now: " + str(self.curr_chat_history) + " Answer my question succintly for simplicity"
        elif (key == 0):
            print(0)
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) +  "Here is our conversation up till now: " + str(self.curr_chat_history)
        elif (key == 1):
            prompt = "just tell me hi. nothing else. just hi"
            print(1)
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) + "I want you to have book a few appointments for me. Can you find availabilities for a the steps I need to take and list out a few available times for each of them. Use my location to find relevant hospitals/health centers and make a table to simplify it for me. Also make sure to keep in mind my insurance plan to maximize my benefit. Please give me the contact number of each place as well. Here is our conversation up till now: " + str(self.curr_chat_history)
        elif (key == 2):
            print(2)
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) + "Draft an email using the cost that I have been given to my insurance company stating that the cost is above the market rate (after looking at market rates) and negotiate the price for me. Make sure to include points from my insurance plan and draft a short succint email stating my name (Yashil Vora) and clear state how my cost can be reduced. Here is our conversation up till now: " + str(self.curr_chat_history)
        elif (key == 3):
            print(3)
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + "Here is my diagnosis: " +str(self.diagnosis) + "You know my prescription and diagnosis. Can you please suggest me whether I need to make a second opinion? Are these the medicines typically given to patients with this issue. If you think there is something ofof/incorrect with my diagnosis or prescription, make sure to alert me about it. Please output whether or not you think a second opinion is needed, why you think so, and give me options and contact information for 2 other healthcare providers (again, keeping in mind my location and insurance plan) in order where I can get a second opinion. Here is our conversation up till now: " + str(self.curr_chat_history)


        response = model.generate_content(prompt)
        answer = response.text
        self.chat_history.append((self.question,answer))
        self.curr_chat_history += "I asked: " + self.question + " \nYou replied: " + answer + "n"

        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.0075)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield
            