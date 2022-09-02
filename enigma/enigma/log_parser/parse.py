import glob
import os
import re


def get_log_file_path():
    list_of_files = glob.glob('/var/log/postgresql/*')
    latest_log_file = max(list_of_files, key=os.path.getctime)
    return latest_log_file

def read_log(file_p)->dict:
    line = file_p.readline()
    line_regex = re.compile("duration")
    final_dict=None
    if (line_regex.search(line)):
        line = line.split(' ')
    
        log_date = ' '.join(line[:2])
        query_duration = line[8]

        query = ' '.join(line[12:])
        final_dict={}
        final_dict['date']=log_date
        final_dict['query']=query[:-2]
        final_dict['duration']=query_duration

    return final_dict