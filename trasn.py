import boto3

def translate_text(text, source_language_code, target_language_code): 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
    )
    print(response["TranslatedText"]) 

def main():
    translate_text('Hello, I am Shawn and I am currently working with Python','en','es')

if __name__=="__main__":
    main()
