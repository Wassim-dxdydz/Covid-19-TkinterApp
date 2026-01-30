"""
This module contains the main entry point for running the COVID analysis GUI.

It imports and initializes the GUI application from the 'gui' module, which handles
the user interface and data processing for COVID-related analysis.

"""

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    from gui import launch_gui
    launch_gui()
