import flet as ft
import asyncio

async def get_BatteryInfos(page: ft.Page):
    async def refresh_info():
        level = await battery.get_battery_level()              #Obtention du niveau de la batterie
        state = await battery.get_battery_state()              #Obtention de l'état de la batterie (par exemple, "charging", "discharging", "full" ou "unknown".)
        if level is None:                                      #Si le niveau de la batterie est "None", cela signifie que l'information n'est pas disponible, donc on l'affiche comme "Unknown".
            level = "Unknown"

        print(f"Battery level: {level}%")
        print(f"State: {state}")
        

    async def on_state_change(e: ft.BatteryStateChangeEvent):  #Obtention de l'état de la batterie par un événement "BatteryStateChangeEvent" 
        print(f"State changed: {e.state}")
        await refresh_info()

    async def monitor_battery():
        # Surveillance périodique
        while True:
            await refresh_info()
            # Attendre 30 secondes avant la prochaine lecture
            await asyncio.sleep(30)                            #Comptabilisation de la batterie toutes les 30 secondes pour éviter une surcharge de requêtes.


    battery = ft.Battery(on_state_change=on_state_change)      #Event déclenché lorsque l'état de la batterie change (par exemple, lorsqu'elle passe de "charging" à "discharging").
    page.services.append(battery)                              #Reference à l'objet batterie pour éviter qu'il ne soit collecté par le "garbage collector"
    await refresh_info()                                       #Obtention initiale des informations sur la batterie
    asyncio.create_task(monitor_battery())                     #Interrogation périodique de la batterie


if __name__ == "__main__":
    ft.run(get_BatteryInfos) #Permet d'obtenir les informations sur la batterie et de les afficher dans la console.