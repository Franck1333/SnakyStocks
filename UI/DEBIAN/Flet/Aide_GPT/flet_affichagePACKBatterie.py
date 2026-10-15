import flet as ft
import asyncio


async def main(page: ft.Page):

    async def refresh_info():
        level = await battery.get_battery_level()
        state = await battery.get_battery_state()
        if level is None:
            level = "Unknown"

        print(f"Battery level: {level}%")
        print(f"State: {state}")
        

    async def on_state_change(e: ft.BatteryStateChangeEvent):
        print(f"State changed: {e.state}")
        await refresh_info()

    async def monitor_battery():
        # Surveillance périodique
        while True:
            await refresh_info()
            # Attendre 30 secondes avant la prochaine lecture
            await asyncio.sleep(30)


    battery = ft.Battery(on_state_change=on_state_change)
    page.services.append(battery)  # need to keep a reference to the service
    await refresh_info() 
    asyncio.create_task(monitor_battery()) #Interrogation périodique de la batterie


if __name__ == "__main__":
    ft.run(main)
