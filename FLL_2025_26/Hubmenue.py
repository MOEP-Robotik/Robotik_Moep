from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "T")

# Based on the selection, run a program.
if selected == "1":
    import Programm1
elif selected == "2":
    import Programm2
elif selected == "3":
    import Programm3
elif selected == "T":
    import test