from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("iletisim", url="https://t.me/caferpazvant")],
        [InlineKeyboardButton(
            "Bug bildir 🎃", url="https://t.me/caferpazvant")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help komutunu daha fazla bilgi almak icin kullanabilirsin"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
