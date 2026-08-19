from model.model1 import get_response
def main_bot():
    print("Chatbot: Hi! How can I assist you today?")

    while True:
        user_input = input("User: ").lower()
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input == "goodbye":
            break
