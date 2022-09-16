class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: str
    memory: str
    operating_system: str
    year_made: str
    price: str

    # How will you set up your constructor?


    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        

    # What methods will you need?