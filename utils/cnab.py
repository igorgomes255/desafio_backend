from datetime import datetime


def cnab_parser(file_name):

    cnab_array = []

    path = file_name

    file = open(path)

    read_file = file.readlines()

    for lines in read_file:
        type = int(lines[0])
        date = lines[1:9]
        value = int(lines[9:19])
        cpf = lines[19:30]
        card = lines[30:42]
        hour = lines[42:48]
        owner_shop = lines[48:62]
        name_shop = lines[62:81]

        in_date = datetime.strptime(date, "%Y%m%d")
        formated_date = datetime.strftime(in_date, "%Y-%m-%d")

        formated_value = value / 100

        in_time = datetime.strptime(hour, "%H%M%S")
        formated_hour = datetime.strftime(in_time, "%H:%M:%S")

        new_obj = {
            "type": type,
            "date": formated_date,
            "value": formated_value,
            "cpf": cpf,
            "card": card,
            "hour": formated_hour,
            "owner_shop": owner_shop,
            "name_shop": name_shop,
        }

        cnab_array.append(new_obj)

    return cnab_array
