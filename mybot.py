

from aiogram import Bot, Dispatcher, executor, types

# init aiogram
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def gpt_answer(message: types.Message):
    # await message.answer(message.text)
    await message.answer("Vchu programyvannia and NEVER GIVE UP :)")

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
