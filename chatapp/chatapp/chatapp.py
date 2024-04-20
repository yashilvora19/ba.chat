# chatapp.py
import reflex as rx
from chatapp import style
from chatapp.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Your Diagnosis/Questions",
            on_change=State.set_question,
            style=style.input_style,
            variant='soft',
            color_scheme='purple',
            size =10),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to BA.Chat!", size="9"),
            # rx.input(
            #     placeholder="Your Diagnosis",
            # ),
            rx.image(
                src="logo-detailed.png",
                width="400px", 
                height="auto"
            ), 
            rx.input(
                placeholder="Your Location", size =10,
            ),
            rx.input(
                placeholder="Google Calendar", size =10,
            ),
            # insurance_company(),
            rx.select(
                ["UC Ship", "Kiser", "Cigna"],
                color="pink",
                variant="soft",
                radius="full",
                width="50%",
            ),
            chat(),
            action_bar(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
