from flet import *
from login.login import login_container

def main(page: Page):
    page.title = "InelvaBot"
    page.bgcolor = "#3871A5"
    page.add(Container(content=login_container))


app(main)
