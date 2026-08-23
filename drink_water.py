"""Send a desktop notification every hour to encourage drinking water."""

import time

from plyer import notification


REMINDER_INTERVAL_SECONDS = 60 * 60
NOTIFICATION_TITLE = "Hello Mishtee!"
NOTIFICATION_MESSAGE = "Time to drink a glass of water."


def send_water_reminder() -> None:
    """Display one water-reminder notification."""
    notification.notify(
        title=NOTIFICATION_TITLE,
        message=NOTIFICATION_MESSAGE,
        app_name="Water Reminder",
        timeout=10,
    )


def water_reminder() -> None:
    """Keep sending water-reminder notifications at the configured interval."""
    print("Water reminder started. Press Ctrl+C to stop.")

    try:
        while True:
            send_water_reminder()
            time.sleep(REMINDER_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nWater reminder stopped.")


if __name__ == "__main__":
    water_reminder()


