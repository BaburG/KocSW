from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from material_selection import MaterialSelectionTab
from laser_parameters import LaserParametersTab
from file_simulation_parameters import FileSimulationParametersTab
from simulation import SimulationTab

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laser Simulation")
        self.resize(800, 800)
        
        # Create tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Create and add tabs
        self.tabs.addTab(MaterialSelectionTab(), "Material Selection")
        self.tabs.addTab(LaserParametersTab(), "Laser Parameters")
        self.tabs.addTab(FileSimulationParametersTab(), "File and Simulation Parameters")
        self.tabs.addTab(SimulationTab(), "Simulation")

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)