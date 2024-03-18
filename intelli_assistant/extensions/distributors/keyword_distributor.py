from intelli_assistant.extensions.handlers.searchers.weather_searcher import handle_search_weather
from intelli_assistant.extensions.handlers.searchers.wikipedia_searcher import handle_search_wikipedia
from intelli_assistant.extensions.handlers.checkers.text_space_checker import check_text_space

distribute_keyword = {
    'weather': handle_search_weather,
    'wikipedia': handle_search_wikipedia,
    'check_text_space': check_text_space
}
