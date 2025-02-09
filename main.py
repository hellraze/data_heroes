from datetime import datetime
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def date_to_weekday(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    weekday = date_obj.strftime('%A')
    return weekday

if __name__ == "__main__":

    df = pd.read_csv('data.csv')
    result = {}
    data = {}

    for row in df.iterrows():
        weekday = date_to_weekday(row[1]['event_date'])

        result[weekday] = [0, 0, 0]

    print(result)

    for row in df.iterrows():
        weekday = date_to_weekday(row[1]['event_date'])
        isAttend = row[1]['is_attend']

        if isAttend == 0:
            result[weekday][1] += 1
            result[weekday][2] += 1
        else:
            result[weekday][0] += 1
            result[weekday][2] += 1

    for day in result:
        data[day] = result[day][0] / result[day][2]

    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    values = [data[day] for day in days_order]

    sns.set_theme(style="whitegrid", palette="muted")

    plt.figure(figsize=(10, 6))
    colors = sns.color_palette("husl", len(days_order))  # Разные цвета

    sns.barplot(x=days_order, y=values, palette=colors)

    plt.xlabel("День недели", fontsize=14)
    plt.ylabel("Значение", fontsize=14)
    plt.title("Среднее значение посещений в день", fontsize=16)

    plt.show()

