import reflex as rx
from pygments.styles.dracula import background


def section_title(title: str, subtitle: str = "") -> rx.Component:
    return rx.stack(
        rx.heading(title, size="7", weight="bold"),
        rx.text(subtitle, color="gray") if subtitle else rx.box(),
        spacing="2",
        align="start",
        width="100%"
    )

def sticker_card(title: str, body: str):
    return rx.box(
        rx.vstack(
            rx.text(title, weight="bold", size="6"),
            rx.text(body, color="gray", size="2"),
            spacing="2",
            align="start"
        ),
        padding="16px",
        border="2px solid var(--gray-6)",
        border_radius="14px",
        background="var(--gray-1)",
        box_shadow="3px 3px 0px var(--gray-7)",
        width="100%"
    )

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.box(
            rx.vstack(
                rx.heading(
                    "Knockoff",
                    size="9",
                    weight="bold",
                ),
                rx.text(
                    "Pick a closed-source app. Rebuild it open-source. Ship it in 30 days.",
                    size="4",
                    color="gray",
                ),
                rx.text(
                    "steal the idea, not the code.",
                    size="3",
                    color="gray",
                    weight="medium",
                ),
                rx.hstack(
                    rx.button("Start building", size="3", color_scheme="purple"),
                    rx.button("Read rules", size="3", variant="outline"),
                    spacing="3",
                ),
                spacing="4",
                align="start",
                width="100%",
            ),
            width="100%",
            padding="24px",
            border_radius="20px",
            border="2px solid var(--gray-6)",
            background="var(--gray-2)",
            box_shadow="4px 4px 0px var(--gray-7)"
        ),

        rx.vstack(
            section_title("Ground rules", "small constraints so everyone ships."),
            rx.grid(
                sticker_card("Self-hostable", "Anyone should be able to run it themselves"),
                sticker_card("Actually works", "Functional, deployed, and demo-able."),
                sticker_card("30 days", "One month from start to submission."),
                sticker_card("Closed-source inspo", "Build an open-source alternative."),
                columns="2",
                spacing="3",
                width="100%",
            ),
            spacing="4",
            width="100%"
        )
    )


app = rx.App()
app.add_page(index)