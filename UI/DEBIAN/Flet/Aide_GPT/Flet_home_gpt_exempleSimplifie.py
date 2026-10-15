import flet as ft


def main(page: ft.Page):

    page.title = "HOMESCREEN"
    page.padding = 0

    page.add(
        ft.Stack(
            width=400,
            height=700,

            controls=[

                # ==========================
                # POSITIONNEMENT PRÉCIS
                # ==========================

                ft.Container(
                    content=ft.Text("NETWORK"),
                    left=20,
                    top=20,
                ),

                ft.Container(
                    content=ft.Text("09:41"),
                    left=180,
                    top=20,
                ),

                ft.Container(
                    content=ft.Text("BATTERY"),
                    right=20,
                    top=20,
                ),


                # ==========================
                # ORGANISATION AUTOMATIQUE
                # ==========================

                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.CupertinoButton(
                                content="ACTION 1"
                            ),

                            ft.CupertinoButton(
                                content="ACTION 2"
                            ),

                            ft.CupertinoButton(
                                content="ACTION 3"
                            ),
                        ]
                    ),

                    left=130,
                    top=180,
                ),


                # ==========================
                # DOCK
                # ==========================

                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.CupertinoButton(content="1"),
                            ft.CupertinoButton(content="2"),
                            ft.CupertinoButton(content="3"),
                            ft.CupertinoButton(content="4"),
                        ]
                    ),

                    left=40,
                    bottom=30,
                ),
            ],
        )
    )


ft.run(main)
