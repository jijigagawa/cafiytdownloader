from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Simdilik sadece tekli linkleri destekliyor  (playlist değil) sadece youtube linkini yolla"
    await message.reply_text(helptxt)
