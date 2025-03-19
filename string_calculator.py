class StringCalculator:
    def __init__(self):
        self.call_count = 0
        self.add_occurred = None

    def add(self, numbers):
        self.call_count += 1
        
        if not numbers:
            result = 0
        else:
            delimiters = [',', '\n']
            
            if numbers.startswith('//'):
                delimiter_section = numbers.split('\n')[0]
                if delimiter_section.startswith('//['):
                    delimiter_part = delimiter_section[3:-1]
                    multiple_delimiters = delimiter_part.split('][')
                    delimiters.extend(multiple_delimiters)
                else:
                    custom_delimiter = delimiter_section[2:]
                    delimiters.append(custom_delimiter)
                numbers = numbers.split('\n', 1)[1]
            
            # Split with multiple delimiters
            for delimiter in delimiters:
                numbers = numbers.replace(delimiter, ',')
            
            numbers_array = numbers.split(',')
            numbers_array = [n for n in numbers_array if n]  # Remove empty strings
            
            negatives = [n for n in numbers_array if int(n) < 0]
            if negatives:
                raise ValueError(f"negative numbers not allowed: {', '.join(negatives)}")
            
            result = sum(int(n) for n in numbers_array if int(n) <= 1000)
        
        if self.add_occurred:
            self.add_occurred(numbers, result)
        
        return result

    def get_called_count(self):
        return self.call_count 