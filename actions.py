from __future__ import (
    absolute_import, division,
    print_function, unicode_literals
)

import requests

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class GetTodaysHoroscope(Action):
    def name(self):  # type: () -> Text
        return "get_todays_horoscope"

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]

        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        url = f'http://horoscope-api.herokuapp.com/horoscope/today/{user_horoscope_sign}'

        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = f"Here's your horoscope for today:\n {todays_horoscope}"

        dispatcher.utter_message(response)

        return [SlotSet('horoscope_sign', user_horoscope_sign)]


class SubscribeUser(Action):
    def name(self):  # type: () -> Text
        return "subscribe_user"

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]

        subscribe = tracker.get_slot('subscribe')

        if subscribe:
            response = "You've been successfully subscribed"
        else:
            response = "You've been successfully unsubscribed"

        dispatcher.utter_message(response)

        return [SlotSet('subscribe', subscribe)]
