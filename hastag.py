import re

messages = [
    "🔸Private #banks continue to gain market share which stood at 42% in terms of advances in FY24 compared to 35% in FY20. Market share in deposits also inched up from 30% in FY20 to 35% in FY24.",
    "🔸As per ET reports, The National Highways Authority of India (#NHAI) plans to offer 15 road projects worth ₹44,000 crore, covering 900 km, for bids under the build-operate-transfer (BOT) mode in FY25.",
    "🔸#LarsenAndToubro L&T has won 'significant' orders in its Buildings and Factories business vertical. The orders have been secured from Asian Institute of Gastroenterology, Hyderabad for constructing a super speciality hospital at Gachibowli in the #Hyderabad city.",
    "🔸#NBCC recently was awarded a project from Grid controller of India Ltd for planning, designing and execution of interior works including furniture’s, fitout works, cabling and other infrastructure works at Grand Reu- Ayur Vigyan Nagar, #NewDelhi. The project amounts to ₹70 crore approx.",
    "🔸#Cipla will invest an additional EUR 3 million (approx. Rs 27 cr) in Ethris GmbH a global leader in delivering mRNAs directly to the respiratory system.",
    "🔸Dr Reddy’s Laboratories (#DRL) and global private equity firms EQT and Warburg Pincus are the frontrunners for acquiring Advent’s stake in #Mumbai-headquartered biopharmaceuticals firm Bharat Serums and Vaccines (#BSV), said sources close to the development.",
    "🔸#Infosys has launched Infosys AsterTM, an #AI-amplified marketing suite aimed at enhancing brand experiences, marketing efficiency, and business growth.",
    "🔸#Wipro has entered into a strategic partnership with GBST to enhance superannuation, wealth, and pensions administration services. This collaboration combines GBST's Composer SaaS platform with Wipro's expertise in administration and contact center services, creating an integrated solution for companies transitioning from legacy IT systems."
]

# Function to extract hashtags without the '#' symbol
def extract_hashtags(text):
    return [tag[1:] for tag in re.findall(r'#\w+', text)]

# Extract hashtags from each message
all_hashtags = []
for message in messages:
    hashtags = extract_hashtags(message)
    all_hashtags.extend(hashtags)

# Write each hashtag separately
with open('words_list.txt', 'w') as file:
    for hashtag in all_hashtags:
        file.write(f"{hashtag}\n")
