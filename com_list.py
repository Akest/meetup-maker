import csv

def get_meetups():
    rt = "Список встреч:\n"
    msg = "id: {id}. {name}\n{description}\nBy {a_login}. {cur_num}/{need_num}"
    with open('data.csv', 'r', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=';', lineterminator='\r')
        for row in r:
            m_id, login, name, description, need_num, cur_num = row
            m_str = msg.format(id=m_id, name=name, description=description,
                a_login=login, cur_num=cur_num, need_num=need_num)
            rt += m_str
            rt += "\n\n"
    return rt[:len(rt) - 1]

def com_list(message, com, bot):
    message_str = get_meetups()
    bot.send_message(message.chat.id, message_str)
    return True