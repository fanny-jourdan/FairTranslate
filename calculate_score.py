import pandas as pd
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import comet
from comet import download_model, load_from_checkpoint


# Function to calculate BLEU score for a single sentence pair
def calculate_bleu_score(reference, candidate):
    """
    Calculate the BLEU score for a given sentence pair.
    :param reference: Reference sentence (string)
    :param candidate: Machine-translated sentence (string)
    :return: BLEU score (float)
    """
    reference_tokens = reference.split()
    candidate_tokens = candidate.split()
    # Use smoothing to avoid 0 scores for short sentences
    smoothie = SmoothingFunction().method4
    return sentence_bleu([reference_tokens], candidate_tokens, smoothing_function=smoothie)


# Load the COMET model
model_path = download_model("Unbabel/wmt22-comet-da")         
comet_model = load_from_checkpoint(model_path)

# Function to calculate the COMET score for a single sentence pair
def calculate_comet_score(source, reference, hypothesis):
    """
    Calculate the COMET score for a given sentence pair.
    :param source: Source sentence (string)
    :param reference: Reference sentence (string)
    :param hypothesis: Machine-translated sentence (string)
    :return: COMET score (float)
    """
    data = [
        {"src": source, "mt": hypothesis, "ref": reference}
    ]
    scores = comet_model.predict(data, batch_size=1)
    return scores[0][0]



#### Import Data ####

type_context = "Moral and Linguistic"

if type_context == "Baseline":
    file_path_translation = "translation/FairTranslate_with_MT.csv"
    file_path_score = "score/FairTranslate_score.csv"
elif type_context == "Moral":
    file_path_translation = "translation/FairTranslate_with_MT_MC.csv"
    file_path_score = "score/FairTranslate_score_MC.csv"
elif type_context == "Linguistic":
    file_path_translation = "translation/FairTranslate_with_MT_LC.csv"
    file_path_score = "score/FairTranslate_score_LC.csv"
elif type_context == "Moral and Linguistic":
    file_path_translation = "translation/FairTranslate_with_MT_MLC.csv"
    file_path_score = "score/FairTranslate_score_MLC.csv"


data_translation = pd.read_csv(file_path_translation, delimiter=';', quotechar='"', encoding="utf-8")
data_score = pd.read_csv(file_path_score, delimiter=';', quotechar='"', encoding="utf-8")


#model_name = 'gemma2:2b'
#model_name = "mistral:7b"
model_name = 'llama3.1:8b'
#model_name = "llama3.3:latest"


### Calculate scores for all data ###

# Apply BLEU score calculation for each row
data_score[f'bleu_score_{model_name}'] = data_translation.apply(
    lambda row: calculate_bleu_score(row['french'], row[f"MT_french_{model_name}"]), axis=1
)

data_score.to_csv(file_path_score, sep=';', quotechar='"', encoding="utf-8", index=False)

# Apply COMET score calculation for each row
data_score[f'comet_score_{model_name}'] = data_translation.apply(
    lambda row: calculate_comet_score(row['english'], row['french'], row[f'MT_french_{model_name}']), axis=1
)

data_score.to_csv(file_path_score, sep=';', quotechar='"', encoding="utf-8", index=False)