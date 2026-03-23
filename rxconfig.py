import reflex as rx

config = rx.Config(
    app_name="Knockoff",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)