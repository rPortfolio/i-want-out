class MenuOption:
    """Options used in menus.  Contain a name and some content."""
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def get_content(self):
        return self.content


class Menu:
    """Class used to select choices"""
    def __init__(self, name, options):
        self.name = name
        self.options = options

    def print_menu(self):
        print(self.name)
        for i, option in enumerate(self.options):
            option_text = f"  [{i}] {option.name}"
            print(option_text)
    
    def choose_option(self):
        try:
            option_index = int(input("  :"))
            selection = self.options[option_index]
            return selection
        except:
            return self.choose_option()

    #Returns a menu option
    def start_menu(self):
        self.print_menu()
        return self.choose_option()