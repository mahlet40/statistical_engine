class StatEngine:
    def __init__(self, data):
        self.data = self._clean_data(data)

    def _clean_data(self, data):
        cleaned = []
        for item in data:
            try:
                cleaned.append(float(item))
            except (ValueError, TypeError):
                continue
        if not cleaned:
            raise ValueError("No valid numbers found!")
        return cleaned

    def get_mean(self):
        return sum(self.data) / len(self.data)
    def get_median(self):
        # 1. Sort the data from smallest to largest
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        # 2. If the count is odd, take the middle one
        if n % 2 != 0:
            return sorted_data[mid]
        # 3. If even, average the two middle numbers
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self):
        # Count how many times each number appears
        counts = {}
        for num in self.data:
            counts[num] = counts.get(num, 0) + 1
        
        # Find the highest count
        max_count = max(counts.values())
        
        # If everything appears only once, there is no mode
        if max_count == 1:
            return "No unique mode"
            
        # Get all numbers that hit that max count
        modes = [num for num, count in counts.items() if count == max_count]
        return modes[0] if len(modes) == 1 else modes
    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        # Bessel's correction: use (n-1) for sample, (n) for population
        denominator = len(self.data) - 1 if is_sample else len(self.data)
        return sum((x - mean) ** 2 for x in self.data) / denominator

    def get_standard_deviation(self, is_sample=True):
        return self.get_variance(is_sample) ** 0.5
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()
        # Returns numbers that are more than 'threshold' std devs away from mean
        return [x for x in self.data if abs(x - mean) > threshold * std_dev]