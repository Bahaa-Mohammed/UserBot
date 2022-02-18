from userge import userge, Message

@userge.on_cmd("test", about="help text to this command")
async def test_cmd(message: Message):
   # some other stuff
   await message.edit("testing...")
   # some other stuff
