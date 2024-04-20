from openai import chat
from rxconfig import config
import reflex as rx

docs_url = "https://www.google.com/search?q=rickroll&oq=rick&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRhAMgYIAhBFGDkyDAgDEAAYQxiABBiKBTIMCAQQABhDGIAEGIoFMg8IBRAuGEMYsQMYgAQYigUyDQgGEC4YgwEYsQMYgAQyDQgHEC4YgwEYsQMYgATSAQgxOTkyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:d7b50f1f,vid:dQw4w9WgXcQ,st:0"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
# def insurance_company() -> rx.Component:
#     return rx.hstack(
#         rx.dropdown(
#             options=["UC Ship", "Kiser", "Cigna"],  # List of insurance company options
#             placeholder="Select your insurance company",
#         ),
#         align="center",
#         spacing="2",
#         font_size="1.2em",
#     )

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to BA.Chat!", size="9"),
            rx.input(
                placeholder="Your Diagnosis",
            ),
            rx.input(
                placeholder="Your Location",
            ),
            rx.input(
                placeholder="Share your Google Calendar",
            ),
            # insurance_company(),
            rx.select(
                ["UC Ship", "Kiser", "Cigna"],
                color="pink",
                variant="soft",
                radius="full",
                width="100%",
            ),
            rx.button(
                "Chat with us!",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_sizing="border-box",
                color="white",
                opacity=1,
                _hover={
                    "opacity": 0.5,
                },
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)