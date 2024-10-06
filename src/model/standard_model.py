import yaml

class ExtensionStandard:
    mandatory: int
    critical: int
    value: dict
    
    def from_dict(cls,input:dict):
        obj = cls()
        for key, value in input.items():
            setattr(obj, key, value)
        return obj
    

class CertificateStandard:
    signature_algorithm: list[str]
    x509_version: int
    serial_number_max_length: int
    allowed_issuer_dn: list[str]
    minimum_issuer_dn: list[str]
    validity_in_year: int
    allowed_dn_component: list[str]
    minimum_subject_dn_personal: list[str]
    minimum_subject_dn_affiliated: list[str]
    minimum_subject_dn_segel: list[str]
    
    authority_key_identifier: ExtensionStandard
    subject_key_identifier: ExtensionStandard
    keyusage: ExtensionStandard
    policies: ExtensionStandard
    san: ExtensionStandard
    ian: ExtensionStandard
    basic_constraint: ExtensionStandard
    name_constraint: ExtensionStandard
    eku: ExtensionStandard
    crldp: ExtensionStandard
    fresh_crl: ExtensionStandard
    aia: ExtensionStandard
    
    @classmethod
    def from_dict(cls,input:dict):
        obj = cls()
        for key, value in input.items():
            setattr(obj, key, value)
        return obj
    
    def to_string(self):
        return_dict = {}
        input = self.__dict__
        
        for key, value in input.items():
            if(isinstance(value, ExtensionStandard)):
                return_dict[key] = value.__dict__
            else:    
                return_dict[key] = value
        
        return return_dict
        
        
    
    def load_config(self, conf:dict):
        basic_conf = conf["basic"]
        
        for key, value in basic_conf.items():
            setattr(self, key, value)
            
        extension_conf = conf["extension"]
        
        for key, value in extension_conf.items():
            value_obj = ExtensionStandard.from_dict(ExtensionStandard,value)
            setattr(self, key, value_obj)
        
        
    
    
class StandardModel:
    interoperability_version: int
    oid_version: int
    oid_mapping: dict[str, str]
    certificate_standard: CertificateStandard
    
    def load_yaml(self):
        with open("../standard/main.yaml") as stream:
            try:
                yaml_data = yaml.safe_load(stream)
                # set version
                self.interoperability_version = yaml_data["interoperability_version"]
                self.oid_version = yaml_data["oid_version"]
    
                # oid mapping
                self.oid_mapping = yaml_data["oid_mapping"]
                
                self.certificate_standard = CertificateStandard()
                self.certificate_standard.load_config(yaml_data["certificate"])
                
            except yaml.YAMLError as exc:
                print(exc)