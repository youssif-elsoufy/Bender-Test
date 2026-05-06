import os
import re
import pandas as pd

data = []

base_path = "Bender_Gestalt_Test\Student Drawings by Year and Gender"

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    
    for img in os.listdir(folder_path):
        data.append({
            "image_name": img,
            "folder": folder,
            "path": os.path.join(folder_path, img)
        })

df = pd.DataFrame(data)
df.to_csv("images_index.csv", index=False)

df_labels = pd.read_excel("Bender_Gestalt_Test\\real_results.xlsx", sheet_name="ردود النموذج 1")

df_labels = pd.read_excel("Bender_Gestalt_Test\\real_results.xlsx", sheet_name="ردود النموذج 1")

print("\nColumns:")
df_labels.columns.tolist()

def extract_case_number(image_name):
    match = re.search(r'page-(\d+)', image_name)
    if match:
        return int(match.group(1))
    return None



