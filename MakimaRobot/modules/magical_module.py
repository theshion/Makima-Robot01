from pyrogram import Client, filters
import random

# Replace this with your bot token
bot_token = "6572281811:AAFvA1ktlZJsz7vRh-Epdb-uOh3TB7qwXc8"

# Create a Pyrogram client
app = Client("my_bot", bot_token=bot_token)

# Define a command handler to cast a spell
@app.on_message(filters.command("castspell"))
async def cast_spell(_, message):
    mystical_responses = [
        "✨ You have summoned a magical aura of light! ✨",
        "🌟 A mystical door to another realm has opened before you! 🌟",
        "🔮 A swirling vortex of enchantment surrounds you! 🔮",
        "🌠 The stars above align to reveal a secret path of wonder! 🌠",
        "🪄 A burst of fairy dust and sparkles fills the air! 🪄",
    ]
    magical_response = random.choice(mystical_responses)

    await message.reply(magical_response)

# Start the bot
app.run()
