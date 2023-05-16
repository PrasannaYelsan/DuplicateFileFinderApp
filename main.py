import datetime
import time
import os
from datetime import datetime
import timeddd

class DuplicateFinder():

    def __init__(self, drive, file_ext):
        self.drive = drive
        self.file_ext = file_ext


    def searchDrives(self):
        for root, folder, files in os.walk(self.drive):
            paths = root,folder, files
            for file in files:
                if file.endswith(".mp4"):
                    comp_path = str(root)+"\\"+str(file)
                    yield comp_path

    def convert_bytes(self, size):
        """ Convert bytes to KB, or MB or GB"""
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0

    def file_with_size(self):
        count = 0
        dict = {}
        for i in (clsDuplicate.searchDrives()):
            # print (i)
            f_size = os.path.getsize(i)
            x = clsDuplicate.convert_bytes(f_size)
            count = count + 1
            #print('file is ' + str(i), x)
            dict[str(i)] = x
        #print (dict)
        #print(count)
        return dict

    def add_value_to_dict(self):
        flipped = {}

        for key, value in self.file_with_size().items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
        # printing result
        #print("final_dictionary", str(flipped))
        return (flipped)

    def check_value_counts(self):
        count = 0
        for key, val in self.add_value_to_dict().items():
            if len(val)>1:
                count = count + 1
                print(key,val)
        print(count)

start = time.time()
start_t = (time.ctime(start).split(" "))
t1 = datetime.strptime(start_t[3], "%H:%M:%S")
print('Start time:', t1.time())

####################
clsDuplicate = DuplicateFinder("F:\\",".mp4")
clsDuplicate.file_with_size()
clsDuplicate.add_value_to_dict()
clsDuplicate.check_value_counts()

###################
end = time.time()
end_t = (time.ctime(end).split(" "))
t2 = datetime.strptime(end_t[3], "%H:%M:%S")
print('end time:', t2.time())
t = t2-t1
print(t)

