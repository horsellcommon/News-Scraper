from gnews import GNews
import webbrowser

def select_headline():
        headline_select = int(input("Select a headline by entering the corresponding number (1-38): "))
        if 1 <= headline_select <= len(the_headlines):
            selected_headline = the_headlines[headline_select - 1]
            URL['link'] = selected_headline['url']
            print(f"Opening: {selected_headline['title']}")
            webbrowser.open(URL['link'])
        else:
            print("Invalid selection. Please enter a number between 1 and 38.")
            return select_headline()

def specific_news():
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
     keyword = input("Enter a keyword to search for news on a specific topic: ")
     search_results = GNews().get_news(keyword)
     print("--- Results ---")
     for i, result in enumerate(search_results):
         print(f"{i + 1}. {result['title']} - {result['published date']}")
     print("--- End of Results ---")
     user_selection()

def continue_on():
     continue_choice = input("Do you want to search for a more specific topic? (yes/no): ")
     if continue_choice.lower() == 'yes':
        specific_news()
        return
     elif continue_choice.lower() == 'no':
        return
     else:
          while continue_choice.lower() not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue_on()

def main():
    choice = input("Show today's top headlines or search for specific news? (Enter 'top' or 'specific'): ")
    if choice.lower() == 'top':
        print("--- Today's Headlines ---")
        for i, result in enumerate(the_headlines):
                print(f"{i + 1}. {result['title']} - {result['published date']}")
        print("--- End of Results ---")
        select_headline()
        continue_on()
    elif choice.lower() == 'specific':
        specific_news()
        return
    else:
        print("Invalid choice. Please enter 'top' or 'specific'.")
        return main()

URL = {}
the_headlines = GNews().get_top_news()
main()