import re

file_name = 'email.txt'
with open(file_name, 'r') as file:
  content = file.read()
  file_lines = content.splitlines()

mail_pattern = r'<(.*)>'
recipient_line_pattern = r"From:"
sender_line_pattern = r"To:"
subject_line_pattern = r"Subject:"
body_pre_index_pattern = r"^\n$"

recipient_mail = ''
sender_mail = ''
mail_subject = ''
mail_body = ''
is_body = False

for line in file_lines:
  if is_body: 
    mail_body += line + '\n'
    continue

  recipient_match = re.match(recipient_line_pattern,line) 
  sender_match = re.match(sender_line_pattern,line) 
  subject_match = re.match(subject_line_pattern,line)
  body_match = re.match(body_pre_index_pattern, line)

  if line == '':
    is_body = True
    continue
 
  if recipient_match:
    mail_span = re.search(mail_pattern,line).span()
    recipient_mail = line[mail_span[0] + 1:mail_span[1] - 1]
  if sender_match:
    mail_span = re.search(mail_pattern,line).span()
    sender_mail = line[mail_span[0] + 1:mail_span[1] - 1]
  if subject_match:
    mail_subject = line.removeprefix('Subject:').lstrip()
  

print('sender:', sender_mail)
print('recipient:', recipient_mail)
print('subject:', mail_subject)
print(mail_body)


