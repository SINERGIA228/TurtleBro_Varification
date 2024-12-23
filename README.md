<img src="https://user-images.githubusercontent.com/57194638/201707251-5aa29404-2494-4e16-be4a-0cd821a1c0d9.png" width="800" height="300">

# Основные материалы для работы с роботом

```
Введение в ROS - http://docs.voltbro.ru/starting-ros/
Образовательный портал с уроками ROS -  http://learn.voltbro.ru
Базовый мануал по старту работы с роботом - https://manual.turtlebro.ru/
Основной репозиторий - https://github.com/voltbro    
Параметры и настройка через launch -  https://manual.turtlebro.ru/paket-turtlebro/params
Подключение робота к Сети - https://manual.turtlebro.ru/pervoe-vklyuchenie-i-nastroika-robota/networking
```
## Основные команды для проверки роботоспособности робота:

Присвоенное имя робота в сети:	
```
echo $ROS_HOSTNAME
```
IP-адрес робота в сети роутера-полигона:	
```
hostname -I (ip a)
```
Название дистрибутива Linux:	
```
lsb_release -a
```
Кодовое имя сборки Linux:	
```
lsb_release -a
```
Версия интерпретатора Python3:	
```
python3 -V (python3 --version)
```
Версия библиотеки rospy:	
```
pip3 show rospy
```
Версия пакета turtlebro:
```
rosversion turtlebro
```
Версия прошивки микроконтроллера материнской платы:	
```
rosservice call /board_info "request: {}"
```
Серийный номер системной платы робота (mcu_id):	
```
rosservice call /board_info "request: {}"
```
Размер оперативной памяти (Мбайт):
```
free -h
```
Текущий часовой пояс на роботе в формате “Time zone:Continent/City (XXX, +XXXX)”:
```
timedatectl | grep zone
```
Версия образа ОС, установленной на Raspberry Pi:
```
cat /boot/version
```
Топики из инструкции к роботу присутствуют на роботе:	
```
rostopic list
```
Температура процессора в градусах (С):	
```
vcgencmd measure_temp
```
Температура входит в указанный в Акте диапазон температур:	
```
vcgencmd measure_temp
```
Максимальное разрешение камеры (пикселей):	
```
v4l2-ctl --list-formats-ext
```
Значение напряжения аккумуляторной сборки из топика батареи:	
```
rostopic echo /bat -n 1 | grep voltage
```
Камера работоспособна,Одометрия корректна при линейном движении робота,Одометрия корректна при угловом вращении робота:	
```
через веб-интерфейс ip:8080
```
Проверка работы IMU-датчика:	
```
rostopic echo /imu -n 1
```
Проверка работы датчика-Lidar:	
```
rostopic echo /scan -n 1
```
Проверка работы подсветки робота:	
```
FastLed 30 пин 24 светодиода
скетч проверки работы светодиодной ленты- fastledTurtleBro.ino
```
Работоспособность кнопок D22-D25 можно проверисть с помощью примера библиотеки digital программы arduino IDE
