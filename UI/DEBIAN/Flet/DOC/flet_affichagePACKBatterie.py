import flet as ft


async def main(page: ft.Page):

    async def refresh_info():
        level = await battery.get_battery_level()
        state = await battery.get_battery_state()
        print(str(level)+"%")
        print(state)

    async def on_state_change(e: ft.BatteryStateChangeEvent):
        print(f"State changed: {e.state}")
        await refresh_info()

    battery = ft.Battery(on_state_change=on_state_change)
    page.services.append(battery)  # need to keep a reference to the service
    await refresh_info()


if __name__ == "__main__":
    ft.run(main)
