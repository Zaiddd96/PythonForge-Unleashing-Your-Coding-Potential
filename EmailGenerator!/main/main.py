RECIPIENT = "[Your Name]"

with open("names.txt", "r") as names:
    names_list = names.readlines()

with open("mail.txt", "r") as mail:
    mail_content = mail.read()

for name in names_list:
    name = name.rstrip()
    personalized_names = mail_content.replace(RECIPIENT, name)
    personalized_mail = personalized_names.replace("[Your Recruiter's Name]", "Nigel Frank")
    with open(f"{name}'s_offer_letter.txt", "w") as new_mail:
        new_mail.write(personalized_mail)
