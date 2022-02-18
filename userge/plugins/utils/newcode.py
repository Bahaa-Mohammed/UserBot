from userge import userge, Message, filters

@userge.on_filters(filters.me & filters.private)
async def test_filter(message: Message):
   # some other stuff
   await message.reply(f"you typed - {message.text}")
   # some other stuff
