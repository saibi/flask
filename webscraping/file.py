def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", "w")
  file.write("Position,Company,Location,URL\n")
  
  for job in jobs:
    position=job['position'].replace(',', ' ')
    location=job['location'].replace(',', ' ')
    file.write(f"{position},{job['company']},{location},{job['link']}\n")

  file.close()
  