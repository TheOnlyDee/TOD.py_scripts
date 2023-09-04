import qrcode

text = input("Che testo/url vuoi che il QR contenga? (incolla testo/url): ")
file_name = input("Quale vuoi che sia il nome del file dove sarà salvato? (finisci con .png): ")

def generate_qr(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

generate_qr(text, file_name)

print("Operazione Conclusa. Buona Giornata!")
