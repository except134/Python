from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, CallbackQuery)
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
from BotToken import api

bot = Bot(token = api)

dp = Dispatcher(storage=MemoryStorage())

class UserState(StatesGroup):
    nostate = State()
    age = State()
    growth = State()
    weight = State()

keyboard_inline = InlineKeyboardBuilder()
button_inline1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_inline2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
keyboard_inline.add(button_inline1, button_inline2)

def add_buttons(name1, name2: str):
    button = [[KeyboardButton(text=f'{name1}'), KeyboardButton(text=f'{name2}')]]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True, one_time_keyboard=False)

@dp.message(Command('start'))
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, "Привет! Я бот помогающий твоему здоровью.", reply_markup=add_buttons("Рассчитать", "Информация."))

@dp.message(F.text == "Рассчитать")
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Выбери опцию:", reply_markup=keyboard_inline.as_markup())

@dp.callback_query(F.data == "main_menu")
async def main_menu2(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Выбери опцию:", reply_markup=keyboard_inline.as_markup())

@dp.message(F.text == "Информация")
async def info_message(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, 'Информация')

@dp.callback_query(F.data == "formulas")
async def formulas_message(callback: CallbackQuery, state: FSMContext):
    inline_back = InlineKeyboardBuilder()
    inline_back.add(
        InlineKeyboardButton(text="Назад в меню", callback_data="main_menu")
    )
    await callback.message.answer(text="для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
                                       "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161",
                                        reply_markup=inline_back.as_markup()
                                  )

@dp.callback_query(F.data == "calories")
async def calories_message(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите свой возраст:")
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
    await state.set_state(UserState.nostate)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
