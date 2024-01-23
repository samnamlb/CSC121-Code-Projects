#
# Aleem Azimov
# 11/20/2022
# Application that calculates a customer's purchase.
#
import tkinter as tk
import tkinter.messagebox as mb


class CashRegisterGUI:
    def __init__(self):
        # Constants
        self.WB_COST = 8.50
        self.TB_COST = 24.00
        self.MAG_COST = 5.95
        self.DISCOUNT = 0.25

        self.main_window = tk.Tk()
        self.main_window.title('Cash Register')
        self.main_window.geometry('250x150')

        # Frames
        self.line1_frame = tk.Frame(self.main_window)
        self.line2_frame = tk.Frame(self.main_window)
        self.line3_frame = tk.Frame(self.main_window)
        self.line4_frame = tk.Frame(self.main_window)
        self.line5_frame = tk.Frame(self.main_window)
        self.line6_frame = tk.Frame(self.main_window)

        # Workbooks
        self.wb_label = tk.Label(self.line1_frame, text='Workbooks: ')
        self.wb_entry = tk.Entry(self.line1_frame, width=10)
        self.wb_label.pack(side='left')
        self.wb_entry.pack(side='left')

        # Textbooks
        self.tb_label = tk.Label(self.line2_frame, text='Textbooks: ')
        self.tb_entry = tk.Entry(self.line2_frame, width=10)
        self.tb_label.pack(side='left')
        self.tb_entry.pack(side='left')

        # Magazines
        self.mag_label = tk.Label(self.line3_frame, text='Magazines: ')
        self.mag_entry = tk.Entry(self.line3_frame, width=10)
        self.mag_label.pack(side='left')
        self.mag_entry.pack(side='left')

        # Checkbox discount
        self.discount_var = tk.IntVar()
        self.discount_check = tk.Checkbutton(self.line4_frame, text='25% Discount', variable=self.discount_var)
        self.discount_check.pack(side='left')

        # Total
        self.total_label = tk.Label(self.line5_frame, text='Total: ')
        self.total_value = tk.StringVar()
        self.total_result_label = tk.Label(self.line5_frame, textvariable=self.total_value)
        self.total_value.set('-------')
        self.total_label.pack(side='left')
        self.total_result_label.pack(side='left')

        # Calculate Total Button
        self.calc_total_button = tk.Button(self.line6_frame, text='Calculate', command=self.show_total)
        self.quit_button = tk.Button(self.line6_frame, text='Quit', command=self.main_window.destroy)
        self.calc_total_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()
        self.line4_frame.pack()
        self.line5_frame.pack()
        self.line6_frame.pack()

        tk.mainloop()

    def show_total(self):
        try:
            # Calculate total cost
            wb_count = int(self.wb_entry.get())
            tb_count = int(self.tb_entry.get())
            mag_count = int(self.mag_entry.get())
            discount_status = int(self.discount_var.get())

            total = (wb_count * self.WB_COST) + (tb_count * self.TB_COST) + (mag_count * self.MAG_COST)

            # if discount checked
            if discount_status == 1:
                total = total - (total * self.DISCOUNT)
            self.total_value.set(f'${total:.2f}')
        except ValueError:
            mb.showerror('Error', 'Please enter valid integers.')


start_program = CashRegisterGUI()
