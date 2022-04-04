def join_get_params(message, com, bot):
    coms = com.split(';')
    if len(coms) != 1:
        bot.send_message(message.chat.id, 'Попробуйте !join id')
        return False
    id = coms[0].strip()
    if id.isdigit() is False:
        bot.send_message(message.chat.id, 'id должно быть числом')
        return False
    return [id]


def com_join(message, com, bot):
    p = join_get_params(message, com, bot)
    if p is False:
        return False
    id = p
    #new_client(id)
    return True
