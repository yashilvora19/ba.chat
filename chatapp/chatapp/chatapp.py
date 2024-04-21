# chatapp.py
import reflex as rx
from chatapp import style
from chatapp.state import State

def navbar() -> rx.Component:

    return rx.hstack(
        rx.hstack(
            rx.image(src="/new_logo.png", width="7.5em"),
            # rx.heading("BA.Chat", font_family="Exo", font_size="2em", color="white"),
            # rx.cardrx.card("Basics. Affordable.", color="black", variant="surface", size="1")
        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        
        rx.flex(
            rx.card("Resources", color="black", variant="surface", size="1",  _hover={"color": "#ffffff", "border" : "DDDDDD"}),
            rx.card("Documentation", color="black", variant="surface", size="1",  _hover={"color": "#ffffff", "border" : "DDDDDD"}),
            rx.card("Mission", color="black", variant="surface", size="1",  _hover={"color": "#ffffff", "border" : "DDDDDD"}),
            rx.card("Our Team", color="black", variant="surface", size="1",  _hover={"color": "#ffffff", "border" : "DDDDDD"}),
            spacing="8",
            width="50%",
            align="stretch",
            justify ="between",

    ),
    rx.spacer(),
    rx.spacer(),
        

        # rx.spacer(),
        # rx.button("Our Vision", font_family="DM Sans", font_size="1em", color_scheme="bronze", align="center"),
        # rx.button("Our Team", font_family="DM Sans", font_size="1em", color_scheme="bronze", align="center"),
        # rx.button("Documentation", font_family="DM Sans", font_size="1em", color_scheme="bronze", align="center"),
        # ),
        position="center",
        top="0px",
        background_color="#000000",
        color="#443d39",
        padding="1em",
        height="5em",
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
                    width="450px"
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
            on_change=State.set_location,
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
