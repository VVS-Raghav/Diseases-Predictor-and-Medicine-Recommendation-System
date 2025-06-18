import sys
import pickle
import numpy as np
import pandas as pd
import json
import ast

svc = pickle.load(open('models/svc.pkl', 'rb'))
sym_des = pd.read_csv("datasets/symtoms_df.csv")
precautions = pd.read_csv("datasets/precautions_df.csv")
workout = pd.read_csv("datasets/workout_df.csv")
description = pd.read_csv("datasets/description.csv")
medications = pd.read_csv('datasets/medications.csv')
diets = pd.read_csv("datasets/diets.csv")

with open('symptoms.json', 'r') as file:
    symptoms_dict = json.load(file)

diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}

def helper(dis):
    desc = " ".join(description[description['Disease'] == dis]['Description'])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.flatten().tolist()
    
    med_str = medications[medications['Disease'] == dis]['Medication'].values
    med = ast.literal_eval(med_str[0]) if len(med_str) > 0 else []

    die_str = diets[diets['Disease'] == dis]['Diet'].values
    die = ast.literal_eval(die_str[0]) if len(die_str) > 0 else []

    wrkout = workout[workout['disease'] == dis]['workout'].tolist()
    return desc, pre, med, die, wrkout

def predict(symptom_str):
    user_symptoms = [s.strip("[]' ") for s in symptom_str.split(',')]
    input_vector = np.zeros(len(symptoms_dict))
    for item in user_symptoms:
        if item in symptoms_dict:
            input_vector[symptoms_dict[item]] = 1
    pred = diseases_list[svc.predict([input_vector])[0]]
    desc, pre, med, diet, wrkout = helper(pred)
    return {
        "predicted_disease": pred,
        "dis_des": desc,
        "my_precautions": pre,
        "medications": med,
        "my_diet": diet,
        "workout": wrkout
    }

if __name__ == "__main__":
    user_input = sys.argv[1]
    result = predict(user_input)
    print(json.dumps(result))
