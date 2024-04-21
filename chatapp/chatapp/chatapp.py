# chatapp.py
import reflex as rx
from chatapp import style
from chatapp.state import State

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/logo.png", width="2em"),
            rx.heading("BA.Chat: Basically Affordable", font_family="Roboto, Helvetica, sans-serif", font_size="1.5em"),
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

def sectioning() -> rx.Component:
    return rx.flex(
        rx.section(
            # rx.heading("Section 1"),
            # rx.text("This is the first content section"),
            action_bar(),
            padding_left="12px",
            padding_right="12px",
            background_color="var(--gray-2)",
            width="45vw",
        ),
        rx.divider(orientation="vertical", size="4"),
        rx.flex(
            rx.scroll_area(
                rx.flex(
                    chat(),
                    direction="column",
                    padding_left="12px",
                    padding_right="12px",
                    width="45vw",
                    background_color="var(--gray-2)",
                ),
                type="always",
                scrollbars="vertical",
                style={"height": 660},
            ),
            rx.flex(
                rx.input(
                    value=State.question,
                    placeholder="Any further questions?",
                    on_change=State.set_question,
                    style=style.input_style,
                    variant='soft',
                    color_scheme='bronze',
                    size =10
                ),
                rx.spacer(),
                rx.button("Send", on_click=State.answer, style=style.button_style),
            ),
            direction="column",
        ),
        spacing="4",
        width="80%",
        max_height="80vh",
        align="center",
    )

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.markdown(answer, style=style.answer_style),
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
    return rx.vstack(
        rx.select(
                ["UC Los Angeles", "UC San Diego", "UC Berkeley", "UC Santa Barbara", "UC Riverside", "UC Merced", "UC Santa Cruz", "UC Irvine"],
                placeholder="UC Insurance Provider",
                value=State.location,
                color="#d49d56",
                variant="soft",
                radius="full",
                color_scheme='bronze',
                # width="50%",
            ),
        rx.spacer(),
        rx.input(
            value=State.location,
            placeholder="Your Location",
            # on_change=State.set_question,
            style=style.input_style,
            variant='soft',
            color_scheme='bronze',
            size =10),
        rx.spacer(),
        rx.input(
            value=State.calendar_link,
            placeholder="Calendar Link",
            # on_change=State.set_question,
            style=style.input_style,
            variant='soft',
            color_scheme='bronze',
            size =10),
        rx.spacer(),
        rx.text_area(
            value=State.question,
            placeholder="Your Diagnosis",
            on_change=State.set_question,
            style=style.input_style,
            variant='soft',
            color_scheme='bronze',
            size ="3",
            rows="5",
        ),
        rx.spacer(),
        rx.button("Negotiate Price", on_click=State.answer, style=style.button_style),
        rx.button("Book Appointment", on_click=State.answer, style=style.button_style),
        rx.button("Insurance Analysis", on_click=State.answer, style=style.button_style),
        rx.button("Second Opinion?", on_click=State.answer, style=style.button_style),
        # rx.button("Ask", on_click=State.answer, style=style.button_style),
        spacing="2",
        height="80vh",
    )
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            sectioning(),
            # rx.heading("Welcome to BA.Chat!", size="9"),

            # rx.input(
            #     placeholder="Your Diagnosis",
            # ),

            # rx.image(
            #     src="logo-detailed.png",
            #     width="400px", 
            #     height="auto"
            # ), 

            # rx.input(
            #     placeholder="Your Location", size =10,
            # ),
            # rx.input(
            #     placeholder="Google Calendar", size =10,
            # ),
            # insurance_company(),
            # rx.select(
            #     ["UC Ship", "Kaiser Permanente", "Cigna"],
            #     color="#c4730c",
            #     variant="soft",
            #     radius="full",
            #     width="50%",
            # ),

            # chat(),
            # action_bar(),
            # align="center",
        )
    )


app = rx.App()
app.add_page(index)
