# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import threading

# Флаг для завершения работы
should_exit = False

def input_thread():
    global should_exit
    input("Нажмите Enter, чтобы остановить робота и завершить выполнение программы...\n")
    should_exit = True

rospy.init_node(name="circle_movement")

# Создаем Publisher для управления роботом
cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Ввод радиуса круга и проверка корректности ввода
while True:
    try:
        radius = float(input("Введите радиус круга в метрах: "))  # Радиус круга
        if radius <= 0:
            print("Радиус должен быть положительным числом. Попробуйте еще раз.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите допустимое числовое значение.")

linear_speed = 0.25  # линейная скорость в м/с
angular_speed = linear_speed / radius  # угловая скорость для движения по кругу
# Выбор направления вращения
direction = input("Выберите направление вращения (2 - по часовой стрелке, 1 - против): ")
if direction == "1":
    angular_speed = -angular_speed  # Изменяем знак угловой скорости для вращения по часовой стрелке
def move_in_circle():
    global should_exit
    twist = Twist()

    # Настраиваем линейную и угловую скорости
    twist.linear.x = linear_speed
    twist.angular.z =-angular_speed

    while not rospy.is_shutdown() and not should_exit:
        cmd_pub.publish(twist)  # Публикуем команду движения
        rospy.sleep(0.1)  # Небольшая задержка для регулирования частоты публикации
    # Остановка робота после выхода из цикла
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    cmd_pub.publish(twist)  # Публикуем команду остановки

if __name__ == '__main__':
    try:
        # Запуск потока для ввода с клавиатуры
        thread = threading.Thread(target=input_thread)
        thread.start()

        move_in_circle()
    except rospy.ROSInterruptException:
        pass  # Завершение выполнения при исключении
    finally:
        print("Завершение программы.")
