class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print('distance', self.distance)
        print('rate', self.rate_per_km)
        print('fare', self.fare)

def main():
    # your program
    first_ride = TaxiRide(4)
    second_ride = TaxiRide(6)
    first_ride.calculate_fare(20)
    second_ride.calculate_fare(10)
    first_ride.print_receipt()
    second_ride.print_receipt()

if __name__ == "__main__":
    main()
