import json
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, 
                             QPushButton, QDialog, QLineEdit, QMessageBox, QFormLayout)
from PyQt5.QtCore import Qt
from material import Material

class MaterialSelectionTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        # Left side - Material List
        left_layout = QVBoxLayout()
        self.material_list = QListWidget()
        self.material_list.itemClicked.connect(self.show_material_details)
        left_layout.addWidget(QLabel("Materials:"))
        left_layout.addWidget(self.material_list)

        # Right side - Material Details
        right_layout = QVBoxLayout()
        self.details_label = QLabel("Select a material to view details")
        right_layout.addWidget(self.details_label)

        # Buttons
        button_layout = QHBoxLayout()
        select_button = QPushButton("Select")
        select_button.clicked.connect(self.select_material)
        add_button = QPushButton("Add New Material")
        add_button.clicked.connect(self.open_add_material_dialog)
        button_layout.addStretch()
        button_layout.addWidget(select_button)
        button_layout.addWidget(add_button)

        right_layout.addStretch()
        right_layout.addLayout(button_layout)

        layout.addLayout(left_layout)
        layout.addLayout(right_layout)
        self.setLayout(layout)

        self.load_materials()

    def load_materials(self):
        try:
            with open('materials.json', 'r') as f:
                materials_data = json.load(f)
            self.materials = [Material(**data) for data in materials_data]
            self.material_list.clear()
            for material in self.materials:
                self.material_list.addItem(material.name)
        except FileNotFoundError:
            self.materials = []

    def show_material_details(self, item):
        material = next((m for m in self.materials if m.name == item.text()), None)
        if material:
            details = f"Name: {material.name}\n"
            details += f"Density: {material.density} kg/m³\n"
            details += f"Conductivity: {material.conductivity} W/(m·K)\n"
            details += f"Specific Heat: {material.specific_heat} J/(kg·K)\n"
            details += f"Diffusion: {material.diffusion} m²/s"
            self.details_label.setText(details)

    def select_material(self):
        selected_items = self.material_list.selectedItems()
        if selected_items:
            selected_material = selected_items[0].text()
            print(f"Selected material: {selected_material}")
        else:
            print("No material selected")

    def open_add_material_dialog(self):
        dialog = AddMaterialDialog(self)
        if dialog.exec_():
            self.load_materials()

class AddMaterialDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Material")
        self.layout = QFormLayout()

        self.name_input = QLineEdit()
        self.density_input = QLineEdit()
        self.conductivity_input = QLineEdit()
        self.specific_heat_input = QLineEdit()
        self.diffusion_input = QLineEdit()

        self.layout.addRow("Name:", self.name_input)
        self.layout.addRow("Density (kg/m³):", self.density_input)
        self.layout.addRow("Conductivity (W/(m·K)):", self.conductivity_input)
        self.layout.addRow("Specific Heat (J/(kg·K)):", self.specific_heat_input)
        self.layout.addRow("Diffusion (m²/s):", self.diffusion_input)

        buttons = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_material)
        buttons.addWidget(self.cancel_button)
        buttons.addWidget(self.save_button)

        self.layout.addRow(buttons)
        self.setLayout(self.layout)

    def save_material(self):
        if self.validate_inputs():
            new_material = Material(
                name=self.name_input.text(),
                density=float(self.density_input.text()),
                conductivity=float(self.conductivity_input.text()),
                specific_heat=float(self.specific_heat_input.text()),
                diffusion=float(self.diffusion_input.text())
            )
            self.save_to_json(new_material)
            self.accept()

    def validate_inputs(self):
        empty_fields = []
        if not self.name_input.text():
            empty_fields.append("Name")
        if not self.density_input.text():
            empty_fields.append("Density")
        if not self.conductivity_input.text():
            empty_fields.append("Conductivity")
        if not self.specific_heat_input.text():
            empty_fields.append("Specific Heat")
        if not self.diffusion_input.text():
            empty_fields.append("Diffusion")

        if empty_fields:
            QMessageBox.warning(self, "Empty Fields", f"The following fields are empty: {', '.join(empty_fields)}")
            return False

        try:
            float(self.density_input.text())
            float(self.conductivity_input.text())
            float(self.specific_heat_input.text())
            float(self.diffusion_input.text())
            return True
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "All numeric fields must be valid numbers")
            return False

    def save_to_json(self, new_material):
        try:
            with open('materials.json', 'r') as f:
                materials_data = json.load(f)
        except FileNotFoundError:
            materials_data = []

        materials_data.append(new_material.to_dict())

        with open('materials.json', 'w') as f:
            json.dump(materials_data, f, indent=2)