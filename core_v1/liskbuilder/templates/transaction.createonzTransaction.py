var lisk = require("onz-js");

var transaction = lisk.transaction.createTransaction(
    '{{ recipientId }}',
    {{ amount }},
    '{{ secret }}'
    {% if secondSecret %}
        ,'{{ secondSecret }}'
    {% endif %}
);

console.log(JSON.stringify(transaction));