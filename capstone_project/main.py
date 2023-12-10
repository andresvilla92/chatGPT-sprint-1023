#!/usr/bin/env python3

from brain_module import ChatGPT
import json

if  __name__ == "__main__":
    bot = ChatGPT()
    
    commander = input("What commander do you want to upgrade: ")
    deck = input("Provide de decklist of your commander: ")
    aspect = input("What aspect do you want to improve of the deck: ")

    # commander = "Atraxa, Praetors' Voice"
    deck = """
        1 Ajani, Sleeper Agent
        1 Arcane Sanctum
        1 Arcane Signet
        1 Astral Cornucopia
        1 Birds of Paradise
        1 Blighted Agent
        1 Bloated Contaminator
        1 Breeding Pool
        1 Brokers Ascendancy
        1 Cankerbloom
        1 Chromatic Lantern
        1 Command Tower
        1 Contagion Engine
        1 Contaminant Grafter
        1 Counterspell
        1 Court of Garenbrig
        1 Cultivate
        1 Cyclonic Rift
        1 Deepglow Skate
        1 Delighted Halfling
        1 Demonic Tutor
        1 Doubling Season
        1 Drown in Ichor
        1 Everflowing Chalice
        1 Evolution Sage
        1 Evolving Wilds
        1 Exotic Orchard
        1 Experimental Augury
        1 Ezuri, Stalker of Spheres
        1 Farseek
        1 Flooded Strand
        1 Flux Channeler
        3 Forest
        1 Four Knocks
        1 Glistening Sphere
        1 Godless Shrine
        1 Hallowed Fountain
        1 Ichor Rats
        1 Ichormoon Gauntlet
        1 Indatha Triome
        1 Inexorable Tide
        1 Infectious Bite
        1 Infectious Inquiry
        3 Island
        1 Ixhel, Scion of Atraxa
        1 Karn's Bastion
        1 Lae'zel, Vlaakith's Champion
        1 Lightning Greaves
        1 Marsh Flats
        1 Misty Rainforest
        1 Narset, Parter of Veils
        1 Nature's Lore
        1 Norn's Choirmaster
        1 Norn's Decree
        1 Oko, Thief of Crowns
        1 Opulent Palace
        1 Overgrown Tomb
        1 Phyresis Outbreak
        1 Plains
        1 Polluted Delta
        1 Prologue to Phyresis
        1 Radstorm
        1 Raffine's Tower
        1 Rejuvenating Springs
        1 Rhystic Study
        1 Ripples of Potential
        1 Roaming Throne
        1 Sandsteppe Citadel
        1 Seaside Citadel
        1 Shalai, Voice of Plenty
        1 Skrelv, Defector Mite
        1 Smothering Tithe
        1 Sol Ring
        1 Spara's Headquarters
        1 Swamp
        1 Swords to Plowshares
        1 Tainted Observer
        1 Tamiyo, Field Researcher
        1 Teferi, Master of Time
        1 Tekuthal, Inquiry Dominus
        1 Temple Garden
        1 Tezzeret's Gambit
        1 The Millennium Calendar
        1 Thrummingbird
        1 Unnatural Restoration
        1 Venerated Rotpriest
        1 Verdant Catacombs
        1 Voidwing Hybrid
        1 Vorinclex, Monstrous Raider
        1 Vraska's Fall
        1 Vraska, Betrayal's Sting
        1 Vronos, Masked Inquisitor
        1 Watery Grave
        1 Windswept Heath
        1 Zagoth Triome
    """
    response = bot.request_openai(f"""
                                Suggest me list of 5 Magic the gathering cards in json format, that would upgrade my 
                                {commander} commander deck. And what cards to replace from the deck.
                                The deck contains this list of cards: {deck}, and the main focus on the upgrades should be on {aspect}
                                  """)
    # parse the response:
    cards = json.loads(response)

    # 
    print(json.dumps(cards, indent=4))

