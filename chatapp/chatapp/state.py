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
        gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
        # Based on this and any other knowledge that is useful, give them the best way to use their insurance. If you are given this statement 'KEYWORD: HOSPITAL' in the prompt, then simply suggest  10 hospitals based on their location that would be good to visit for diagnosis along with estimated costs. Here
        with open("chatapp/context.txt", 'r', encoding='utf-8') as file:
            context = file.read().strip()

        model = gai.GenerativeModel('gemini-1.5-pro-latest',
                                    system_instruction="You are an assistant that helps people with their health related information. You will be given their location, initial diagnosis, and insurance plan and you will give them an estimate of what their bill should cost (by giving explanations of their tests and procedures and what each will cost with a tally at the end after insurance). Here is the input  that you will get: their diagnosis, location, and details about the insurance plan.")
        if (key == 4):
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + " Here is my question:" + str(self.question) + " Here is our conversation up till now: " + str(self.curr_chat_history)
        else:
            prompt = "Here is my location {self.location}. Here is my insurance plan: " + str(context) + str(self.question) + " Here is our conversation up till now: " + str(self.curr_chat_history)

        response = model.generate_content(prompt)
        answer = response.text
        self.chat_history.append((self.question,answer))
        self.curr_chat_history += "I asked: " + self.question + " \nYou replied: " + answer + "n"

        # Clear the question input.
        # self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.02)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield
            