# class Auth:
#     def __init__(self, Login):
#         self.login = Login

#     def Log(self):
#         return f"{self.login} bu sizning loginingiz"
    
# class Reg(Auth):
#     def __init__(self, Login, Email):
#         super().__init__(Login)
        
#         self.Email = Email

#     def Gmail(self):
#         return f"{self.Email} bu sizning emailingiz"
    
# obj = Reg('12345678LO' 'gamingalexuz@gmail.com')
# print(obj.Gmail())


# class Auth:
#     def __init__(self, Login):
#         self.login = Login

#     def Log(self):
#         return f"{self.login} bu sizning loginingiz"
    
# class Reg(Auth):
#     def __init__(self, Login, Email):
#         super().__init__(Login)
#         self.Email = Email

#     def Gmail(self):
#         return f"{self.Email} bu sizning emailingiz"
    
# class index(Reg):
#     def __init__(self, Login, Email, index):
#         super().__init__(Login, Email)
#         self.index = index

#     def ind(self):
#         return f"{self.index} bu sizning indexingiz"
    
# obj = index('12345678LO', 'gamingalexuz@gmail.com', "auth.html, index.html")
# print(obj.ind(), obj.Gmail())


# class Chart:
#     def __init__(self, person):
#         self.person = person

#     def People(self):
#         if self.person[2:] == "99":
#             return f"{self.person} bu odamni raqami 99 likdan boshlanadi"
#         else:
#             return f"{self.person} bu odamni raqami 99 likdan boshlanmaydi"
        
# obj = Chart("ad99")
# print(obj.People())

# class Math:
#     def __init__(self, math):
#         self.math = math

#     def Matem(self):
#         user_input = input("Python kalkulyator (exit uchun 'exit' kiriting): ")
#         if user_input.lower() == "exit":
#             print("Dasturdan chiqilmoqda...")
#             exit()

#         try:
#             num1, operation, num2 = user_input.split()
#             num1 = int(num1)
#             num2 = int(num2)

#             if operation == "➖" or operation == "-":
#                 return f"Natija: {num1 - num2}"
#             elif operation == "➕" or operation == "+":
#                 return f"Natija: {num1 + num2}"
#             elif operation == "✖️" or operation == "*":
#                 return f"Natija: {num1 * num2}"
#             elif operation == "➗" or operation == "/":
#                 if num2 == 0:
#                     return "Nolga bo'lish mumkin emas!"
#                 return f"Natija: {num1 / num2}"
#             else:
#                 return "Noto'g'ri amal kiritildi!"
#         except ValueError:
#             return "Xatolik: Iltimos, ikki son va amalni kiriting!"
#         except Exception as e:
#             return f"Xatolik: {e}"


# obj = Math(10)

# while True:
#     print(obj.Matem())


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Math:
    def __init__(self, math):
        self.math = math

    def Matem(self, user_input):
        try:
            num1, operation, num2 = user_input.split()
            num1 = int(num1)
            num2 = int(num2)

            if operation == "➖" or operation == "-":
                return f"Natija: {num1 - num2}"
            elif operation == "➕" or operation == "+":
                return f"Natija: {num1 + num2}"
            elif operation == "✖️" or operation == "*":
                return f"Natija: {num1 * num2}"
            elif operation == "➗" or operation == "/":
                if num2 == 0:
                    return "Nolga bo'lish mumkin emas!"
                return f"Natija: {num1 / num2}"
            else:
                return "Noto'g'ri amal kiritildi!"
        except ValueError:
            return "Xatolik: Iltimos, ikki son va amalni kiriting!"
        except Exception as e:
            return f"Xatolik: {e}"

def calculate():
    user_input = entry.get()
    result = obj.Matem(user_input)
    messagebox.showinfo("Natija", result)

root = tk.Tk()
root.title("Python Kalkulyatori")
root.geometry("400x400")
root.configure(bg="#2c3e50")

obj = Math(10)

header_label = tk.Label(root, text="Kalkulyator", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
header_label.pack(pady=20)

entry_label = tk.Label(root, text="Amalni kiriting):", font=("Helvetica", 14), fg="#ecf0f1", bg="#2c3e50")
entry_label.pack(pady=5)

entry = tk.Entry(root, font=("Helvetica", 14), width=20, justify="center", bd=5, relief="solid")
entry.pack(pady=10)

calculate_button = ttk.Button(root, text="Hisoblash", style="TButton", command=calculate)
calculate_button.pack(pady=20)

exit_button = ttk.Button(root, text="Chiqish", style="TButton", command=root.quit)
exit_button.pack()

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), background="#3498db", padding=10)
style.map("TButton", background=[("active", "#2980b9")])

root.mainloop()