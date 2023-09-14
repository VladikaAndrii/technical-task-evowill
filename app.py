from typing import Optional
import typer

from wrapper import BoredAPIWrapper
from db_actions import ActivityDatabase
from loguru import logger

from enums import TypeEnum

app = typer.Typer(pretty_exceptions_short=True)
db = ActivityDatabase()
wrapper = BoredAPIWrapper()


@app.command("new", help="This command gets a random activity from the bored API "
                         "with given parameters and saves it in the database")
def new_command(type: Optional[TypeEnum] = None,
                participants: int = None,
                price_min: Optional[float] = None,
                price_max: Optional[float] = None,
                accessibility_min: Optional[float] = None,
                accessibility_max: Optional[float] = None) -> None:
    activity = wrapper.get_random_activity(type, participants, price_min,
                                           price_max, accessibility_min, accessibility_max)
    db.save_activity(activity)
    logger.info(f"Saved activity in database: {activity['activity']}")


@app.command("list", help="Return the last 5 activities saved in the database")
def list_command() -> None:
    latest_activities = db.get_latest_activities()
    for index, activity in enumerate(latest_activities, start=1):
        logger.info(f"{index}. Activity: {activity[1]}, Type: {activity[2]}, Participants: {activity[3]}, "
                    f"Price: {activity[4]}, Accessibility: {activity[5]}")


if __name__ == "__main__":
    app()
