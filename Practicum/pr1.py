import pandas
data = pandas.read_csv('app_stats.csv')

payments = list(data['payments']) # список с числом платежей
installs = list(data['installs']) # список с числом установок

campaign_weeks = [7, 9, 13, 15, 17, 19, 29, 31, 33, 45]

installs_from_ads = []

for i in range(len(campaign_weeks)):
    installs_from_ads.append(installs[campaign_weeks[i]] - installs[campaign_weeks[i] - 1])


print(installs_from_ads) # выводим результаты на экран
