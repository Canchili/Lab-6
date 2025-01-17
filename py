import tkinter as tk
from tkinter import messagebox


def setup_entries():
    for widget in frame_objects.winfo_children():
        widget.destroy()

    try:
        num_objects = int(entry_num_objects.get())
        if num_objects < 2:
            messagebox.showerror("Ошибка", "Число объектов должно быть не меньше 2.")
            return
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число объектов.")
        return

    for i in range(num_objects):
        tk.Label(frame_objects, text=f"Введите имя объекта {i + 1}:").pack()
        entry_name = tk.Entry(frame_objects)
        entry_name.pack()

        tk.Label(frame_objects, text=f"Введите стоимость объекта {i + 1}:").pack()
        entry_price = tk.Entry(frame_objects)
        entry_price.pack()
        entries.append((entry_name, entry_price))

    tk.Label(frame_objects, text="Введите количество дней:").pack()
    entry_days.pack()

    btn_calculate.pack()


def calculate():
    try:
        days = int(entry_days.get())
        totals = []

        for name, price_entry in entries:
            name_value = name.get()
            price_value = float(price_entry.get())
            totals.append((name_value, price_value * days))

        cheapest = min(totals, key=lambda x: x[1])

        savings_info = []
        for item in totals:
            if item != cheapest:
                savings = item[1] - cheapest[1]
                savings_info.append(f"{item[0]}: сэкономите {savings:.2f}")

        savings_message = "\n".join(savings_info) if savings_info else "Нет других объектов для сравнения."

        message = (f"{cheapest[0]} является самым выгодным. Общая стоимость: {cheapest[1]:.2f}.\n"
                   f"Сравнение с другими объектами:\n{savings_message}")
        messagebox.showinfo("Результат", message)

    except ValueError:
        messagebox.showerror("Ошибка", "Убедитесь, что все стоимости и дни введены корректно.")


# Создание главного окна
root = tk.Tk()
root.title("Расчет стоимости")

# Ввод количества объектов
tk.Label(root, text="Введите количество объектов для сравнения:").pack()
entry_num_objects = tk.Entry(root)
entry_num_objects.pack()

btn_setup = tk.Button(root, text="Установить объекты", command=setup_entries)
btn_setup.pack()

# Фрейм для объектов
frame_objects = tk.Frame(root)
frame_objects.pack()

# Ввод количества дней
entry_days = tk.Entry(root)

# Кнопка для расчёта
btn_calculate = tk.Button(root, text="Рассчитать", command=calculate)

# Список для хранения введенных объектов
entries = []

# Запуск приложения
root.mainloop()
