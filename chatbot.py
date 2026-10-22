import re

responses = {
    "greeting": "Hello! Welcome to our customer support chatbot.",
    "hours": "Our business hours are Monday to Saturday, 9 AM to 6 PM.",
    "product": "We offer laptops, mobiles, and accessories.",
    "return": "Products can be returned within 7 days with a valid receipt.",
    "thanks": "You're welcome! Is there anything else I can help with?"
}

patterns = {
    "greeting": r"\b(hello|hi|hey)\b",
    "hours": r"\b(hours|timing|open|closed)\b",
    "product": r"\b(product|products|laptop|mobile|price)\b",
    "return": r"\b(return|refund|exchange)\b",
    "thanks": r"\b(thanks|thank you)\b"
}

print("Customer Support Chatbot")
print("Ask about business hours, products, or returns.")
print("Type 'bye', 'exit', or 'quit' to stop.\n")

while True:
    try:
        message = input("You: ").strip().lower()

        if re.search(r"\b(bye|exit|quit)\b", message):
            print("Bot: Goodbye! Have a nice day!")
            break

        found = False

        for intent, pattern in patterns.items():
            if re.search(pattern, message):
                print("Bot:", responses[intent])
                found = True

        if not found:
            print("Bot: Sorry, I didn't understand. Please ask about our hours, products, or returns.")

    except (KeyboardInterrupt, EOFError):
        print("\nBot: Goodbye!")
        break