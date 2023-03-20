This project will focus on a success clone of AirBnB website.

AirBnB Clone So this project is the first step towards building a first full web application (which is an AirBnB clone). This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

Step 1: Write a command interpreter (Console) Models The folder models contains all the classes used in this project.

a unique id generated using uuid package the attribute created_at, a datetime object, indicating when the object is created the attribute updated_at, a datetime object, indicating when the object is last updated the attribute class, a str object, indicating what is the object's type (model) File Description Attributes base_model.py BaseModel class for all the other classes id, created_at, updated_at user.py User class for future user information email, password, first_name, last_name amenity.py Amenity class for future amenity information name city.py City class for future location information state_id, name state.py State class for future location information name place.py Place class for future accomodation information city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids review.py Review class for future user/host review information place_id, user_id, text File storage The folder engine manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in file_storage.py with methods to follow this flow: -> to_dict() -> -> JSON dump -> -> FILE -> -> JSON load -> ->

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

Resources cmd module packages concept page uuid module datetime unittest module args/kwargs Python test cheatsheet Auhtors Oragwu Obinna Edward [email] legiondesignsed@gmail.com| Github Ezeiru Chibuike [email] ezeiruchibuike@gmail.com|Github
