def chatbot(msg):
    match msg.lower():
        case "hi" | "hello":
            return "Hello! How can I help you?"
        case "bye":
            return "Goodbye! Have a nice day."
        case "help":
            return "I can answer basic questions."
        case _:
            return "Sorry, I don't understand."

while True:
    user = input("You: ")
    if user == "exit":
        print("Chatbot: Bye!")
        break
    print("Chatbot:", chatbot(user))
