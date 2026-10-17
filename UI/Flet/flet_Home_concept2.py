#https://flet.dev/docs/

import flet as ft

def main(page: ft.Page):

    page.title = "HOMESCREEN2"

#DESSUS!
    page.add(ft.Text("PLACEHOLDER_NETWORK"))
    page.add(ft.Text("PLACEHOLDER_HEURE"))
    page.add(ft.Text("PLACEHOLDER_NIV.BATTERIE"))

#MILLIEU
    page.add(ft.Text("BOUTONS ACTIONS A PLACER ET A CONFIGURER!"))
    page.add(ft.CupertinoButton(content="Enabled button"))
    page.add(ft.CupertinoButton(content="Disabled button", disabled=True))
    page.add(ft.CupertinoButton(content="FULLSCREEN", disabled=True))
    page.add(ft.CupertinoTintedButton("Tap me"))

#DESSOUS
    page.add(ft.Text(" 4 BOUTONS ACTIONS A PLACER, A ALIGNER puis A CONFIGURER! En bas."))
    page.add(ft.CupertinoButton(content="Enabled button 1"))
    page.add(ft.CupertinoButton(content="Enabled button 2"))
    page.add(ft.CupertinoButton(content="Enabled button 3"))
    page.add(ft.CupertinoButton(content="Enabled button 4"))



    
ft.run(main)
