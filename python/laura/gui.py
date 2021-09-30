import py_cui
from time import sleep

class App:
    def __init__(self, master: py_cui.PyCUI):
        self.master = master
        self.master.title_bar.set_color(py_cui.BLACK_ON_CYAN)
        self.master.status_bar.set_color(py_cui.BLACK_ON_GREEN)

        self.master.set_title('LAURA - an erotic game by TransGirl')
        self.master.set_status_bar_text('      Move: NESW       Quit: Q')
        self.master.add_block_label(self.get_logo_text(), 0, 4, row_span = 1, column_span = 3)

        self.storyline = self.master.add_text_block(
                    'Storyline', 
                    0, 0, 
                    row_span = 4, column_span = 4, 
                    initial_text=self.get_intro_text())

        self.statusbox = self.master.add_text_block(
                'Status',
                1, 4,
                row_span = 2, column_span = 3,
                initial_text = self.get_status_text())

    def get_status_text(self):
        with open('data/gui/0000-status.txt') as f:
            out = f.read()
        return out


    def get_intro_text(self):
        """Function that gets the introduction text

        Returns
        -------
        out : str
            The introduction text
        """
        with open('data/story/0000-intro.txt') as f:
            out = f.read()
        return out


    def get_logo_text(self):
        """Function that gets ascii art LAURA logo

        Returns
        -------
        out : str
            Ascii-art LAURA logo
        """
        out = ""
        out = out + " _        _   _   _ ____      _     \n"
        out = out + "| |      / \ | | | |  _ \    / \    \n"
        out = out + "| |     / _ \| | | | |_) |  / _ \   \n"
        out = out + "| |___ / ___ \ |_| |  _ <  / ___ \  \n"
        out = out + "|_____/_/   \_\___/|_| \_\/_/   \_\ \n"
        return out


def main():
    root = py_cui.PyCUI(4, 7)
    root.toggle_unicode_borders()
    root.set_widget_border_characters("╔", "╗", "╚", "╝", "═", "║")
    app = App(root)
    root.start()


if __name__ == '__main__':
    main()
