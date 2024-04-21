# chatapp.py
import reflex as rx
from chatapp import style
from chatapp.state import State

def navbar() -> rx.Component:

    return rx.hstack(
        rx.hstack(
            rx.image(src="/new_logo.png", width="7.5em"),
        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        
        rx.flex(
            rx.link("Resources", href="https://myucship.org/",color="white", variant="surface", size="3", _hover={"color": "#ffffff"}),
            rx.link("Documentation", href="https://github.com/yashilvora19/BA.Chat", color="white", variant="surface", size="3", _hover={"color": "#ffffff"}),
            rx.link("Our Team", href="/team", color="white", variant="surface", size="3", _hover={"color": "#ffffff"}),
            rx.link("Vision", href="https://github.com/yashilvora19/BA.Chat/blob/main/README.md", color="white", variant="surface", size="3", _hover={"color": "#ffffff"}),
            spacing="8",
            width="50%",
            align="stretch",
            justify ="between",
        ),
        rx.spacer(),
        rx.spacer(),
        position="center",
        top="0px",
        background_color="#000000",
        color="#443d39",
        padding="1em",
        height="4.5em",
        width="100vw",
        z_index="5",
    )

def sectioning() -> rx.Component:
    return rx.flex(
        rx.section(
            action_bar(),
            padding_left="12px",
            padding_right="12px",
            background_color="#272727",
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
                    background_color="",
                ),
                type="always",
                scrollbars="vertical",
                style={"height": 660},
            ),
            rx.flex(
                rx.input(
                    value=State.question,
                    placeholder="Please type in any further questions here",
                    on_change=State.set_question,
                    style=style.input_style,
                    variant='soft',
                    color_scheme='blue',
                    width="550px"
                ),
                rx.spacer(),
                rx.button("Send", on_click=State.answer(4), style=style.button_style),
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


def footer() -> rx.Component:
    return rx.box(
        rx.text("Ba.chat: Basics, Affordable.", align="left", color="white"),
        background_color="#0000",
        padding="20px",
    )

def action_bar() -> rx.Component:
    return rx.vstack(
        rx.select(
                ["UC Los Angeles", "UC San Diego", "UC Berkeley", "UC Santa Barbara", "UC Riverside", "UC Merced", "UC Santa Cruz", "UC Irvine"],
                placeholder="UC Insurance Provider",
                value=State.location,
                on_change=State.set_location,
                color="#444444",
                variant="classic",
                radius="full",
                width="400px",
            ),
        rx.spacer(),
        rx.input(
            value=State.location_2,
            placeholder="Your Location",
            on_change=State.set_location_2,
            style=style.input_style,
            variant='classic',
            width="400px",
            ),
        rx.spacer(),
        rx.input(
            value=State.calendar_link,
            placeholder="Calendar Link",
            on_change=State.set_calendar_link,
            style=style.input_style,
            variant='classic',
            width="400px"),
        rx.spacer(),
        rx.text_area(
            value=State.question,
            placeholder="Your Diagnosis",
            on_change=State.set_diagnosis,
            style=style.input_style,
            variant='classic',
            width="400px",
            rows="4",
        ),
        rx.spacer(),
        rx.flex(
            rx.button("Insurance Analysis 🏥", on_click=State.answer(0), style=style.button_style),
            rx.button("Schedule Appointment 🗓️", on_click=State.answer(1), style=style.button_style),
            rx.button("Negotiate Price 💰", on_click=State.answer(2), style=style.button_style),
            rx.button("Double Check for Medical Error ⚕", on_click=State.answer(3), style=style.button_style),
            direction="column",
            spacing="4"
        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        spacing="2",
        height="80vh",
        
    ),

    
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            sectioning(),
            footer(),
        )
    )
    


app = rx.App()
app.add_page(index)