import wikipedia
from intelli_assistant.decorators.auto_log_decorator import auto_log

@auto_log(log_file='wikipedia.log')
def handle_search_wikipedia(**kwargs):
    search = kwargs.get('search')
    try:
        search_results = wikipedia.search(search)
        search_result = search_results[0]
        return wikipedia.summary(search_result, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        return(e.options)
    except wikipedia.exceptions.PageError as e:
        return "Sorry, no results found."

if __name__ == "__main__":
    search = input("search wikipedia: ") or "Python"
    print(handle_search_wikipedia(search=search))