from datetime import datetime
class DNModel:
    class DnComponent:
        oid: str
        name: str
        value: str
    
    dn_components: list[DnComponent] = []
    
    def to_string_representation(self):
        str_ = ""
        for comp in self.dn_components:
            str += comp.name + "=" + comp.value
        return str_
        

class CertificateModel:
    
    signature_algorithm: str
    x509_version: int
    serial_number_max_length: str
    issuer_dn: DNModel
    subject_dn: DNModel
    valid_from: datetime
    valid_to: datetime
    subject_key_algorithm: str
    subject_key_length: int
    