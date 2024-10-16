import unittest
import src.util.cert_handler as cert_handler
import os

class CertHandlerTest(unittest.TestCase):

    def test_is_pem(self):
        self.assertTrue(os.path.isfile("test/test_pem_chain.pem"))
        self.assertTrue(cert_handler.check_pem("test/test_pem_chain.pem"))
        self.assertFalse(cert_handler.check_pem("test/test_der.cer"))

    def test_is_cert(self):
        self.assertTrue(cert_handler.check_is_certificate("test/test_pem_chain.pem"))
        self.assertTrue(cert_handler.check_is_certificate("test/test_der.cer"))
        self.assertFalse(cert_handler.check_is_certificate("test/test_zip.zip"))
    
    

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()