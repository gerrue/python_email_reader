#!/usr/bin/python

import email
from email.Parser import Parser
import sys
import os
import re

email_message = sys.stdin.read()
email_parse = email.message_from_string(email_message)

if email.Utils.parseaddr(email_parse['from'])[1] == 'you@example.com':
  for w in email_parse.walk():
    if w.get_filename() is not None \
        and re.search(r'\.csv$', w.get_filename(), re.IGNORECASE):
#     print 'attachment: ' + w.get_filename()
      filename = w.get_filename()
      att_path = os.path.join("/file/name", filename)
      if not os.path.isfile(att_path):
        fp = open(att_path, 'wb')
        fp.write(w.get_payload(decode=True))
        fp.close()

sys.exit(0)
