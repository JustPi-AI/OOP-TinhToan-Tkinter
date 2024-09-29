import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
win = tk.Tk()
win.title("Tính toán")

# Hàm xử lý khi nhấn nút
def click_me():
    try:
        num1 = float(number.get())
        num2 = float(number1.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Không thể chia cho 0"
        else:
            result = "Phép tính không hợp lệ"

        ketqua_entry.config(state='normal')  # Cho phép chỉnh sửa để nhập kết quả
        ketqua_entry.delete(0, tk.END)       # Xóa dữ liệu cũ
        ketqua_entry.insert(0, str(result))  # Hiển thị kết quả
        ketqua_entry.config(state='readonly') # Đặt lại thành chỉ đọc
    except ValueError:
        ketqua_entry.config(state='normal')
        ketqua_entry.delete(0, tk.END)
        ketqua_entry.insert(0, "Lỗi nhập liệu")
        ketqua_entry.config(state='readonly')

# Ô nhập số đầu tiên
number = tk.StringVar()
number_entered = ttk.Entry(win, width=12, textvariable=number)
number_entered.grid(column=0, row=0)

# Ô nhập số thứ hai
number1 = tk.StringVar()
number_entered1 = ttk.Entry(win, width=12, textvariable=number1)
number_entered1.grid(column=0, row=1)

# Nút "Click Me"
action = tk.Button(win, text="Click Me", command=click_me)
action.grid(column=2, row=0)

# Ô chọn phép tính
operator = tk.StringVar()
operator_combobox = ttk.Combobox(win, width=10, textvariable=operator)
operator_combobox['values'] = ('+', '-', '*', '/')
operator_combobox.grid(column=2, row=1)
operator_combobox.current(0)

# Ô hiển thị kết quả
ketqua_label = tk.Label(win, text="Kết quả:")
ketqua_label.grid(column=1, row=0)

ketqua_entry = ttk.Entry(win, width=12, state='readonly')
ketqua_entry.grid(column=1, row=1)

# Chạy chương trình
win.mainloop()
