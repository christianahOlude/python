def nested_dicts():
	nested_dict = {
	"person1":{"name":"Alice","age":25},
	"person2":{"name":"Bob","age":30}
	}
nested_dicts["person1"]["city"]="New York"
print(nested_dicts)