import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.base import Certificate, CertificateRevocationList
from cryptography.x509.oid import NameOID
import logging
logger = logging.getLogger("logger")

PEM_START_STRING = "-----BEGIN CERTIFICATE-----"
PEM_END_STRING = "-----END CERTIFICATE-----"

def check_is_certificate(path):
    returnval = False
    try:
        with open(path, 'rb') as cert_file:  # try open file in text mode
            certdata = cert_file.read()
        returnval = x509.load_pem_x509_certificate(certdata, default_backend())
        returnval = True
    except:  # if fail then file is non-text (binary)
        logger.debug("Not in PEM")
    
    try:
        with open(path, 'rb') as cert_file:    
            certdata = cert_file.read()
        returnval = x509.load_der_x509_certificate(certdata, default_backend())
        returnval = True
    except:
        logger.debug("Not in DER")
        
    return returnval

def check_pem(path):
    try:
        with open(path, 'r') as cert_file:  # try open file in text mode
            certdata = cert_file.read()
            logger.debug(certdata)
            if PEM_START_STRING in certdata and PEM_END_STRING in certdata:
                return True
                
    except:  # if fail then file is non-text (binary)
        logger.debug("Not in PEM")
    
    return False
