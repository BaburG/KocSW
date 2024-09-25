from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider, QFileDialog
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import numpy as np
import re

class FileSimulationParametersTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layers = []
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()

        # File selection button
        self.file_button = QPushButton("Select G-code File")
        self.file_button.clicked.connect(self.select_file)
        left_layout.addWidget(self.file_button)

        # PyQtGraph chart
        self.chart = pg.PlotWidget()
        left_layout.addWidget(self.chart)

        # Set up additional axes
        self.chart.showAxis('right')
        self.chart.showAxis('top')
        self.chart.getAxis('right').setLabel('Y (mm)')
        self.chart.getAxis('top').setLabel('X (mm)')
        self.chart.getAxis('left').setLabel('Y (mm)')
        self.chart.getAxis('bottom').setLabel('X (mm)')

        # Link the additional axes
        self.chart.getAxis('right').linkToView(self.chart.getViewBox())
        self.chart.getAxis('top').linkToView(self.chart.getViewBox())

        # Layer info layout
        layer_info_layout = QHBoxLayout()
        self.layer_number_label = QLabel("Layer: 0")
        self.travel_distance_label = QLabel("Travel distance: 0 mm")
        layer_info_layout.addWidget(self.layer_number_label)
        layer_info_layout.addWidget(self.travel_distance_label)
        left_layout.addLayout(layer_info_layout)

        # Select layer button
        self.select_layer_button = QPushButton("Select Layer")
        self.select_layer_button.clicked.connect(self.select_layer)
        left_layout.addWidget(self.select_layer_button)

        main_layout.addLayout(left_layout)

        # Layer slider (vertical)
        self.layer_slider = QSlider(Qt.Vertical)
        self.layer_slider.setMinimum(0)
        self.layer_slider.setMaximum(100)  # Placeholder max value
        self.layer_slider.valueChanged.connect(self.update_chart)
        main_layout.addWidget(self.layer_slider)

        self.setLayout(main_layout)

        # Global variable to store the current layer
        self.current_layer = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select G-code File", "", "G-code Files (*.gcode)")
        if file_path:
            self.parse_gcode(file_path)
            self.layer_slider.setMaximum(len(self.layers) - 1)
            self.update_chart()

    def parse_gcode(self, file_path):
        self.layers = []
        current_layer = []
        current_z = None

        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('G0') or line.startswith('G1'):
                    x, y, z = None, None, None
                    match = re.search(r'X([-\d.]+)', line)
                    if match:
                        x = float(match.group(1))
                    match = re.search(r'Y([-\d.]+)', line)
                    if match:
                        y = float(match.group(1))
                    match = re.search(r'Z([-\d.]+)', line)
                    if match:
                        z = float(match.group(1))

                    if z is not None and z != current_z:
                        if current_layer:
                            self.layers.append(current_layer)
                        current_layer = []
                        current_z = z

                    if x is not None and y is not None:
                        current_layer.append((x, y))

        if current_layer:
            self.layers.append(current_layer)

    def update_chart(self):
        layer = self.layer_slider.value()
        if 0 <= layer < len(self.layers):
            self.chart.clear()
            x, y = zip(*self.layers[layer])
            self.chart.plot(x, y)
            self.current_layer = self.layers[layer]
            
            # Calculate total travel distance
            total_distance = sum(
                np.sqrt((x2-x1)**2 + (y2-y1)**2) 
                for (x1, y1), (x2, y2) in zip(self.current_layer[:-1], self.current_layer[1:])
            )
            
            # Update layer number and travel distance labels
            self.layer_number_label.setText(f"Layer: {layer + 1}")
            self.travel_distance_label.setText(f"Travel distance: {total_distance:.2f} mm")

            # Update axis ranges
            self.chart.getViewBox().setRange(xRange=(min(x), max(x)), yRange=(min(y), max(y)))

    def select_layer(self):
        if self.current_layer is not None:
            # Here you would save the current_layer as a global variable
            # For now, we'll just print a message
            print("Layer selected as global variable")
        else:
            print("No layer data to select")