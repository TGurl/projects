"""
This example demonstrates how you would handle having multiple "windows" for one py_cui application
"""
import py_cui

class MultiWindowDemo:

    def __init__(self, root: py_cui.PyCUI):

        # Root PyCUI window
        self.root = root

        # Collect current CUI configuration as a widget set object
        self.widget_set_A = self.root.create_new_widget_set(3, 3)

        # Add a button to the CUI
        self.widget_set_A.add_button('Open 2nd Window', 1, 1, command=self.open_set_B)

        # apply the initial widget set
        self.root.apply_widget_set(self.widget_set_A)

        # Create a second widget set (window). This one wil have a 5x5 grid, not 3x3 like the original CUI
        self.widget_set_B = self.root.create_new_widget_set(5, 5)

        # Add a text box to the second widget set
        self.text_box_B = self.widget_set_B.add_text_box('Enter something', 0, 0, column_span=2)
        self.text_box_B.add_key_command(py_cui.keys.KEY_ENTER, self.open_set_A)

    def open_set_A(self):
        # Fired on the ENTER key in the textbox. Use apply_widget_set to switch between "windows"
        self.root.apply_widget_set(self.widget_set_A)

    def open_set_B(self):
        # Fired on button press. Use apply_widget_set to switch between "windows"
        self.root.apply_widget_set(self.widget_set_B)


# Create CUI objects, pass to wrapper class, and start the CUI
root = py_cui.PyCUI(3, 3)
wrapper = MultiWindowDemo(root)
root.start()
