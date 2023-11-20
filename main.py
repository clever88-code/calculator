import tkinter as tk

def on_button_click(value):
    # Получаем текущий текст из виджета ввода
    current_text = entry.get()

    # Если нажата кнопка "C", очищаем поле ввода
    if value == 'C':
        entry.delete(0, tk.END)
    else:
        # Добавляем значение кнопки к текущему тексту в поле ввода
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + value)

def clear_entry():
    # Очищаем поле ввода
    entry.delete(0, tk.END)

def calculate():
    try:
        # Вычисляем результат выражения в поле ввода
        result = eval(entry.get())

        # Очищаем поле ввода и вставляем результат
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        # Если произошла ошибка при вычислении, показываем "Error"
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Создание главного окна
root = tk.Tk()
root.title("by clever")

# Создание виджета для ввода текста
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Определение кнопок для калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Расположение кнопок на сетке
row_val = 1
col_val = 0

for button in buttons:
    # Создание кнопки с текстом button и привязка соответствующей функции
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: on_button_click(b) if b != '=' else calculate() if b == '=' else clear_entry()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Запуск главного цикла
root.mainloop()
