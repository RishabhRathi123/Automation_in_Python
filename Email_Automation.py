import yagmail

# initiating connection with SMTP(Simple Mail Trsansfer Protocol) server
yag=yagmail.SMTP("22ucs166@lnmiit.ac.in","Enter your Email-Password here")

try:
  yag.send(to="22ucs166@lnmiit.ac.in", cc="22ucs165@lnmiit.ac.in", subject="Checking Automation in sending email using Python", contents="Here's your daily message", attachments=[r"__location_of_attachments__"])
  print("Email sent to recipients")
except:
  print("Email not sent")
