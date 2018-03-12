##### Call Center

class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print 'Unique ID: {}'.format(self.unique_id)
        print 'Caller Name: {}'.format(self.caller_name)
        print 'Caller Phone Number: {}'.format(self.caller_phone_number)
        print 'Time of Call: {}'.format(self.time_of_call)
        print 'Reason for Call: {}'.format(self.reason_for_call)
        return self


class CallCenter(object):
    def __init__(self, calls=[]):
        self.calls = calls
        self.queue_size = len(self.calls)
        # print self.calls
        # print self.queue_size
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        # print self.calls
        # print self.queue_size
        # for cal in self.calls:
        #     cal.display()
        return self
    def subtract(self):
        self.queue_size -= 1
        self.calls.pop(0)
        return self
    def info(self):
        for cal in self.calls:
            print 'name: {} phone num: {}'.format(cal.caller_name, cal.caller_phone_number)
        print self.queue_size
        return self



        

    # def remove(self):

call1 = Call( 1, 'victor', 1234567, '8:51am', 'coding question')
call2 = Call( 2, 'sultan', 3456789, '8:59am', 'flat tire')
call3 = Call( 3, 'mish', 4567890, '9:12am', 'fortnite question')
call4 = Call( 4, 'max', 2345678, '9:35am', 'directions')
call5 = Call( 5, 'sam', 5678901, '9:54am', 'workout problem')
call6 = Call( 6, 'ashley', 9876543, '10:15am', 'how is miso')

all_calls = [call1, call2, call3, call4, call5, call6]
# for x in all_calls:
#     x.display()

callCenter1 = CallCenter()

callCenter1.add(call1)
callCenter1.add(call2)
callCenter1.add(call3)
callCenter1.add(call4)

callCenter1.info()

callCenter1.subtract().info().subtract().info()

# callCenter


    


