# Enes193 Library

## Package Download and Installation 
In this section, you will download the package and upload it to your microcontroller through Thonny IDE. 
1) To download the package, click the green  **<> Code** drop down at the top of the page. Then click **Download ZIP**.
2) Open Thonny and navigate to **Tools > Manage packages...**
3) Using **Install from local file**, find the file on your computer and upload it to your device.

## Usage
`from enes193.tank import tank`

To use the package, you have to direct the compiler to include it in your code. Add it manually by typing the above at the very top of your file.

## Functions
`tank.turn_off_motors()` sets the pwm of both motors to 0.

`tank.set_left_PWM(pwm)` sets motors on left speeds to specified pwm (pwm: -1023 to 1023).

`tank.set_right_PWM(pwm)` sets motors right speeds to specified pwm (pwm: -1023 to 1023).

`tank.read_distance_sensor()` reads and returns distance in centimeters.

`tank.set_servo(deg)` sets servo motor to specified angle (deg: 0-180).
