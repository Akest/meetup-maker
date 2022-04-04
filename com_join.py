def join_get_params(message, com, bot):
    coms = com.split(';')
    if len(coms) != 1:
        bot.send_message(message.chat.id, 'Попробуйте !join id')
        return False
    meetup_id = coms[0].strip()
    if meetup_id.isdigit() is False:
        bot.send_message(message.chat.id, 'id должно быть числом')
        return False
    return meetup_id


def com_join(message, com, bot):
    p = join_get_params(message, com, bot)
    if p is False:
        return False
    meetup_id = p
    #new_member(meetup_id)
    return True
