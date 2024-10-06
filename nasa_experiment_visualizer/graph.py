import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = [
    {'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI1', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '32 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '6-Dec-18', 'Dissection Dates': '9-Dec-19 and 7-Jan-20 to 9-Jan-20', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': '-80 degree Celsius', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI2', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '32 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '6-Dec-18', 'Dissection Dates': '9-Dec-19 and 7-Jan-20 to 9-Jan-20', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': '-80 degree Celsius', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI3', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '32 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '6-Dec-18', 'Dissection Dates': '9-Dec-19 and 7-Jan-20 to 9-Jan-20', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': '-80 degree Celsius', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI4', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '32 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '6-Dec-18', 'Dissection Dates': '9-Dec-19 and 7-Jan-20 to 9-Jan-20', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': '-80 degree Celsius', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI5', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '32 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '6-Dec-18', 'Dissection Dates': '9-Dec-19 and 7-Jan-20 to 9-Jan-20', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': '-80 degree Celsius', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_ISS-T_YNG_BI11', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '10 to 12 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '6-Dec-18', 'Dissection Dates': '9-Dec-19 and 7-Jan-20 to 9-Jan-20', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': '-80 degree Celsius', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_LAR_YNG_BL1', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '10 to 12 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '5-Dec-18 to 6-Dec-18', 'Dissection Dates': '5-Dec-18 to 6-Dec-18', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': 'Not Applicable', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_LAR_YNG_BL2', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '10 to 12 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '5-Dec-18 to 6-Dec-18', 'Dissection Dates': '5-Dec-18 to 6-Dec-18', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': 'Not Applicable', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_LAR_YNG_BL3', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '10 to 12 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '5-Dec-18 to 6-Dec-18', 'Dissection Dates': '5-Dec-18 to 6-Dec-18', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': 'Not Applicable', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_LAR_YNG_BL4', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '10 to 12 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '5-Dec-18 to 6-Dec-18', 'Dissection Dates': '5-Dec-18 to 6-Dec-18', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': 'Not Applicable', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
    {'Sample Name': 'RR8_LVR_BSL_LAR_YNG_BL5', 'Strain': 'BALB/cAnNTac', 'Sex': 'Female', 'Spaceflight': 'Basal Control', 'Duration': '0 day', 'Euthanasia Location': 'On Earth', 'Age': '10 to 12 week', 'Light Cycle': '12 h light/dark cycle', 'Diet': 'Nutrient Upgraded Rodent Food Bar (NuRFB)', 'Feeding Schedule': 'ad libitum', 'Euthanasia Dates': '5-Dec-18 to 6-Dec-18', 'Dissection Dates': '5-Dec-18 to 6-Dec-18', 'Euthanasia Method': 'ketamine/xylazine overdose and exsanguination/double thoracotomy', 'Carcass Preservation Method': 'Not Applicable', 'Sample Preservation Method': 'Liquid Nitrogen', 'Sample Storage Temperature': '-80 degree Celsius'},
]

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Visualize the distribution of samples by strain
plt.figure(figsize=(10, 6))
df['Strain'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Samples by Strain')
plt.xlabel('Strain')
plt.ylabel('Number of Samples')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()

# Visualize the age distribution of samples
plt.figure(figsize=(10, 6))
df['Age'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Age Distribution of Samples')
plt.xlabel('Age')
plt.ylabel('Number of Samples')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()

# Visualize the feeding schedule of samples
plt.figure(figsize=(10, 6))
df['Feeding Schedule'].value_counts().plot(kind='bar', color='salmon')
plt.title('Feeding Schedule of Samples')
plt.xlabel('Feeding Schedule')
plt.ylabel('Number of Samples')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()

# Visualize the euthanasia method of samples
plt.figure(figsize=(10, 6))
df['Euthanasia Method'].value_counts().plot(kind='bar', color='lightcoral')
plt.title('Euthanasia Method of Samples')
plt.xlabel('Euthanasia Method')
plt.ylabel('Number of Samples')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
