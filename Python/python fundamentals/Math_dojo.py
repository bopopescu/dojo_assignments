##### Math Dojo

### Part 1
# class MathDojo(object):
#     def __init__(self):
#         self.result = 0
#     def add(self, *vals):
#         self.result += sum(vals)
#         return self
#     def subtract(self, *vals):
#         self.result -= sum(vals)
#         return self

# md = MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result

### Part 2
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *vals):
        for val in vals:
            if isinstance(val, int) or isinstance(val, float):
                self.result += val
            elif isinstance(val, list) or isinstance(val, tuple):
                self.result += sum(val)
        return self
    def subtract(self, *vals):
        for val in vals:
            if isinstance(val, int) or isinstance(val, float):
                self.result -= val
            elif isinstance(val, list) or isinstance(val, tuple):
                self.result -= sum(val)
        return self

md = MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result