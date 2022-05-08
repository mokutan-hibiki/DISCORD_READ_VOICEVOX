import discord

def HelpText():
    embed = discord.Embed(title="コマンド一覧",description="以下のように使用して下さい",color=discord.Colour.from_rgb(252, 3, 211))
    embed.add_field(name="`v_st`",value="読み上げを開始します。\nボイスチャンネルに接続していない場合エラーになります。",inline=False)
    embed.add_field(name="`v_end`",value="読み上げを終了します。。\n読み上げを開始していない場合エラーになります。",inline=False)
    embed.add_field(name="`v_ls`",value="ボイスIDの一覧を表示します。\n下のv_voコマンドで使用できるボイスIDが確認出来ます。",inline=False)
    embed.add_field(name="`v_vo`",value="読み上げボイスを変更出来ます。以下のように使用して下さい\n```v_voボイスID-スピード-ピッチ```",inline=False)
    embed.add_field(name="ボイスロイド",value="スピード,ピッチともに0.50から4.00まで有効です。(小数点2桁まで有効)",inline=False)
    embed.add_field(name="ソフトーク",value="スピード,ピッチともに0から300まで有効です。(整数のみ)",inline=False)
    embed.add_field(name="`v_lm`",value="読み上げ制限を変更します。\n```v_lm読み上げ上限数```",inline=False)
    embed.add_field(name="`v_dict`",value="辞書を追加します。\n```v_dict-文字-読み```",inline=False)
    return embed

def ReadStart(interaction: discord.Interaction):
    embed = discord.Embed(title="読み上げ開始",color=discord.Colour.from_rgb(3, 115, 252))
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.add_field(name="`ボイスチャンネル`",value=interaction.user.voice.channel.name)
    embed.add_field(name="`テストチャンネル`",value=interaction.channel.name)
    embed.add_field(name="`開始`",value=interaction.user.display_name)

    return embed

def ReadEnd(interaction: discord.Interaction):
    embed = discord.Embed(title="読み上げ終了",color=discord.Colour.from_rgb(149, 105, 245))
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.add_field(name="`終了`",value=interaction.user.display_name)

    return embed

def NoUserConnection():
    embed = discord.Embed(title="あなたはボイスチャンネルに接続していません。",color=discord.Colour.from_rgb(255, 0, 0))

    return embed

def NoReadStart():
    embed = discord.Embed(title="読み上げを開始して下さい",color=discord.Colour.from_rgb(255, 0, 0))

    return embed

def VoiceChange(voice,speed,pitch):
    embed = discord.Embed(title="ボイス設定を変更しました。",description=voice,color=discord.Colour.from_rgb(252, 82, 3))
    embed.add_field(name="速度",value=speed)
    embed.add_field(name="ピッチ",value=pitch)

    return embed

def DictionaryAdd(key,value):
    embed = discord.Embed(title="辞書を追加しました",color=discord.Colour.from_rgb(252, 82, 3))
    embed.add_field(name="文字",value=key)
    embed.add_field(name="読み",value=value)

    return embed
