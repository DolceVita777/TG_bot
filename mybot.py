

from aiogram import Bot, Dispatcher, executor, types

# init aiogram
bot = Bot(token="5694540297:AAFuLk8Je6mPFWgRFOf6iAp2d0Ko9S9i-3s")
dp = Dispatcher(bot)

@dp.message_handler()
async def gpt_answer(message: types.Message):
    # await message.answer(message.text)
    await message.answer("Vchu programyvannia and NEVER GIVE UP :)")

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)