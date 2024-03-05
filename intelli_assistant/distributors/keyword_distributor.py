from intelli_assistant.searchers.weather_searcher import handle_search_weather
from intelli_assistant.searchers.wikipedia_searcher import handle_search_wikipedia
from intelli_assistant.checkers.text_space_checker import check_text_space

distribute_keyword = {
    'weather': handle_search_weather,
    'wikipedia': handle_search_wikipedia,
    'check_text_space': check_text_space
}
