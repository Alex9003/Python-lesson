# Повторення

[Markdown syntax](https://www.jetbrains.com/help/hub/markdown-syntax.html)

[GitHub Section links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#links)
### 1. Виведення даних

```hs 
print("Text")

print('Text1', 'Text2', 123)

print('Text: %s Number: %d' %('Text', 123))

-- Форматований текст
name = 'Jon' 
num = 123
print(f'Text {name}, Integer{num}')
```

__Так неправильно:__

> print "Text"

або

> print(y)


Буде помилка, перед виведенням змінна має бути визначена   

`NameError: name 'x' is not defined)`

### 2. Введення даних

```hs 
name = input('Введіть імя: ')

age = int(input('Введіть ваш вік: '))

nuber = float(input('Введіть дробове чиcло: '))
```

### 3. Арифметичні оператори

`+` додавання _6 + 3 = 9_

`-` віднімання _7 - 5 = 2_

`*` множення _6 * 2 = 12_

`/` ділення _10 / 2 = 5_

`//` цілочисельне ділення _11 // 3 = 3_

`%` залишок від ділення _11 % 3 = 2_

`**` піднесення до степеня _4 ** 2 = 16_

### 4. Оператори присвоювання 

`=` Присвоювання _a = 4_

`+=` Додавання з присвоюванням _a += 2 → a = a + 2_

`-=` Віднімання з присвоюванням _a −= 4 → a = a − 4_

`*=` Множення з присвоюванням _a *= 5 → a = a * 5_

`/=` Ділення із присвоюванням _a /= 6 → a = a / 6_

`%=` Залишок від ділення з присвоюванням _a %= 7 → a = a % 7_

`**=` Піднесення до степеня з присвоюванням	_a **= 8 → a = a ** 8_

### 5. Оператори порівняння 

`==` Дорівнює	_2 == 4 → False_

`!=` Не дорівнює	_2 != 5 → True_

`>` Більше ніж	_2 > 4 → False_

`<` Менше ніж	_2 < 4 → True_

`>=` Більше або Дорівнює	_2 >= 4 → False_

`<=` Менше або Дорівнює	_2 <= 4 → True_


### 6. Функції

> **int()**
>
>  `n = int("123")`
>
> **str()**
>
>  `string = str(555)`
>
> **float()**
>
>  `f = float("123.456")`
>


> **help()**
>
> `help(int)`
>
    class int(object)
        |  int([x]) -> integer
        |  int(x, base=10) -> integer
        |  Convert a number or string to an integer, or ...

### 7. Оператор умови

Оператор if використовується для перевірки умови: якщо умова виконується, ми виконуємо блок операторів (званий блоком if), інакше ми обробляємо інший блок операторів (званий блоком else).

```hs
a = 3
if a == 2:
    print('Yes')
else:
    print('No')
```
