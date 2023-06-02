from dotenv import load_dotenv
import os
import openai
import random

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

max_tokens = 300  # The maximum length of the model's responses

animals = [
    "Aardvark",
    "Ant eater",
    "Ape",
    "Baboon",
    "Badger",
    "Bat",
    "Bear",
    "Bee",
    "Bison",
    "Butterfly",
    "Camel",
    "Cat",
    "Cheetah",
    "Chicken",
    "Chimpanzee",
    "Crocodile",
    "Dolphin",
    "Dog",
    "Donkey",
    "Elephant",
    "Emu",
    "Fish",
    "Fox",
    "Frog",
    "Goat",
    "Goldfish",
    "Goose",
    "Giraffe",
    "Hamster",
    "Hare",
    "Hippopotamus",
    "Horse",
    "Hummingbird",
    "Iguana",
    "Kangaroo",
    "Koala",
    "Lemur",
    "Lizard",
    "Lion",
    "Monkey",
    "Mouse",
    "Mule",
    "Narwhal",
    "Ostrich",
    "Otter",
    "Peacock",
    "Penguin",
    "Pig",
    "Platypus",
    "Polar bear",
    "Rabbit",
    "Rat",
    "Reindeer",
    "Rhinoceros",
    "Scorpion",
    "Sea lion",
    "Seal",
    "Shark",
    "Sheep",
    "Snail",
    "Snake",
    "Spider",
    "Squirrel",
    "Tiger",
    "Turtle",
    "Vulture",
    "Whale",
    "Wolf",
    "Zebra",
]

def do(animal):
    if not animal:
        animal = random.choice(animals)
    prompt = f"please give me a fun fact about {animal}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=max_tokens
    )

    resp1 = response['choices'][0]['text']

    prompt2 = f'based on {resp1}, write a prompt for DALL-E to generate a funny picture about {animal} in cartoon style'

    response2 = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt2,
        temperature= 1,
        max_tokens=max_tokens
    )

    img_prompt = response2['choices'][0]['text'] + 'cartoon style, full body with background'
    #print(img_prompt)
    img_resp = openai.Image.create(
        prompt=img_prompt,
        n=1,
        size="512x512",
    )

    img = img_resp['data'][0]['url']

    return resp1, img

if __name__ == '__main__':
    do()