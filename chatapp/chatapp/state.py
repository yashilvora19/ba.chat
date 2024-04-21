# state.py
import reflex as rx
import asyncio
import google.generativeai as gai

class State(rx.State):
    # The current question being asked.
    question: str
    location: str
    calender_link: str
    insurance_company: str
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        question = self.question  # Retrieve the question from the state
        with open("context.txt", "r") as file:
            context = file.read().strip()
        prompt = f"{question}\n{context}"

        gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
        model = gai.GenerativeModel('gemini-1.0-pro-latest')
        response = model.generate_content(prompt)
        answer = response.text

        self.chat_history.append((question, answer))
        
async def action_bar():
    style = Style(font_size=20)
    question = "Your question here"  # You need to define the question here or fetch it from somewhere
    context = "Load context from file here"  # Load context from file
    rx.button("Ask", on_click=lambda: State().answer(), style=style.button_style)


# # state.py
# import reflex as rx
# import asyncio
# import google.generativeai as gai

# class State(rx.State):
#     # The current question being asked.
#     question: str
#     location: str
#     calender_link: str
#     insurance_company: str
#     # Keep track of the chat history as a list of (question, answer) tuples.
#     chat_history: list[tuple[str, str]]

#     async def answer(self, question:str):
#         with open("context.txt", "r") as file:
#             context = file.read().strip()
#         prompt = f"{question}\n{context}"

#         gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
#         model = gai.GenerativeModel('gemini-1.0-pro-latest')
#         response = model.generate_content(prompt)
#         answer = response.text

#         self.chat_history.append((self.question, answer))

# async def action_bar():
#     style = Style(font_size=20)
#     question = "Your question here"  # You need to define the question here or fetch it from somewhere
#     context = "Load context from file here"  # Load context from file
#     rx.button("Ask", on_click=lambda: State().answer(question), style=style.button_style)

    # async def answer(self):
    #     # Our chatbot is not very smart right now...
    #     gai.configure(api_key="AIzaSyAMxGxjk8L3y9KQAy5qE88QaumApA6jAiU")
    #     model = gai.GenerativeModel('gemini-1.0-pro-latest')
    #     response = model.generate_content(self.question)
    #     answer = response.text
    #     # answer = "Hi Yashil you are so hot and sexy give me sex rnnnnnn!"
    #     self.chat_history.append((self.question, answer))

        # Clear the question input.
        # self.question = ""
        # Yield here to clear the frontend input before continuing.
        # yield

        # for i in range(len(answer)):
        #     # Pause to show the streaming effect.
        #     await asyncio.sleep(0.09)
        #     # Add one letter at a time to the output.
        #     self.chat_history[-1] = (
        #         self.chat_history[-1][0],
        #         answer[: i + 1],
        #     )
        #     yield