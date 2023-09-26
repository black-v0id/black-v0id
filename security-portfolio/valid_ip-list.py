###############################################################
# Scenario: The security team has a list of subnets that are trusted, this list changes every so often and we need to remove a provided list of IP addresses. 
# Assumption: the working directory has a file of allowed IP addresses called "allow_list.txt"
### 


# Function to remove IP addresses from a list of allowed IP addresses
def remove_addresses(import_file, remove_list):

  # read in the initial contents of the file
  with open(import_file, "r") as file:
    ip_addresses = file.read()

  # convert `ip_addresses` from a string to a list
  ip_addresses = ip_addresses.split()
  
  # Iteratie loop to search through list of approved IP addresses and remove any matches to our remove_list
  for element in ip_addresses:
    if element in remove_list:
      ip_addresses.remove(element)

  # Convert `ip_addresses` back to a string so that it can be written into the text file 
  ip_addresses = ", ".join(ip_addresses)       

  # Rewrite the original file
  with open(import_file, "w") as file:
    file.write(ip_addresses)



# Call function to remove specified IP addresses
remove_addresses("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

# Read in the updated file to validate
with open("allow_list.txt", "r") as file:
  text = file.read()
  
# Display file contents
print(text)
