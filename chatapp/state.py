import reflex as rx
import asyncio
from gemini_agent import Gemini_agent
from user import user  # Import User class

class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]
    def agents(self):
        self.gemini_agent = Gemini_agent()
        self.user = user()  # Create instance of User

    async def answer(self):
        # Send question to User for interaction
        # user_input = await self.user.get_input(self.question)

        # Send user input to Gemini Agent for processing
        answer = self.agents(self.question)

        # Update chat history with question and answer
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        # Simulate streaming effect for displaying answer
        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.09)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield
