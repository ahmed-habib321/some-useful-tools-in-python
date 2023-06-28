from tkinter import *
from tkinter import ttk
from tkinter import messagebox




def msg(message):
    """Displays a messagebox with an error message."""
    messagebox.showinfo("Error", message)


def dye(form, red, green, blue):
    """Changes the background color of a form to the specified RGB value."""
    form.config(background="#%02x%02x%02x" % (red, green, blue))

def make_space(frame, size):
    """Creates empty space in a frame of a specified size."""
    Label(frame, text=" ", font=("", size), background=frame["bg"]).pack()

def strVar(value=""):
    """Creates and returns a StringVar object with an initial value."""
    return StringVar(value=value)

def intVar(value=0):
    """Creates and returns an IntVar object with an initial value."""
    return IntVar(value=value)


def boolVar(value=False):
    """Creates and returns a BooleanVar object with an initial value."""
    return BooleanVar(value=value)

def digits(text):
    """Checks if a string consists only of digits or is empty."""
    return str.isdigit(text) or text == ''


def form(height, title="", is_center=True, width=0):
    """
    Creates a new Tk form window with the specified height, title, and width.

    Arguments:
    - height: The height of the form.
    - title: The title of the form (default is an empty string).
    - is_center: A boolean indicating whether the form should be centered on the screen (default is True).
    - width: The width of the form (default is 0, which means the form width will be the same as the height).

    Returns:
    - The created Tk form window.
    """
    f = Tk()
    f.title(title)
    f.resizable(False, False)
    if width == 0:
        f.geometry("%dx%d" % (height, height))
    else:
        f.geometry("%dx%d" % (width, height))
    if is_center:
        center(f)
    return f

def Toplvl(height, title="", is_center=True, width=0):
    """
    Creates a new Toplevel window with the specified height, title, and width.

    Arguments:
    - height: The height of the Toplevel window.
    - title: The title of the Toplevel window (default is an empty string).
    - is_center: A boolean indicating whether the Toplevel window should be centered on the screen (default is True).
    - width: The width of the Toplevel window (default is 0, which means the window width will be the same as the height).

    Returns:
    - The created Toplevel window.
    """
    f = Toplevel()
    f.title(title)
    if width == 0:
        f.geometry("%dx%d" % (height, height))
    else:
        f.geometry("%dx%d" % (width, height))
    if is_center:
        center(f)
    return f

def frame(form, bg=None):
    """
    Creates a new frame inside a specified form.

    Arguments:
    - form: The form in which the frame should be created.
    - bg: The background color of the frame (default is None, which means it will inherit the background color of the form).

    Returns:
    - The created frame.
    """
    if bg is not None:
        return Frame(form, bg=bg)
    else:
        return Frame(form)


def button(form, text=' Button ', command=None):
    """
    Creates a new button inside a specified form.

    Arguments:
    - form: The form in which the button should be created.
    - text: The text displayed on the button (default is ' Button ').
    - command: The function to be called when the button is clicked (default is None).

    Returns:
    - The created button.
    """
    btn = ttk.Button(form, text=text)
    if command is not None:
        btn.config(command=command)
    return btn


def label(form, text='Label'):
    """
    Creates a new label inside a specified form.

    Arguments:
    - form: The form in which the label should be created.
    - text: The text displayed on the label (default is 'Label').

    Returns:
    - The created label.
    """
    return ttk.Label(form, text=text)


def textbox(form, variable=None, is_number_only=False, read_only=False):
    """
    Creates a new textbox (Entry widget) inside a specified form.

    Arguments:
    - form: The form in which the textbox should be created.
    - variable: The variable associated with the textbox (default is None).
    - is_number_only: A boolean indicating whether the textbox should only accept numeric input (default is False).
    - read_only: A boolean indicating whether the textbox should be read-only (default is False).

    Returns:
    - The created textbox.
    """
    reg = form.register(digits)
    txt = ttk.Entry(form)
    if is_number_only:
        txt.config(validate='key', validatecommand=(reg, "%P"))
    if variable is not None:
        txt.config(textvariable=variable)
    if read_only:
        txt.config(state="readonly")
    return txt

def passwordbox(form, variable=None):
    """
    Creates a new password entry textbox (Entry widget) inside a specified form.

    Arguments:
    - form: The form in which the password entry textbox should be created.
    - variable: The variable associated with the password entry textbox (default is None).

    Returns:
    - The created password entry textbox.
    """
    txt = textbox(form=form, variable=variable, is_number_only=False, read_only=False)
    txt.config(show="•")
    return txt

