'use strict';
// key api


Blockly.Blocks['key_id'] = {
  init: function() {
    this.jsonInit({
        "type": "number",
        "message0": "key id",
        "output": "Number",
        "colour": 160
    });
  }
};

Blockly.Python.key_id = function(block) {
    return ["key.id()", Blockly.Python.ORDER_ATOMIC];
};