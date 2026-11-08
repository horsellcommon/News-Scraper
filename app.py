from gnews import GNews
import webbrowser

URL = {}
keyword = input("Search for news with the keyword: ")
search_results = GNews().get_news(keyword)

def enumerate_results():
    for i, result in enumerate(search_results):
        print(f"{i + 1}. {result['title']} - {result['published date']}")

def user_selection():
    selection = int(input("Select a result by entering the corresponding number (1-100): "))
    if 1 <= selection <= len(search_results):
        selected_result = search_results[selection - 1]
        URL['link'] = selected_result['url']
        print(f"Opening: {selected_result['title']}")
        webbrowser.open(URL['link'])
    else:
        print("Invalid selection. Please enter a number between 1 and 100.")
        user_selection()


print("--- Results ---")
print(enumerate_results())
print("--- End of Results ---")
user_selection()