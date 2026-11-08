from gnews import GNews

keyword = input("Search for news with the keyword: ")
search_results = GNews().get_news(keyword)

for result in search_results:
    print(result['title'])