def radio(form, text='Radio', value=0, variable=None):
    """
    Creates a new radio button inside a specified form.

    Arguments:
    - form: The form in which the radio button should be created.
    - text: The text displayed next to the radio button (default is 'Radio').
    - value: The value associated with the radio button (default is 0).
    - variable: The variable associated with the radio button (default is None).

    Returns:
    - The created radio button.
    """
    rdo = ttk.Radiobutton(form, text=text, value=value)
    if variable is not None:
        rdo.config(variable=variable)
    return rdo


def checkbox(form, text=' CheckBox ', variable=None):
    """
    Creates a new checkbox inside a specified form.

    Arguments:
    - form: The form in which the checkbox should be created.
    - text: The text displayed next to the checkbox (default is ' CheckBox ').
    - variable: The variable associated with the checkbox (default is None).

    Returns:
    - The created checkbox.
    """
    cbx = ttk.Checkbutton(form, text=text)
    if variable is not None:
        cbx.config(variable=variable)
    return cbx


def combobox(form, values=None, readonly=False):
    """
    Creates a new combobox (dropdown menu) inside a specified form.

    Arguments:
    - form: The form in which the combobox should be created.
    - values: The values to be displayed in the combobox (default is None).
    - readonly: A boolean indicating whether the combobox should be read-only (default is False).

    Returns:
    - The created combobox.
    """
    cbx = ttk.Combobox(form)
    if values is not None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state='readonly')
    return cbx


def listbox(form, values=None):
    """
    Creates a new listbox inside a specified form.

    Arguments:
    - form: The form in which the listbox should be created.
    - values: The values to be displayed in the listbox (default is None).

    Returns:
    - The created listbox.
    """
    lbx = Listbox(form)
    if values is not None:
        i = 0
        for x in values:
            lbx.insert(i, x)
            i += 1
    return lbx


def center(form: Tk):
    """
    Centers a specified form on the screen.

    Arguments:
    - form: The form to be centered.
    """
    form.update()
    fw = form.winfo_width()
    fh = form.winfo_height()
    sw = form.winfo_screenwidth()
    sh = form.winfo_screenheight()
    x = (sw - fw) / 2
    y = (sh - fh) / 2
    form.geometry('%dx%d+%d+%d' % (fw, fh, x, y))


def bgall(form: Tk, bg):
    """
    Sets the background color of a specified form and all its child widgets.

    Arguments:
    - form: The form whose background color should be set.
    - bg: The background color to be set (in hexadecimal format, e.g., '#RRGGBB').
    """
    form.update()
    ctrls = form.winfo_children()
    form.config(bg=bg)
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            bgall(c, bg)
        if ci == 'Label' or ci == 'Button' or ci == 'Entry' or ci == 'Radiobutton':
            c['bg'] = bg
        if ci == 'TLabel' or ci == 'TButton' or ci == 'TEntry' or ci == 'TRadiobutton' or ci == 'TCheckbutton' or ci == "TFrame":
            my = ttk.Style()
            my.configure('TLabel', background=bg)
            my.configure('TButton', background=bg)
            my.configure('TEntry', background=bg)
            my.configure('TFrame', background=bg)
            my.configure('TRadiobutton', background=bg)
            my.configure('TCheckbutton', background=bg)


def fgall(form, fg):
    """
    Sets the foreground color of a specified form and all its child widgets.

    Arguments:
    - form: The form whose foreground color should be set.
    - fg: The foreground color to be set (in hexadecimal format, e.g., '#RRGGBB').
    """
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            fgall(c, fg)
        if ci == 'Label' or ci == 'Button' or ci == 'Entry' or ci == 'Radiobutton':
            c['fg'] = fg
        if ci == 'TLabel' or ci == 'TButton' or ci == 'TEntry' or ci == 'TRadiobutton' or ci == 'TCheckbutton' or ci == "TFrame":
            my = ttk.Style()
            my.configure('TLabel', foreground=fg)
            my.configure('TButton', foreground=fg)
            my.configure('TEntry', foreground=fg)
            my.configure('TFrame', foreground=fg)
            my.configure('TRadiobutton', foreground=fg)
            my.configure('TCheckbutton', foreground=fg)






