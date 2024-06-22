#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chatbot():
    print("Hi! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'hello' or user_input == 'hi':
            print("Chatbot: Hello! How are you?")
        elif user_input == 'how are you?':
            print("Chatbot: I'm just a computer program, but I'm here to help you!")
        elif 'your name' in user_input:
            print("Chatbot: I'm a chatbot created to assist you.")
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Chatbot: You're welcome!")
        elif user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()


# In[ ]:




