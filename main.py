from typing import Any
import aiohttp
import discord
import discord.message
import os
import toml

config: dict[str, Any] = {}

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message: discord.message.Message):
    if message.guild is not None:
        return

    user_id = config["discord"]["user_id"]

    if str(message.author.id) != user_id:
        return

    async with aiohttp.ClientSession() as http:
        for attachment in message.attachments:
            async with http.post(
                config["urlroulette"]["host"],
                data=attachment.url,
                headers={
                    "Authorization": "Secret " + config["urlroulette"]["secret"],
                    "User-Agent": f"discord2urlroulette ({user_id})",
                }
            ):
                await message.channel.send(f"done {attachment.id} on {message.id}")


def main():
    global config

    filename = os.getenv("CONFIG")

    if not filename:
        filename = "config.toml"

    print("config is " + filename)

    with open(filename, "r") as f:
        config = toml.load(f)

    client.run(config["discord"]["token"])


if __name__ == "__main__":
    main()
