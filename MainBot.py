import os
import discord
from discord import app_commands
from dotenv import load_dotenv

from Massage import MessageList


def main():
    load_dotenv()

    MY_GUILD = discord.Object(id=os.environ['MY_GUILD'])
    TOKEN = os.environ['TOKEN']
    APPLICATION_ID = os.environ['APPLICATION_ID']

    class MyClient(discord.Client):
        def __init__(self, *, intents: discord.Intents, application_id: int):
            super().__init__(intents=intents, application_id=application_id)
            self.tree = app_commands.CommandTree(self)

        async def setup_hook(self):
            self.tree.copy_global_to(guild=MY_GUILD)
            await self.tree.sync(guild=MY_GUILD)

    intents = discord.Intents.all()
    client = MyClient(intents=intents, application_id=APPLICATION_ID)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user} (ID: {client.user.id})')
        print('------')

    @client.tree.command()
    async def read_start(interaction: discord.Interaction):
        """読み上げを開始する"""

        user = interaction.user
        if user.voice is None:
            await interaction.response.send_message(embed=MessageList.NoUserConnection(), ephemeral=True)
            return

        await user.voice.channel.connect()
        await interaction.response.send_message(embed=MessageList.ReadStart(interaction))

    @client.tree.command()
    async def read_end(interaction: discord.Interaction):
        """読み上げを終了する"""

        user = interaction.user
        if user.guild.voice_client is None:
            await interaction.response.send_message(embed=MessageList.NoReadStart(), ephemeral=True)
            return

        await user.guild.voice_client.disconnect()
        await interaction.response.send_message(embed=MessageList.ReadEnd(interaction))

    # メッセージ受信時に動作する処理
    @client.event
    async def on_message(message):
        # メッセージの送信者がbotだった場合は無視
        if message.author.bot:
            return
        # メッセージの送信したサーバーのボイスチャンネルに切断していない場合は無視
        if message.guild.voice_client is None:
            return

        print(message.content)

    client.run(TOKEN)


if __name__ == "__main__":
    main()
