# state.py
import reflex as rx
import asyncio
import google.generativeai as gai
from uagents import Bureau
from .user import user  # Imports the user agent configuration
from .gemini_agent import Gemini_agent  # Imports the Gemini agent configuration

class State(rx.State):
    # The current question being asked.
    question: str
    location: str
    calendar_link: str
    insurance_company: str
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):

        # gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
        # model = gai.GenerativeModel('gemini-1.0-pro-latest')

        # with open("chatapp/context.txt", 'r', encoding='utf-8') as file:
        #     context = file.read().strip()
        # prompt = f"{self.question}\n{context}"
        # response = model.generate_content(prompt)
        # answer = response.text
        bureau = Bureau(endpoint="http://127.0.0.1:5000/submit", port=8000)

        bureau.add(Gemini_agent)
        # bureau.add(user)
        bureau.run()
        prompt = self.question
        response = Gemini_agent.handle_message(prompt)
        self.chat_history.append((self.question, response))
        # Clear the question input.
        # self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(response)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.02)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                -self.chat_history[-1][0],
                response[: i + 1],
            )
            yield