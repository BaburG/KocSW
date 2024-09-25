from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QDoubleValidator

class LaserParametersTab(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create input fields and set as class variables
        self.laser_power = QLineEdit()
        self.velocity = QLineEdit()
        self.diameter = QLineEdit()
        self.layer_thickness = QLineEdit()
        self.absorbability = QLineEdit()
        
        # Set up validators for numeric input
        double_validator = QDoubleValidator()
        for field in [self.laser_power, self.velocity, self.diameter, self.layer_thickness, self.absorbability]:
            field.setValidator(double_validator)
        
        # Create form layout
        form_layout = QFormLayout()
        form_layout.addRow("Laser Power (W):", self.laser_power)
        form_layout.addRow("Velocity (mm/s):", self.velocity)
        form_layout.addRow("Diameter (mm):", self.diameter)
        form_layout.addRow("Layer Thickness (mm):", self.layer_thickness)
        form_layout.addRow("Absorbability (%):", self.absorbability)
        
        # Create save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_parameters)
        
        # Set up main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.save_button)
        self.setLayout(main_layout)

    def save_parameters(self):
        # Validate all fields are not empty
        fields = [self.laser_power, self.velocity, self.diameter, self.layer_thickness, self.absorbability]
        field_names = ["Laser Power", "Velocity", "Diameter", "Layer Thickness", "Absorbability"]
        
        for field, name in zip(fields, field_names):
            if not field.text():
                QMessageBox.warning(self, "Validation Error", f"{name} cannot be empty.")
                return
        
        # If all validations pass, save the parameters
        # You can add your saving logic here
        QMessageBox.information(self, "Success", "Parameters saved successfully!")