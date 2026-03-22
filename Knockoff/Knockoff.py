import reflex as rx


def section_title(title: str, subtitle: str = "") -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="8", weight="bold"),
        rx.text(subtitle, color="gray", size="3") if subtitle else rx.fragment(),
        spacing="1",
        align="start",
        width="100%"
    )

def prize_row(name: str, points: str, desc: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(points, weight="bold", size="3", white_space="nowrap"),
            padding="6px 12px",
            border_radius="999px",
            background="var(--purple-3)",
            border="1.5px solid var(--purple-6)"
        ),
        rx.vstack(
            rx.text(name, weight="bold", size="3"),
            rx.text(desc, color="gray", size="2"),
            spacing="1",
            align="start"
        ),
        spacing="3",
        align="center",
        width="100%",
        padding="12px 0",
        border_bottom="1px dashed var(--gray-5)",
    )


def example_chip(closed: str, open_alt: str) -> rx.Component:
    return rx.hstack(
        rx.text(closed, weight="bold", size="3"),
        rx.text("→", size="3", color="gray"),
        rx.text(open_alt, weight="bold", size="3", color="var(--purple-9)"),
        spacing="2",
        align="center",
        padding="10px 16px",
        border="1.5px solid var(--gray-5)",
        border_radius="10px",
        background="var(--gray-1)",
    )

def step_item(number: str, title: str, desc: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(number, weight="bold", size="5", color="white"),
            width="44px",
            height="44px",
            display="flex",
            align_items="center",
            justify_content="center",
            border_radius="12px",
            background="var(--purple-9)",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(title, weight="bold", size="4"),
            rx.text(desc, color="gray", size="2"),
            spacing="1",
            align="start",
        ),
        spacing="3",
        align="start",
        width="100%",
    )

def faq_item(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.el.details(
            rx.el.summary(
                rx.text(question, weight="bold", size="3", cursor="pointer")
            ),
            rx.text(answer, color="gray", size="2", padding_top="8px")
        ),
        padding="16px",
        border="1.5px solid var(--gray-5)",
        border_radius="12px",
        width="100%"
    )

def rule_card(emoji: str, title: str, body: str):
    return rx.box(
        rx.vstack(
            rx.text(emoji, size="7"),
            rx.text(title, weight="bold", size="5"),
            rx.text(body, color="gray", size="2"),
            spacing="2",
            align="start"
        ),
        padding="20px",
        border="2px solid var(--gray-6)",
        border_radius="14px",
        background="var(--gray-7)",
        _hover={
            "transform": "translate (-2px,-2px)",
            "box_shadow": "6px 6px 0px var(--gray-8)"
        },
        transition="all 0.15s ease",
        width="100%"
    )

