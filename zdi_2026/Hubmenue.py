from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "8", "T")

# Based on the selection, run a program.
if selected == "1":
    import Run_1
elif selected == "2":
    import Run_2
elif selected == "3":
    import Run_3
elif selected == "4":
    import Run_4
elif selected == "5":
    import Run_5
elif selected == "6":
    import Run_6
elif selected == "7":
    import Run_7
elif selected == "8":
    import Run_6_alt
elif selected == "T":
    import motortest