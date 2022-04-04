from data_main import write_row

def create_get_params(message, com, bot):
    coms = com.split(';')
    if len(coms) != 3:
        bot.send_message(message.chat.id, 'Попробуйте !create Название; Описание; Кол-во человек(число)')
        return False
    name, decr, num = coms[0].strip(), coms[1].strip(), coms[2].strip()
    if num.isdigit() is False:
        bot.send_message(message.chat.id, 'Попробуйте !create Название; Описание; Кол-во человек(число)')
        return False
    return [name, decr, num]


def com_create(message, com, bot):
    p = create_get_params(message, com, bot)
    if p is False:
        return False
    name, description, num = p
    login = message.from_user.username
    write_row(login, name, description, num)
    bot.send_message(message.chat.id, 'Встреча успешно создана!')
    return True