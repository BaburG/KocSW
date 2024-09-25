class Material:
    def __init__(self, name, density, conductivity, specific_heat, diffusion):
        self.name = name
        self.density = density
        self.conductivity = conductivity
        self.specific_heat = specific_heat
        self.diffusion = diffusion

    def __str__(self):
        return f"Material: {self.name}"

    def __repr__(self):
        return f"Material(name='{self.name}', density={self.density}, conductivity={self.conductivity}, specific_heat={self.specific_heat}, diffusion={self.diffusion})"

    def to_dict(self):
        return {
            'name': self.name,
            'density': self.density,
            'conductivity': self.conductivity,
            'specific_heat': self.specific_heat,
            'diffusion': self.diffusion
        }