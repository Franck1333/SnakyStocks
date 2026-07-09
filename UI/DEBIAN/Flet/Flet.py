#https://flet.dev/docs/

import flet as ft

def main(page: ft.Page):

    page.title = "SnakyStocks"
    page.add(ft.Text("Hello Finance €$£%µ@"))

    banner = ft.Banner(
        leading=ft.Icon(ft.Icons.INFO_OUTLINED, color=ft.Colors.PRIMARY),
        content=ft.Text("Affichage d'une bannière"),
        actions=[ft.TextButton("OK!")],
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        open=True,
    )
    page.show_dialog(banner)

    page.show_dialog(ft.SnackBar(ft.Text("Opened snack bar")))

    page.add(ft.CupertinoButton(content="Enabled button"))
    page.add(ft.CupertinoButton(content="Disabled button", disabled=True))
    page.add(ft.CupertinoTintedButton("Tap me"))

    page.add(ft.Image(src="https://flet.dev/img/logo.svg",width=128,height=128,))

    page.add(ft.Text(value=(
    "Lorem ipsum dolor sit amet, consectetur adipiscing "
    "elit. Curabitur quis nibh vitae purus consectetur "
    "facilisis sed vitae ipsum. Quisque faucibus sed nulla "
    "placerat sagittis. Phasellus condimentum risus vitae "
    "nulla vestibulum auctor. Curabitur scelerisque, nibh "
    "eget imperdiet consequat, odio ante tempus diam, sed "
    "volutpat nisl erat eget turpis. Sed viverra, diam sit "
    "amet blandit vulputate, mi tellus dapibus lorem, vitae "
    "vehicula diam mauris placerat diam. Morbi sit amet "
    "pretium turpis, et consequat ligula. Nulla velit sem, "
    "suscipit sit amet dictum non, tincidunt sed nulla. "
    "Aenean pellentesque odio porttitor sagittis aliquam. "
    "Name various at metus vitae vulputate. Praesent "
    "faucibus nibh lorem, eu pretium dolor dictum nec. "
    "Phasellus eget dui laoreet, viverra magna vitae, "
    "pellentesque diam."),max_lines=10,),)

    
ft.run(main)
