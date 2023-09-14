import requests


class BoredAPIWrapper:
    URL = "https://www.boredapi.com/api/activity"

    def get_random_activity(self,
                            type: str | None,
                            participants: int | None,
                            price_min: float | None,
                            price_max: float | None,
                            accessibility_min: float | None,
                            accessibility_max: float | None) -> dict:
        params = {
            "type": type,
            "participants": participants,
            "minprice": price_min,
            "maxprice": price_max,
            "minaccessibility": accessibility_min,
            "maxaccessibility": accessibility_max
        }
        response = requests.get(self.URL, params=params)
        json_response = response.json()
        if "error" in json_response:
            raise Exception(f"Exception: {json_response['error']}")
        return json_response
