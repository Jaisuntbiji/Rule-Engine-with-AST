async function createRule() {
    const rule = document.getElementById('ruleInput').value;

    const response = await fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule: rule }),
    });

    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}

async function combineRules() {
    const rules = document.getElementById('combineInput').value.split(',');

    const response = await fetch('/combine_rules', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rules: rules }),
    });

    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}

async function evaluateRule() {
    const userData = document.getElementById('userData').value;

    const response = await fetch('/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_data: JSON.parse(userData) }),
    });

    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data, null, 2);
}

