# chatapp.py
import reflex as rx
from chatapp import style
from chatapp.state import State

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/logo.png", width="2em"),
            rx.heading("Welcome to BA.Chat!", font_family="Roboto, Helvetica, sans-serif", font_size="1.5em"),
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Use our Chatbot", font_family="Roboto, Helvetica, sans-serif", font_size="1em"),
            ),
        ),
        position="sticky",
        top="0px",
        background_color="#04507d",
        color="white",
        padding="1em",
        height="4em",
        width="100vw",
        z_index="5",
    )

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
            navbar(),
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
                ["UC Ship", "Kaiser Permanente", "Cigna"],
                color="#c4730c",
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
