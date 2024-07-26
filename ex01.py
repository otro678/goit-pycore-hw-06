from records import Record
from addressbook import AddressBook

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

try:
    john_record.add_phone("abcde")
except Exception as e:
    print(e)

try:
    john_record.add_phone("12345")
except Exception as e:
    print(e)

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")


book.delete("Jane")
print(book.find("Jane"))

try:
    book.delete("Jane")
except Exception as e:
    print(e)