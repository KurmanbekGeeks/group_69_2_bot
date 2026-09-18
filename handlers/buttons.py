from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def product_actions(product_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='✏️ Редактировать', callback_data=f'edit:{product_id}'), InlineKeyboardButton(text='Удалить', callback_data='')]
        ]
    )

# edit:1003

edit_fields = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Название', callback_data='field_name'),
         InlineKeyboardButton(text='Цена', callback_data='field_price')],
         [InlineKeyboardButton(text='Описание', callback_data='field_description'),
          InlineKeyboardButton(text='Категория', callback_data='field_category')]
    ]
)