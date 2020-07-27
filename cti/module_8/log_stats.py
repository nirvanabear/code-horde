
'''
You are given a stream of logging statements for a server as a list. Your product manager wants to know what categories of error are the most common, as well as what errors in the most common categories are the most common. 

Here are a few log lines, each is a string structured similarly to this:


[
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 Login Successful',
'[INFO] 200 User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


Return a dictionary with logging statistics, that is formatted like so ( don't worry about spacing or formatting, only the data matters )
 

{
	'WARNING': {
		'403': {
			'Forbidden': {
				'No token in request parameters': 1
			}
		}
	},
	'ERROR': {
		'500': {
			'Server Error': {
				'int is not subscriptable': 2
			}
		}
	},
	'INFO': {
		'200': {
			'OK': {
				'Login Successful': 1,
				'User sent a message': 1
			}
		}
	}
}


When printed it will more likely look like this:
 

{'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}}, 'ERROR': {'500': {'Server Error': {'int is not subscriptable': 2}}}, 'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}}}



** pseudocode **

create log dictionary
for log in list:
    alpha between [ and ] stored as key
    integer between ' ' and ' ' stored as key for sub-dict
    alpha between ' ' and ':' stored as key for sub-sub-dict
    alpha between ': ' and end of string stored as key in Counter



** scratch paper **

    log_dict = {}
    for log in logs:
        log_dict[re.search(r'\[(.*)\]', log).group(1))] = dict(re.search(r'\s([0-9]+)\s', log).group(1) = dict(re.search(r'\s(\w+):', log).group(1) = Counter(re.search(r':\s(.*)', log).group(1))))


print(log_dict[re.search(r'\[(.*)\]', log).group(1))] = {re.search(r'\s([0-9]+)\s', log).group(1) : {re.search(r'\s(\w+):', log).group(1) : Counter(re.search(r':\s(.*)', log).group(1))


    # if not have_entries:
    #     counts = 1
    #     log_dict[log_level] = {status_code : {status : {message : counts}}}
    #     have_entries += 1
    # else:
    #     if message not in log_dict[status_code][status]:
    #         counts = 1
    #     else:
    #         counts += 1
    #     log_dict[log_level] = {status_code : {status : {message : counts}}}


    
    # if message not in log_dict[log_level][status_code][status]:
    #     counts = 0
    # else:
    #     counts += 1


** repl.it unit test exceptions **

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 53, in test_example
    self.assertEquals(log_stats(test_data), {'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}}, 'ERROR': {'500': {'Server Error': {'int is not subscriptable': 2}}}, 'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}}})
AssertionError: {'WAR[84 chars]': {'Error': {'int is not subscriptable': 2}}}[72 chars]1}}}} != {'WAR[84 chars]': {'Server Error': {'int is not subscriptable[79 chars]1}}}}
- {'ERROR': {'500': {'Error': {'int is not subscriptable': 2}}},
+ {'ERROR': {'500': {'Server Error': {'int is not subscriptable': 2}}},
?                     +++++++

   'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}},
   'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}}}


'''
import re

def log_stats(logs):
    log_dict = {}
    for log in logs:
        level = re.search(r'\[(.*)\]', log).group(1)
        status_code = re.search(r'\s([0-9]+)\s', log).group(1)
        status = re.search(r'[0-9]+\s(.+):', log).group(1)
        message = re.search(r':\s(.*)', log).group(1)

        if not level in log_dict:
            log_dict[level] = {}

        if not status_code in log_dict[level]:
            log_dict[level][status_code] = {}

        if not status in log_dict[level][status_code]:
            log_dict[level][status_code][status] = {}

        if not message in log_dict[level][status_code][status]:
            log_dict[level][status_code][status][message] = 1
        else:
            log_dict[level][status_code][status][message] += 1

    return log_dict







if __name__ == '__main__':
    test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]

print(log_stats(test_data))
