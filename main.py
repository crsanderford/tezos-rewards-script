import http
import requests
import csv
import sys

bakingrewards = []
endorsementrewards = []

for x in range (0, 62):
  response = requests.get("https://api6.tzscan.io/v3/rewards_split/yourbakingaddresshere", params = {"cycle": x})

  data = response.json()
  print(x)


  bakingrewards.append(data["blocks_rewards"])
  endorsementrewards.append(data["endorsements_rewards"])
  


with open('bakingrewardsdata.csv', 'w') as output:
    out = csv.writer(output)
    out.writerows(map(lambda x: [x], bakingrewards))

with open('endorsementrewardsdata.csv', 'w') as output:
    out = csv.writer(output)
    out.writerows(map(lambda x: [x], endorsementrewards))
