from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio
from BotToken import api

bot = Bot(token = api)

dp = Dispatcher(storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(Command('start'))
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, "Привет! Я бот помогающий твоему здоровью.\nДля подсчета нормы колорий введи /Calories")

@dp.message(Command('Calories'))
async def set_age(message: types.Message, state: FSMContext):
    await  bot.send_message(message.chat.id, "Введите свой возраст:")
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await bot.send_message(message.chat.id, "Введите свой рост:")
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await bot.send_message(message.chat.id, "Введите свой вес:")
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    summery_men = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    summery_women = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) - 161
    await bot.send_message(message.chat.id, f"Для мужчины норма калорий {summery_men}\nДля женщины норма калорий {summery_women}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
