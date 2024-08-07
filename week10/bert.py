import numpy as np
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import pandas as pd
from transformers import BertTokenizer, TFBertModel
import pickle

# Función para inicializar el pool con el modelo y el tokenizer
def iniciarPool(model_name):
    global tokenizer, model
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = TFBertModel.from_pretrained(model_name)
    
def generarEmbeddings(text):
    inputs = tokenizer(text, return_tensors='tf', padding=True, truncation=True)
    outputs = model(**inputs)   
    return outputs.last_hidden_state[:, 0, :]  # Presentacion del token en forma [CLS]

def paralelismo(texts,model_name):
    print("inicia funcion de paralelismo")
    num_cores = cpu_count()
    print(f"Ahora estamos usando {num_cores} cores")
    pool = Pool(processes=num_cores, initializer=iniciarPool, initargs=(model_name,))

    resultados = []
    with tqdm(total=len(texts)) as pbar:    
        for resultado in pool.imap(generarEmbeddings, texts):
            resultados.append(resultado)
            pbar.update()

    pool.close()
    pool.join()
    print("termina funcion")
    return np.array(resultados).transpose(0,2,1)

if __name__ == "__main__":
    # Cargar datos
    wine_df = pd.read_csv('./data/winemag-data_first150k.csv')
    corpus = wine_df['description']
    print("Datos cargados exitosamente")
    
    # Cargar modelo BERT preentrenado y tokenizer
    bert = paralelismo(corpus,'bert-base-uncased')

    with open('bert.pkl', 'wb') as f:
        pickle.dump(bert, f)

   