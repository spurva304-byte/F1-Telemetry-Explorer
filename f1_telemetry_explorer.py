import fastf1
import matplotlib.pyplot as plt

session = fastf1.get_session(2024, 'São Paulo', 'R')
session.load()


results = session.results


print(results[['Position', 'FullName', 'TeamName']].head())

driver_laps = session.laps.pick_drivers('VER')

fastest_lap = driver_laps.pick_fastest()

print(fastest_lap[['LapTime', 'SpeedST']])

lap1 = session.laps.pick_driver('OCO').pick_fastest()
lap2 = session.laps.pick_driver('VER').pick_fastest()

tel1 = lap1.get_car_data().add_distance()
tel2 = lap2.get_car_data().add_distance()


plt.plot(tel1['Distance'], tel1['Speed'], label='Esteban')
plt.plot(tel2['Distance'], tel2['Speed'], label='Verstappen')

plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.title('Speed Comparison')
plt.show()
