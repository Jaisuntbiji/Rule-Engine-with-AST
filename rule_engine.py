import ast

# Function to create a rule from a string and return an AST node
def create_rule(rule_string):
    return ast.parse(rule_string, mode='eval')

# Function to combine multiple AST rules into one
def combine_rules(rule_strings):
    ast_nodes = [create_rule(rule) for rule in rule_strings]
    combined = ast_nodes[0]
    for node in ast_nodes[1:]:
        combined = ast.BoolOp(op=ast.And(), values=[combined, node])
    return combined

# Function to evaluate a rule AST against user data
def evaluate_rule(rule_ast, data):
    compiled_rule = compile(rule_ast, '<string>', 'eval')
    return eval(compiled_rule, {}, data)
