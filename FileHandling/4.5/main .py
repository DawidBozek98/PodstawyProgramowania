import emails

def main():
    with open("email.txt", "r") as file:
        email_content = file.read()  # Wczytujemy zawartość pliku

    # Używamy funkcji z modułu emails do pobrania danych
    sender = emails.email_sender(email_content)
    recipient = emails.email_recipient(email_content)
    subject = emails.email_subject(email_content)
    body = emails.email_body(email_content)

    print("Sender:", sender)
    print("Recipient:", recipient)
    print("Subject:", subject)
    print("Body:", body)

if __name__ == "__main__":
    main()
