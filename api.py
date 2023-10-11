from flask import Flask, render_template, request, jsonify
from app import generate_response
import json
# text to speech
import gtts  
from playsound import playsound  

app = Flask(__name__, template_folder='templates')

conversation = []

@app.route('/')
def chat():
    return render_template('chat.html', chats=conversation)

@app.route("/", methods=['POST'])
def converse():
    text = request.form['message']

    # speech to text
    # if 'audio' in request.files:
    #     file = request.files['audio']
    #     file.save(os.path.join('audio', "audio.wav"))
    #     text = speech_to_text()

    # previous knowledge if any
    if len(request.form['Trascriber']) > 0:
        newObject = {"role": "user", "content": request.form['Trascriber']}
        conversation.append(newObject)

    newObject = {"role": "user", "content": text}
    conversation.append(newObject)

    output = generate_response(conversation_history=conversation)

    newObject = {"role": "system", "content": output}
    conversation.append(newObject)

    t1 = gtts.gTTS(output)
    t1.save("output" + str(len(conversation)) + ".mp3")
    # playsound("output.mp3")

    return render_template('chat.html', chats=conversation)

@app.route("/chat", methods=['POST'])
def api():
    print(request.data)
    data = request.args
    print(data)
    text = data['message']

    newObject = {"role": "user", "content": text}
    conversation.append(newObject)

    output = generate_response(conversation_history=conversation)

    newObject = {"role": "system", "content": output}
    conversation.append(newObject)

    t1 = gtts.gTTS(output)
    t1.save("output" + str(len(conversation)) + ".mp3")

    return jsonify({'message': output})


if __name__ == "__main__":
    app.run(debug=True)
