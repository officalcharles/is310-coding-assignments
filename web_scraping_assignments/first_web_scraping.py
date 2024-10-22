from bs4 import BeautifulSoup
import requests
import random

response = requests.get("https://batman.fandom.com/wiki/Category:Bat_Family")
soup = BeautifulSoup(response.text, "html.parser")
heroes = soup.find_all('a', class_="category-page__member-link")

responseV = requests.get("https://batman.fandom.com/wiki/Category:Villains")
soupV = BeautifulSoup(responseV.text, "html.parser")
villains = soupV.find_all('a', class_="category-page__member-link")

love_inst = requests.get("https://batman.fandom.com/wiki/Category:Love_Interests")
soupL = BeautifulSoup(love_inst.text, "html.parser")
lovers = soupL.find_all('a', class_="category-page__member-link")

hero = [char['title'] for char in heroes if "Category" or "Family" not in char['title']]
villain = [char['title'] for char in villains if "Category" not in char['title']]
lover = [char['title'] for char in lovers if "Category" or "Batman" not in char['title']]


random_hero = random.choice(hero)
random_villain = random.choice(villain)
random_love_interest = random.choice(lover)
print(f"In this exciting new story {random_hero} will take on")
print(f"{random_villain} and thwart {random_villain}'s diabolical plans!")
print(f"{random_hero} won't be alone! In this issue {random_love_interest} will look to acquire the caped crusader's heart!")