from intelli_assistant.searchers.weather_searcher import handle_search_weather
from intelli_assistant.searchers.wikipedia_searcher import handle_search_wikipedia

distribute_keyword = {
    'weather': handle_search_weather,
    'wikipedia': handle_search_wikipedia
}