def index() -> rx.Component:
    # ... existing code ...
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("🏴‍☠️", size="8"),
                        rx.heading("Knockoff", size="9", weight="bold"),
                        align="center",
                        spacing="3"
                    ),
                    rx.text(
                        "Pick a closed-source app. Rebuild it open-source. Ship it in 30 days.",
                        size="5",
                        color="gray",
                        max_width="540px"
                    ),
                    rx.text(
                        "steal the idea, not the code.",
                        size="3",
                        color="var(--purple-9)",
                        weight="medium",
                        font_style="italic"
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button("🚀 Start building", size="3", color_scheme="purple", cursor="pointer"),
                            href="#how-to-submit",
                        ),
                        rx.link(
                            rx.button("📖 Read rules", size="3", variant="outline", cursor="pointer"),
                            href="#rules",
                        ),
                        spacing="3",
                    ),
                    rx.text("a Hack Club YSWS", size="2", color="gray"),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
                width="100%",
                padding="32px 24px",
                border_radius="20px",
                border="2px solid var(--gray-6)",
                background="var(--gray-2)",
                box_shadow="5px 5px 0px var(--gray-7)"
            ),

            rx.vstack(
                section_title("What's the deal?"),
                rx.box(
                    rx.text(
                        "Knockoff is a a ",
                        rx.text.strong("You Ship, We Ship"),
                        " program. You build something cool -> we give you cool stuff. "
                        "Specifically: pick any closed-souce product (Notion, Figma, Discord, whatever). ",
                        "Build a legit open-souce alternative that people can actually use and self-host "
                        "and earn points you can spend in our prize shop.",
                        size="3",
                        line_height="1.7"
                    ),
                    spacing="3",
                    width="100%"
                )
            ),

            rx.vstack(
                section_title("Ground Rules", "small constraints so everyone ships"),
                rx.grid(
                    rule_card("🏠", "Self-hostable", "Anyone should be able to clone and run it themselves. Docker, one-liner, whatever - it needs to be easy"),
                    rule_card("✅", "Actually works", "Functional, Deployed and demo-able. No vaporware."),
                    rule_card("⏰", "30 days", "One month from start to submission. Ship fast."),
                    rule_card("🔓", "Open-source twin", "Your project must be inspired by an existing closed-source product."),
                    columns=rx.breakpoints(initial="1", sm="2"),
                    spacing="4",
                    width="100%"
                ),
                spacing="4",
                width="100%",
                id="rules"
            ),

            rx.vstack(
                section_title("Points system", "code more → earn more → get more free stuff."),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("🕐", size="6"),
                            rx.vstack(
                                rx.text("10 points per hour of coding", weight="bold", size="4"),
                                rx.text(
                                    "Tracked via Hackatime or Lapse. Just code - we'll count the time.",
                                    color="gray",
                                    size="2"
                                ),
                                spacing="1",
                                align="start",
                            ),
                            spacing="3",
                            align="center",
                            width="100%",
                        ),
                        rx.divider(),
                        rx.text("🎯 Bonus point tasks", weight="bold", size="3"),
                        rx.vstack(
                            rx.text("• Write real documentation → +50 pts", size="2", color="gray"),
                            rx.text("• Add Docker / one-click deploy → +75 pts", size="2", color="gray"),
                            rx.text("• Get 5+ GitHub stars → +100 pts", size="2", color="gray"),
                            rx.text("• Record a demo video → +50 pts", size="2", color="gray"),
                            rx.text("• Get someone else to self-host it → +150 pts", size="2", color="gray"),
                            spacing="2",
                            align="start",
                            width="100%"
                        ),
                        spacing="3",
                        align="start",
                        width="100%"
                    ),
                    padding="24px",
                    border_radius="16px",
                    border="2px solid var(--purple-6)",
                    background="var(--purple-2)",
                    box_shadow="4px 4px 0px var(--purple-7)",
                    width="100%"
                ),
                spacing="4",
                width="100%"
            ),

            rx.vstack(
                section_title("🛒 Prize shop", "spend your points on real stuff."),
                rx.box(
                    rx.vstack(
                        prize_row("Hack Club stickers", "10 pts", "Custom-made Knockoff and random Hack Club stickers."),
                        prize_row("Custom Knockoff T-Shirt", "150 pts", "A shirt only for certified Shippers."),
                        prize_row("$10 Domain + Hosting credits", "15 points", "Get your knockoff online for real."),
                        prize_row("Raspberry Pi 5", "100 pts", "Self-host on actual hardware."),
                        prize_row("Dev Tools (IDE / AI subs)", "500 pts", "Level up your workflow."),
                        prize_row("Laptop Grant", "1500 pts", "The big one. Ship hard, earn big."),
                        spacing="1",
                        width="100%"
                    ),
                    padding="20px",
                    border_radius="16px",
                    border="2px solid var(--gray-6)",
                    background="var(--gray-1)",
                    width="100%"
                ),
                spacing="4",
                width="100%"
            ),

            rx.vstack(
                section_title("💡 Knockoff ideas", "need inspiration? here are some bangers."),
                rx.flex(
                    example_chip("Notion", "AppFlowy"),
                    example_chip("Figma", "Penpot"),
                    example_chip("Discord", "Revolt"),
                    example_chip("Vercel", "Coolify"),
                    example_chip("Google Analytics", "Umami"),
                    example_chip("1Password", "Bitwarden"),
                    example_chip("Trello", "WeKan"),
                    example_chip("Slack", "Mattermost"),
                    wrap="wrap",
                    spacing="3",
                    width="100%",
                ),
                rx.text(
                    "Or pick literally anything else. If it's closed source and you can build a usable open-source alternative, it counts",
                    size="2",
                    color="gray",
                    font_style="italic",
                ),
                spacing="4",
                width="100%",
            ),

            rx.vstack(
                section_title("🚢 How to submit"),
                rx.vstack(
                    step_item("1", "Pick your target", "Choose a closed-source app you want to knock off."),
                    step_item("2", "Build it", "You have 30 days. Track your time with Hackatime."),
                    step_item("3", "Ship it", "Deploy it somewhere. Make a README. Record a demo."),
                    step_item("4", "Submit", "Open a PR to our gallery repo with your project info."),
                    step_item("5", "Spend points", "Hit the prize shop and claim your loot."),
                    spacing="4",
                    width="100%",
                ),
                spacing="4",
                width="100%",
                id="how-to-submit",
            ),

            rx.vstack(
                section_title("❓ FAQ", "the stuff people always ask."),
                rx.vstack(
                    faq_item(
                        "Do I have to build the ENTIRE app?",
                        "Nope. Build the core features that make it useful. Nobody expects you to clone all of Notion in 30 days. Focus on the key functionality.",
                    ),
                    faq_item(
                        "Can I use existing open-source libraries?",
                        "Absolutely. Standing on the shoulders of giants is encouraged. Just don't fork an existing alternative and call it yours.",
                    ),
                    faq_item(
                        "What counts as 'self-hostable'?",
                        "If someone can clone your repo, follow your README, and get it running on their own machine or server in under 15 minutes — you're good. Docker is your friend.",
                    ),
                    faq_item(
                        "How is coding time tracked?",
                        "We use Hackatime (Hack Club's WakaTime instance). Install the plugin, link your account, and just code. We'll see the hours automatically.",
                    ),
                    faq_item(
                        "Can I work in a team?",
                        "Solo only for now. This is about YOUR skills and YOUR shipped project. But you can totally ask for help in the Slack!",
                    ),
                    faq_item(
                        "What if my knockoff already exists as open-source?",
                        "Then pick something else, or make yours significantly better/different. The point is to CREATE, not duplicate what's already out there.",
                    ),
                    faq_item(
                        "I'm a beginner — can I still do this?",
                        "YES. Pick a simpler target. A basic Linktree clone counts just as much as a Figma clone. Ship what you can.",
                    ),
                    spacing="3",
                    width="100%",
                ),
                spacing="4",
                width="100%",
            ),

            rx.box(
                rx.vstack(
                    rx.divider(),
                    rx.hstack(
                        rx.text("🏴‍☠️ Knockoff", weight="bold", size="3"),
                        rx.text("·", color="gray"),
                        rx.text("a Hack Club YSWS", size="2", color="gray"),
                        spacing="2",
                        align="center",
                    ),
                    rx.text(
                        "Made with 🖤 and questionable amounts of caffeine.",
                        size="1",
                        color="gray",
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                    padding_y="24px",
                ),
                width="100%",
            ),
            spacing="7",
            width="100%",
            padding_y="48px",
        ),
        max_width="720px",
        padding_x="16px"
    )


app = rx.App()
app.add_page(index)