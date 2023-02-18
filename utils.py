import csv
import json
import os

ads_csv = os.path.join("datasets", "ad.csv")
ads_json = os.path.join("fixtures", "ad.json")
categories_csv = os.path.join("datasets", "category.csv")
categories_json = os.path.join("fixtures", "category.json")
location_csv = os.path.join("datasets", "location.csv")
user_csv = os.path.join("datasets", "user.csv")
location_json = os.path.join("fixtures", "location.json")
user_json = os.path.join("fixtures", "user.json")


def category_to_json(csv_file, json_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            data_dict = {"model": "ads.category", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


def ads_to_json(csv_file, json_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            if rows["is_published"] == "TRUE":
                rows["is_published"] = True
            else:
                rows["is_published"] = False

            data_dict = {"model": "ads.advertisement", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


def location_to_json(csv_file, json_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            data_dict = {"model": "users.location", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


def user_to_json(csv_file, json_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            # del rows["id"]
            data_dict = {"model": "users.user", "pk": rows["id"], "fields": rows}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


location_to_json(location_csv, location_json)
user_to_json(user_csv, user_json)
ads_to_json(ads_csv, ads_json)
category_to_json(categories_csv, categories_json)
