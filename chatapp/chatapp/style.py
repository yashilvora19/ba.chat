# style.py
import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="0.5em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="50em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow
)
button_style = dict(
    background_color="purple",
    border_radius="1em",
    box_shadow="rgba(0, 0, 255, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg, #6A0DAD, #00008B 50%, #6A0DAD)",
    box_sizing="border-box",
    color="white",
    opacity=1,
    _hover={
        "opacity": 0.5,
    },
)

