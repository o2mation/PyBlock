'use strict';
// sys api


Blockly.Blocks['delay_ms'] = {
  init: function() {
    this.jsonInit({
      "type": "field_number",
      "message0": "delay_ms: %1(ms)",
      "args0": [
        {
          "type": "field_number",
          "name": "Delay",
          "value": 100
        }
      ],
      "colour": 160,
      "previousStatement": "Action",
      "nextStatement": "Action"
    });
  }
};

Blockly.Python.delay_ms = function(block) {
    // Blockly.Python.definitions_.import_sys = "import sys\n";
    var value = block.getFieldValue("Delay");
    console.log(value);
    return "sys.delay_ms" + "(" + value  + ")" + "\n";
};