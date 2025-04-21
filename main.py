class Property:
    def __init__(self, property_id, address, rent):
        self.property_id = property_id
        self.address = address
        self.rent = rent
        self.is_rented = False

    def mark_as_rented(self):
        self.is_rented = True

    def mark_as_available(self):
        self.is_rented = False

    def __str__(self):
        return self.address.title()


class Tenant:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.rented_property = None

    def rent_property(self, property):
        if not property.is_rented:
            self.rented_property = property
            property.mark_as_rented()
            print(f"{self.name} has rented: {property.address}")
        else:
            print(f"{property.address.title()} is already rented!")

    def vacate_property(self):
        if self.rented_property:
            print(f"{self.name} has vacated: {self.rented_property.address}")
            self.rented_property.mark_as_available()
            self.rented_property = None
        else:
            print("You don't have any property to vacate!")


class Landlord:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def add_property(self, property):
        property_id = property.property_id
        if property_id not in self.properties:
            self.properties[property_id] = property
            print(f"Property added: {property.address}")
        else:
            print(f"Property ({property.address}) is already own by you!")

    def remove_property(self, property):
        property_id = property.property_id
        if property_id in self.properties:
            del self.properties[property_id]
            print(f"Property removed: {property.address}")
        else:
            print(f"You already don't owned that property {property.address}")

    def list_available_properties(self):
        print("\nAvailable Properties:")
        for property in self.properties:
            property_obj = self.properties[property]
            if not property_obj.is_rented:
                print(f"- {property_obj}")

        if not self.properties:
            print("You don't have any property!")

if __name__ == '__main__':
    p1 = Property(1, "221B Baker Street", 1500)
    p2 = Property(2, "12 Grimmauld Place", 1800)

    landlord = Landlord("Mr. John")
    landlord.add_property(p1)
    landlord.add_property(p2)

    tenant = Tenant("Harry", "harry@hogwarts.com")
    tenant.rent_property(p1)

    landlord.list_available_properties()

    tenant.vacate_property()
    landlord.list_available_properties()
