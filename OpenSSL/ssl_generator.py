from OpenSSL import crypto


def generate_certificate():
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)

    cert = crypto.X509()

    cert.get_subject().C = "TW"
    cert.get_subject().O = "ORG_NAME"
    cert.get_subject().CN = "127.0.0.1:8000"

    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)

    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')

    with open("key.pem", "wt") as key_file:
        key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
    with open("cert.pem", "wt") as key_file:
        key_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))


if __name__ == '__main__':
    generate_certificate()
