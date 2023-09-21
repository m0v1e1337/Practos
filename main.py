#Площадь прямоугольника
def rectangle_area(width, height):
    area = width*height
    return area

w = 5
h = 10
result = rectangle_area(w, h)
print("Площадь прямоугольника равна:", result)

#True False
def if_else(num):
     if num % 2 == 0:
         return True
     else:
         return False

#Сумма
def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

number = 12345
sum = sum_digits(number)
print("Сумма цифр числа:", sum)