import requests

# data owner A will specify a policy that he wants to create

# The following JSON specifies a policy
p_one = {"subject": "programB", "object": "fileA", "action": "read"}

# Making a post request (posting the policy) to create a policy
r_create = requests.post('http://127.0.0.1:8000/policy/', json=p_one)

# The following JSON specifies a policy
p_two = {"subject": "programB", "object": "fileA", "action": "read"}

# Making a post request (posting the policy) to create a policy
r_delete = requests.delete('http://127.0.0.1:8000/policy/', json=p_two)

# The following JSON specifie a dataset
f_one = {"object": "fileA"}
r_read = requests.get('http://127.0.0.1:8000/policy/', json=f_one)
print(r_read.json())


