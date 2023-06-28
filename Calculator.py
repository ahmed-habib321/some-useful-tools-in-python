from tkinter import Button, Entry, Frame, Label, Tk, messagebox, StringVar, ttk

class Calculator:
    def __init__(self):
        self._title = "Calculator"
        self._height = 300
        self._width = 300
        self._x = int((1920 - self._width) / 2)
        self._y = int((1080 - self._height) / 2)
        self._frame = Tk()
    

    def set_title(self, title):
        self._title = title
        return self

    def set_size(self, *dimensions):
        if len(dimensions) == 1:
            self._height = dimensions[0]
            self._width = dimensions[0]
        elif len(dimensions) == 2:
            self._height = dimensions[0]
            self._width = dimensions[1]
        return self

    def set_frame_location(self, x, y):
        self._x = x
        self._y = y
        return self

    def _get_location(self):
        return "+" + str(self._x) + "+" + str(self._y)

    def create_form(self):
        self._frame.title(self._title)
        self._frame.geometry(str(self._width) + "x" + str(self._height) + self._get_location())
        self._frame.resizable(False, False)
        return self._frame

    def set_background_color(self, red, green, blue):
        self._frame.config(background="#%s%s%s" % (red, green, blue))
        return self


def make_space(frame, size):
    ttk.Label(frame, text=" ", font=("", size), background=frame["bg"]).pack()


def create_label(frame, size, text):
    return ttk.Label(frame, text=text, font=("", size), background=frame["bg"], foreground="white")


def create_button(frame, font, height, width, bg, fg, text, command):
    button = Button(frame, font=font, height=height, width=width, bg=bg, fg=fg, text=text, command=command)
    return button


try:
    frame = Calculator().set_background_color("00", "00", "00").set_size(330, 360).create_form()

    frame = Frame(frame)
    frame.grid(row=0, column=0, columnspan=5)

    ftt = ' None 25 bold '
    
    font_style = 'None 25 bold'

    v = StringVar()
    screen = Entry(frame, font=font_style, textvariable=v)
    screen.grid(row=0, column=0, columnspan=5, pady=10)
    
    def append_to_screen(s):
        if(s=='.' and v.get().__contains__('.')):
            return 

        v.set(v.get() + s)


    class CalculatorOperations:
        def __init__(self):
            self.num1 = None
            self.num2 = None
            self.operation = None

        def clear_calculator(self):
            v.set("")
            self.num1 = None
            self.num2 = None

        def set_operation(self, op):
            if self.num1 is not None:
                self.num2 = None
            self.num1 = float(screen.get())
            v.set("")
            self.operation = op

        def calculate(self):
            if self.operation == "+":
                return self.num1 + self.num2
            elif self.operation == "-":
                return self.num1 - self.num2
            elif self.operation == "*":
                return self.num1 * self.num2
            elif self.operation == "/":
                if self.num2 == 0:
                    v.set("Error divide by zero")
                    return 
                return self.num1 / self.num2
            elif self.operation == "x10":
                return self.num1 * pow(10, self.num2)
            else:
                return "Error"
                
        def show_result(self):
            if self.num2 is None:
                self.num2 = float(screen.get())
            else:
                self.num1 = float(screen.get())
            result = self.calculate()
            if result % 1 == 0:
                result = int(result)
            v.set(result)

    calculator = CalculatorOperations()

    button_width = 3
    button_height = 1
    button_background = "navy"
    button_foreground = "light blue"

    
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 7 ',
                  lambda: append_to_screen("7")).grid(row=1, column=0, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 8 ',
                  lambda: append_to_screen("8")).grid(row=1, column=1, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 9 ',
                  lambda: append_to_screen("9")).grid(row=1, column=2, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 4 ',
                  lambda: append_to_screen("4")).grid(row=2, column=0, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 5 ',
                  lambda: append_to_screen("5")).grid(row=2, column=1, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 6 ',
                  lambda: append_to_screen("6")).grid(row=2, column=2, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 1 ',
                  lambda: append_to_screen("1")).grid(row=3, column=0, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 2 ',
                  lambda: append_to_screen("2")).grid(row=3, column=1, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 3 ',
                  lambda: append_to_screen("3")).grid(row=3, column=2, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' 0 ',
                  lambda: append_to_screen("0")).grid(row=4, column=0, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, '00',
                  lambda: append_to_screen("00")).grid(row=4, column=1, sticky="nsew")
    create_button(frame, font_style, button_height, button_width, button_background, button_foreground, ' . ',
                  lambda: append_to_screen(".")).grid(row=4, column=2, sticky="nsew")

    # control btn
    create_button(frame, font=font_style, height=button_height, width=7, bg=button_background, fg=button_foreground, text='AC',
                  command=lambda: calculator.clear_calculator()).grid(row=1, column=3, columnspan=2, sticky="nsew")
    create_button(frame, font=font_style, height=button_height, width=button_width, bg=button_background, fg=button_foreground,
                  text='+', command=lambda: calculator.set_operation("+")).grid(row=3, column=3, sticky="nsew")
    create_button(frame, font=font_style, height=button_height, width=button_width, bg=button_background, fg=button_foreground,
                  text='-', command=lambda: calculator.set_operation("-")).grid(row=3, column=4, sticky="nsew")
    create_button(frame, font=font_style, height=button_height, width=button_width, bg=button_background, fg=button_foreground,
                  text='*', command=lambda: calculator.set_operation("*")).grid(row=2, column=3, sticky="nsew")
    create_button(frame, font=font_style, height=button_height, width=button_width, bg=button_background, fg=button_foreground,
                  text='/', command=lambda: calculator.set_operation("/")).grid(row=2, column=4, sticky="nsew")
    create_button(frame, font=font_style, height=button_height, width=button_width, bg=button_background, fg=button_foreground,
                  text='x10', command=lambda: calculator.set_operation("x10")).grid(row=4, column=3, sticky="nsew")
    create_button(frame, font=font_style, height=button_height, width=button_width, bg=button_background, fg=button_foreground,
                  text='=', command=lambda: calculator.show_result()).grid(row=4, column=4, sticky="nsew")

    frame.mainloop()

except Exception as e:
    print(e)
    input("Press Enter to exit")