class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # score will be final answer, record is our stack of ops
        # iterate through the ops.
        #   if integer, add to record
        #   if '+' sum prev two ints into record
        #   if 'D' peek prev and * 2
        #   if 'C' pop from the record

        # sum resulting record list
        score = 0
        record = []

        for i in range(0, len(operations)):
            if operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                record.append(int(record[-1]) * 2)
            elif operations[i] == '+':
                curr = 0
                for j in range(len(record) - 2, len(record)):
                    curr += int(record[j])
                record.append(curr)
            else:
                record.append(int(operations[i]))
            print(record)

        return sum(record)
