class Solution(object):
    def partitionLabels(self, s):
        # Save the last position of each character in the string
        last_index = {}
        i = 0
        while i < len(s):
            last_index[s[i]] = i 
            i += 1

        max_size = 0
        result = []
        idx = 0 
    
        # Go through the string and find the biggest possible partitions
        while idx < len(s):

            actual_char = s[idx]  
            max_size = last_index[actual_char]  
            i = idx

            # Keep updating max_size while characters inside the partition appear later in the string
            while i <= max_size:
                max_size = max(max_size, last_index[s[i]])
                i += 1

            # Add the size of the partition to the result
            result.append(max_size - idx + 1)

            # Move to the next partition
            idx = max_size + 1

        return result