pythonfrom pyrogram import Client, filters
import random
# Replace this with your bot tokenbot_token = "YOUR_BOT_TOKEN"
# Create a Pyrogram client
app = Client("my_bot", bot_token=bot_token)
# Define a command handler to summon a mythical creature@app.on_message(filters.command("summon"))
async def summon_creature(_, message):    mythical_creatures = ["Unicorn", "Dragon", "Phoenix", "Griffin", "Mermaid", "Centaur", "Basilisk"]
    summoned_creature = random.choice(mythical_creatures)
    await message.reply(f"You have summoned a {summoned_creature}! ")
# Define a command handler to get a magical fortune@app.on_message(filters.command("fortune"))
async def get_magical_fortune(_, message):    magical_fortunes = [
        "A great adventure awaits you.",        "You will discover a hidden treasure.",
        "A powerful spell will change your destiny.",        "A mystical creature will guide you on a journey.",
        "Your dreams will come true with a touch of magic.",        "You are destined for greatness in a magical realm.",
    ]    random_fortune = random.choice(magical_fortunes)
    await message.reply(f" Magical Fortune: {random_fortune}")
# Start the bot
app.run()
