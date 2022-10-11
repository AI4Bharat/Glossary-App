import os

db_cluster = os.environ.get('MONGO_CLUSTER_URL', 'mongodb+srv://sriharimn:Harikane@cluster0.1frkl.mongodb.net/')
app_host = os.environ.get('DGLOS_APP_HOST', 'localhost')
app_port = os.environ.get('DGLOS_APP_PORT', 5001)
context_path = os.environ.get('DMU_GLOS_CONTEXT_PATH', '/glossary-service')
db = os.environ.get('DMU_GLOS_DB', "dmu-glossary")
user_collection = os.environ.get('DMU_GLOS_USER_COL', "users")
dglos_collection = os.environ.get('DMU_GLOS_GLOSSARY_COL', "glossary")
es_url = os.environ.get('DMU_GLOS_ES_URL', 'http://127.0.0.1:9200')
base_index = os.environ.get('DMU_GLOS_BASE_INDEX', 'glossary-base-index')
session_collection = os.environ.get('DMU_GLOS_GLOSSARY_COL', "sessions")
session_timeout_in_ms = os.environ.get('DMU_DUS_SESSION_TIMEOUT_IN_MS', 86400000)
allowed_file_types = ["xls","xlsx","csv","tsv"]
local_storage_path = os.environ.get('DMU_GLOS_LOCAL_STORAGE_PATH', "‪C:/Users/Test/Documents/gloss")
x_key = os.environ.get('DMU_GLOS_X_KEY', "d6fd7481-f43e-4b76-b882-2ec512350d75")
max_file_size_in_mb = os.environ.get('DMU_GLOS_MAX_FILE_SIZE_IN_MB', 5000)
glossary_keys = ['srcLanguage','tgtLanguage','srcText','tgtText','domain','collectionSource','level']
levels = ['w','s','p']
if isinstance(max_file_size_in_mb, str):
    max_file_size_in_mb = eval(max_file_size_in_mb)
phrase_length_in_words = os.environ.get('DMU_GLOS_PHRASE_LENGTH_IN_WORDS', 100)
discarded_response_data=["@timestamp","audit"]

