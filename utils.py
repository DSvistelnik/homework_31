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
