#!/usr/bin/env python3

from brain_module import ChatGPT, MagicCommanderDeck
import json

if  __name__ == "__main__":
    bot = ChatGPT()
        
    deck = MagicCommanderDeck()
    commander_file = input("Input your commander file: ")
    deck.process_deck_file(commander_file)

    commander = deck.commander_name()
    text_deck = deck.deck_list_to_string()

    aspect = input("What aspect of your deck you want to improve: ")
    budget = input("How much do you want to spend on these upgrades: ")
    
    response = bot.request_openai(f"""
                                Suggest me list of 5 Magic the gathering cards in json format, that would upgrade my 
                                {commander} commander deck. And what cards to replace from the deck.
                                The deck contains this list of cards: {text_deck}, and the main focus on the upgrades should be on {aspect}. 
                                With a {budget} budget
                                  """)
    # parse the response:
    cards = json.loads(response)

    # 
    print(json.dumps(cards, indent=4))

