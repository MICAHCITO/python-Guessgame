
# import random as rand
# Greetings = [
#     'Howdy {}, you good?',
#     'Hello {}, how you?',
#     'Good day {}',
#     'Whats up, {}?'
# ]
# Greetings_size =range(1, len(Greetings) + 1)
# Greetings_dict = dict(zip(Greetings_size, Greetings))


# def choose_random_templete()->str:
#     random_num = rand.choice(Greetings_size)
#     return Greetings_dict[random_num]


# def choose_selected()->str:
#     try:
#        pick = int(input(f'Enter a number between 1 and {max(Greetings_size)}: '))
#        greeting = Greetings_dict[pick]
#     except ValueError:
#         print('Enter a digit')
#     except IndexError:
#         print('Digit not included in the system')
#     else:
#         return greeting
#     # finally:
#     #     print('Sorry you have to enter a digit')    

# def run_all()-> None:
#     name = input('Enter your name: ')
#     if not name:
#         return
#     try:
#         your_choice = int(input('Choose 1 for random and 2 for selected greeting: '))
#     except ValueError:
#         print('Enter a digit')
#         return
#     if your_choice == 1:
#         random_message = choose_random_templete()
#         print(random_message.format(name))

#     elif your_choice == 2:
#         selected_message = choose_selected()
#         print(selected_message.format(name))
#     else:
#         print('You need to select 1 or 2')

# run_all()

import random as rand
import tkinter as tk
from tkinter import messagebox

Greetings = [
    'Howdy {}, you good?',
    'Hello {}, how you?',
    'Good day {}',
    'Whats up, {}?'
]
Greetings_size = range(1, len(Greetings) + 1)
Greetings_dict = dict(zip(Greetings_size, Greetings))


def choose_random_templete() -> str:
    random_num = rand.choice(Greetings_size)
    return Greetings_dict[random_num]


def choose_selected(pick) -> str:
    try:
        greeting = Greetings_dict[pick]
    except IndexError:
        messagebox.showerror('Error', 'Digit not included in the system')
    else:
        return greeting


def run_all():
    name = name_entry.get()
    if not name:
        messagebox.showerror('Error', 'Please enter your name')
        return

    try:
        your_choice = int(choice_entry.get())
    except ValueError:
        messagebox.showerror('Error', 'Enter a digit')
        return

    if your_choice == 1:
        random_message = choose_random_templete()
        messagebox.showinfo('Random Greeting', random_message.format(name))
    elif your_choice == 2:
        try:
            pick = int(pick_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Enter a digit')
            return
        if pick not in Greetings_size:
            messagebox.showerror('Error', 'Please enter a valid number between 1 and {}'.format(max(Greetings_size)))
            return
        selected_message = choose_selected(pick)
        if selected_message:
            messagebox.showinfo('Selected Greeting', selected_message.format(name))
    else:
        messagebox.showerror('Error', 'You need to select 1 or 2')


# Creating the main window
root = tk.Tk()
root.title("Greetings App")

# Creating and placing widgets
name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

choice_label = tk.Label(root, text="Choose 1 for random and 2 for selected greeting:")
choice_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

choice_entry = tk.Entry(root)
choice_entry.grid(row=1, column=1, padx=5, pady=5)

pick_label = tk.Label(root, text="Enter a number between 1 and {}: ".format(max(Greetings_size)))
pick_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

pick_entry = tk.Entry(root)
pick_entry.grid(row=2, column=1, padx=5, pady=5)

run_button = tk.Button(root, text="Run", command=run_all)
run_button.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