def set_font_all(form, font):
    """
    Set the font for all relevant widgets in a form.

    Args:
        form (Tk or Toplevel): The form for which to set the font.
        font (str): The font configuration to apply.
    """
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            set_font_all(c, font)
        if ci in ['Label', 'Button', 'Entry', 'Radiobutton', 'TEntry']:
            c['font'] = font
        if ci in ['TLabel', 'TButton', 'TRadiobutton', 'TCheckbutton']:
            my_style = ttk.Style()
            my_style.configure('TLabel', font=font)
            my_style.configure('TButton', font=font)
            my_style.configure('TRadiobutton', font=font)
            my_style.configure('TCheckbutton', font=font)


def justify_all(form, justify):
    """
    Set the text justification for all relevant widgets in a form.

    Args:
        form (Tk or Toplevel): The form for which to set the text justification.
        justify (str): The text justification to apply.
    """
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            justify_all(c, justify)
        if ci == 'Entry':
            c['justify'] = justify
        if ci == 'TEntry':
            c.config(justify=justify)


def check_entry(txt: Entry, f: Toplevel, sv: StringVar):
    """
    Check if the entry field is empty and display a warning if necessary.

    Args:
        txt (Entry): The entry field to check.
        f (Toplevel): The parent top-level window.
        sv (StringVar): The StringVar associated with the entry field.
    """
    if txt.get().strip() == "":
        messagebox.showwarning("Warning", "You have not entered anything.")
        sv.set("")
        txt.focus()
    else:
        f.destroy()


def create_input_box(text: str, number_only=False):
    """
    Create an input box window.

    Args:
        text (str): The title of the input box.
        number_only (bool, optional): Specify if only numbers are allowed in the input. Defaults to False.

    Returns:
        str: The value entered in the input box.
    """
    f = Toplevel()
    f.title(text)
    f.geometry(str(TOOL_INPUT_WIDTH) + "x" + str(TOOL_INPUT_HEIGHT))
    f.resizable(False, False)
    center(f)
    ttk.Label(f, text=text, font=TOOL_FONT, background="#EEEEEE", foreground="black").pack(pady=10)
    sv = StringVar()
    txt = ttk.Entry(f, font=TOOL_FONT, width=35, textvariable=sv, foreground="black")

    if number_only:
        reg = f.register(digits)
        txt.config(validate='key', validatecommand=(reg, "%P"))

    txt.pack(pady=10)
    txt.bind('<Return>', lambda my: check_entry(txt, f, sv))
    ttk.Style().configure('in.TButton', font=TOOL_FONT)
    ttk.Button(f, text=' OK ', command=lambda: check_entry(txt, f, sv), style="in.TButton").pack(pady=10)
    f.grab_set()
    txt.focus()
    f.wait_window()
    return sv.get()


def create_table(frame, header, matrix: list, even_color, odd_color):
    """
    Create a table inside a frame.

    Args:
        frame (Frame): The frame in which to create the table.
        header (list): The header row of the table.
        matrix (list): The data matrix for the table.
        even_color (str): The background color for even rows.
        odd_color (str): The background color for odd rows.

    Returns:
        Frame: The table frame.
    """
    ttk.Style().configure("odd.TLabel", background=odd_color, width=TABLE_WIDTH, foreground="black")
    ttk.Style().configure("even.TLabel", background=even_color, width=TABLE_WIDTH, foreground="black")

    matrix.insert(0, header)

    table_frame = ttk.Frame(frame)

    for i in range(len(matrix)):
        q = label(table_frame, "")
        if (i + 1) % 2 != 0:
            q.config(style="odd.TLabel")
        else:
            q.config(style="even.TLabel")
        q.grid(row=i, column=0, columnspan=len(matrix[0]), sticky="nswe", padx=PAD1)

        for j in range(len(matrix[0])):
            q = label(table_frame, matrix[i][j])
            if i == 0:
                q.config(style="odd.TLabel", foreground="navy")
            if (i + 1) % 2 != 0:
                q.config(style="odd.TLabel")
            else:
                q.config(style="even.TLabel")
            q.grid(row=i, column=j, padx=PAD1)

    return table_frame

def show_confirmation_box(text: str):
    """
    Display a confirmation box.

    Args:
        text (str): The message to display.

    Returns:
        bool: True if "Yes" is clicked, False if "No" is clicked.
    """
    return messagebox.askyesno(title="Alert", message=text)