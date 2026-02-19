from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# ReplyKeyboardMarkup (обычная клавиатура)
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кнопка 1"),
            KeyboardButton(text="Кнопка 2")
        ],
        [
            KeyboardButton(text="Кнопка 3"),
            KeyboardButton(text="Кнопка 4")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие"
)

# ReplyKeyboardMarkup с контактом и локацией
reply_keyboard_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер", request_contact=True)
        ],
        [
            KeyboardButton(text="Отправить локацию", request_location=True)
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

# InlineKeyboardMarkup
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кнопка 1", callback_data="button1"),
            InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
        ],
        [
            InlineKeyboardButton(text="Ссылка", url="https://example.com")
        ]
    ]
)


# ReplyKeyboardBuilder
def get_reply_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Кнопка 1"))
    builder.add(KeyboardButton(text="Кнопка 2"))
    builder.add(KeyboardButton(text="Кнопка 3"))
    builder.add(KeyboardButton(text="Кнопка 4"))
    builder.adjust(2, 2)
    return builder.as_markup(resize_keyboard=True)


# InlineKeyboardBuilder
def get_inline_keyboard_builder():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Кнопка 1", callback_data="btn1"))
    builder.add(InlineKeyboardButton(text="Кнопка 2", callback_data="btn2"))
    builder.add(InlineKeyboardButton(text="Кнопка 3", callback_data="btn3"))
    builder.add(InlineKeyboardButton(text="Кнопка 4", callback_data="btn4"))
    builder.adjust(2, 2)
    return builder.as_markup()


# InlineKeyboardBuilder с URL и другими типами
def get_mixed_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Ссылка", url="https://example.com"),
        InlineKeyboardButton(text="Профиль", url="tg://user?id=123456789")
    )
    builder.row(
        InlineKeyboardButton(text="Вперед", callback_data="next"),
        InlineKeyboardButton(text="Назад", callback_data="prev")
    )
    builder.row(
        InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    )
    return builder.as_markup()


# Клавиатура с динамическими кнопками
def get_dynamic_keyboard(items, row_width=2):
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.add(InlineKeyboardButton(text=item["text"], callback_data=item["callback"]))
    builder.adjust(row_width)
    return builder.as_markup()


# Клавиатура для пагинации
def get_pagination_keyboard(current_page, total_pages, prefix="page"):
    builder = InlineKeyboardBuilder()
    buttons = []

    if current_page > 1:
        buttons.append(InlineKeyboardButton(text="◀️", callback_data=f"{prefix}_prev_{current_page}"))

    buttons.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="current"))

    if current_page < total_pages:
        buttons.append(InlineKeyboardButton(text="▶️", callback_data=f"{prefix}_next_{current_page}"))

    builder.row(*buttons)
    builder.row(InlineKeyboardButton(text="Закрыть", callback_data="close"))

    return builder.as_markup()


# Клавиатура для выбора количества
def get_quantity_keyboard(item_id, current_quantity, min_qty=1, max_qty=10):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="➖", callback_data=f"dec_{item_id}_{current_quantity}"),
        InlineKeyboardButton(text=f"{current_quantity}", callback_data="current"),
        InlineKeyboardButton(text="➕", callback_data=f"inc_{item_id}_{current_quantity}")
    )
    builder.row(
        InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"confirm_{item_id}_{current_quantity}"),
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
    )
    return builder.as_markup()


# Удаление клавиатуры
from aiogram.types import ReplyKeyboardRemove

remove_keyboard = ReplyKeyboardRemove()