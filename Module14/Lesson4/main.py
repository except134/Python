from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, CallbackQuery, FSInputFile)
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio, os
from BotToken import api
from db import *

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

product_keyboard_inline = InlineKeyboardBuilder()
button_product1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_product2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_product3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_product4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
product_keyboard_inline.add(button_product1, button_product2, button_product3, button_product4)

def add_buttons(name1, name2, name3: str):
    button = [[KeyboardButton(text=f'{name1}'), KeyboardButton(text=f'{name2}')], [KeyboardButton(text=f'{name3}')]]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True, one_time_keyboard=False)

@dp.message(Command('start'))
async def start_message(message: types.Message):
    initiate_db()
    await bot.send_message(message.chat.id, "Привет! Я бот помогающий твоему здоровью.", reply_markup=add_buttons("Рассчитать", 
                                                                                                                  "Информация", 
                                                                                                                  "Купить"))

@dp.message(F.text == "Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выбери опцию:", reply_markup=keyboard_inline.as_markup())

@dp.message(F.text == "Информация")
async def info_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Информация')

@dp.message(F.text == "Купить")
async def buy_message(message: types.Message):
    for i in get_all_products():
        photo = FSInputFile(f"{i[4]}")
        await message.answer_photo(
            photo=photo,
            caption=f'{i[1]} '
                    f'| Описание: {i[2]} '
                    f'| Цена: {i[3]}'
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=product_keyboard_inline.as_markup())

@dp.callback_query(F.data == "main_menu")
async def main_menu2(callback: CallbackQuery):
    await callback.message.answer("Выбери опцию:", reply_markup=keyboard_inline.as_markup())

@dp.callback_query(F.data == "formulas")
async def formulas_message(callback: CallbackQuery):
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

@dp.callback_query(F.data == "product_buying")
async def send_confirm_message(callback: CallbackQuery):
    await bot.send_message(callback.message.chat.id, "Вы успешно купили продукт!")

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
