import pandas as pd
import json
import re


def read(path: str) -> pd.DataFrame:
    data = []
    with open(path, "r", encoding="utf8") as file:
        for line in file:
            data.append(json.loads(line))

    return pd.DataFrame.from_records(data)


def _room_and_size(s, index=0, sep1=",", sep2=" "):
    if s is None:
        return

    try:
        return int(s.strip().split(sep1)[index].strip().split(sep2)[0])
    except IndexError:
        return


def _price(p):
    num_p = re.sub(r"\D", "", p.replace("\xa0", ""))
    if not num_p:
        return
    return int(num_p)


def pre_process(data: pd.DataFrame) -> pd.DataFrame:
    data.price = data.price.apply(_price)
    data["rooms"] = data.size_and_rooms.apply(lambda x: _room_and_size(x))
    data["surface"] = data.size_and_rooms.apply(lambda x: _room_and_size(x, index=1))
    data["city"] = data.location.apply(lambda x: x.split("à")[-1])
    data["district"] = data.location.apply(lambda x: x.split("à")[0])
    data.title = data.title.str.lower().str.strip()
    data.city = data.city.str.lower().str.strip()
    data.district = data.district.str.lower().str.strip()

    data.drop(columns=["location", "size_and_rooms", "images"], inplace=True)
    return data
