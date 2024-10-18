from flask import Flask, request, jsonify, render_template
from rule_engine import create_rule, combine_rules, evaluate_rule
import ast
from db import insert_rule, get_all_rules

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule')
    try:
        # Create the rule in the database
        insert_rule(rule_string)  # Save the rule to the database
        return jsonify({"message": "Rule created successfully!", "rule": rule_string}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    try:
        combined_ast = combine_rules(rules)
        return jsonify({"combined_ast": ast.dump(combined_ast)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_ast = ast.literal_eval(request.json.get('rule_ast'))
    user_data = request.json.get('user_data')
    try:
        result = evaluate_rule(rule_ast, user_data)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True,port=3066)
