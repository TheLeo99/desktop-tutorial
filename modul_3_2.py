def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if '@' not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if '@' not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Good Morning', 'f@gmail.com')
send_email('Good Morning', 'f@gmail.su')
send_email('Good Morning', 'f@gmail.com', sender='colledge.help@gmail.ru')
send_email('Good Morning', 'f@gmail.com', sender='university.help@gmail.su')
send_email('Good Morning', 'university.help@gmail.com', sender='university.help@gmail.com')
