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

def shop_category(emoji: str, label: str) -> rx.Component:
    return rx.hstack(
        rx.text(emoji, size="5"),
        rx.text(label, weight="bold", size="3"),
        spacing="2",
        align="center",
        padding="12px 18px",
        border="1.5px solid var(--gray-5)",
        border_radius="10px",
        background="var(--gray-1)",
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

def shop() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.link(
                rx.text("← Back to Knockoff", size="2", color="var(--purple-9)", weight="medium"),
                href="/",
            ),
            rx.vstack(
                rx.heading("🛒 Prize Shop", size="9", weight="bold"),
                rx.text(
                    "Earn points by coding and completing tasks. Spend them here.",
                    size="4",
                    color="gray"
                ),
                spacing="2",
                align="start",
                width="100%"
            ),
            rx.grid(
                rx.vstack(
                    rx.text("🎨 Swag & Stickers", weight="bold", size="5"),
                    rx.vstack(
                        prize_row("Knockoff Sticker Pack", "25 pts", "Custom-made Knockoff stickers + random Hack Club classics."),
                        prize_row("Custom Knockoff T-Shirt", "100 pts", "A shirt only for certified shippers."),
                        prize_row("Hoodie", "250 pts", "For late-night coding sessions."),
                        spacing="1", width="100%",
                    ),
                    spacing="3", width="100%",
                ),
                rx.vstack(
                    rx.text("🌐 Domains & Hosting", weight="bold", size="5"),
                    rx.vstack(
                        prize_row("Domain name", "50 pts", "A .com, .dev, or .org for your project."),
                        prize_row("Hosting credits", "75 pts", "Cloud credits to keep your knockoff running."),
                        prize_row("Domain + hosting bundle", "100 pts", "Both of the above, discounted."),
                        spacing="1", width="100%",
                    ),
                    spacing="3", width="100%",
                ),
                rx.vstack(
                    rx.text("🔧 Dev Tools & Subscriptions", weight="bold", size="5"),
                    rx.vstack(
                        prize_row("IDE subscription", "150 pts", "JetBrains, etc."),
                        prize_row("AI coding tools", "100 pts", "Copilot, Cursor, or similar."),
                        prize_row("Dev tools bundle", "200 pts", "IDE + AI combo."),
                        spacing="1", width="100%",
                    ),
                    spacing="3", width="100%",
                ),
                rx.vstack(
                    rx.text("🖥️ Hardware", weight="bold", size="5"),
                    rx.vstack(
                        prize_row("Raspberry Pi", "350 pts", "Self-host your knockoff on real hardware."),
                        prize_row("Mini PC", "750 pts", "A proper home server."),
                        prize_row("Laptop grant", "2500 pts", "The big one. Ship hard, earn big."),
                        spacing="1", width="100%",
                    ),
                    spacing="3", width="100%",
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="7",
                width="100%",
            ),
            rx.box(
                rx.text(
                    "Point values and availability may change. More items coming soon.",
                    size="2", color="gray", font_style="italic",
                ),
                padding_top="12px",
            ),
            spacing="7",
            width="100%",
            padding_y="48px",
        ),
        max_width="1200px",
        padding_x="24px"
    )


def task_row(name: str, points: str, desc: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(points, weight="bold", size="2", white_space="nowrap"),
            padding="4px 10px",
            border_radius="999px",
            background="var(--green-3)",
            border="1.5px solid var(--green-6)",
        ),
        rx.vstack(
            rx.text(name, weight="bold", size="3"),
            rx.text(desc, color="gray", size="2"),
            spacing="1",
            align="start",
        ),
        spacing="3",
        align="center",
        width="100%",
        padding="12px 0",
        border_bottom="1px dashed var(--gray-5)",
    )


def qte_chip(name: str, points: str) -> rx.Component:
    return rx.hstack(
        rx.text("⚡", size="3"),
        rx.text(name, size="2", weight="medium"),
        rx.box(
            rx.text(points, weight="bold", size="1", white_space="nowrap"),
            padding="2px 8px",
            border_radius="999px",
            background="var(--orange-3)",
            border="1px solid var(--orange-6)",
        ),
        spacing="2",
        align="center",
        padding="8px 14px",
        border="1.5px solid var(--gray-5)",
        border_radius="10px",
        background="var(--gray-1)",
    )


