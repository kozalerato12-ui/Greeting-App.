import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    name = ""

    name_field = ft.TextField(label="Your name", width=300)

    async def on_continue(e):
        nonlocal name
        name = name_field.value.strip()

        if not name:
            page.show_dialog(
                ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Missing name"),
                    content=ft.Text("Please enter your name"),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: page.pop_dialog())
                    ],
                )
            )
            return

        await page.push_route("/greeting")

    async def on_back(e):
        await page.push_route("/")

    def route_change(e=None):
        page.views.clear()

        if page.route == "/greeting":
            page.views.append(
                ft.View(
                    route="/greeting",
                    controls=[
                        ft.Text(f"Hello, {name}!", size=30),
                        ft.Button("Back", on_click=on_back),
                    ],
                )
            )
        else:
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Text("Welcome", size=30),
                        name_field,
                        ft.Button("Continue", on_click=on_continue),
                    ],
                )
            )

        page.update()

    page.on_route_change = route_change
    route_change()


ft.run(main)

 


