import pyperclip  # pip install pyperclip
import requests  # pip install requests


# function to fetch a random quote from the API
def fetch_random_quote():
    try:
        response = requests.get("https://dummyjson.com/quotes/random")
        if response.status_code == 200:
            data = response.json()
            # Fixed key from 'quotes' to 'quote' to match usage
            return {"quote": data["quote"], "author": data["author"]}
        else:
            print("Error fetching quote. Try again later.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# function to display the menu
def display_menu():
    print("\n Welcome to the Quote Generator written in Python")
    print("1. Generate a new random quote")
    print("2. Copy the quote to clipboard")
    print("3. Exit")


# main application function
def run_quote_generator():
    current_quote = None

    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            current_quote = fetch_random_quote()
            if current_quote:
                # Used double quotes for f-string to prevent syntax errors
                print(f"Quote: {current_quote['quote']}")
                print(f"Author: {current_quote['author']}")

        elif choice == "2":  # Un-indented out of the choice == '1' block
            if current_quote:
                # Fixed syntax: changed colon (:) to equals sign (=)
                quote_text = (
                    f"{current_quote['quote']} - {current_quote['author']}"
                )
                pyperclip.copy(quote_text)
                print("Your quote has been copied to the clipboard!")
            else:
                print("Generate a quote first.")

        elif choice == "3":
            print("Thank you for your time. Goodbye!")
            break

        else:
            print("You need to enter something valid (1, 2, or 3).")


# run the app
run_quote_generator()
