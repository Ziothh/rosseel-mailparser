from .SETTINGS import ROSSEEL, ROSSEEL_TEST


def __create_profile(settings: dict, running_message: str, is_test: bool):
    return {
        "settings": settings,
        "running_message": running_message,
        "is_test": is_test
    }


LAUNCH_PROFILES = {
    "dev": __create_profile(
        settings=ROSSEEL_TEST,
        running_message="🚀 Running in Test Mode",
        is_test=True
    ),
    "rosseel": __create_profile(
        settings=ROSSEEL,
        running_message="> Running in Production Mode",
        is_test=False
    ),
}
