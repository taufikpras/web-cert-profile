from src.model.standard_model import StandardModel

obj = StandardModel()

obj.load_yaml()
print(obj.certificate_standard.to_string())