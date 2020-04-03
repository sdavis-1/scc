from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index2.html')


## API 역할을 하는 부분
@app.route('/coffee', methods=['POST'])
def write_coffee():
	# 1. 클라이언트가 준 name, amount, address, number 가져오기.
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

	# 2. DB에 정보 삽입하기
    doc = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'number': number_receive

    }
    db.coffee.insert_one(doc)

	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'coffees': '주문이 성공적으로 되었습니다.'})


@app.route('/coffee', methods=['GET'])
def read_coffee():
    # DB에 삽입할 review 만들기
    coffees = list(db.coffee.find({}, {'_id': False}))
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'coffees': coffees})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)