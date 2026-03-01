from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "T")

# Based on the selection, run a program.
if selected == "1":
    import Run0
elif selected == "2":
    import Run1
elif selected == "3":
    import Run2
elif selected == "4":
    import Run3
elif selected == "5":
    import run4
elif selected == "6":
    import Run8
elif selected == "7":
    import silo
elif selected == "T":
    import test