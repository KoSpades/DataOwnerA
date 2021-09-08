import requests

# data owner A will specify a policy that he wants to create

# The following JSON specifies a policy
p_one = {"subject": "programB", "object": "fileA", "action": "read"}

# Making a post request to create a policy
r_create = requests.post('http://127.0.0.1:8000/policy/', json=p_one)

# The following JSON specifies a policy
p_two = {"subject": "programB", "object": "fileA", "action": "read"}

# Making a delete request to delete a policy
r_delete = requests.delete('http://127.0.0.1:8000/policy/', json=p_two)

# The following JSON specifie a dataset
f_one = {"object": "fileA"}

# Making a get request to read all policies with respect to a specified dataset
r_read = requests.get('http://127.0.0.1:8000/policy/', json=f_one)
print(r_read.json())

# Lastly, we deal with UPDATE
p_old = {"subject": "programA", "object": "fileA", "action": "read"}
p_new = {"subject": "programB", "object": "fileA", "action": "read"}
p_update = {"old_policy": p_old, "new_policy": p_new}

# Making the update request
r_update = requests.put('http://127.0.0.1:8000/policy/', json=p_update)
print(r_update.text)



