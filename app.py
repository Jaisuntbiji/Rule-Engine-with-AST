from flask import Flask, request, jsonify, render_template
from rule_engine import create_rule, combine_rules, evaluate_rule
import ast
from db import insert_rule, get_all_rules

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to create a rule and store it
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule')
    try:
        rule_ast = create_rule(rule_string)
        insert_rule(rule_string)  # Save the rule to the database
        return jsonify({"message": "Rule created successfully!", "rule": rule_string}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to combine rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    try:
        combined_ast = combine_rules(rules)
        combined_ast_str = ast.dump(combined_ast)
        combined_rule_str = " AND ".join(f"({rule})" for rule in rules)  # Combine rules in SQL-like form
        insert_rule(combined_rule_str)
        return jsonify({"combined_ast": combined_ast_str,}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to evaluate all rules against user data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    user_data = request.json.get('user_data')
    all_rules = get_all_rules()  # Fetch all rules from the database
    results = {}

    for rule in all_rules:
        try:
            rule_ast = create_rule(rule)
            result = evaluate_rule(rule_ast, user_data)
            results[rule] = result
        except Exception as e:
            results[rule] = {"error": str(e)}
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True,port=3306)
