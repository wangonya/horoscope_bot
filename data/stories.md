## story_001
* greeting
  - utter_greet
* get_horoscope
  - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "Capricon"}
  - slot{"horoscope_sign": "Aries"}
  - get_todays_horoscope
  - utter_subscribe

## story_002
* greeting
  - utter_greet
* get_horoscope{"horoscope_sign": "Capricon"}
  - slot{"horoscope_sign": "Cancer"}
  - get_todays_horoscope
  - utter_subscribe
* subscription
  - slot{"subscribe": "True"}
  - subscribe_user

## Horoscope query with horoscope_sign
* greeting
  - utter_greet
* get_horoscope
  - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "capricon"}
  - slot{"horoscope_sign": "capricon"}
  - get_todays_horoscope
  - slot{"horoscope_sign": "capricon"}
  - utter_subscribe
* subscription{"subscribe": "True"}
  - slot{"subscribe": "True"}
  - subscribe_user
  - slot{"subscribe": true

## Horoscope with sign provided
* greeting
  - utter_greet
* get_horoscope{"horoscope_sign": "leo"}
  - slot{"horoscope_sign": "leo"}
  - get_todays_horoscope
  - slot{"horoscope_sign": "leo"}
  - utter_subscribe
* subscribe{"subscribe": "True"}
  - slot{"subscribe": "True"}
  - subscribe_user
  - slot{"subscribe": true}

## When user directly asks for subscription
* greeting
  - utter_greet
* subscription{"subscribe": "True"}
  - slot{"subscribe": "True"}
  - subscribe_user
  - slot{"subscribe": true}