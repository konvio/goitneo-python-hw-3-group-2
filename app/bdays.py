from collections import defaultdict
from datetime import datetime, timedelta, date

from app.model import Contact


def get_next_week_bdays(contacts: list[Contact]) -> list[str]:
    bday_dict = defaultdict(list)
    for contact in contacts:
        if not contact.birthday:
            continue
        name = contact.name
        bday = contact.birthday
        bday_dict[(bday.month, bday.day)].append(name)

    res = []
    for day in [date.today() + timedelta(days=i) for i in range(7)]:
        names = bday_dict[(day.month, day.day)]
        if names:
            res.extend(names)
        
    return res