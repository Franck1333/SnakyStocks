import flet as ft


def app_button(name):
    return ft.Container(
        width=64,
        height=64,
        content=ft.CupertinoButton(
            content=name
        ),
    )


def main(page: ft.Page):

    page.title = "Homescreen Complexifié"
    page.padding = 0

    # ==================================================
    # CANEVAS PRINCIPAL
    # ==================================================

    page.add(

        ft.Stack(
            width=1280,
            height=720,

            controls=[

                # ==================================================
                # STATUS BAR
                # Positionnée dans le Stack
                # mais organisée avec un Row
                # ==================================================

                ft.Container(

                    content=ft.Row(
                        controls=[
                            ft.Text("09:41"),
                            ft.Text("WiFi"),
                            ft.Text("🔋 100%"),
                        ],

                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),

                    left=20,
                    right=20,
                    top=15,
                ),


                # ==================================================
                # APPLICATIONS
                # Positionnées dans le Stack
                # organisées avec Column + Row
                # ==================================================

                ft.Container(

                    content=ft.Column(
                        controls=[

                            # Première rangée
                            ft.Row(
                                controls=[
                                    app_button("📷"),
                                    app_button("🌤"),
                                    app_button("🎵"),
                                    app_button("⚙️"),
                                ],

                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ),

                            # Deuxième rangée
                            ft.Row(
                                controls=[
                                    app_button("📚"),
                                    app_button("❤️"),
                                    app_button("📈"),
                                    app_button("🗺"),
                                ],

                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ),
                        ],

                        spacing=9,
                    ),

                    left=15,
                    right=15,
                    top=120,
                ),


                # ==================================================
                # DOCK
                # Positionné avec Stack
                # organisé avec Row
                # ==================================================

                ft.Container(

                    width=1280,
                    height= 720,

                    content=ft.Row(
                        controls=[
                            app_button("🌐"),
                            app_button("✉"),
                            app_button("🎵"),
                            app_button("⚙"),
                        ],

                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),

                    left=15,
                    bottom=20,
                ),
            ],
        )
    )


ft.run(main)
