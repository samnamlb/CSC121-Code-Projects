#
# Aleem Azimov
# 11/20/2022
# Grade calculator GUI Application, uses Frames, Labels, Entry, and Buttons.
#
import tkinter as tk


class GradeCalcGUI:
    def __init__(self):
        # Grade average constants
        self.TEST_WEIGHT = 0.20
        self.LAB_WEIGHT = 0.30
        self.EXAM_WEIGHT = 0.50

        self.main_window = tk.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')

        # Frames
        self.line1_frame = tk.Frame(self.main_window)
        self.line2_frame = tk.Frame(self.main_window)
        self.line3_frame = tk.Frame(self.main_window)
        self.line4_frame = tk.Frame(self.main_window)
        self.line5_frame = tk.Frame(self.main_window)

        # Tests grade
        self.test_label = tk.Label(self.line1_frame, text='Tests Grade: ')
        self.test_entry = tk.Entry(self.line1_frame, width=10)
        self.test_label.pack(side='left')
        self.test_entry.pack(side='left')

        # Lab grade
        self.lab_label = tk.Label(self.line2_frame, text='Labs Grade: ')
        self.lab_entry = tk.Entry(self.line2_frame, width=10)
        self.lab_label.pack(side='left')
        self.lab_entry.pack(side='left')

        # Exams grade
        self.exams_label = tk.Label(self.line3_frame, text='Exams Grade: ')
        self.exams_entry = tk.Entry(self.line3_frame, width=10)
        self.exams_label.pack(side='left')
        self.exams_entry.pack(side='left')

        # Average
        self.avg_label = tk.Label(self.line4_frame, text='Grade Average: ')
        self.avg_value = tk.StringVar()
        self.avg_result_label = tk.Label(self.line4_frame, textvariable=self.avg_value)
        self.avg_value.set('-------')
        self.avg_label.pack(side='left')
        self.avg_result_label.pack(side='left')

        # Calculate Avg Button
        self.calc_avg_button = tk.Button(self.line5_frame, text='Calculate', command=self.show_average)
        self.quit_button = tk.Button(self.line5_frame, text='Quit', command=self.main_window.destroy)
        self.calc_avg_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()
        self.line4_frame.pack()
        self.line5_frame.pack()

        tk.mainloop()

    def show_average(self):
        try:
            # Calculate average
            test = float(self.test_entry.get())
            lab = float(self.lab_entry.get())
            exams = float(self.exams_entry.get())
            calc_grade_avg = (test * self.TEST_WEIGHT) + (lab * self.LAB_WEIGHT) + (exams * self.EXAM_WEIGHT)
            grade_avg = float(format(calc_grade_avg, '.1f'))

            if grade_avg >= 90:
                letter_grade = 'A'
            elif grade_avg >= 80:
                letter_grade = 'B'
            elif grade_avg >= 70:
                letter_grade = 'C'
            elif grade_avg >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'

            self.avg_value.set(f'{grade_avg} ({letter_grade})')
        except ValueError:
            self.avg_value.set('Error')


grade_calc = GradeCalcGUI()
