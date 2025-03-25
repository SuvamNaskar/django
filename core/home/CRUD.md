# CRUD Operations

PS D:\codes\django\core> `py manage.py shell`

>>> from home.models import *<br>
>>> car = Car()<br>
>>> car.save()<br>
>>> car = Car(name="Nexon", speed=120)<br>
>>> car.save()<br>
>>> car        <br>
<Car: Car object (2)><br>
>>> car = Car(name="XUV 700", speed=160)<br>
>>> car<br>
<Car: Car object (None)><br>
>>> car.save()<br>
>>> car       <br>
<Car: Car object (3)><br>
>>> car_dict = {'name': 'Alto', 'speed': 60'}<br>
  File "<console>", line 1<br>
    car_dict = {'name': 'Alto', 'speed': 60'}<br>
                                           ^<br>
SyntaxError: unterminated string literal (detected at line 1)<br>
>>> car_dict = {'name': 'Alto', 'speed': 60} <br>
>>> Car.objects.create(**car_dict)<br>
<Car: Car object (4)><br>
>>> # read<br>
>>> <br>
>>> <br>
>>> cars = Car.objects.all()<br>
>>> cars = Car.objects.all()<br>
>>> cars<br>
<QuerySet [<Car: Car object (1)>, <Car: Car object (2)>, <Car: Car object (3)>, <Car: Car object (4)>]><br>
>>>  <br>
KeyboardInterrupt<br>
>>> exit<br>
Use exit() or Ctrl-Z plus Return to exit<br>
>>> ^Z<br>
<br>
now exiting InteractiveConsole...<br>
PS D:\codes\django\core> py manage.py shell<br>
<br>
>>> from home.models import *<br>
>>> cars = Car.objects.all() <br>
>>> cars<br>
<QuerySet [<Car: >, <Car: Nexon>, <Car: XUV 700>, <Car: Alto>]><br>
>>> for car in cars:<br>
...     print(f"Car: {car.name}, Speed: {car.speed}")<br>
... <br>
Car: , Speed: 60<br>
Car: Nexon, Speed: 120<br>
Car: XUV 700, Speed: 160<br>
Car: Alto, Speed: 60<br>
>>><br>
>>> <br>
>>> # update<br>
>>> <br>
>>> car = Car.objects.get(id = 1)<br>
>>> car.name = "Creta"<br>
>>> car.speed = 140    <br>
>>> car.save()<br>
>>> car<br>
<Car: Creta><br>
>>> cars = Car.objects.all()<br>
>>> for car in cars:         <br>
...     print(f"Car: {car.name}, Speed: {car.speed}")<br>
...                                <br>
Car: Creta, Speed: 140<br>
Car: Nexon, Speed: 120<br>
Car: XUV 700, Speed: 160<br>
Car: Alto, Speed: 60<br>
>>><br>
>>> <br>
>>> # delete<br>
>>> <br>
>>> Car.objects.get(id=1).delete()<br>
(1, {'home.Car': 1})<br>
>>> Car.objects.all()       <br>
<QuerySet [<Car: Nexon>, <Car: XUV 700>, <Car: Alto>]><br>
>>> Car.objects.all().delete()<br>
(3, {'home.Car': 3})<br>
>>> Car.objects.all()<br>
<QuerySet []><br>
>>><br>