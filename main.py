from logging import debug
from flask import Flask, render_template, request

from textblob import TextBlob
from textblob import Word

app1 = Flask(__name__)


@app1.route('/')
def hello():
    return render_template('base.html')

@app1.route('/detect',methods = ['POST'])
def define():
    ip_word = request.form.get('ip-word')
    blob = TextBlob(ip_word)
    res = blob.detect_language()
    temp=['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','zh-CN','zh-TW','co','hr','cs','da','nl','en','eo','et','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','he','hi','hmn','hu','is','ig','id','ga','it','ja','jv','kn','kk','km','rw','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ny','or','ps','fa','pl','pt','pa','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tl','tg','ta','tt','te','th','tr','tk','uk','ur','ug','uz','vi','cy','xh','yi','yo','zu']
    
    k = ['Afrikaans','Albanian','Amharic','Arabic','Armenian','Azerbaijani','Basque','Belarusian','Bengali','Bosnian','Bulgarian','Catalan','Cebuano','Chinese (Simplified)','Chinese (Traditional)','Corsican','Croatian','Czech','Danish','Dutch','English','Esperanto','Estonian','Finnish','French','Frisian','Galician','Georgian','German','Greek','Gujarati','Haitian Creole','Hausa','Hawaiian','Hebrew','Hindi','Hmong','Hungarian','Icelandic','Igbo','Indonesian','Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Kazakhmer','Kinyarwanda','Korean','Kurdish','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi','Mongolian','Myanmar (Burmese)','Nepali','Norwegian','Nyanja (Chichewa)','Odia (Oriya)','Pashto','Persian','Polish','Portuguese (Portugal, Brazil)','Punjabi','Romanian','Russian','Samoan','Scots Gaelic','Serbian','Sesotho','Shona','Sindhi','Sinhala (Sinhalese)','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tagalog (Filipino)','Tajik','Tamil','Tatar','Telugu','Thai','Turkish','Turkmen','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu']
    res = k[temp.index(res)]
    return render_template('base.html',prediction_text=f'\n the entered text is in : {res}')

if __name__=='__main__':
    app1.run(debug=True)
