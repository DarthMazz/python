import os

bind = '0.0.0.0:' + str(os.getenv('PORT', 9876))
proc_name = 'Infrastructure-Practice-Flask'
workers = 1
accesslog = './access.log'