def tasks() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.link(
                rx.text("← Back to Knockoff", size="2", color="var(--purple-9)", weight="medium"),
                href="/",
            ),
            rx.vstack(
                rx.heading("🎯 Tasks & Points", size="9", weight="bold"),
                rx.text(
                    "Everything that earns you points. Code, complete tasks, catch quick-time events.",
                    size="4", color="gray",
                ),
                spacing="2",
                align="start",
                width="100%",
            ),
            rx.grid(
                rx.vstack(
                    rx.text("🕐 Coding Time", weight="bold", size="5"),
                    rx.box(
                        rx.vstack(
                            rx.text("10 points per hour of coding", weight="bold", size="4"),
                            rx.text(
                                "Tracked automatically via Hackatime. Install the plugin, link your account, and just code. "
                                "Hours are counted from the moment you start your project.",
                                color="gray", size="2", line_height="1.6",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        padding="20px",
                        border_radius="14px",
                        border="2px solid var(--purple-6)",
                        background="var(--purple-2)",
                        width="100%",
                    ),
                    spacing="3", width="100%",
                ),
                rx.vstack(
                    rx.text("⚡ Quick-Time Events", weight="bold", size="5"),
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Random challenges that drop without warning. They're available for a limited time only. "
                                "Catch them in the Slack or on the dashboard for instant bonus points.",
                                color="gray", size="2", line_height="1.6",
                            ),
                            rx.text("Examples of past QTEs:", weight="bold", size="2", padding_top="8px"),
                            rx.flex(
                                qte_chip("Add a config file", "+10 pts"),
                                qte_chip("Write one test", "+15 pts"),
                                qte_chip("Add a /health endpoint", "+10 pts"),
                                qte_chip("Make it work offline", "+25 pts"),
                                qte_chip("Add dark mode", "+10 pts"),
                                qte_chip("Shrink your Docker image", "+20 pts"),
                                wrap="wrap",
                                spacing="2",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        padding="20px",
                        border_radius="14px",
                        border="2px dashed var(--orange-6)",
                        background="var(--orange-2)",
                        width="100%",
                    ),
                    spacing="3", width="100%",
                ),
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="7",
                width="100%",
            ),
            rx.vstack(
                rx.text("📋 Bonus Tasks", weight="bold", size="5"),
                rx.grid(
                    task_row("Write real documentation", "+25 pts", "A proper README with setup instructions, screenshots, and usage guide."),
                    task_row("Add Docker / one-click deploy", "+50 pts", "Dockerfile or docker-compose that actually works out of the box."),
                    task_row("Get 5+ GitHub stars", "+50 pts", "Convince real people your project is worth starring."),
                    task_row("Record a demo video", "+25 pts", "2-minute walkthrough showing your knockoff in action."),
                    task_row("Get someone else to self-host it", "+75 pts", "Another person follows your docs and gets it running. Proof required."),
                    task_row("Add CI/CD pipeline", "+50 pts", "GitHub Actions, GitLab CI, whatever — automated tests and/or deploys."),
                    task_row("Write a blog post about it", "+50 pts", "Explain what you built, why, and what you learned."),
                    columns=rx.breakpoints(initial="1", lg="2"),
                    spacing="1",
                    width="100%",
                ),
                spacing="3", width="100%",
            ),
            rx.box(
                rx.text(
                    "Tasks and point values may be updated. QTEs are announced in real-time.",
                    size="2", color="gray", font_style="italic",
                ),
                padding_top="12px",
            ),
            spacing="7",
            width="100%",
            padding_y="48px",
        ),
        max_width="1200px",
        padding_x="24px",
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

            rx.grid(
                rx.vstack(
                    section_title("What's the deal?"),
                    rx.box(
                        rx.text(
                            "Knockoff is a ",
                            rx.text.strong("You Ship, We Ship"),
                            " program. You build something cool -> we give you cool stuff. "
                            "Specifically: pick any closed-source product (Notion, Figma, Discord, whatever). ",
                            "Build a legit open-source alternative that people can actually use and self-host "
                            "and earn points you can spend in our prize shop.",
                            size="3",
                            line_height="1.7"
                        ),
                        spacing="3",
                        width="100%"
                    ),
                    spacing="4",
                    width="100%",
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
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="7",
                width="100%",
            ),

            rx.grid(
                rx.vstack(
                    section_title("⭐ Points system", "code more → earn more → get more free stuff."),
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text("🕐", size="6"),
                                rx.vstack(
                                    rx.text("10 points per hour of coding", weight="bold", size="4"),
                                    rx.text(
                                        "Tracked via Hackatime and Lapse. Just code — we'll count the time.",
                                        color="gray", size="2",
                                    ),
                                    spacing="1",
                                    align="start",
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                            ),
                            rx.divider(),
                            rx.hstack(
                                rx.text("🎯", size="6"),
                                rx.vstack(
                                    rx.text("Bonus tasks", weight="bold", size="4"),
                                    rx.text(
                                        "Earn extra points for things like writing docs, adding Docker support, getting GitHub stars, and more.",
                                        color="gray", size="2",
                                    ),
                                    spacing="1",
                                    align="start",
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                            ),
                            rx.divider(),
                            rx.hstack(
                                rx.text("⚡", size="6"),
                                rx.vstack(
                                    rx.text("Quick-time events", weight="bold", size="4"),
                                    rx.text(
                                        "Random pop-up challenges — like \"add a config file\" or \"write a test\" — for instant bonus points. Stay ready and watch #knockoff closely!",
                                        color="gray", size="2",
                                    ),
                                    spacing="1",
                                    align="start",
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                            ),
                            spacing="3",
                            align="start",
                            width="100%",
                        ),
                        padding="24px",
                        border_radius="16px",
                        border="2px solid var(--purple-6)",
                        background="var(--purple-2)",
                        box_shadow="4px 4px 0px var(--purple-7)",
                        width="100%",
                    ),
                    rx.link(
                        rx.button(
                            "See all tasks & point values →",
                            size="3",
                            variant="outline",
                            color_scheme="purple",
                            cursor="pointer",
                        ),
                        href="/tasks",
                    ),
                    spacing="4",
                    width="100%",
                ),
                rx.vstack(
                    section_title("🛒 Prize shop", "earn points, spend 'em on real stuff."),
                    rx.flex(
                        shop_category("🎨", "Swag & stickers"),
                        shop_category("🌐", "Domains & hosting"),
                        shop_category("🔧", "Dev tools & subscriptions"),
                        shop_category("🖥️", "Hardware"),
                        wrap="wrap",
                        spacing="3",
                        width="100%",
                    ),
                    rx.link(
                        rx.button(
                            "Browse the full shop →",
                            size="3",
                            variant="outline",
                            color_scheme="purple",
                            cursor="pointer",
                        ),
                        href="/shop",
                    ),
                    spacing="4",
                    width="100%",
                ),
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="7",
                width="100%",
            ),
            rx.grid(
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
                        step_item("3", "Complete tasks", "Try to complete as many tasks as you can"),
                        step_item("4", "Ship it", "Deploy it somewhere. Make a README. Record a demo."),
                        step_item("5", "Submit", "Open a PR to our gallery repo with your project info."),
                        step_item("6", "Spend points", "Hit the prize shop and claim your loot."),
                        spacing="4",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                    id="how-to-submit",
                ),
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="7",
                width="100%",
            ),

            rx.vstack(
                section_title("❓ FAQ", "the stuff people always ask."),
                rx.grid(
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
                        "If someone can clone your repo, follow your README, and get it running on their own machine or server in under 15 minutes - you're good. Docker is your friend.",
                    ),
                    faq_item(
                        "How is coding time tracked?",
                        "We use Hackatime and Lapse. Install the plugin, link your account, and just code. We'll see the hours automatically.",
                    ),
                    faq_item(
                        "Can I work in a team?",
                        "Solo only for now. This is about YOUR skills and YOUR shipped project. But you can totally ask for help in the Slack!",
                    ),
                    faq_item(
                        "How many projects can I make?",
                        "There isn't a limit to the number of projects, but don't make slop.",
                    ),
                    faq_item(
                        "I'm a beginner — can I still do this?",
                        "YES. Pick a simpler target. A basic Linktree clone counts just as much as a Figma clone. Ship what you can.",
                    ),
                    columns=rx.breakpoints(initial="1", lg="2"),
                    spacing="3",
                    width="100%",
                ),
                spacing="4",
                width="100%",
            ),

            rx.box(
                rx.grid(
                    rx.divider(),
                    rx.hstack(
                        rx.text("🏴‍☠️ Knockoff", weight="bold", size="3"),
                        rx.text("·", color="gray"),
                        rx.link(
                            rx.text("Hack Club", size="2", color="var(--purple-9)", weight="medium"),
                            href="https://hackclub.com",
                            is_external=True,
                        ),
                        rx.text("·", color="gray"),
                        rx.link(
                            rx.text("Join the Slack", size="2", color="var(--purple-9)", weight="medium"),
                            href="https://hackclub.com/slack",
                            is_external=True,
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.text(
                        "Made with 🖤 and questionable amounts of caffeine by ketr4x.",
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
        max_width="1200px",
        padding_x="24px"
    )


app = rx.App()
app.add_page(index, title="Knockoff")
app.add_page(shop, route="/shop", title="Knockoff — Prize Shop")
app.add_page(tasks, route="/tasks", title="Knockoff — Tasks & Points")