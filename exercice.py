#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    result = (a + b + c) / 3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degree = angle_degs + angle_mins / 60 + angle_secs / 3600
    rads = math.radians (degree)
    rads = round(rads, 3)
    return rads


def to_degrees(angle_rads: float) -> tuple:
   degree = math.degrees (angle_rads)
   angle_degs = round (degree)
   angle_mins = (degree - angle_degs) * 60
   angle_secs = round ((angle_mins - int (angle_mins)) * 60, 2)
   angle_mins = int (angle_mins)
   return angle_degs, angle_mins, angle_secs


def to_farenheit(temperature: float) -> float:
    result = (1.8 * temperature) + 32
    return result


def to_celsius(temperature: float) -> float:
    result = (temperature - 32) / 1.8 
    result = round(result, 1)
    return result


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
