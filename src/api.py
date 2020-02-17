from flask import Flask ,request, jsonify 
import torch 

app = Flask(__name__)
@app.route('/', methods=['POST'])
def predict():
    input_json=request.get_json(force=True)
    model=torch.load('checkpoint.pth')
    #print(input_json['data'])
    input_tensor=torch.tensor(input_json['data'])
    #print (input_tensor)

    model.eval()
    predicted_output=model(input_tensor)
    new_dict={}
    new_dict['output']=predicted_output.data[0].item()
    #print (new_dict)
    return jsonify(new_dict)
if __name__=='__main__':
    port=5000
    app.run(host="0.0.0.0", port=port, debug=True)







