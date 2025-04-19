#1. Tello Drone ile Bağlantı Kurma (DJI Tello SDK)

from djitellopy import Tello

tello = Tello()
tello.connect()
print(f"Battery: {tello.get_battery()}%")
#2. Tello Drone’u Uçurmak (Takeoff, Land)

tello.takeoff()
tello.move_up(50)
tello.land()
#3. DroneKit ile ArduPilot Bağlantısı

from dronekit import connect

vehicle = connect('127.0.0.1:14550', wait_ready=True)
print(f"GPS: {vehicle.location.global_frame}")
#4. Otonom Kalkış (DroneKit)

from dronekit import VehicleMode

vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
while not vehicle.armed:
    pass
vehicle.simple_takeoff(10)  # 10 metre
#5. Belirli Noktaya Gitme (GPS Koordinatı ile)

from dronekit import LocationGlobalRelative

target_location = LocationGlobalRelative(-35.363261, 149.165230, 10)
vehicle.simple_goto(target_location)
#6. Kamera Görüntüsü Alma (Tello)

import cv2

tello.streamon()
frame = tello.get_frame_read().frame
cv2.imshow("Tello", frame)
cv2.waitKey(0)
#7. Nesne Takibi (OpenCV ile Renk Takibi)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (100,150,0), (140,255,255))
#8. Yüz Tanıma ile Uçuş

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(frame, 1.3, 5)
#9. Lidar (Simülasyon) ile Engelden Kaçınma

if distance_sensor.read_distance() < 100:
    drone.move_right(50)
#10. Joystick ile Manuel Kontrol (pygame)

import pygame
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
#11. Uçuş Loglarını Kaydetme

with open("log.txt", "w") as f:
    f.write(str(vehicle.location.global_frame))
#12. GPS Rota Planlayıcı

waypoints = [(lat1, lon1), (lat2, lon2), (lat3, lon3)]
for wp in waypoints:
    vehicle.simple_goto(LocationGlobalRelative(wp[0], wp[1], 10))
#13. Tello ile 360° Dönme

tello.rotate_clockwise(360)
#14. Batarya İzleme

if tello.get_battery() < 20:
    tello.land()
#15. QR Kod ile Görev Tetikleme

import pyzbar.pyzbar as pyzbar

decoded = pyzbar.decode(frame)
for obj in decoded:
    print("QR Code:", obj.data)
#16. Sesli Komut ile Kontrol (Speech Recognition)

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
command = r.recognize_google(audio)
#17. Uçuş Verilerini Gerçek Zamanlı Grafikle Gösterme

import matplotlib.pyplot as plt

plt.plot(time_list, altitude_list)
plt.show()

#18. Termal Kamera ile Görüntü İşleme (simülasyon)

thermal_image = cv2.applyColorMap(frame, cv2.COLORMAP_JET)

#19. Arayüz ile Kontrol (Tkinter)
import tkinter as tk

def takeoff():
    tello.takeoff()
tk.Button(text="Takeoff", command=takeoff).pack()
tk.mainloop()

#20. ArduPilot MAVLink Mesajı Gönderme

from pymavlink import mavutil
master = mavutil.mavlink_connection('udp:127.0.0.1:14551')
master.mav.command_long_send(master.target_system, master.target_component,
 mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
 0, 1, 0, 0, 0, 0, 0, 0)