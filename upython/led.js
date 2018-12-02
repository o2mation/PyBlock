'use strict';
// led api

Blockly.Blocks['led_on'] = {
  init: function() {
    this.jsonInit({
      "type": "textinput",
      "message0": "led_on: %1",
      "args0": [
        {
          "type": "field_input",
          "name": "LedKey",
          "text": "led0"
        }
      ],
      "colour": 160,
      "previousStatement": "Action",
      "nextStatement": "Action"
    });
  }
};

Blockly.Python.led_on = function(block) {
    var value = block.getFieldValue("LedKey");
    return "led.led_on(\"" + value + "\"" + ")" + "\n";
};


Blockly.Blocks['led_off'] = {
  init: function() {
    this.jsonInit({
      "type": "textinput",
      "message0": "led_off: %1",
      "args0": [
        {
          "type": "field_input",
          "name": "LedKey",
          "text": "led0"
        }
      ],
      "colour": 160,
      "previousStatement": "Action",
      "nextStatement": "Action"
    });
  }
};

Blockly.Python.led_off = function(block) {
    var value = block.getFieldValue("LedKey");
    return "led.led_off(\"" + value + "\"" + ")" + "\n";
};