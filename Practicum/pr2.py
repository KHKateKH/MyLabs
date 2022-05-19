import pandas

data = pandas.read_csv('app_stats.csv')

installs = list(data['installs'])
payments = list(data['payments'])

print(600*payments[-8] / installs[-8])  
print(600*payments[-7] / installs[-7])  
print(600*payments[-6] / installs[-6])  
print(600*payments[-5] / installs[-5])  
print(600*payments[-4] / installs[-4])  
print(600*payments[-3] / installs[-3])  
print(600*payments[-2] / installs[-2])  
print(600*payments[-1] / installs[-1])  
